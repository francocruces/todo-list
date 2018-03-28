from django.test import TestCase
from todo_list.models import TodoList

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
        
        # when
        todo.add_task('hacer un to-do list')
        
        # then
        self.assertFalse(todo.is_empty())
        self.assertTrue('hacer un to-do list' in todo.get_tasks())
        
    def test_add_many_tasks(self):
        # given
        todo = TodoList()
        todo.add_task('hacer un to-do list')
        
        # when
        todo.add_task('hacer otra to-do list')
        todo.add_task('hacer una to-do list mas')
        
        # then
        self.assertFalse(todo.is_empty())
        self.assertTrue('hacer otra to-do list' in todo.get_tasks())
        self.assertTrue('hacer una to-do list mas' in todo.get_tasks())