#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
import os


def get(Nompatient, entree, Birthvalue, Birthentree):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox == 1:
        Nompatient = entree.get()
        Birthvalue = Birthentree.get()
        print(Nompatient)
        print(entree.get())
        print(Birthvalue)
        print(Birthentree.get())
        testExistFile()
        gui.destroy()
    else:           
        NoforQ = messagebox.showinfo('Return', 'Data not saved')

def testExistFile():
    try:
        if os.path.getsize('./newpatient/entryfile2.txt'):
            print("+ File 'entryfile2.txt' exist !")
            with open('./newpatient/entryfile2.txt', 'a+') as namefile:
                namefile.write(entree.get() + '\n')
                namefile.write(Birthentree.get() + '\n')
                namefile.write(str('----------------\n'))
    except FileNotFoundError as outcom:
        print("+ Sorry, file 'entryfile2.txt' not exist !")
        print(str(outcom))
        print("+ File 'entryfile2.txt' created !")
        with open('./newpatient/entryfile2.txt', 'a+') as namefile:
            namefile.write(entree.get() + '\n')
            namefile.write(Birthentree.get() + '\n')
            namefile.write(str('----------------\n'))

gui=Tk()
gui.title("Enter new patient 2")
gui.configure(bg='gray17')
gui.geometry('300x200')

labelName = Label(gui)
labelName = Label(text='Enter Name : ', font="Times 14 bold", 
    fg='cyan', bg='gray17')
labelName.pack(pady=10)

Nompatient=StringVar()
Nompatient.set('Firstname + Lastname')
entree = Entry(gui, textvariable=Nompatient, highlightbackground='gray', bd=4)
entree.pack()

labelBirth = Label(gui)
labelBirth = Label(text='Birth Date : ', font="Times 14 bold",
    fg='cyan', bg='gray17')
labelBirth.pack(pady=10)

Birthvalue=StringVar()
Birthvalue.set('Format: 00/00/0000')
Birthentree = Entry(gui, textvariable=Birthvalue, highlightbackground='gray', bd=4)
Birthentree.pack()

bouton1 = Button(gui, text="Enter", width=8, fg='yellow', bg='navy',
    command = lambda: get(Nompatient, entree, Birthvalue, Birthentree))
bouton1.pack(side=LEFT, padx=30, pady=10)

buttQuit=Button(gui, text="Quit", width=8, fg='cyan', bg='navy', 
    command=quit)
buttQuit.pack(side=LEFT, padx=15, pady=10)

gui.mainloop()
