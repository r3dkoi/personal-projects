"""PERSONAL MANAGEMENT TOOL - TO DO LIST
WELCOME!
Student Name: Kyla Sofocado
Student Number: 1034672
"""

def main():
    """
    This function holds the main program and where the tasks will be stored.
    The main menu is found here.
    """
    tasks = [] #Stores the task list

    while True: #Program continues until user inputs a valid integer
        print ("/n==== TO DO LIST ====")
        print ("/nWelcome to the Main Menu")
        print("1. Add tasks")
        print("2. Show tasks")
        print("3. Delete tasks")
        print("4. Mark tests as done")
        print("5. Exit")
        
        choice = int(input("Choose a number to begin: ")) #Prompts user to begin the program

        try:
            if choice == "1":
                print adding_tasks(choice)
            elif choice == "2":
                print show_tasks(choice)
            elif choice == "3":
                print delete_tasks(choice)
            elif choice == "4":
                print marking_tests(choice)
            elif choice == "5":
                print exit(choice)
            else:
                print("Please choose from the options above only. Thank you.")
        except ValueError:
            print("Please enter a valid number only. Not whatever you just did. Thanks :)")
            
