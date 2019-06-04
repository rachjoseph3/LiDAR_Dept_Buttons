# -*- coding: cp1252 -*-
#Mike's Button
#Mike can click this and it will tell him everything is going to be ok

import tkinter as tk
from tkinter import W, E
import random

#definitions
def clearTheField():
    e1.delete(0,tk.END)

def runTheProgram():
    phrase = [
        "Everything is going to be OK!\n",
        "Breathe\n",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill\n",
        "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis\n",
        "It's not whether you get knocked down. It's whether you get up. - Vince Lombardi\n",
        "The harder you work for something, the greater you'll feel when you achieve it.\n",
        "Let's take three deep breaths.\n",
        "You're going to be OK\n",
        "Calmness is the cradle of power. - Josiah Gilbert Holland\n",
        ]
    text.insert(tk.INSERT, random.choice(phrase))
    clearTheField()

#GUI
master = tk.Tk()
master.title("Mike's Button")
master.configure(background = '#5fb6f4')

tk.Label(master, text="Tell me what's wrong then click the Run button to send it to the void: ", anchor=E, background = '#5fb6f4').grid(row=0)

text = tk.Text(master)
text.grid(row=3, column=1)
text.insert(tk.INSERT, ">>>")

e1 = tk.Entry(master, width=90)

e1.grid(row=0, column=1)

tk.Button(master, text='Run', command=runTheProgram).grid(row=4, column=1, sticky=W, pady=4)
tk.Button(master, text='Quit', command=master.quit).grid(row=4, column=2, sticky=W, pady=4)

tk.mainloop( )
