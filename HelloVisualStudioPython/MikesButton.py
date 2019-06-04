#Mike's Button
#Mike can click this and it will tell him everything is going to be ok

import tkinter as tk
from tkinter import W, E
#import random

#definitions
def runTheProgram():
    text.insert(tk.INSERT, "Everything is going to be OK!\n")

#GUI
master = tk.Tk()
master.title("Mike's Button")
master.configure(background = '#ccf2ff')

tk.Label(master, text="Tell me what's wrong and I will let you know how things are going to be: ", anchor=E, background = '#ccf2ff').grid(row=0)

text = tk.Text(master)
text.grid(row=3, column=1)
text.insert(tk.INSERT, ">>>")

e1 = tk.Entry(master, width=120)

e1.grid(row=0, column=1)

tk.Button(master, text='Run', command=runTheProgram).grid(row=4, column=1, sticky=W, pady=4)
tk.Button(master, text='Quit', command=master.quit).grid(row=4, column=2, sticky=W, pady=4)

tk.mainloop( )
