from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasks
from .form import TasksForms
# Create your views here.


def index(request):
    form = TasksForms(request.POST)
    if request.method == 'POST':
        form = TasksForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    tasks = Tasks.objects.all()
    context = {
        'form': form,
        'task': tasks,
    }

    return render(request, 'todo/index.html', context)


def task_retreive(request, pk):
    tasks = Tasks.objects.get(id=pk)
    context = {
        'task': tasks,
    }
    return render(request, 'todo/index.html', context)


def add_task(request):
    form = TasksForms(request.POST)
    if request.method == 'POST':
        form = TasksForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'todo/create_tasks.html', context)


def task_update(request, pk):
    task = Tasks.objects.get(id=pk)
    form = TasksForms(instance=task)
    if request.method == 'POST':
        form = TasksForms(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'todo/update_task.html', context)


def delete_task(request, pk):
    task = Tasks.objects.get(id=pk)
    task.delete()
    return redirect('/')
