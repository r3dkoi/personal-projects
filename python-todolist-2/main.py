"""PERSONAL MANAGEMENT TOOL - TO DO LIST
WELCOME!
Student Name: Kyla Sofocado
Student Number: 1034672
"""
from functions_2 import adding_tasks
def main():
    """
    This function holds the main program and where the tasks will be stored.
    The main menu is found here.
    """

    while True: #Program continues until user inputs a valid integer
        print ("==== TO DO LIST ====")
        print ("Welcome to the Main Menu")
        print("1. Add tasks")
        print("2. Show tasks")
        print("3. Delete tasks")
        print("4. Mark tests as done")
        print("5. Exit")
        try:
            choice = int(input("Choose a number to begin: ")) #Prompts user to begin the program

            if choice == "1":
                adding_tasks(choice)
            elif choice == "2":
                show_tasks(choice)
            elif choice == "3":
                delete_tasks(choice)
            elif choice == "4":
                marking_tests(choice)
            elif choice == "5":
                exit(choice)
            else:
                print("Please choose from the options above only. Thank you.")
        except ValueError:
            print("Please enter a valid number only. Not whatever you just did. Thanks :)")

if __name__ == "__main__":
    main()
