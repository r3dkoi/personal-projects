"""CORE Functions file for the to-do list
"""

import sys, json

def adding_tasks(tasks): #Will be altering the tasks variable
    print("==== ADDING TASKS ====")
    if go_back():
        return #Exits the function and returns to main menu
    while True:
        try:
            n_tasks = int(input("How many tasks would you like to add: "))
            if n_tasks <= 10:
                break #Ends while loop and disregards except block
            else:
                print("Sorry, I can only let you add up to 10 tasks and no more. Thanks for understanding!")
        except ValueError:
            print("Please enter a valid number.")
    for i in range(n_tasks): #Creates task list that ends on amount user had inputted
        task = input("Please enter task description: ")
        tasks.append({
            "Task": task, 
            "done": False
        }) #Adding user inputted task to the task list. Status is set to false initially. 
    save_tasks_to_file(tasks) #Saves data and writes it into json.file

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
    if go_back():
        return
    elif not tasks: 
        print("No tasks to delete.")
    else:
            try:
                task_deleted = int(input("Choose the task's number that you wish to delete: ")) - 1 #Adjusts for 0-based indexing
                if 0 <= task_deleted and task_deleted < len(tasks): #Checks if the number the user inputted is in the index range of the task list
                    deleted_task_display = tasks[task_deleted]["Task"] #Accesses task list and the created task is selected via the inputted index value
                    print(f"The task: '{deleted_task_display}' has been deleted.")
                    del tasks[task_deleted] #Removes task at the specified index from the list
                    save_tasks_to_file(tasks)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please select a valid number from the task list.")

def marking_tasks(tasks):
    print ("==== MARKING TASKS ====")
    if go_back():
        return
    elif not tasks:
        print("No tasks to mark as complete.")
    else:
            try:
                marked_task = int(input("Choose the task number you wish to mark as complete: ")) - 1
                if 0 <= marked_task and marked_task < len(tasks):
                    marked_task_display =  tasks[marked_task]["Task"] #Accesses task list and the key Task that matches the user input index value is selected to be marked.
                    print (f"Task: {marked_task_display} is marked as complete. Well done!")
                    tasks[marked_task]["done"] =  True #Accesses the value at index position of marked_task and sets the key of "done" as True to trigger the change of "status" in the show_tasks
                    save_tasks_to_file(tasks)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please select a valid number from the task list.")

def exit_program():
    global tasklist_loop
    print(" ==== EXIT ====")
    print("Thank you for using this program!")
    print("See you later :)")
    sys.exit() #Terminates the program
    
def save_tasks_to_file(tasks, filename="C:\\Users\\sofoc\\repos\\personal-projects\\python-todolist-2\\stored_data.json"):
    with open(filename, "w") as file: #Writes into json file
        json.dump(tasks, file, indent=4) #Data input from main will be written into stored_data.json 
                                        #indenting it by 4 makes it easier to read

def load_tasks_to_file(filename="C:\\Users\\sofoc\\repos\\personal-projects\\python-todolist-2\\stored_data.json"):
    try:
        with open(filename, "r") as file: #Reads json file only
            return json.load(file)
    except FileNotFoundError: #If json.file is not detected
        print("File not found. Returning an empty list.")  # Debug print
        return []

def go_back():
    while True:
        choice = input("Did you accidentally press this option and wish to go back? If yes, select Y. If not, press N: ").lower() #Made it case-insensitive
        if choice.isalpha(): # Check if the input is a string
            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print("Please enter a valid option (Y/N).")
        else:
            print("Invalid input. Please enter a valid option (Y/N).")
