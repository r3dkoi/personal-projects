import unittest
from unittest.mock import patch
from log_functions import log_subject

class TestLogFunctions(unittest.TestCase):

    @patch('builtins.input', return_value='Mathematics')
    def test_log_subject_basic_input(self, mock_input):
        result = log_subject()
        self.assertEqual(result, 'Mathematics')

    @patch('builtins.input', return_value='')
    def test_log_subject_empty_input(self, mock_input):
        result = log_subject()
        self.assertEqual(result, '')

    @patch('builtins.input', return_value='Computer Science')
    def test_log_subject_with_space(self, mock_input):
        result = log_subject()
        self.assertEqual(result, 'Computer Science')

    @patch('builtins.input', return_value='123')
    def test_log_subject_numeric_input(self, mock_input):
        result = log_subject()
        self.assertEqual(result, '123')

    @patch('builtins.input', return_value='!@#$%')
    def test_log_subject_special_chars(self, mock_input):
        result = log_subject()
        self.assertEqual(result, '!@#$%')

if __name__ == '__main__':
    unittest.main()

