"""CORE Functions file for the to-do list
"""

def adding_tasks(tasks): #Will be altering the tasks variable
    print("/n ==== ADDING TASKS ====")
    while True:
        try:
            n_tasks = int(input("How many tasks would you like to add: "))
            break #Ends while loop and disregards except block
        except ValueError:
            print("Please enter a valid number.")
    for i in range(n_tasks): #Creates task list that ends on amount user had inputted
        task = input("Please enter task description").lower
        tasks.append({
            "Task:", task,
            "done:", False
        }) #Status is set to false initially.

        
