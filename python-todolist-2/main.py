"""PERSONAL MANAGEMENT TOOL - TO DO LIST
WELCOME!
Student Name: Kyla Sofocado
Student Number: 10346722
"""
from functions_2 import adding_tasks, show_tasks, delete_tasks, marking_tasks, exit_program, load_tasks_to_file
global tasks
tasks = load_tasks_to_file("stored_data.json")  #Loads tasks that have been saved previously
print(f"Initial tasks: {tasks}")  # Debug print

def main():
    """
    This function holds the main program and where the tasks will be stored.
    The main menu is found here.
    """
    
    while True: #Program continues until user exits
        print ("==== TO DO LIST ====")
        print ("Welcome to the Main Menu")
        print("1. Add tasks")
        print("2. Show tasks")
        print("3. Delete tasks")
        print("4. Mark tests as done")
        print("5. Exit")
        try:
            choice = int(input("Choose a number to begin: ")) #Prompts user to begin the program

            if choice == 1:
                adding_tasks(tasks)
            elif choice == 2:
                show_tasks(tasks)
            elif choice == 3:
                delete_tasks(tasks)
            elif choice == 4:
                marking_tasks(tasks)
            elif choice == 5:
                exit_program()
            else:
                print("Please choose from the options above only. Thank you.")
        except ValueError:
            print("Please enter a valid number only. Not whatever you just did. Thanks :)")

if __name__ == "__main__":
    main()
