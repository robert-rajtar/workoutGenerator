import unittest
from unittest.mock import patch
from itertools import cycle
from generator import select_exercises


class TestSelectExercises(unittest.TestCase):
    @patch('builtins.input', side_effect=cycle(['1 2', '3', '5', '2', '6']))
    def test_select_exercises(self, mock_input):
        class MockDB:
            @staticmethod
            def get_exercises_by_group(group):
                return [(1, 'Exercise 1'), (2, 'Exercise 2'), (3, 'Exercise 3'), (4, 'Exercise 4'), (5, 'Exercise 5')]

        db = MockDB()

        groups = ['Group 1', 'Group 2']

        selected_exercises = select_exercises(db, groups)

        self.assertEqual(selected_exercises,
                         {'Exercise 1': {'series': 3, 'repetitions': 5}, 'Exercise 2': {'series': 2, 'repetitions': 6}})


if __name__ == '__main__':
    unittest.main()
