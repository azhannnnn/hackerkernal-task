from django.contrib import admin
from .models import User, Task

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'id')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_detail', 'task_type', 'user')

admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)
