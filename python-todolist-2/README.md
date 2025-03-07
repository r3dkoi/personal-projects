### WELCOME TO THE PROJECT REPORT ####

1. Project Overview
This program is designed to be a to-do list performed solely on a command-line interface (CLI) if ported as a .exe file OR within a terminal of a Integrated Development Environment (IDE) such as Visual Studio Code.

It's current purpose is to just store tasks and/or activities the user needs to complete, and present it to them in a ordered list format.

I created this program because I always use a to-do list myself in my day-to-day life and wish to discover how they are programmed.

It's current features include:
    - Adding tasks to the to-do list
    - Showing the total list of tasks, it's description and status
    - Marking tasks as complete
    - Deleting tasks, whether they're incomplete or complete
    - Exiting the program 


2. Program Structure & Logic [A Flow-chart is provided in the Project_overview folder, named Todolist.drawio.png]

Programming language used: Python

Main Components involve:
    1. Main Menu
        Where the program begins, and the user is prompted to begin the main loop of the program
    2. Task Management
        Task Storage: Tasks are loaded from a JSON file and/or saved.
        Task Operations: Run from main functions file
                - Adding tasks
                - Removing tasks
                - Marking tasks as complete
                - Deleting tasks
                - Exiting program
                - Saving tasks to JSON file
                - Loading tasks from JSON file to program
    3. User interface
        Input handling: User commands, often in form of integers to progress through the program. Only strings are allowed for task descriptions.
        Output display: Through the showing tasks option (Option 2), which should show the current list of tasks to the user in a ordered and numbered list (Ascending-Descending).
    4. 
