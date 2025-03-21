import tkinter as tk

#Displaying a window on the screen
root = tk.Tk() #The main window in Tkinter = root, but you can rename it


#Places a label on the root window
message = tk.Label(root, text="Hello, World!")
message.pack() 

root.mainloop() #Ensures main window remains visible on screen. If you don't call this, the window will appear and disappear instantly. 
                #Allows the window to display and run until closed
                #Usually you place the mainloop as last statement after creating widgets
