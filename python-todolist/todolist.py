###
# Personal Management Tool Main File
# CST180
# Student No: 1034672

###

#Importing functions section
from functions.py import adding_tasks(); showing_tasks(tasks); marking_tasks(tasks); deleting_tasks(tasks)

def main():
    """Holds all our tasks
    A while True loop used to keep program running until
    user decides to exit.
    """
    tasks = []
    while True:
        print("\n==== To-Do List ====")
        print("1. Add tasks")
        print("2. Show tasks")
        print("3. Mark tasks as done")
        print("4. Delete tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        #Adding tasks
        if choice == '1':
            tasks = adding_tasks(choice)
            print(tasks)
        #Showing tasks
        elif choice == '2':
            tasks = showing_tasks(choice)
            print(tasks)
        #Marking tasks as done 
        elif choice == '3':
            tasks = marking_tasks(choice)
            print(tasks)
        #Deleting tasks section
        elif choice == '4':
            tasks = deleting_tasks(choice)
            print(tasks)
        #Exiting to do list program
        elif choice == '5':
            print("Exiting the To-Do List. Thank you :)")
            break 
        else:
            print("Invalid choice. Please choose from the listed options.")

if __name__ == "__main__":
    main()

            
