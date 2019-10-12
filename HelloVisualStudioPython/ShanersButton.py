#Shane's Button
#User can select what day of the week it is and the button will tell you what percent brainer we're at

import tkinter as tk
from tkinter import W, E

#weekList
weekList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

#definitions
def run():
	day = master.listbox.get(tk.ACTIVE)
	if day == weekList[0]:#Monday
		brainer = 100
	if day == weekList[1]:#Tuesday
		brainer = 75
	if day == weekList[2]:#Wednesday
		brainer = 50
	if day == weekList[3]:#Thursday
		brainer = 25
	if day == weekList[4]:#Friday
		brainer = 0
	
	beerA = beer.get()
	if beerA == 0:
		beerer = "No Beer was had."
	if beerA ==1:
		beerer = "Beer was had!!"

	hockeyA = hockey.get()
	if hockeyA == 0:
		hockeyer = "No hockey was played."
	if hockeyA ==1:
		hockeyer = "Hockey was played!!"
	text.insert(tk.INSERT, "We are at {}% Brainer! {} {}\n".format(brainer, beerer, hockeyer))

#GUI
master = tk.Tk()
master.title("Shaner's Button")
master.configure(background = '#ccf2ff')

#week day list
tk.Label(master, text="Select the day of the week and hit run:", anchor=E, background = '#ccf2ff').grid(row=0, column=0)
master.listbox = tk.Listbox(master)
master.listbox.grid(row=2, column=0, sticky='NS')
for item in weekList: #adding run names to the list in the main window
	master.listbox.insert(tk.END, item)

beer = tk.IntVar()
tk.Checkbutton(master, text="Beer", variable=beer).grid(row=1, column=0, sticky=W)
hockey = tk.IntVar()
tk.Checkbutton(master, text="Hockey", variable=hockey).grid(row=1, column=1, sticky=W)

text = tk.Text(master)
text.grid(row=2, column=3)
text.insert(tk.INSERT, ">>>")

tk.Button(master, text='Run', command=run).grid(row=0, column=1, sticky=W, pady=4)
tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=4, sticky=W, pady=4)

tk.mainloop( )
