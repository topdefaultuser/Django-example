from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseNotFound

from .models import Task, Comment
from .forms import TaskForm, CommentForm 

from .services import render_page, change_task_status



def index(request):
	return render_page(request, request.session.get('filter', 'all_tasks')) 


def show_all_tasks(request):
	request.session['filter'] = 'all_tasks'

	return render_page(request, request.session['filter'])


def show_completed_tasks(request):
	request.session['filter'] = 'completed_tasks'

	return render_page(request, request.session['filter'])


def show_uncompleted_tasks(request):
	request.session['filter'] = 'uncompleted_tasks'

	return render_page(request, request.session['filter'])


def create_task(request):
	error = ''
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo:index')
		else:
			error = 'Указаны некорректные данные!'

	context = {
		'form': TaskForm(),
		'error': error,
	}

	return render(request, 'todo/create_task.html', context)


def create_comment(request):
	if request.method == 'POST':
		try:
			task = Task.objects.get(id=request.POST.get('task_id'))
		except:
			return HttpResponseNotFound(render(request, 'todo/404.html'))
		else:
			task.comment_set.create(text=request.POST.get('text'))

		request.session['active_task_id'] = task.id

		return redirect('todo:index')

	elif request.method == 'GET':
		context = {
			'form': CommentForm(),
			'task_id': request.GET.get('task_id'),
		}

		return render(request, 'todo/create_comment.html', context)

	return HttpResponseForbidden(render(request, 'todo/403.html'))


def delete_task(request):
	if request.method == 'GET':
		try:
			task = Task.objects.get(id=request.GET.get('task_id'))
			task.delete()
		except:
			return HttpResponseNotFound(render(request, 'todo/404.html'))
		else:
			return redirect('todo:index')

	return HttpResponseForbidden(render(request, 'todo/403.html'))


def delete_comment(request):
	if request.method == 'GET':
		try:
			comment = Comment.objects.get(id=request.GET.get('comment_id'))
		except:
			return HttpResponseNotFound(render(request, 'todo/404.html'))
		else:
			active_task_id = comment.task_id
			comment.delete()
			request.session.get('filter', 'all_tasks')

			return render_page(request,
				request.session.get('filter', 'all_tasks'), active_task_id)
	
	return HttpResponseForbidden(render(request, 'todo/403.html'))


def set_completed_status(request):
	if request.method == 'GET':
		return change_task_status(request, request.GET.get('task_id'), is_completed=True)

	return HttpResponseForbidden(render(request, 'todo/403.html'))


def set_uncompleted_status(request):
	if request.method == 'GET':
		return change_task_status(request, request.GET.get('task_id'), is_completed=False)
	
	return HttpResponseForbidden(render(request, 'todo/403.html'))