from django.urls import path
from .views import index
from django.contrib import admin
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('category/<int:category_id>/', views.task_list, name='task_list'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/add/', views.add_task, name='add_task'),
    path('task/<int:task_id>/add_subtask/', views.add_subtask, name='add_subtask'),
]




