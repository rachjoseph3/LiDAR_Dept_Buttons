
import tkinter as tk
from tkinter import W, E
import random

#definitions

def kyle():
    def runTheProgramKyle():
        text.insert(tk.INSERT, "Everything looks right!\n")

    #GUI
    master = tk.Toplevel()
    master.title("Kyle's Button")
    master.configure(background = '#ccf2ff')
    
    tk.Label(master, text="Ask me a question and I will tell you if it looks right: ", anchor=E, background = '#ccf2ff').grid(row=0)
    
    text = tk.Text(master)
    text.grid(row=3, column=1)
    text.insert(tk.INSERT, ">>>")
    
    e1 = tk.Entry(master, width=120)
    e1.grid(row=0, column=1)
    
    tk.Button(master, text='Run', command=runTheProgramKyle).grid(row=4, column=1, sticky=W, pady=4)
    #tk.Button(master, text='Quit', command=master.quit).grid(row=4, column=2, sticky=W, pady=4)
    
    tk.mainloop( )


def mike():
    def clearTheField():
        e1.delete(0,tk.END)

    def runTheProgramMike():
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
            "May your sour cream be care free and your sauerkraut feminine\n",
            ]
        text.insert(tk.INSERT, random.choice(phrase))
        clearTheField()

    #GUI
    master = tk.Toplevel()
    master.title("Mike's Button")
    master.configure(background = '#5fb6f4')
    
    tk.Label(master, text="Tell me what's wrong then click the Run button to send it to the void: ", anchor=E, background = '#5fb6f4').grid(row=0)
    
    text = tk.Text(master)
    text.grid(row=3, column=1)
    text.insert(tk.INSERT, ">>>")
    
    e1 = tk.Entry(master, width=90)
    
    e1.grid(row=0, column=1)
    
    tk.Button(master, text='Run', command=runTheProgramMike).grid(row=4, column=1, sticky=W, pady=4)
    #tk.Button(master, text='Quit', command=master.quit).grid(row=4, column=2, sticky=W, pady=4)
    
    tk.mainloop( )
