from django.test import TestCase
from todo_list.models import TodoList, Task

# Create your tests here.
class TodoTests(TestCase):
    
    def test_empty_list(self):
        # given
        
        # when
        todo = TodoList()
        
        # then
        self.assertTrue(todo.is_empty())
        
    def test_add_task(self):
        # given
        todo = TodoList()
        task = Task('hacer un to-do list')
        
        # when
        todo.add_task(task)
        
        # then
        self.assertFalse(todo.is_empty())
        self.assertTrue(todo.contains(task))
        
    def test_add_many_tasks(self):
        # given
        todo = TodoList()
        task = Task('hacer un to-do list')
        task2 = Task('hacer otra to-do list')
        task3 = Task('hacer una to-do list mas')
        todo.add_task(task)
        
        # when
        todo.add_task(task2)
        todo.add_task(task3)
        
        # then
        self.assertFalse(todo.is_empty())
        self.assertTrue(todo.contains(task2))
        self.assertTrue(todo.contains(task3))
        
    def test_list_tasks(self):
        # given
        todo = TodoList()
        task = Task('hacer un to-do list')
        task2 = Task('hacer otra to-do list')
        task3 = Task('hacer una to-do list mas')
        todo.add_task(task)
        todo.add_task(task2)
        todo.add_task(task3)
        
        # when
        tasks = todo.list_tasks()
        
        # then 
        self.assertEquals(3, len(tasks))
        self.assertTrue('hacer un to-do list' in tasks)
        self.assertTrue('hacer otra to-do list' in tasks)
        self.assertTrue('hacer una to-do list mas' in tasks)
        
    def test_mark_task_as_done(self):
        # given
        todo = TodoList()
        task = Task('hacer un to-do list')
        task2 = Task('hacer otra to-do list')
        task3 = Task('hacer una to-do list mas')
        todo.add_task(task)
        todo.add_task(task2)
        todo.add_task(task3)
        
        # when
        todo.mark_as_done('hacer un to-do list')
        
        # then
        self.assertTrue(task.is_done())
        
    def test_create_task(self):
        # given
        
        # when
        task = Task('hacer una todo list')
        
        # then
        self.assertEqual(task.get_description(), 'hacer una todo list')
        self.assertFalse(task.is_done())
        
        
        