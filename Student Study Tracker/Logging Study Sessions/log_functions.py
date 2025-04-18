import json
import readline
from json_functions import load_sessions, save_sessions, completer

#File to store study sessions
saved_study_sessions = "study_sessions.json"

sessions = load_sessions()

# Function to log subject 
def log_subject():
    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")
    subject = input("Enter subject (Enter tab for suggestions, or type your own):")
    print(f"{subject} entered.")

def log_duration():
    duration = input("Enter study duration in hours (e.g., 1.5): ")
    try:
        duration = float(duration)
        print(f"Duration of {duration} hours entered.")
    except ValueError:
        print("Invalid input. Please enter a number.")


# Creating new session entries and saving them
new_session = {
    "Subject": subject,
    "Duration": duration,
    "Date": date,
    "Type of study": study_type,
}
if sessions is None: 
    sessions = [] #Turns sessions into a list if it is None
    sessions.append(new_session) #Then appends the list into the save file

save_sessions(sessions) #Saves the sessions to the JSON file