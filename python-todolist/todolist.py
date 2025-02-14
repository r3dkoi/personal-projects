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

        #Adding tasks section
        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add: "))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})

        #Showing tasks section
        elif choice == '2':
            print("\nTasks:")
            #Looping through list of tasks with their indices
            for index, task in enumerate(tasks):
                #Calculating current index + 1
                current_index = index + 1
                #Retrieve task description from current task
                task_description = task["task"]
                #Get status of current task
                if task["done"]:
                    status = "Done"
                else:
                    status = "Not Done"
                #Print index, task description, and status
                print(f"{current_index}. {task_description}: {status}.")
               

        #Marking tasks as done section
        elif choice == '3':
            task_done_choice = int(input("Please put the number of the task you have done: ")) - 1
            #Check if index is within the valid range
            if 0 <= task_done_choice < len(tasks):
                #Mark task at given index as done
                tasks[task_done_choice]["done"] = True
                print("Task marked as done.")
            else:
                print("Invalid task number. Returning you to main menu.")

        #Deleting tasks section
        elif choice == '4':
            deleted_choice = int(input("Please state the number of the task you wish to remove: ")) - 1
            if 0 <= deleted_choice <len(tasks):
                #Removing task by index number from task list
                tasks.remove(task)
                print("Task has been removed.")
            else:
                print("Invalid task number. Returning you to main menu.")

        #Exiting to do list section
        elif choice == '5':
            print("Exiting the To-Do List. Thank you :)")
            break 
        else:
            print("Invalid choice. Please choose from the listed options.")

if __name__ == "__main__":
    main()

            
