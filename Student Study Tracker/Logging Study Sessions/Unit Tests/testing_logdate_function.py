import unittest
from unittest.mock import patch, call
from datetime import datetime
from io import StringIO

def log_date():
    try:
        date = input("Enter date (DD/MM/YYYY) or press enter for today:")
        if date == "":
            date = datetime.now().strftime("%d%m%Y")
            print(f"{date} set.")
            return date
        else:
            datetime.strptime(date, "%d/%m/%Y")  # Validate format
            print(f"Date {date} entered.")
            return date
    except ValueError:
        print("Invalid date format. Please enter in DD/MM/YYYY format.")
        return log_date()  # Retry

class TestLogDate(unittest.TestCase):
    @patch('builtins.input', return_value='15/04/2025')
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_date(self, mock_stdout, mock_input):
        result = log_date()
        self.assertEqual(result, '15/04/2025')
        self.assertIn("Date 15/04/2025 entered.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['', ''])  # Empty input → default to today
    @patch('datetime.datetime')
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_input_default_today(self, mock_stdout, mock_datetime, mock_input):
        fixed_now = datetime(2025, 4, 18)  # Mock today's date
        mock_datetime.now.return_value = fixed_now
        result = log_date()
        self.assertEqual(result, '18042025')  # DDMMYYYY format
        self.assertIn("18042025 set.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['31/02/2025', '28/02/2025'])  # Invalid → valid
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_date_then_valid(self, mock_stdout, mock_input):
        result = log_date()
        self.assertEqual(result, '28/02/2025')
        # Check error message and retry
        self.assertIn("Invalid date format. Please enter in DD/MM/YYYY format.", mock_stdout.getvalue())
        self.assertIn("Date 28/02/2025 entered.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['15-04-2025', '15/04/2025'])  # Wrong format → valid
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_format_then_valid(self, mock_stdout, mock_input):
        result = log_date()
        self.assertEqual(result, '15/04/2025')
        self.assertIn("Invalid date format. Please enter in DD/MM/YYYY format.", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main(verbosity=2)
