from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Task, Comment
from .forms import TaskForm


@login_required
def api_set_completed_status(request):
	return api_change_task_status(request, is_completed=True)


@login_required
def api_set_uncompleted_status(request):
	return api_change_task_status(request, is_completed=False)


@login_required
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


@login_required
def api_append_task(request):
	is_appended = False
	task_id = None
	status = 'fail'

	if request.method == 'POST':
		task = Task(author=request.user, title=request.POST.get('title'), text=request.POST.get('text'))
		task.save()		
		
		task_id = task.id
		is_appended = True
		status = 'ok'
		description = 'Task added successfully'

	else:
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


@login_required
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


@login_required
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
			comment_id = task.comments.create(text=comment_text).id
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


@login_required
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


@login_required
def change_task_status(request, task_id, is_completed):
	""" Изменение статуса задания """

	task = Task.objects.get(id=task_id)
	task.completed = is_completed
	task.save(update_fields=['completed'])
