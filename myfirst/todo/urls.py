from django.urls import path

from . import views


app_name = 'todo'

urlpatterns = [
	path('', views.show_all_tasks, name='index'),
	path('index', views.show_all_tasks, name='index'),

	path('create', views.create_task, name='create'),
	path('create_comment<int:task_id>', views.create_comment, name='create_comment'),

	path('completed<int:task_id>', views.set_completed_status, name='completed'),
	path('uncompleted<int:task_id>', views.set_uncompleted_status, name='uncompleted'),

	path('delete<int:task_id>/', views.delete_task, name='delete'),
	path('delete_comment<int:comment_id>/', views.delete_comment, name='delete_comment'),
	
	path('completed_tasks', views.show_completed_tasks, name='completed_tasks'),
	path('uncompleted_tasks', views.show_uncompleted_tasks, name='uncompleted_tasks'),
]
