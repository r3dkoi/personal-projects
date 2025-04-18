import json
import readline
from json_functions import load_sessions, save_sessions, completer

def log_study_session():
    subject = input("Enter subject: ")