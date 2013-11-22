from Tkinter import *
import tkMessageBox
import subprocess


def openNext():
	subprocess.Popen(" python execute.py", shell=True)

def openThisWeek():
	subprocess.Popen(" python execute-edit.py", shell=True)

def openSingleCat():
	subprocess.Popen(" python execute-edit-day.py", shell=True)

def openFiles(selection):
	if selection == 'Next Week':
		subprocess.call(" python execute.py", shell=True)
	elif selection == 'This Week':
		subprocess.call(" python execute-edit.py", shell=True)
	else:
		subprocess.Popen(" python execute-edit-day.py", shell=True)
	return

def aboutMe():
	pass


app = Tk()
app.title('Feature Category Getters')
app.geometry('450x300+100+100')

menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label = "Next Week", command = openNext)
filemenu.add_command(label = "This Week", command = openThisWeek)
filemenu.add_command(label = "Single Category", command = openSingleCat)



filemenu.add_separator()

filemenu.add_command(label = "Quit", command = app.quit)
menubar.add_cascade(label = "File", menu = filemenu)

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_cascade(label = "About Me", command = aboutMe)
menubar.add_cascade(label = "Help", menu = helpmenu)

app.config(menu = menubar)

featureCatFiles = StringVar()
featureCatFiles.set("Select Your Feature Category Process")
files = ['Next Week', 'This Week', "Single Category"]
featureCatDropDown = OptionMenu(app, featureCatFiles, *files, command = openFiles).pack()


# labeltext = StringVar()
# labeltext.set('Click Button')
# label1 = Label(app, textvariable = labeltext, height = 4)
# label1.pack()

# checkBoxVal = IntVar()
# checkBox1 = Checkbutton(app, variable = checkBoxVal, text = "Happy?")
# checkBox1.pack()
myButton1 = Button(app, text = 'Next Week', width = 20, command = openNext)
myButton1.pack(side = 'bottom', padx = 15, pady = 15)
myButton2 = Button(app, text = 'This Week', width = 20, command = openThisWeek)
myButton2.pack(side = 'bottom', padx = 15, pady = 15)
myButton3 = Button(app, text = 'Single Category', width = 20, command = openSingleCat)
myButton3.pack(side = 'bottom', padx = 15, pady = 15)

app.mainloop()

