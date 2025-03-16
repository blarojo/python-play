import unittest
from time_calculator import TimeCalculator
from datetime import timedelta

class Todo:
    def __init__(self, complete):
        self.complete = complete

class TestTimeCalculator(unittest.TestCase):
    def test_calculate_total_time(self):
        todos = [Todo(False), Todo(True), Todo(False)]
        expected_time = timedelta(minutes=60)
        self.assertEqual(TimeCalculator.calculate_total_time(todos), expected_time)

    def test_calculate_total_time_all_complete(self):
        todos = [Todo(True), Todo(True), Todo(True)]
        expected_time = timedelta(minutes=0)
        self.assertEqual(TimeCalculator.calculate_total_time(todos), expected_time)

    def test_calculate_total_time_none_complete(self):
        todos = [Todo(False), Todo(False), Todo(False)]
        expected_time = timedelta(minutes=90)
        self.assertEqual(TimeCalculator.calculate_total_time(todos), expected_time)

if __name__ == '__main__':
    unittest.main()