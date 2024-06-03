from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Subtask, Category
from .forms import TaskForm, SubtaskForm

def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def task_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    tasks = Task.objects.filter(category=category)
    return render(request, 'task_list.html', {'category': category, 'tasks': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    subtasks = Subtask.objects.filter(task=task)
    return render(request, 'task_detail.html', {'task': task, 'subtasks': subtasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def add_subtask(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = SubtaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.task = task
            subtask.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = SubtaskForm()
    return render(request, 'todo_list/add_subtask.html', {'form': form, 'task': task})