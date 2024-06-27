# Simple Text Editor

This is a simple text editor application made using Python's `tkinter` library. It allows you to create, open, edit, and save text files. Below is the detailed explanation of the code and how to use the application.

## Features
- Create a new file
- Open an existing file
- Save the current file
- Save the current file with a new name
- Simple and intuitive graphical user interface

## Requirements
- Python 3.x
- `tkinter` library (comes pre-installed with Python)

## Code Explanation

The following is the complete code for the simple text editor:

```python
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showerror

filename = None

def newFile():
    global filename
    filename = "untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    if filename == "untitled":
        saveAs()
    else:
        t = text.get(0.0, END)
        with open(filename, 'w') as f:
            f.write(t)

def saveAs():
    global filename
    f = asksaveasfilename(defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        with open(f, 'w') as file:
            file.write(t)
        filename = f
    except Exception as e:
        showerror(title="Oops!", message="Unable to save file...")

def openFile():
    global filename
    f = askopenfilename(defaultextension='.txt')
    try:
        with open(f, 'r') as file:
            text.delete(0.0, END)
            text.insert(0.0, file.read())
        filename = f
    except Exception as e:
        showerror(title="Oops!", message="Unable to open file...")

root = Tk()
root.title("Simple Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.pack()

menuBar = Menu(root)
filemenu = Menu(menuBar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menuBar.add_cascade(label="File", menu=filemenu)

root.config(menu=menuBar)
root.mainloop()
```

## Detailed Breakdown

### Importing Required Libraries
```python
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showerror
```
We import the necessary modules from `tkinter` which is the standard GUI library for Python. We also import `askopenfilename` and `asksaveasfilename` for file dialogs, and `showerror` for error messages.

### Global Variable
```python
filename = None
```
We define a global variable `filename` to keep track of the current file.

### Defining Functions

#### New File
```python
def newFile():
    global filename
    filename = "untitled"
    text.delete(0.0, END)
```
This function clears the text area to create a new file and sets `filename` to "untitled".

#### Save File
```python
def saveFile():
    global filename
    if filename == "untitled":
        saveAs()
    else:
        t = text.get(0.0, END)
        with open(filename, 'w') as f:
            f.write(t)
```
This function saves the current file. If the file is untitled, it calls `saveAs()` to prompt the user to save the file with a new name.

#### Save As
```python
def saveAs():
    global filename
    f = asksaveasfilename(defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        with open(f, 'w') as file:
            file.write(t)
        filename = f
    except Exception as e:
        showerror(title="Oops!", message="Unable to save file...")
```
This function prompts the user to save the file with a new name and handles any errors that may occur.

#### Open File
```python
def openFile():
    global filename
    f = askopenfilename(defaultextension='.txt')
    try:
        with open(f, 'r') as file:
            text.delete(0.0, END)
            text.insert(0.0, file.read())
        filename = f
    except Exception as e:
        showerror(title="Oops!", message="Unable to open file...")
```
This function opens an existing file and handles any errors that may occur.

### Setting Up the GUI
```python
root = Tk()
root.title("Simple Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.pack()

menuBar = Menu(root)
filemenu = Menu(menuBar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menuBar.add_cascade(label="File", menu=filemenu)

root.config(menu=menuBar)
root.mainloop()
```
This section initializes the main window, sets up the text area, and creates the menu bar with file options.

## Usage

1. **New File**: Click on `File > New` to create a new file.
2. **Open File**: Click on `File > Open` to open an existing file.
3. **Save File**: Click on `File > Save` to save the current file.
4. **Save As**: Click on `File > Save As` to save the current file with a new name.
5. **Quit**: Click on `File > Quit` to exit the application.


## Conclusion

This simple text editor demonstrates the basic usage of `tkinter` for creating a GUI application in Python. It covers fundamental operations like creating, opening, and saving files, and provides a user-friendly interface for text editing.

Feel free to enhance and customize this editor according to your needs. Happy coding!
