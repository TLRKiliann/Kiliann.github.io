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
            if os.path.getsize('./allergy/allergyfile5.txt'):
                print("+ File 'allergyfile5.txt' exist !")
                with open('./allergy/allergyfile5.txt', 'a+') as namefile:
                    namefile.write(entryall.get() + '\n')
                    namefile.write(str('----------------\n'))
        except FileNotFoundError as outcom:
            print("+ Sorry, file 'allergyfile5.txt' not exist !")
            print(str(outcom))
            print("+ File 'allergyfile5.txt' created !")
            with open('./allergy/allergyfile5.txt', 'a+') as namefile:
                namefile.write(entryall.get() + '\n')
                namefile.write(str('----------------\n'))
    else:           
        NoforQ = messagebox.showinfo('Return', 'Data not saved')

gui=Tk()
gui.title("Enter Allergy")
gui.configure(bg='gray17')
#gui.geometry('250x200')

labelName = Label(gui)
labelName = Label(text='Enter Allergy', font="Times 16 bold", 
    fg='cyan', bg='gray17')
labelName.pack(pady=10)

Allpatient=StringVar()
Allpatient.set('Allergy no-food')
entryall = Entry(gui, textvariable=Allpatient, highlightbackground='gray', bd=4)
entryall.pack(pady=10)

bouton1 = Button(gui, text="Save", width=8, fg='yellow', bg='navy',
    command = lambda: get(Allpatient, entryall))
bouton1.pack(side=LEFT, padx=10, pady=10)

buttQuit=Button(gui, text="Quit", width=8, fg='cyan', bg='navy', 
    command=quit)
buttQuit.pack(padx=10, pady=10)

gui.mainloop()
