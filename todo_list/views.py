from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import TemplateView

from .forms import TaskForm
from .models import Task, Category


class UserTaskListView(TemplateView):
    template_name = 'task_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context

class IndexView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_tasks'] = Task.objects.all()
        return context


class LastTasksView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_tasks'] = Task.objects.order_by('-created_at')[:3]
        return context

class TaskListView(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        tasks = Task.objects.filter(category=category)
        return render(request, 'task_list.html', {'category': category, 'tasks': tasks})

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AddTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'add_task.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.object.pk})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('task_detail', pk=task_id)