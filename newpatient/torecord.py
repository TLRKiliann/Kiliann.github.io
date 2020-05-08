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
        mot = "-"
        mot2 = "--"
        mot3 = "---"
        mot4 = "----"
        mot5 = "-----"
        mot6 = "------"
        mot7 = "-------"
        Nompatient = entree.get()
        Birthvalue = Birthentree.get()
        print(Nompatient)
        print(Birthvalue)
        try:
            if os.path.getsize('./newpatient/entryfile.txt'):
                print("+ File 'entryfile.txt' exist !")
                searchLine1(Nompatient, Birthvalue, mot) 
                try:
                    if os.path.getsize('./newpatient/entryfile2.txt'):
                        print("+ File 'entryfile2.txt' exist !")
                        searchLine2(Nompatient, Birthvalue, mot2)
                        try:
                            if os.path.getsize('./newpatient/entryfile3.txt'):
                                print("+ File 'entryfile3.txt' exist !")
                                searchLine3(Nompatient, Birthvalue, mot3)
                                try:
                                    if os.path.getsize('./newpatient/entryfile4.txt'):
                                        print("+ File 'entryfile4.txt' exist !")
                                        searchLine4(Nompatient, Birthvalue, mot4)
                                        try:
                                            if os.path.getsize('./newpatient/entryfile5.txt'):
                                                print("+ File 'entryfile5.txt' exist !")
                                                searchLine5(Nompatient, Birthvalue, mot5)
                                                try:
                                                    if os.path.getsize('./newpatient/entryfile6.txt'):
                                                        print("+ File 'entryfile6.txt' exist !")
                                                        searchLine6(Nompatient, Birthvalue, mot6)
                                                        try:
                                                            if os.path.getsize('./newpatient/entryfile7.txt'):
                                                                print("+ File 'entryfile7.txt' exist !")
                                                                searchLine7(Nompatient, Birthvalue, mot7)
                                                        except FileNotFoundError as outcom:
                                                            print("+ Sorry, file 'entryfile7.txt' not exist !")
                                                            print(str(outcom))
                                                            print("+ File 'entryfile7.txt' created !")
                                                            with open('./newpatient/entryfile7.txt', 'w') as namefile:
                                                                namefile.write(Nompatient + '\n')
                                                                namefile.write(Birthvalue + '\n')
                                                                namefile.write(str('---\n'))
                                                except FileNotFoundError as outcom1:
                                                    print("+ Sorry, file 'entryfile.txt6' not exist !")
                                                    print(str(outcom1))
                                                    print("+ File 'entryfile.txt6' created !")
                                                    with open('./newpatient/entryfile6.txt', 'w') as namefile:
                                                        namefile.write(Nompatient + '\n')
                                                        namefile.write(Birthvalue + '\n')
                                                        namefile.write(str('---\n'))
                                        except FileNotFoundError as outcom2:
                                            print("+ Sorry, file 'entryfile5.txt' not exist !")
                                            print(str(outcom2))
                                            print("+ File 'entryfile5.txt' created !")
                                            with open('./newpatient/entryfile5.txt', 'w') as namefile:
                                                namefile.write(Nompatient + '\n')
                                                namefile.write(Birthvalue + '\n')
                                                namefile.write(str('---\n'))
                                except FileNotFoundError as outcom3:
                                    print("+ Sorry, file 'entryfile4.txt' not exist !")
                                    print(str(outcom3))
                                    print("+ File 'entryfile4.txt' created !")
                                    with open('./newpatient/entryfile4.txt', 'w') as namefile:
                                        namefile.write(Nompatient + '\n')
                                        namefile.write(Birthvalue + '\n')
                                        namefile.write(str('---\n'))
                        except FileNotFoundError as outcom4:
                            print("+ Sorry, file 'entryfile3.txt' not exist !")
                            print(str(outcom4))
                            print("+ File 'entryfile3.txt' created !")
                            with open('./newpatient/entryfile3.txt', 'w') as namefile:
                                namefile.write(Nompatient + '\n')
                                namefile.write(Birthvalue + '\n')
                                namefile.write(str('---\n'))
                except FileNotFoundError as outcom5:
                    print("+ Sorry, file 'entryfile2.txt' not exist !")
                    print(str(outcom5))
                    print("+ File 'entryfile2.txt' created !")
                    with open('./newpatient/entryfile2.txt', 'w') as namefile:
                        namefile.write(Nompatient + '\n')
                        namefile.write(Birthvalue + '\n')
                        namefile.write(str('---\n'))
        except FileNotFoundError as outcom6:
            print("+ Sorry, file 'entryfile.txt' not exist !")
            print(str(outcom6))
            print("+ File 'entryfile.txt' created !")
            with open('./newpatient/entryfile.txt', 'w') as namefile:
                namefile.write(Nompatient + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(str('---\n'))
    gui.destroy()

def searchLine1(Nompatient, Birthvalue, mot):
    if mot == "-":
        with open('./newpatient/entryfile.txt', 'r') as file:
            lines = file.readlines()
            with open('./newpatient/entryfile.txt', 'w') as file:
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot in line:
                        file.write(Nompatient + '\n')
                        file.write(Birthvalue + '\n')
                        file.write(str('---'))
    else:
        print("Name already checked")

def searchLine2(Nompatient, Birthvalue, mot2):
    if mot2 == "--":
        with open('./newpatient/entryfile2.txt', 'r') as file:
            lines = file.readlines()
            with open('./newpatient/entryfile2.txt', 'w') as file:
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot2 in line:
                        file.write(Nompatient + '\n')
                        file.write(Birthvalue + '\n')
                        file.write(str('---'))
    else:
        print("Name already checked")

def searchLine3(Nompatient, Birthvalue, mot3):
    if mot3 == "---":
        with open('./newpatient/entryfile3.txt', 'r') as file:
            lines = file.readlines()
            with open('./newpatient/entryfile3.txt', 'w') as file:
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot3 in line:
                        file.write(Nompatient + '\n')
                        file.write(Birthvalue + '\n')
                        file.write(str('---'))
    else:
        print("Name already checked")

def searchLine4(Nompatient, Birthvalue, mot4):
    if mot4 == "----":
        with open('./newpatient/entryfile4.txt', 'r') as file:
            lines = file.readlines()
            with open('./newpatient/entryfile4.txt', 'w') as file:
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot4 in line:
                        file.write(Nompatient + '\n')
                        file.write(Birthvalue + '\n')
                        file.write(str('---'))
    else:
        print("Name already checked")

def searchLine5(Nompatient, Birthvalue, mot5):
    if mot5 == "-----":
        with open('./newpatient/entryfile5.txt', 'r') as file:
            lines = file.readlines()
            with open('./newpatient/entryfile5.txt', 'w') as file:
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot5 in line:
                        file.write(Nompatient + '\n')
                        file.write(Birthvalue + '\n')
                        file.write(str('---'))
    else:
        print("Name already checked")

def searchLine6(Nompatient, Birthvalue, mot6):
    if mot6 == "------":
        with open('./newpatient/entryfile6.txt', 'r') as file:
            lines = file.readlines()
            with open('./newpatient/entryfile6.txt', 'w') as file:
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot6 in line:
                        file.write(Nompatient + '\n')
                        file.write(Birthvalue + '\n')
                        file.write(str('---'))
    else:
        print("Name already checked")

def searchLine7(Nompatient, Birthvalue, mot7):
    if mot7 == "-------":
        with open('./newpatient/entryfile7.txt', 'r') as file:
            lines = file.readlines()
            with open('./newpatient/entryfile7.txt', 'w') as file:
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot7 in line:
                        file.write(Nompatient + '\n')
                        file.write(Birthvalue + '\n')
                        file.write(str('---'))
    else:
        print("Name already checked")

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
