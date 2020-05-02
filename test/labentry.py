# Python 3, Tkinter 8.6
# Display Entry in a Label
 
from tkinter import * 
#!/usr/bin/python3
# -*-coding:utf-8-*- 

from tkinter import *

root = Tk()
 
def returnEntry(arg=None):
    """Gets the result from Entry and return it to the Label"""
 
    result = myEntry.get()
    resultLabel.config(text=result)
    myEntry.delete(0,END)
 
# Create the Entry widget
myEntry = Entry(root, width=20)
myEntry.focus()
myEntry.bind("<Return>",returnEntry)
myEntry.pack()
 
# Create the Enter button
enterEntry = Button(root, text= "Enter", command=returnEntry)
enterEntry.pack(fill=X)
 
# Create and emplty Label to put the result in
resultLabel = Label(root, text = "")
resultLabel.pack(fill=X)
 
 
root.geometry("+750+400")
 
root.mainloop()
