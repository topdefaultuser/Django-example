from .models import Task


def bind_comments_from_tasks(tasks):
	""" Привязка комментариев к задачам """
	for task in tasks:
		comments = task.comment_set.all()
		task.comments = comments


def get_tasks(filter_):
	""" Получение списка задач с учетом фильтра """
	if(filter_ == 'all_tasks'):
		tasks = Task.objects.all()

	elif(filter_ == 'completed_tasks'):
		tasks = Task.objects.filter(completed=True)

	elif(filter_ == 'uncompleted_tasks'):
		tasks = Task.objects.filter(completed=False)

	return tasks