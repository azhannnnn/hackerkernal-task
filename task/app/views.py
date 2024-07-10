from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import *
from .models import *
import django_excel as ex


#===========================================================================
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_user')
    else:
        form = UserForm()
    return render(request, 'user.html', {'form': form})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()
    return render(request, 'task.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    pagination = Paginator(users, 10)
    page_no = request.GET.get('page')
    page_object = pagination.get_page(page_no)
    return render(request, 'user_list.html', {'page_obj': page_object})

def task_list(request):
    tasks = Task.objects.all()
    pagination = Paginator(tasks, 10)
    page_no = request.GET.get('page')
    page_object = pagination.get_page(page_no)
    return render(request, 'task_list.html', {'page_obj': page_object})

def export_to_excel(request):
    users = User.objects.all()
    tasks = Task.objects.all()

    data1 = [['User ID', 'Name', 'Email', 'Mobile']]
    for user in users:
        data1.append([user.id, user.name, user.email, user.mobile])

    data2 = [['Task ID', 'Task Detail', 'Task Type', 'User ID', 'User Name']]
    for task in tasks:
        data2.append([task.id, task.task_detail, task.task_type, task.user.id, task.user.name])

    sheet = ex.pe.Sheet(data1, name='Users')
    sheet2 = ex.pe.Sheet(data2, name='Tasks')
    book = ex.pe.Book({'Users': sheet, 'Tasks': sheet2})
    
    return ex.make_response(book, 'xlsx', file_name='users_tasks.xlsx')
