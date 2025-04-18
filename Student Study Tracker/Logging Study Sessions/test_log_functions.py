import unittest
from unittest.mock import patch
import readline

def subject_completer(text, state):
    options = ['Math', 'Physics', 'Chemistry']
    matches = [s for s in options if s.lower().startswith(text.lower())]
    if state < len(matches):
        return matches[state]
    return None

def log_subject():
    readline.set_completer(subject_completer)
    readline.parse_and_bind("tab: complete")
    subject = input("Enter subject (Enter tab for suggestions, or type your own):")
    print(f"{subject} entered.")
    return subject

class TestLogSubject(unittest.TestCase):
    @patch('builtins.input', return_value='Math')
    @patch('readline.set_completer')
    @patch('readline.parse_and_bind')

    def test_log_subject(self, mock_parse, mock_set_completer, mock_input):
        result = log_subject()
        mock_set_completer.assert_called_once_with(subject_completer)
        mock_parse.assert_called_once_with("tab: complete")
        mock_input.assert_called_once_with("Enter subject (Enter tab for suggestions, or type your own):")
        self.assertEqual(result, 'Math')

class TestLogSubjectErrors(unittest.TestCase):
    @patch('builtins.input', side_effect=EOFError)
    @patch('readline.set_completer')
    @patch('readline.parse_and_bind')
    def test_eof_error(self, mock_parse, mock_set_completer, mock_input):
        with self.assertRaises(EOFError):
            log_subject()
        mock_set_completer.assert_called_once_with(subject_completer)
        mock_parse.assert_called_once_with("tab: complete")
    
    @patch('builtins.input', side_effect=KeyboardInterrupt)
    @patch('readline.set_completer')
    @patch('readline.parse_and_bind')
    def test_keyboard_interrupt(self, mock_parse, mock_set_completer, mock_input):
        with self.assertRaises(KeyboardInterrupt):
            log_subject()
        mock_set_completer.assert_called_once_with(subject_completer)
        mock_parse.assert_called_once_with("tab: complete")

    @patch('builtins.input', return_value='')
    @patch('readline.set_completer')
    @patch('readline.parse_and_bind')
    def test_empty_input(self, mock_parse, mock_set_completer, mock_input):
        result = log_subject()
        self.assertEqual(result, '')
        mock_set_completer.assert_called_once_with(subject_completer)
        mock_parse.assert_called_once_with("tab: complete")
    
    @patch('builtins.input', return_value='UnknownSubject')
    @patch('readline.set_completer')
    @patch('readline.parse_and_bind')
    def test_unknown_subject(self, mock_parse, mock_set_completer, mock_input):
        result = log_subject()
        self.assertEqual(result, 'UnknownSubject')
        mock_set_completer.assert_called_once_with(subject_completer)
        mock_parse.assert_called_once_with("tab: complete")

suite = unittest.TestLoader().loadTestsFromTestCase(TestLogSubjectErrors)
result = unittest.TextTestRunner(verbosity=2).run(suite)
    

if __name__ == "__main__":
    unittest.main(verbosity=2)


