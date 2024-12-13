from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.view_tasks, name='view_tasks'),
    path('create/', views.create_task, name='create_task'),
    path('view/', views.view_tasks, name='view_tasks'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
