from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TodoList(models.Model):
    
    def __init__(self):
        self.tasks = []
    
    def is_empty(self):
        return len(self.tasks) == 0

    def get_tasks(self):
        return self.tasks
    
    def add_task(self, a_task):
        self.tasks.append(a_task)