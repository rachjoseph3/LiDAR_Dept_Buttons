#Collin's Button
#Collin can click this and it will randomly pick a pathfinder race and class and prestige class

import tkinter as tk
from tkinter import W, E
import random

#definitions
def runTheProgram():
    raceList = [
        "Human",
        "Dwarf",        
        "Elf",
        "Gnome",
        "Half-Elf",
        "Halfling",
        "Half-Orc",
        ]

    race = random.choice(raceList)

    classList = [
        "Barbarian",
        "Bard",
        "Cleric",
        "Druid",
        "Fighter",
        "Monk",
        "Paladin",
        "Ranger",
        "Rogue",
        "Sorcerer",
        "Wizard",
        ]
    clas = random.choice(classList)

    text.insert(tk.INSERT, "Race: {}, Class: {}\n".format(race, clas))

#GUI
master = tk.Tk()
master.title("Collin's Button")
master.configure(background = '#ccf2ff')

tk.Label(master, text="Hit Run for a random Pathfinder race, class, and prestige class.", anchor=E, background = '#ccf2ff').grid(row=0)

text = tk.Text(master)
text.grid(row=2, column=1)
#text.insert(tk.INSERT, ">>>")

tk.Button(master, text='Run', command=runTheProgram).grid(row=0, column=1, sticky=W, pady=4)
tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
tk.Button(master, text='Clear Text Box', command=text.delete(1.0,tk.END)).grid(row=3, column=1, sticky=W, pady=4)

tk.mainloop( )

