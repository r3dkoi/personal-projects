import json
import readline #For auto-suggesting pre-made subjects

#File to store study sessions
saved_study_sessions = "study_sessions.json"

#Loading subjects from JSON file for tab completion
with open('subject_areas.json', 'r') as f:
          subject_list = json.load(f)

def completer(text, state):
    """Auto-completes subject names from the list."""
    options = [s for s in subject_list if s.lower().startswith(text.lower())]
    if state < len(options):
        return options[state]
    return None
    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")

def load_sessions():
    try:
        with open(saved_study_sessions, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No previous study sessions found. Starting fresh.")

def save_sessions(sessions):
    with open(saved_study_sessions, "w") as f:
        json.dump(sessions, f, indent=4)