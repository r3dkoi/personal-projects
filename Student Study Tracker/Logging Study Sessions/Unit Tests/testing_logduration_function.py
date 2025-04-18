import unittest 
from unittest.mock import patch
from io import StringIO

def log_duration():
    duration = input("Enter study duration in hours (e.g., 1.5): ")
    try:
        duration = float(duration)  # Allows user to input a float value
        if duration <= 0:
            raise ValueError("Duration must be positive.")
        if duration > 24:
            raise ValueError("Duration cannot exceed 24 hours.")
        print(f"Duration of {duration} hours entered.")
        return duration
    except ValueError:
        print("Invalid input. Please enter a number.")



class TestLogDuration(unittest.TestCase):
    @patch('builtins.input', return_value='1.5')
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_float(self, mock_stdout, mock_input):
        result = log_duration()
        self.assertEqual(result, 1.5)
        self.assertIn("Duration of 1.5 hours entered.", mock_stdout.getvalue())

    @patch('builtins.input', return_value='2')
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_integer(self, mock_stdout, mock_input):
        result = log_duration()
        self.assertEqual(result, 2.0)
        self.assertIn("Duration of 2.0 hours entered.", mock_stdout.getvalue())

    @patch('builtins.input', return_value='0')
    @patch('sys.stdout', new_callable=StringIO)
    def test_zero_input(self, mock_stdout, mock_input):
        result = log_duration()
        self.assertIsNone(result)
        self.assertIn("Invalid input. Please enter a number.", mock_stdout.getvalue())

    @patch('builtins.input', return_value='-3')
    @patch('sys.stdout', new_callable=StringIO)
    def test_negative_input(self, mock_stdout, mock_input):
        result = log_duration()
        self.assertIsNone(result)
        self.assertIn("Invalid input. Please enter a number.", mock_stdout.getvalue())

    @patch('builtins.input', return_value='25')
    @patch('sys.stdout', new_callable=StringIO)
    def test_exceeding_max(self, mock_stdout, mock_input):
        result = log_duration()
        self.assertIsNone(result)
        self.assertIn("Invalid input. Please enter a number.", mock_stdout.getvalue())

    @patch('builtins.input', return_value='abc')
    @patch('sys.stdout', new_callable=StringIO)
    def test_non_numeric(self, mock_stdout, mock_input):
        result = log_duration()
        self.assertIsNone(result)
        self.assertIn("Invalid input. Please enter a number.", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main(verbosity=2)
