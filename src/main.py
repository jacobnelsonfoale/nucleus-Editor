from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
import os

#Open File
def OpenFile():
    global currentFilePath
    # Opening a File
    file = filedialog.askopenfilename()
    root.title("Neu" + " - " + file)
    currentFilePath = file
    with open(file, 'r') as f:
        Text.delete(1.0,END)
        Text.insert(INSERT,f.read())

#Save file
def SaveFile():
    currentFilePath = filedialog.asksaveasfilename()
    with open(currentFilePath, 'w') as f:
        f.write(Text.get('1.0','end'))
        root.title("Neu" + " - " + currentFilePath)


#Make Window
root = Tk()  # create a root widget
root.title("Nucleolus Text")
root.geometry("1000x700+50+50")  # width x height + x + y


#Open File Button
OpenFileButton = Button(root, text="Open File", command=OpenFile)
OpenFileButton.grid(row=0, column=0)

#Save File Button
SaveFileButton = Button(root, text="Save File", command=SaveFile)
SaveFileButton.grid(row=0, column=1)

#Text Editor
Text = Text(root, width=500, height=400)
Text.grid(row=0, column=0)

# DropDown Men
menu = Menu(root)
fileDropdown = Menu(menu, tearoff=False)
# Add Commands and and their callbacks
fileDropdown.add_command(label='New')
fileDropdown.add_command(label='Open', command=OpenFile)
fileDropdown.add_separator()
fileDropdown.add_command(label='Save', command=SaveFile)
fileDropdown.add_command(label='About')
menu.add_cascade(label='File', menu=fileDropdown)
# Set Menu to be Main Menu
root.config(menu=menu)


#Keep Window Open
root.mainloop()
