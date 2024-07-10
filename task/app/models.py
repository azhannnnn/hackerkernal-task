from django.db import models

TASK_CHOICES = [
    ('Pending', 'Pending'),
    ('Done', 'Done'),
]

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=15) 
    id = models.AutoField(primary_key=True,unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    task_detail = models.TextField(max_length=50)
    task_type = models.CharField(max_length=7, choices=TASK_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.task_detail
