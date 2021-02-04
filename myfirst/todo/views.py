from django.shortcuts import (render, redirect)
from django.http import Http404
from .models import (Task, Comment)
from .forms import (TaskForm, CommentForm) 

from .utils import (bind_comments_from_tasks, get_tasks) 


def show_all_tasks(request):
	tasks = Task.objects.all()[::-1]

	request.session['filter'] = 'all_tasks'

	bind_comments_from_tasks(tasks)

	context = {
		'tasks': tasks, 
		'filter': 'all_tasks',
	}

	return render(request, 'todo/todo.html', context)


def show_completed_tasks(request):
	tasks = Task.objects.filter(completed=True)[::-1]

	request.session['filter'] = 'completed_tasks'

	bind_comments_from_tasks(tasks)

	context = {
		'tasks': tasks,
		'filter': 'completed_tasks',
	}

	return render(request, 'todo/todo.html', context)


def show_uncompleted_tasks(request):
	tasks = Task.objects.filter(completed=False)[::-1]

	request.session['filter'] = 'uncompleted_tasks'

	bind_comments_from_tasks(tasks)

	context = {
		'tasks': tasks,
		'filter': 'uncompleted_tasks',
	}

	return render(request, 'todo/todo.html', context)


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


def create_comment(request, task_id):
	if request.method == 'POST':
		try:
			task = Task.objects.get(id=task_id)
		except:
			raise Http404('Задача не найдена')
		else:
			task.comment_set.create(text=request.POST.get('text'))

		filter_ = request.session.get('filter', 'all_tasks')

		tasks = get_tasks(filter_)
		bind_comments_from_tasks(tasks)

		context = {
			'tasks': tasks,
			'filter': filter_,
			'active_task': task_id,
		}

		return render(request, 'todo/todo.html', context)

	context = {
		'form': CommentForm(),
		'task_id': task_id,
	}

	return render(request, 'todo/create_comment.html', context)


def delete_task(request, task_id):
	try:
		task = Task.objects.get(id=task_id)
		task.delete()
	except:
		raise Http404('Задача не найдена')

	return redirect('todo:index')


def delete_comment(request, comment_id):
	try:
		comment = Comment.objects.get(id=comment_id)
		task_id = comment.task_id
		comment.delete()
	except:
		raise Http404('Задача не найдена')

	filter_ = request.session.get('filter', 'all_tasks')

	tasks = get_tasks(filter_)
	bind_comments_from_tasks(tasks)

	context = {
		'tasks': tasks,
		'filter': filter_,
		'active_task': task_id,
	}

	return render(request, 'todo/todo.html', context)


def set_completed_status(request, task_id):
	try:
		task = Task.objects.get(id=task_id)
		task.completed = True
		task.save(update_fields=['completed'])
	except:
		raise Http404('Задача не найдена')

	filter_ = request.session.get('filter', 'all_tasks')
	
	tasks = get_tasks(filter_)
	bind_comments_from_tasks(tasks)

	context = {
		'tasks': tasks, 
		'active_task': task_id,
		'filter': request.session['filter'],
	}

	return render(request, 'todo/todo.html', context)


def set_uncompleted_status(request, task_id):
	try:
		task = Task.objects.get(id=task_id)
		task.completed = False
		task.save(update_fields=['completed'])
	except:
		raise Http404('Задача не найдена')

	filter_ = request.session.get('filter', 'all_tasks')

	tasks = get_tasks(filter_)
	bind_comments_from_tasks(tasks)

	context = {
		'tasks': tasks, 
		'active_task': task_id,
		'filter': request.session['filter'],
	}

	return render(request, 'todo/todo.html', context)