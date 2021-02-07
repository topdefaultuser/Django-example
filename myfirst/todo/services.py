from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse

from .models import Task, Comment


def api_set_completed_status(request):
	return api_change_task_status(request, is_completed=True)


def api_set_uncompleted_status(request):
	return api_change_task_status(request, is_completed=False)


def api_change_task_status(request, is_completed):
	if request.method == 'POST':
		task_id = request.POST.get('task_id')
		
		try:
			task = Task.objects.get(id=task_id)
		except:
			status = 'fail'
			description = 'task not found'
		else:
			task.completed = is_completed
			task.save(update_fields=['completed'])
			status = 'ok'
			description = 'status changed successfully'
	else:
		status = 'fail'
		description = 'Not allowed method. Use POST method'

	response = {
		'result': status,
		'is_completed': is_completed,
		'task_id': task_id,
		'description': description,
	}

	return JsonResponse(response)


def api_append_task(request):
	is_appended = False

	if request.method == 'POST':
		task = Task(title=request.POST.get('title'), text=request.POST.get('text'))
		task.save()
		task_id = task.id

		is_appended = True
		status = 'ok'
		description = 'Task added successfully'
		# status = 'fail'
		# description = 'Incorrect data transferred'
	else:
		status = 'fail'
		description = 'Not allowed method. Use POST method'

	response = {
		'result': status,
		'is_appended': is_appended,
		'task_id': task_id,
		'task_title': request.POST.get('title'),
		'task_text': request.POST.get('text'),
		'description': description,
	}

	return JsonResponse(response)


def api_delete_task(request):
	is_deleted = False
	
	if request.method == 'POST':
		task_id = request.POST.get('task_id')
		try:
			task = Task.objects.get(id=task_id)
		except:
			status = 'fail'
			description = 'Task not found'
		else:
			task.delete()
			is_deleted = True
			status = 'ok'
			description = 'Task deleted successfully'
	else:
		status = 'fail'
		description = 'Not allowed method. Use POST method'

	response = {
		'result': status,
		'is_deletet': is_deleted,
		'task_id': task_id,
		'description': description,
	}

	return JsonResponse(response)


def api_delete_comment(request):
	is_deleted = False

	if request.method == 'POST':
		comment_id = request.POST.get('comment_id')
		try:
			comment = Comment.objects.get(id=request.POST.get('comment_id'))
		except:
			status = 'fail'
			is_deleted = False
			description = 'Comment not found'
		else:
			comment.delete()
			is_deleted = True
			status = 'ok'
			description = 'Comment deleted successfully'
	else:
		status = 'fail'
		description = 'Not allowed method. Use POST method'

	response = {
		'result': status,
		'is_deletet': is_deleted,
		'comment_id': comment_id,
		'description': description,
	}

	return JsonResponse(response)


def api_append_comment(request):
	is_appended = False

	if request.method == 'POST':
		task_id = request.POST.get('task_id')
		try:
			task = Task.objects.get(id=task_id)
		except:
			status = 'fail'
			is_appended = False
			description = 'Task to add a comment not found'
		else:
			comment_text = request.POST.get('text')
			comment_id = task.comment_set.create(text=comment_text).id
			is_appended = True
			status = 'ok'
			description = 'Comment added to task successfully'
	else:
		status = 'fail'
		description = 'Not allowed method. Use POST method'

	response = {
		'result': status,
		'is_appended': is_appended,
		'task_id': task_id,
		'comment_text': comment_text,
		'comment_id': comment_id,
		'description': description,
	}

	return JsonResponse(response)


def change_task_status(request, task_id, is_completed):
	try:
		task = Task.objects.get(id=task_id)
	except (ValueError, models.Task.DoesNotExist):
		return HttpResponseNotFound(render(request, 'todo/404.html'))
	else:
		task.completed = is_completed
		task.save(update_fields=['completed'])

		return render_page(request, 
			request.session.get('filter', 'all_tasks'), int(task_id))

	return HttpResponseNotFound(render(request, 'todo/404.html'))


def render_page(request, tasks_filter, active_task=None):
	if not active_task:
		active_task = request.session.get('active_task_id')

	tasks = get_tasks(tasks_filter)
	bind_comments_from_tasks(tasks)

	context = {
		'tasks': tasks, 
		'filter': tasks_filter,
		'active_task': active_task,
	}

	return render(request, 'todo/todo.html', context)


def bind_comments_from_tasks(tasks):
	""" Привязка комментариев к задачам """
	for task in tasks:
		comments = task.comment_set.all()[::-1]
		task.comments = comments


def get_tasks(filter_):
	""" Получение списка задач с учетом фильтра """
	if(filter_ == 'all_tasks'):
		tasks = Task.objects.all()[::-1]

	elif(filter_ == 'completed_tasks'):
		tasks = Task.objects.filter(completed=True)[::-1]

	elif(filter_ == 'uncompleted_tasks'):
		tasks = Task.objects.filter(completed=False)[::-1]

	return tasks
