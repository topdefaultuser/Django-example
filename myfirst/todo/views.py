from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Task, Comment
from .forms import TaskForm, CommentForm
from .forms import UserRegisterForm, UserLoginForm

from .services import change_task_status


class BasePageView(LoginRequiredMixin, ListView):
	""" Супер класс, от которого наследуются все классы генерирующие главную страницу """
	model = Task
	template_name = 'todo/todo.html'
	context_object_name = 'tasks'
	title = ''
	extra_context = {}
	# login_url = None # Я указал адрес для авторизации в настройках

	# Перезапись метода родительского класса ListView унаследуваного от BaseListView->MultipleObjectMixin
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = self.title
		context.update(self.extra_context)
		return context 

	# Перезапись метода родительского класса ListView унаследуваного от BaseListView->MultipleObjectMixin
	def get_queryset(self):
		# order_by('-id') разворачивает задания, чтобы более старые были внизу списка
		return Task.objects.filter(author=self.request.user).order_by('-id')


class BaseCreateFormView(LoginRequiredMixin, CreateView):
	success_url = reverse_lazy('todo:index')
	title = ''
	extra_context = {}
	# login_url = None # Я указал адрес для авторизации в настройках

	# Перезапись метода родительского класса CreateView унаследуваного от BaseListView->MultipleObjectMixin
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = self.title
		context.update(self.extra_context)
		return context


class Index(BasePageView):
	""" Рендерит главную страницу """

	title = 'Главная страница'


class ShowAllTasks(BasePageView):
	""" Рендерит главную страницу со всеми типами задач """

	title = 'Все задачи'
	extra_context = {'filter': 'all_tasks'}


class ShowCompletedTasks(BasePageView):
	""" Рендерит главную страницу только с выполненными задачами """

	title = 'Выполненные задачи'
	extra_context = {'filter': 'completed_tasks'}

	# Перезапись метода родительского класса BasePageView
	def get_queryset(self):
		return Task.objects.filter(author=self.request.user, completed=True).order_by('-id')


class ShowUncompletedTasks(BasePageView):
	""" Рендерит главную страницу только с выполненными задачами """

	title = 'Невыполненные задачи'
	extra_context = {'filter': 'uncompleted_tasks'}

	# Перезапись метода родительского класса BasePageView
	def get_queryset(self):
		return Task.objects.filter(author=self.request.user, completed=False).order_by('-id')


class CreateTaskView(BaseCreateFormView):
	""" Создание задачи """
	form_class = TaskForm
	template_name = 'todo/create_task.html'
	title = 'Добавление задания'

	# Перезапись метода родительского класса CreateView унаследуваного от ModelFormMixin
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.author = self.request.user
		self.object.save()
		return super().form_valid(form)


class DeleteTaskView(LoginRequiredMixin, DeleteView):
	""" Удаление задачи """

	def get(self, request, pk):
		try:
			task = Task.objects.get(id=pk)
			task.delete()
		except:
			return HttpResponseNotFound(render(request, 'todo/404.html'))
		else:
			return redirect('todo:index')


	def post(self, request, post):
		return HttpResponseNotFound(render(request, 'todo/403.html'))


class CreateCommentView(BaseCreateFormView):
	""" Создание комментария """
	form_class = CommentForm
	template_name = 'todo/create_comment.html'
	title = 'Добавление комментария'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = self.title
		context['task_id'] = self.request.GET.get('task_id')
		return context

	# Перезапись метода родительского класса CreateView унаследуваного от ModelFormMixin
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.task_id = self.request.POST.get('task_id')
		self.object.save()
		return super().form_valid(form)


class DeleteCommentView(LoginRequiredMixin, DeleteView):
	""" Удаление комментария """

	def get(self, request, pk):
		try:
			task = Comment.objects.get(id=pk)
			task.delete()
		except:
			return HttpResponseNotFound(render(request, 'todo/404.html'))
		else:
			return redirect('todo:index')


	def post(self, request, post):
		return HttpResponseNotFound(render(request, 'todo/403.html'))


class UpdateTaskView(BaseCreateFormView, UpdateView):
	""" Изменение заголовка и текста задачи """
	model = Task
	form_class = TaskForm
	template_name = 'todo/update_task.html'
	title = 'Изменение задания'


class SetCompletedStatusView(BasePageView):
	""" Установка выполненного состояния задачи """

	def get(self, request, pk):
		try:
			change_task_status(request, pk, is_completed=True)
		except:
			return HttpResponseNotFound(render(request, 'todo/404.html'))
		else:
			return redirect('todo:index')


	def post(self, request, post):
		return HttpResponseNotFound(render(request, 'todo/403.html'))


class SetUncompletedStatusView(BasePageView):
	""" Установка невыполненного состояния задачи """

	def get(self, request, pk):
		try:
			change_task_status(request, pk, is_completed=False)
		except:
			return HttpResponseNotFound(render(request, 'todo/404.html'))
		else:
			return redirect('todo:index')


	def post(self, request, post):
		return HttpResponseNotFound(render(request, 'todo/403.html'))


class RegisterUserView(CreateView):
	""" Регистрация пользователя """
	model = User
	form_class = UserRegisterForm
	template_name = 'todo/register.html'
	success_url = reverse_lazy('todo:index')


	def form_valid(self, form):
		form_valid = super().form_valid(form)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password1']
		auth_user = authenticate(username=username, password=password)
		login(self.request, auth_user)
		return form_valid


class LoginUserView(LoginView):
	""" Авторизация пользователя """
	model = User
	form_class = UserLoginForm
	template_name = 'todo/login.html'
	success_url = reverse_lazy('todo:index')


class LogoutUserView(LogoutView):
	""" Выход пользователя с личного кабинета"""
	next_page = reverse_lazy('todo:login')

