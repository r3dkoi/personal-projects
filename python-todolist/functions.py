## Functions file for to-do list

def adding_tasks():
            while True:
                print()
                try:
                        n_tasks = int(input("How many tasks do you want to add: "))
                        break
                except ValueError:
                        print("Please enter a valid number.")
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
             return tasks

def showing_tasks(tasks):
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
        return tasks

