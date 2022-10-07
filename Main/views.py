from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .models import Task
from .forms import TaskForm


# python manage.py runserver --insecure

class ActiveTask(ListView):
    model = Task
    template_name = 'Main/index.html'
    extra_context = {'title': 'Активные задачи'}
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(done=False).order_by('time_update')


class DidTask(ListView):
    model = Task
    template_name = 'Main/index.html'
    extra_context = {'title': 'Выполненные задачи'}
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(done=True).order_by('-time_update')


class AllTask(ListView):
    model = Task
    template_name = 'Main/index.html'
    extra_context = {'title': 'Все задачи'}
    context_object_name = 'tasks'
    ordering = ['-time_update']


class AddTask(CreateView):
    template_name = 'Main/add.html'
    form_class = TaskForm
    success_url = '/'
    extra_context = {'title': 'Добавить задачу'}


def readyTask(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.done = True
    task.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def activateTask(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.done = False
    task.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeleteTask(DeleteView):
    model = Task
    success_url = '/'
    template_name = 'Main/delete.html'
    extra_context = {'title': 'Удаление задачи'}


class UpdateTask(UpdateView):
    model = Task
    template_name = 'Main/add.html'
    form_class = TaskForm
    success_url = '/'
    extra_context = {'title': 'Редактирование задачи'}


def error404(request, exception=None):
    return render(request, 'Main/404.html', {'title': 'Страница не найдена'}, status=404)