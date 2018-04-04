from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Task(models.Model):
    
    def __init__(self, description):
        self.description = description
        self.done = False
        
    def get_description(self):
        return self.description
        
    def is_done(self):
        return self.done
        
    def mark_as_done(self):
        self.done = True
        
class TodoList(models.Model):
    
    def __init__(self):
        self.tasks = []
    
    def is_empty(self):
        return len(self.tasks) == 0

    def get_tasks(self):
        return self.tasks
    
    def add_task(self, a_task):
        self.tasks.append(a_task)
        
    def contains(self, task):
        for t in self.tasks:
            if t.get_description() == task.get_description():
                return True
        return False
    
    def list_tasks(self):
        task_list = []
        for t in self.tasks:
            done = ' [Done]' if t.is_done() else ''
            task_list.append(t.get_description() + done)
        return task_list

    def mark_as_done(self, description):
        for t in self.tasks:
            if t.get_description() == description:
                t.mark_as_done()