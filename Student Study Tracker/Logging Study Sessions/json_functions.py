import json

#File to store study sessions
saved_study_sessions = "study_sessions.json"

#Loading subjects from JSON file for tab completion
with open('Student Study Tracker\\Logging Study Sessions\\subject_areas.json', 'r') as f:
          data = json.load(f)
          subject_list = []
          for category in data.values():
               subject_list.extend(category) # Flatten the list of subjects

def subject_completer(text, state):
    """Auto-completes subject names from the list."""
    options = [s for s in subject_list if s.lower().startswith(text.lower())]
    if state < len(options):
        return options[state]
    return None

#Loading study_types from JSON file for tab completion
with open('Student Study Tracker\\Logging Study Sessions\\study_type.json', 'r') as f:
            study_type_list = json.load(f)

def study_type_completer(text, state):  
    """Auto-completes study types from the list."""
    options = [s for s in study_type_list if s.lower().startswith(text.lower())]
    if state < len(options):
        return options[state]
    return None

def load_sessions():
    try:
          with open('Student Study Tracker\\Logging Study Sessions\\saved_study_sessions.json', "r") as f:
              data = json.load(f)
              # Convert list to dict with numbered keys 
              if isinstance(data, list):
                  return {f"Session {i+1}": session for i, session 
    in enumerate(data)}
              return data
    except (FileNotFoundError, json.JSONDecodeError): 
          # If the file doesn't exist or is empty, return an empty list
          return {}

def save_sessions(sessions):
    with open('Student Study Tracker\\Logging Study Sessions\\saved_study_sessions.json', "w") as f:
        json.dump(sessions, f, indent=4) #Saves as a file in JSON format with indentation for readability