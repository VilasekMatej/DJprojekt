from django.urls import path
from django.contrib import admin
from .views import IndexView, TaskListView, TaskDetailView, AddTaskView, UserTaskListView, complete_task

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/<int:category_id>/', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/add/', AddTaskView.as_view(), name='add_task'),
    path('my_tasks/', UserTaskListView.as_view(), name='user_tasks'),
    path('my_tasks/<int:task_id>/register/', complete_task, name='complete_task'),
    path('admin/', admin.site.urls),
]