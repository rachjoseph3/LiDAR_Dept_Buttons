#Zach's Button
#Zach can click this and it will tell him to take time off

import tkinter as tk
from tkinter import W, E

#definitions
def runTheProgram():
    text.insert(tk.INSERT, "TAKE A VACATION!!\n")

#GUI
master = tk.Tk()
master.title("Zach's Button")
master.configure(background = '#ccf2ff')

tk.Label(master, text="Hey Zach! Click this button! -> ", anchor=E, background = '#ccf2ff').grid(row=0)

text = tk.Text(master)
text.grid(row=1, column=1)

tk.Button(master, text='Run', command=runTheProgram).grid(row=0, column=1, sticky=W, pady=4)
tk.Button(master, text='Quit', command=master.quit).grid(row=2, column=1, sticky=W, pady=4)

tk.mainloop( )
