#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
import os


gui=Tk()
gui.title("Enter new patient")
gui.configure(bg='gray17')
gui.geometry('300x200')

def get(Nompatient, entree, Birthvalue, Birthentree):
    """
    Test at first time and
    after when file was earased
    """
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox == 1:
        Magicword = "----------------"
        Nompatient = entree.get()
        Birthvalue = Birthentree.get()
        print(Nompatient)
        print(entree.get())
        print(Birthvalue)
        print(Birthentree.get())
        try:
            if os.path.getsize('./newpatient/entryfile.txt'):
                print("+ File 'entryfile.txt' exist !")
                with open('./newpatient/entryfile.txt', 'r') as filer:
                    lines = filer.readlines()
                    for i in range(len(lines)):
                        line = lines[i]
                        if Magicword in line:
                            print(Magicword)
                            with open('./newpatient/entryfile.txt', 'w') as filew:
                                filew.write(entree.get() + '\n')
                                filew.write(Birthentree.get() + '\n')
                                filew.write(str('---\n'))
        except FileNotFoundError as outcom6:
            print("+ Sorry, file 'entryfile.txt' not exist !")
            print(str(outcom6))
            print("+ File 'entryfile.txt' created !")
            with open('./newpatient/entryfile.txt', 'a+') as namefile:
                namefile.write(entree.get() + '\n')
                namefile.write(Birthentree.get() + '\n')
                namefile.write(str('---\n'))
        try:
            if os.path.getsize('./newpatient/entryfile2.txt'):
                print("+ File 'entryfile2.txt' exist !")
                with open('./newpatient/entryfile2.txt', 'r') as filer:
                    lines = filer.readlines()
                    for i in range(len(lines)):
                        line = lines[i]
                        if Magicword in line:
                            print(Magicword)
                            with open('./newpatient/entryfile2.txt', 'w') as filew:
                                filew.write(entree.get() + '\n')
                                filew.write(Birthentree.get() + '\n')
                                filew.write(str('---\n'))
        except FileNotFoundError as outcom5:
            print("+ Sorry, file 'entryfile2.txt' not exist !")
            print(str(outcom5))
            print("+ File 'entryfile2.txt' created !")
            with open('./newpatient/entryfile2.txt', 'a+') as namefile:
                namefile.write(entree.get() + '\n')
                namefile.write(Birthentree.get() + '\n')
                namefile.write(str('---\n'))
        try:
            if os.path.getsize('./newpatient/entryfile3.txt'):
                print("+ File 'entryfile3.txt' exist !")
                with open('./newpatient/entryfile3.txt', 'r') as filer:
                    lines = filer.readlines()
                    for i in range(len(lines)):
                        line = lines[i]
                        if Magicword in line:
                            print(Magicword)
                            with open('./newpatient/entryfile3.txt', 'w') as filew:
                                filew.write(entree.get() + '\n')
                                filew.write(Birthentree.get() + '\n')
                                filew.write(str('---\n'))
        except FileNotFoundError as outcom4:
            print("+ Sorry, file 'entryfile3.txt' not exist !")
            print(str(outcom4))
            print("+ File 'entryfile3.txt' created !")
            with open('./newpatient/entryfile3.txt', 'a+') as namefile:
                namefile.write(entree.get() + '\n')
                namefile.write(Birthentree.get() + '\n')
                namefile.write(str('---\n'))
        try:
            if os.path.getsize('./newpatient/entryfile4.txt'):
                print("+ File 'entryfile4.txt' exist !")
                with open('./newpatient/entryfile4.txt', 'r') as filer:
                    lines = filer.readlines()
                    for i in range(len(lines)):
                        line = lines[i]
                        if Magicword in line:
                            print(Magicword)
                            with open('./newpatient/entryfile4.txt', 'w') as filew:
                                filew.write(entree.get() + '\n')
                                filew.write(Birthentree.get() + '\n')
                                filew.write(str('---\n'))
        except FileNotFoundError as outcom3:
            print("+ Sorry, file 'entryfile4.txt' not exist !")
            print(str(outcom3))
            print("+ File 'entryfile4.txt' created !")
            with open('./newpatient/entryfile4.txt', 'a+') as namefile:
                namefile.write(entree.get() + '\n')
                namefile.write(Birthentree.get() + '\n')
                namefile.write(str('---\n'))
        try:
            if os.path.getsize('./newpatient/entryfile5.txt'):
                print("+ File 'entryfile5.txt' exist !")
                with open('./newpatient/entryfile5.txt', 'r') as filer:
                    lines = filer.readlines()
                    for i in range(len(lines)):
                        line = lines[i]
                        if Magicword in line:
                            print(Magicword)
                            with open('./newpatient/entryfile5.txt', 'w') as filew:
                                filew.write(entree.get() + '\n')
                                filew.write(Birthentree.get() + '\n')
                                filew.write(str('---\n'))
        except FileNotFoundError as outcom2:
            print("+ Sorry, file 'entryfile5.txt' not exist !")
            print(str(outcom2))
            print("+ File 'entryfile5.txt' created !")
            with open('./newpatient/entryfile5.txt', 'a+') as namefile:
                namefile.write(entree.get() + '\n')
                namefile.write(Birthentree.get() + '\n')
                namefile.write(str('---\n'))
        try:
            if os.path.getsize('./newpatient/entryfile6.txt'):
                print("+ File 'entryfile6.txt' exist !")
                with open('./newpatient/entryfile6.txt', 'r') as filer:
                    lines = filer.readlines()
                    for i in range(len(lines)):
                        line = lines[i]
                        if Magicword in line:
                            print(Magicword)
                            with open('./newpatient/entryfile6.txt', 'w') as filew:
                                filew.write(entree.get() + '\n')
                                filew.write(Birthentree.get() + '\n')
                                filew.write(str('---\n'))
        except FileNotFoundError as outcom1:
            print("+ Sorry, file 'entryfile.txt6' not exist !")
            print(str(outcom1))
            print("+ File 'entryfile.txt6' created !")
            with open('./newpatient/entryfile6.txt', 'a+') as namefile:
                namefile.write(entree.get() + '\n')
                namefile.write(Birthentree.get() + '\n')
                namefile.write(str('---\n'))
        try:
            if os.path.getsize('./newpatient/entryfile7.txt'):
                print("+ File 'entryfile7.txt' exist !")
                with open('./newpatient/entryfile7.txt', 'r') as filer:
                    lines = filer.readlines()
                    for i in range(len(lines)):
                        line = lines[i]
                        if Magicword in line:
                            print(Magicword)
                            with open('./newpatient/entryfile7.txt', 'w') as filew:
                                filew.write(entree.get() + '\n')
                                filew.write(Birthentree.get() + '\n')
                                filew.write(str('---\n'))
        except FileNotFoundError as outcom:
            print("+ Sorry, file 'entryfile7.txt' not exist !")
            print(str(outcom))
            print("+ File 'entryfile7.txt' created !")
            with open('./newpatient/entryfile7.txt', 'a+') as namefile:
                namefile.write(entree.get() + '\n')
                namefile.write(Birthentree.get() + '\n')
                namefile.write(str('---\n'))
        gui.destroy()
    else:           
        NoforQ = messagebox.showinfo('Return', 'Data not saved')

labelName = Label(gui)
labelName = Label(text='Enter Name and Surname : ', font="Times 14 bold", 
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


