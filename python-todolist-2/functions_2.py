"""CORE Functions file for the to-do list
"""


def adding_tasks(tasks): #Will be altering the tasks variable
    print("==== ADDING TASKS ====")
    while True:
        try:
            n_tasks = int(input("How many tasks would you like to add: "))
            break #Ends while loop and disregards except block
        except ValueError:
            print("Please enter a valid number.")
    for i in range(n_tasks): #Creates task list that ends on amount user had inputted
        task = input("Please enter task description: ")
        tasks.append({
            "Task": task,
            "done": False
        }) #Status is set to false initially.

def show_tasks(tasks):
    print("==== SHOW TASKS ====")
    if not tasks:
        print("No tasks to show. Add some now.")
    else:
        print("Your current tasks: ")
        for index, task in enumerate(tasks): #Shows index with the key pair values
            if task["done"]:  #Takes the key done value from adding_tasks 
                status = "Done"
            else:
                status = "Not done"
            current_index = index + 1 #increments index no. by 1 depending on range from n_tasks
            task_description = task["Task"] #Accesses the task value inputted by the user from adding_tasks's dictionary.
            print(f"{current_index}. Task: {task_description}. Status: {status}.")

def delete_tasks(tasks):
    print("==== DELETE TASKS ====")
    if not tasks: 
        print("No tasks to delete.")
    else:
            try:
                task_deleted = int(input("Choose the task's number that you wish to delete: ")) - 1 #Adjusts for 0-based indexing
                if 0 <= task_deleted and task_deleted < len(tasks): #Checks if the number the user inputted is in the index range of the task list
                   deleted_task_display = tasks[task_deleted]["Task"] #Accesses task list and the created task is selected via the inputted index value
                   print(f"The task: '{deleted_task_display}' has been deleted.")
                   del tasks[task_deleted] #Removes specified index from the list
                   
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please select a valid number from the task list.")

def marking_tasks(tasks):
    print "==== MARKING TASKS ===="
    if not tasks:
        print("No tasks to mark as complete.")
    else:
        try:
            marked_task = int("Choose the task number you wish to mark as complete: ")
            if marked_task IN tasks:
                marked_task_display =  tasks[marked_task]["Task"] #Accesses task list and the key Task that matches the user input index value is selected to be marked.
                print (f"Task: {marked_task_display} is marked as complete. Well done!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please select a valid number from the task list.")
