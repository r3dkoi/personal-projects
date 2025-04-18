import json 
import readline  # For auto-suggesting pre-made subjects
from datetime import datetime
from log_functions import log_subject, log_duration, log_date, log_study_type
from json_functions import load_sessions, save_sessions

def log_session():
    """Function to log a study session."""
    # Load existing sessions from JSON file
    sessions = load_sessions()

    # Log subject with auto-completion
    subject = log_subject()

    # Log duration
    duration = log_duration()

    # Log date
    date = log_date()

    # Log type of study with auto-completion
    study_type = log_study_type()

    # Create a new session dictionary
    new_session = {
        "Subject": subject,
        "Duration": duration,
        "Date": date,
        "Type of study": study_type,
    }
    
    # If sessions is None, initialize it as an empty list
    if sessions is None:
        sessions = []
        
    # Append the new session to the list
    sessions.append(new_session)
    
    # Save the updated sessions to the JSON file
    save_sessions(sessions)
    
    print("Study session logged successfully!")
    
    return sessions
