from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Task, Subtask, Category
from .forms import TaskForm, SubtaskForm

class IndexView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'

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

class AddSubtaskView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        form = SubtaskForm()
        return render(request, 'add_subtask.html', {'form': form, 'task': task})

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        form = SubtaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.task = task
            subtask.save()
            return redirect('task_detail', pk=task_id)
        return render(request, 'add_subtask.html', {'form': form, 'task': task})