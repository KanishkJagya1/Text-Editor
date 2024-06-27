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
        f = open(filename, 'w')
        f.write(t)
        f.close()

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
root.maxsize(width=1000, height=1000)

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
