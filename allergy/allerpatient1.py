#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
import os


def get(Allpatient, entryall):
    MsgBox = messagebox.askyesno('Save data', 'Data saved !')
    if MsgBox == 1:
        Allpatient = entryall.get()
        print(Allpatient)
        print(entryall.get())
        try:
            if os.path.getsize('./allergy/allergyfile.txt'):
                print("+ File 'allergyfile.txt' exist !")
                with open('./allergy/allergyfile.txt', 'a+') as namefile:
                    namefile.write(entryall.get() + '\n')
                    namefile.write(str('----------------\n'))
        except FileNotFoundError as outcom:
            print("+ Sorry, file 'allergyfile.txt' not exist !")
            print(str(outcom))
            print("+ File 'allergyfile.txt' created !")
            with open('./allergy/allergyfile.txt', 'a+') as namefile:
                namefile.write(entryall.get() + '\n')
                namefile.write(str('----------------\n'))
    else:           
        NoforQ = messagebox.showinfo('Return', 'Data not saved')

gui=Tk()
gui.title("Enter Allergy")
gui.configure(bg='gray17')
gui.geometry('300x200')

labelName = Label(gui)
labelName = Label(text='Enter Allergy : ', font="Times 14 bold", 
    fg='cyan', bg='gray17')
labelName.pack(pady=10)

Allpatient=StringVar()
Allpatient.set('Allergie')
entryall = Entry(gui, textvariable=Allpatient)
entryall.pack()

bouton1 = Button(gui, text="Enter", width=8, fg='yellow', bg='navy',
    command = lambda: get(Allpatient, entryall))
bouton1.pack(side=LEFT, padx=30, pady=10)

buttQuit=Button(gui, text="Quit", width=8, fg='cyan', bg='navy', 
    command=quit)
buttQuit.pack(side=LEFT, padx=15, pady=10)

gui.mainloop()
