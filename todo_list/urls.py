from django.urls import path
from .views import IndexView, TaskListView, TaskDetailView, AddTaskView, AddSubtaskView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/<int:category_id>/', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/add/', AddTaskView.as_view(), name='add_task'),
    path('task/<int:task_id>/add_subtask/', AddSubtaskView.as_view(), name='add_subtask'),
]