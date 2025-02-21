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
        task = input("Please enter task description: ").lower
        tasks.append({
            "Task:", task,
            "done:", False
        }) #Status is set to false initially.

def show_tasks(tasks):
    print("==== SHOW TASKS ====")
    if tasks == 0:
        print("No tasks to show. Add some now.")
    else:
        print("Your current tasks: ")
        for index, task in enumerate(tasks): #Shows index with the key pair values
            if task[done]: 
                print("Done")
            else:
                print("Not done")
            current_index = index + 1 #increments index no. by 1 depending on range from n_tasks
            task_description = task #Takes the task value from adding_tasks
            status = done #Takes the key done value from adding_tasks 
            print(f"{current_index}. Task: {task_description}. Status: {status}.")


        
