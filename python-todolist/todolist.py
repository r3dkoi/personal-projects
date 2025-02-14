def main():
    """Holds all our tasks
    A while True loop used to keep program running until
    user decides to exit.

    User is prompted to input their choice
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
                print(f"{current_index}.{task_description}: {status}.")
                
            
