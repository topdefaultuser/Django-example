from django.urls import path

from . import views
from . import services

app_name = 'todo'

urlpatterns = [
	path('', views.index, name='index'),
	path('index', views.index, name='index'),
	path('all_tasks', views.show_all_tasks, name='all_tasks'),

	path('api_set_completed_status', services.api_set_completed_status, name='api_set_completed_status'),
	path('api_set_uncompleted_status', services.api_set_uncompleted_status, name='api_set_uncompleted_status'),
	path('api_append_task', services.api_append_task, name='api_append_task'),
	path('api_delete_task', services.api_delete_task, name='api_delete_task'),
	path('api_append_comment', services.api_append_comment, name='api_append_comment'),
	path('api_delete_comment', services.api_delete_comment, name='api_delete_comment'),

	path('create', views.create_task, name='create'),
	path('create_comment', views.create_comment, name='create_comment'),

	path('completed', views.set_completed_status, name='completed'),
	path('uncompleted', views.set_uncompleted_status, name='uncompleted'),

	path('delete', views.delete_task, name='delete'),
	path('delete_comment', views.delete_comment, name='delete_comment'),

	path('completed_tasks', views.show_completed_tasks, name='completed_tasks'),
	path('uncompleted_tasks', views.show_uncompleted_tasks, name='uncompleted_tasks'),
]
