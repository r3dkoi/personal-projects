import json
from datetime import datetime
import readline
from json_functions import load_sessions, save_sessions, subject_completer, study_type_completer

#File to store study sessions
saved_study_sessions = "study_sessions.json"

sessions = load_sessions()

# Function to log subject 
def log_subject():
    readline.set_completer(subject_completer)
    readline.parse_and_bind("tab: complete")
    subject = input("Enter subject (Enter tab for suggestions, or type your own):")
    print(f"{subject} entered.")
    return subject


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
        return log_duration()


def log_date():
    try:
        date = input("Enter date (DD/MM/YYYY) or press enter for today:")
        if date == "":
            date = datetime.now().strftime("%d%m%Y")
            print(f"{date} set.")
            return date
        else:
            datetime.strptime(date, "%d/%m/%Y")  # Validate date format
            print(f"Date {date} entered.")
            return date
    except ValueError:
        print("Invalid date format. Please enter in DD/MM/YYYY format.")
        return log_date()  # Retry if invalid

def log_study_type():
    readline.set_completer(study_type_completer)
    readline.parse_and_bind("tab: complete")
    # Set up tab completion for study types
    study_type = input("Enter type of study (Enter tab for suggestions or type your own): ")
    print(f"Study type {study_type} entered.")
    if not study_type.strip():
        print("This field cannot be left empty.")
        return log_study_type()
  
