#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
import subprocess
import time
from tkinter import messagebox


def saveData():
    """
    No need to test if file
    exist or not. Already test
    it before.
    """
    with open('./auxsrc/doc_auxsrc4/auxsrcfile4.txt', 'a+') as filerecord:
        filerecord.write(textBox.get("1.0", "end-1c") + "\n\n")

def messFromSafeButt():
    """
    Message of confirmation
    with messagebox.
    """
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        saveData()
        textBox.insert(INSERT, "\n---Data saved !---")
        print("+ Data saved !")
    else:
        textBox.insert(INSERT, "Nothing has been saved !")
        print("+ Nothing has been saved !")

def readerFile():
    """
    To read into the txt file.
    """
    subprocess.call('./auxsrc/doc_auxsrc4/aux_read.py')

def addText():
    """
    Display text into widget Text
    before to add comment.
    """
    textBox.delete('1.0', END)
    textBox.insert(INSERT, "Dated : ")
    textBox.insert(END, time.strftime("%d/%m/%Y at %H:%M:%S :") + '\n')
    textBox.update()

def importationFile(fichier, encodage="Utf-8"):
    """
    First display of txt file
    when the user start app.
    """
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

with open('./newpatient/entryfile4.txt', 'r') as filename:
    line1=filename.readline()

root=Tk()
root.title("Auxiliary resources")
root.configure(background='#82193e')

# To place side by side labelo + entrylab
top = Frame(root, bg='#82193e')
bottom = Frame(root, bg='#82193e')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(root, text="Auxiliary resources : ",
    font='Arial 18 bold', fg='cyan', bg='#82193e')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

textname=StringVar()
entryName=Entry(root, textvariable=textname)
textname.set(line1)
entryName.pack(in_=top, side=LEFT, padx=10, pady=20)

textBox=Text(root, height=15, width=60, font=18, relief=SUNKEN)
textBox.insert(INSERT, "\nDated : ")
textBox.insert(END, time.strftime("%d/%m/%Y at %H:%M:%S :\n"))
textBox.pack(padx=30, pady=30)

buttonLire=Button(root, text="Read", width=8, bd=3,
    fg='cyan', bg='navy', activebackground='dark turquoise',
    highlightbackground='grey17', command=readerFile)
buttonLire.pack(side='left', padx=10, pady=10)

buttonEffacer=Button(root, text="1-Add", width=8, bd=3,
    fg='yellow', bg='navy', activebackground='dark turquoise',
    highlightbackground='grey17', command=addText)
buttonEffacer.pack(side='left', padx=10, pady=10)

buttonEnter=Button(root, text="2-Save", width=8, bd=3, 
    fg='yellow', bg='navy', activebackground='dark turquoise',
    highlightbackground='grey17', command=messFromSafeButt)
buttonEnter.pack(side='left', padx=10, pady=10)

buttonQuitter=Button(root, text="Quit", width=8, bd=3,
    fg='white', bg='navy', activebackground='dark turquoise', 
    highlightbackground='grey17', command=quit)
buttonQuitter.pack(side='right', padx=10, pady=10)

importationFile('./auxsrc/doc_auxsrc4/auxsrcfile4.txt',
    encodage="Utf-8")

mainloop()
