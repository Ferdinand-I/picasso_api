"""Tasks test module."""
from django.test import TestCase

from ..tasks import change_processed_flag


class TasksTestCase(TestCase):
    """Tests."""
    def setUp(self) -> None:
        self.wrong_arg = 'test_wrong_arg'

    def test_wrong_task_arg(self):
        """Test return of task-function with wrong arg."""
        message = f'Processing of "{self.wrong_arg}" cannot be finished!'
        self.assertTrue(change_processed_flag(self.wrong_arg) == message)
