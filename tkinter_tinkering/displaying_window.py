import tkinter as tk
from tkinter import ttk #Imports classic and new Tk themed widgets
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

#Displaying a window on the screen
root = tk.Tk() #The main window in Tkinter = root, but you can rename it

root.title('Tkinter Window Demo')

 #Changes window size and the position to 50 px from top and left of screen
root.geometry('600x400+50+50')

#Ttk label testing
ttk.Button(root, text='Button').pack()
ttk.Checkbutton(root, text='Checkbutton').pack()
ttk.Entry(root, text='Entry').pack()
ttk.Menubutton(root, text='Menubutton').pack()
ttk.Radiobutton(root, text="Radiobutton").pack()
ttk.Spinbox(root, text="Spinbox").pack()
ttk.Combobox(root, text="Combobox").pack()


#Places a classic label on the root window
message = tk.Label(root, text="Window Display Testing :)")
message.pack() 



root.mainloop() #Ensures main window remains visible on screen. If you don't call this, the window will appear and disappear instantly. 
                #Allows the window to display and run until closed
                #Usually you place the mainloop as last statement after creating widgets
