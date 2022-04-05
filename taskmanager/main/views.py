from django.http import request
from django.shortcuts import render, redirect
from .models import TaskForm, Task


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def get_tasks(request):
    context = {"dataset": Task.objects.all()}

    return render(request, "new.html", context)


# def new(request):
#     error = ''
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             error = 'Не верно'
#
#     form = TaskForm()
#     context = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'main/new.html', context)



def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не верна'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
