from django.urls import path

from . import views
from . import services

app_name = 'todo'

urlpatterns = [
	path('', views.Index.as_view(), name=''),
	path('index', views.Index.as_view(), name='index'),
	path('all_tasks', views.ShowAllTasks.as_view(), name='all_tasks'),
	path('completed_tasks', views.ShowCompletedTasks.as_view(), name='completed_tasks'),
	path('uncompleted_tasks', views.ShowUncompletedTasks.as_view(), name='uncompleted_tasks'),
	# Добавление/Удаление задач 
	path('create_task', views.CreateTaskView.as_view(), name='create_task'),
	path('delete_task/<int:pk>', views.DeleteTaskView.as_view(), name='delete_task'),
	# Добавление/Удаление комментариев	
	path('create_comment', views.CreateCommentView.as_view(), name='create_comment'),
	path('delete_comment/<int:pk>', views.DeleteCommentView.as_view(), name='delete_comment'),
	# Изменение текста и заголовка задачи 
	path('update_task/<int:pk>', views.UpdateTaskView.as_view(), name='update_task'),
	# Изменение статуса сообщения (выполнено/невыполнено)
	path('completed/<int:pk>', views.SetCompletedStatusView.as_view(), name='completed'),
	path('uncompleted/<int:pk>', views.SetUncompletedStatusView.as_view(), name='uncompleted'),
	# Регистрация/авторизация/выход пользователя
	path('register', views.RegisterUserView.as_view(), name='register'),
	path('login/', views.LoginUserView.as_view(), name='login'),
	path('logout', views.LogoutUserView.as_view(), name='logout'),
	# Api для ajax
	path('api_set_completed_status', services.api_set_completed_status, name='api_set_completed_status'),
	path('api_set_uncompleted_status', services.api_set_uncompleted_status, name='api_set_uncompleted_status'),
	path('api_append_task', services.api_append_task, name='api_append_task'),
	path('api_delete_task', services.api_delete_task, name='api_delete_task'),
	path('api_append_comment', services.api_append_comment, name='api_append_comment'),
	path('api_delete_comment', services.api_delete_comment, name='api_delete_comment'),
]
