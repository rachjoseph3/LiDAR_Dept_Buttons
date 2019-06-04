#Kyle's Button
#Kyle can click this and it will tell him everything looks right

import tkinter as tk
from tkinter import W, E

#definitions
def runTheProgram():
    text.insert(tk.INSERT, "Everything looks right!\n")

#GUI
master = tk.Tk()
master.title("Kyle's Button")
master.configure(background = '#ccf2ff')

tk.Label(master, text="Ask me a question and I will tell you if it looks right: ", anchor=E, background = '#ccf2ff').grid(row=0)

text = tk.Text(master)
text.grid(row=3, column=1)
text.insert(tk.INSERT, ">>>")

e1 = tk.Entry(master, width=120)

e1.grid(row=0, column=1)

tk.Button(master, text='Run', command=runTheProgram).grid(row=4, column=1, sticky=W, pady=4)
tk.Button(master, text='Quit', command=master.quit).grid(row=4, column=2, sticky=W, pady=4)

tk.mainloop( )
