### MAIN MENU ###
import sys
sys.path.append("Student Study Tracker\\Logging Study Sessions")
from log_session import log_session

def main():
    """Function holds the main program, all other options are linked here."""
    while True: #Program continues until user exits
        print("Welcome to your study tracker. Please select the options below to begin :)")
        print ("==== STUDY TRACKER PROTOTYPE ====")
        print ("MAIN MENU")
        print("1. Log your study sessions")
        print("2. Manage your subjects")
        print("3. Search through sessions")
        print("4. Session Summaries")
        print("5. Exit program")
        try:
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                log_session()
            elif choice == 2:
                from manage_subjects import manage_subjects
                manage_subjects()
            elif choice == 3:
                from search_sessions import search_sessions
                search_sessions()
            elif choice == 4:
                from session_summaries import session_summaries
                session_summaries()
            elif choice == 5:
                print("Thank you for using the study tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()