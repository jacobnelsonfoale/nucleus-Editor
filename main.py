## NT V 24.2 ##
## Source Code below is given as is and is subject to licence listed on github page ##


## IMPORT ##
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
import os


## FUNCTIONS ##
## When a button is pressed it most likely fires off a function displayed below ##

#Open File
def OpenFile():
    global currentFilePath
    
    file = filedialog.askopenfilename()
    root.title("Neu" + " - " + file)
    currentFilePath = file
    with open(file, 'r') as f:
        Text.delete(1.0,END)
        Text.insert(INSERT,f.read())

#New File
def NewFile():
    res = messagebox.askquestion('NT v23.1', 'Do you want to close current file?', icon="warning")
    if res == "yes":
        currentFilePath = ""
        root.title("NT - V24.2")
        Text.delete(1.0,END)
#New File Shortcut
def NewFileE(e):
    res = messagebox.askquestion('NT v23.1', 'Do you want to close current file?', icon="warning")
    if res == "yes":
        currentFilePath = ""
        root.title("NT - V24.2")
        Text.delete(1.0,END)

#About Menu
def AboutMessage():
    messagebox.showinfo("NT v24.2", "Created by Jacob Nelson-Foale\nID: 224004\nLightweight Text Editor For Python")

#Save File
def SaveFile():
    currentFilePath = filedialog.asksaveasfilename()
    with open(currentFilePath, 'w') as f:
        f.write(Text.get('1.0','end'))
        root.title("Neu" + " - " + currentFilePath)

#Change Log Menu
def ChangeLogMessage():
    messagebox.showinfo("Change Log", "v23.1\nFirst Release of NT. Features include Open File, Save File, New File Menus. This is the first build of Nucleus-Editor.\nv24.2 Stable\nAdded Edit and Help menu to top bar and added the scrollbar to textbox. First stable build of NT.")

def DocsMessage():
    messagebox.showinfo("Docs", "v24.2\nCurrently no documentation has been written yet. Visit https://jacobnelsonfoale.github.io/ for updates and consult the github page to make sure your nucleus-editor is up to date.") 


## SHORTCUTS ##
## Functions that are turned into shortcuts need to have a copy of them put here with a (e) paramiter to stop compiler from getting angry (I know not the best solution but it works) ##

#Save File Shortcut
def SaveFileE(e):
    currentFilePath = filedialog.asksaveasfilename()
    with open(currentFilePath, 'w') as f:
        f.write(Text.get('1.0','end'))
        root.title("Neu" + " - " + currentFilePath)

#Open File Shortcut
def OpenFileE(e):
    global currentFilePath
    
    file = filedialog.askopenfilename()
    root.title("Neu" + " - " + file)
    currentFilePath = file
    with open(file, 'r') as f:
        Text.delete(1.0,END)
        Text.insert(INSERT,f.read())


## GUI Elements ##
## This is where elements are initialized and drawn to the screen ##

#Make Window
root = Tk()  # create a root widget
root.title("NT - V24.2")
root.geometry("1000x700+50+50")  # width x height + x + y

#Keybind
root.bind('<Control-s>', SaveFileE)
root.bind('<Control-n>', NewFileE)
root.bind('<Control-o>', OpenFileE)

#TextBox
Text = scrolledtext.ScrolledText(root, wrap=WORD, width=500, height=400, undo=True)
Text.pack()


## TOPBAR MENU ##
## This is the code for the menubar ##

# DropDown Menu Init
menu = Menu(root)

# File FileMenu
fileDropdown = Menu(menu, tearoff=False)
fileDropdown.add_command(label='New     Ctrl + N', command=NewFile)
fileDropdown.add_command(label='Open    Ctrl + O', command=OpenFile)
fileDropdown.add_command(label='Save    Ctrl + S', command=SaveFile)
menu.add_cascade(label='File', menu=fileDropdown)

#Edit FileMenu
editFiledropdown = Menu(menu, tearoff=False)
editFiledropdown.add_command(label="Undo", command=Text.edit_undo)
editFiledropdown.add_command(label="Redo", command=Text.edit_redo)
menu.add_cascade(label="Edit", menu=editFiledropdown)

#Help FileMenu
helpFiledropdown = Menu(menu, tearoff=False)
helpFiledropdown.add_command(label="Docs", command=DocsMessage)
helpFiledropdown.add_command(label="Change Log", command=ChangeLogMessage)
helpFiledropdown.add_command(label="About", command=AboutMessage)
menu.add_cascade(label="Help", menu=helpFiledropdown)

#Set Menu to be Main Menu
root.config(menu=menu)

## KEEP PROGRAM RUNNING ##
root.mainloop()
