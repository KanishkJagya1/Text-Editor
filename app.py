from tkinter import *
from tkFileDialog import askopenfilename

filename = None

def newFile():
    global filename
    filename = "untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = askopenfilename(defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f = open(f, 'w')
        f.write(t)
        f.close()
    except:
        pass