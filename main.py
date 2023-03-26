from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
import os

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
        root.title("Nucleolus Text - V23.1")
        Text.delete(1.0,END)
#New File Shortcut
def NewFileE(e):
    res = messagebox.askquestion('NT v23.1', 'Do you want to close current file?', icon="warning")
    if res == "yes":
        currentFilePath = ""
        root.title("Nucleolus Text - V23.1")
        Text.delete(1.0,END)

#About Menu
def AboutMessage():
    messagebox.showinfo("NT v23.1", "\nNT v23.1\n\nDeveloper: Dunn-Dev8\n\nID: 223001\n\nSimple Hackable Editor For Python\n")

#Save File
def SaveFile():
    currentFilePath = filedialog.asksaveasfilename()
    with open(currentFilePath, 'w') as f:
        f.write(Text.get('1.0','end'))
        root.title("Neu" + " - " + currentFilePath)
#Save File Shortcut
def SaveFileE(e):
    currentFilePath = filedialog.asksaveasfilename()
    with open(currentFilePath, 'w') as f:
        f.write(Text.get('1.0','end'))
        root.title("Neu" + " - " + currentFilePath)

#Make Window
root = Tk()  # create a root widget
root.title("Nucleolus Text - V23.1")
root.geometry("1000x700+50+50")  # width x height + x + y

#Keybind
root.bind('<Control-s>', SaveFileE)
root.bind('<Control-n>', NewFileE)

#Open File Button
OpenFileButton = Button(root, text="Open File", command=OpenFile)
OpenFileButton.grid(row=0, column=0)

#Save File Buttontex.delete('1.0', END)
SaveFileButton = Button(root, text="Save File", command=SaveFile)
SaveFileButton.grid(row=0, column=1)

#TextBox
Text = Text(root, width=500, height=400)
Text.grid(row=0, column=0)

# DropDown Menu FILE
menu = Menu(root)
fileDropdown = Menu(menu, tearoff=False)

fileDropdown.add_command(label='New', command=NewFile)
fileDropdown.add_command(label='Open', command=OpenFile)
fileDropdown.add_separator()
fileDropdown.add_command(label='Save', command=SaveFile)
fileDropdown.add_command(label='About', command=AboutMessage)
menu.add_cascade(label='File', menu=fileDropdown)
# Set Menu to be Main Menu
root.config(menu=menu)

#DropDown Menu EDIT

root.mainloop()