from django.urls import path
from .views import *
urlpatterns = [
    path('add_user/', add_user, name='add_user'),
    path('add_task/', add_task, name='add_task'),
    path('users/', user_list, name='user_list'),
    path('tasks/', task_list, name='task_list'),
    path('export/', export_to_excel, name='export_to_excel'),
]
