#!/usr/bin/python3
# -*- coding:utf-8 -*-


import tkinter
from tkinter import *
import os
import time
import subprocess


def sendToFile():
    try:
        if os.path.getsize('./admin/readadmin/fileAdmin2.txt'):
            print("File 'fileAdmin2.txt' exist !")
    except FileNotFoundError as infofile :
        print("File : 'fileAdmin2' does not exist !", infofile)
        print("File : 'fileAdmin2' created !")
    finally:
        with open('./admin/readadmin/fileAdmin2.txt', 'a+') as file:
            file.write(str("Date : "))
            file.write(entreDate.get() + '\n')
            file.write(str("Name : "))
            file.write(entreName.get())
            file.write(str("Birthdate : "))
            file.write(entreBirth.get())
            file.write(str("Addess : "))
            file.write(entreAddr.get() + '\n')
            file.write(str("NPA : "))
            file.write(entreNPA.get() + '\n')
            file.write(str("Locality : "))
            file.write(entrelocal.get() + '\n')
            file.write(str("Phone : "))
            file.write(entretel.get() + '\n')
            file.write(str("Assurance : "))
            file.write(entreAss.get() + '\n')
            file.write(str("AVS : "))
            file.write(entreavs.get() + '\n')
            file.write(str("Contact : "))
            file.write(entreContact.get() + '\n')
            file.write(str("E-mail : "))
            file.write(Emailcontact.get() + '\n')
            file.write(str("Phone number : "))
            file.write(entryFamContact.get() +'\n')
            file.write(str("Friend contact : "))
            file.write(Friendcontact.get() + '\n')
            file.write(str("Friend number : "))
            file.write(Phonecontact.get() +'\n')
            file.write(str("Familiy Dr : "))
            file.write(entreDrg.get() + '\n')
            file.write(str("Phone Dr : "))
            file.write(PhoneDrg.get() + '\n')
            file.write(str("Address Dr : "))
            file.write(AddDrg.get() + '\n')

def readToFile():
	subprocess.call('./admin/readadmin/readadminfile2.py')

# To read name of patient for entry widget
with open('./newpatient/entryfile.txt', 'r') as filename:
    line1=filename.readline()
    line2=filename.readline()
    line3=filename.readline()
    line4=filename.readline()
    line5=filename.readline()

gui = Tk()
gui.title("Administrative Statement")
gui.configure(bg='gray17')

labelDate = Label(gui)
labelDate = Label(text="Administrative Statement", font='Times 28 bold',
    fg='aquamarine', bg='gray17')
labelDate.grid(row=0, column=1, columnspan=4)

labelDate = Label(gui)
labelDate = Label(text="Date : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
labelDate.grid(pady=10, row=1, column=1)

labelName = Label(gui)
labelName = Label(text="Name : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
labelName.grid(pady=10, row=2, column=1)

labelBirth = Label(gui)
labelBirth = Label(text="Birth date : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
labelBirth.grid(pady=10, row=3, column=1)

labelAddr = Label(gui)
labelAddr = Label(text="Address : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
labelAddr.grid(pady=10, row=4, column=1)

labelNpa = Label(gui)
labelNpa = Label(text="NPA : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
labelNpa.grid(pady=10, row=5, column=1)

labelLocal = Label(gui)
labelLocal = Label(text="Locality : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
labelLocal.grid(pady=10, row=6, column=1)

labelTel = Label(gui)
labelTel = Label(text="Phone number : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
labelTel.grid(pady=10, row=7, column=1)

labelAss = Label(gui)
labelAss = Label(text="Assurance : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
labelAss.grid(pady=10, row=8, column=1)

labelAVS = Label(gui)
labelAVS = Label(text="AVS number : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
labelAVS.grid(pady=10, row=9, column=1)

labelContact = Label(gui)
labelContact = Label(text="Family contact : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
labelContact.grid(pady=10, row=10, column=1)

labelphonecontact = Label(gui)
labelphonecontact = Label(text="Phone contact : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
labelphonecontact.grid(pady=10, row=11, column=1)

labelemailcontact = Label(gui)
labelemailcontact = Label(text="Contact email : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
labelemailcontact.grid(pady=10, row=12, column=1)

labelFriendContact = Label(gui)
labelFriendContact = Label(text="Friend contact : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
labelFriendContact.grid(pady=10, row=13, column=1)

labelphonefriend = Label(gui)
labelphonefriend = Label(text="Phone contact : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
labelphonefriend.grid(pady=10, row=14, column=1)

labelDrg = Label(gui)
labelDrg = Label(text="Family Doctor : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
labelDrg.grid(pady=10, row=15, column=1)

labelphoneDr = Label(gui)
labelphoneDr = Label(text="Phone Doctor : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
labelphoneDr.grid(pady=10, row=16, column=1)

LabelAddrDr = Label(gui)
LabelAddrDr = Label(text="Address Doctor : ", font=14,
    width=20, anchor='e', fg='cyan', bg='gray17')
LabelAddrDr.grid(pady=10, row=16, column=1)

#Entry
entreDate = Entry(gui)
date_conf = IntVar()
entreDate = Entry(textvariable=date_conf, 
    highlightbackground="gray", bd=4)
date_conf.set(time.strftime("%d/%m/%Y"))
entreDate.grid(row=1, column=2)

entreName = Entry(gui)
namefile = StringVar()
entreName = Entry(textvariable=namefile,
    highlightbackground="gray", bd=4)
namefile.set(line4)
entreName.grid(row=2, column=2)

entreBirth = Entry(gui)
namebirth = StringVar()
entreBirth = Entry(textvariable=namebirth,
    highlightbackground="gray", bd=4)
namebirth.set(line5)
entreBirth.grid(row=3, column=2)

entreAddr = Entry(gui)
entreAddr = Entry(highlightbackground="gray", bd=4)
entreAddr.grid(row=4, column=2)

entreNPA = Entry(gui)
entreNPA = Entry(highlightbackground="gray", bd=4)
entreNPA.grid(row=5, column=2)

entrelocal = Entry(gui)
entrelocal = Entry(highlightbackground="gray", bd=4)
entrelocal.grid(row=6, column=2)

entretel = Entry(gui)
entretel = Entry(highlightbackground="gray", bd=4)
entretel.grid(row=7, column=2)

entreAss = Entry(gui)
entreAss = Entry(highlightbackground="gray", bd=4)
entreAss.grid(row=8, column=2)

entreavs = Entry(gui)
entreavs = Entry(highlightbackground="gray", bd=4)
entreavs.grid(row=9, column=2)

entreContact = Entry(gui)
entreContact = Entry(highlightbackground="gray", bd=4)
entreContact.grid(row=10, column=2)

entryFamContact = Entry(gui)
entryFamContact = Entry(highlightbackground="gray", bd=4)
entryFamContact.grid(row=11 , column=2)

Emailcontact = Entry(gui)
Emailcontact = Entry(highlightbackground="gray", bd=4)
Emailcontact.grid(row=12, column=2)

Friendcontact = Entry(gui)
Friendcontact = Entry(highlightbackground="gray", bd=4)
Friendcontact.grid(row=13, column=2)

Phonecontact = Entry(gui)
Phonecontact = Entry(highlightbackground="gray", bd=4)
Phonecontact.grid(row=14, column=2)

entreDrg = Entry(gui)
entreDrg = Entry(highlightbackground="gray", bd=4)
entreDrg.grid(row=15, column=2)

PhoneDrg = Entry(gui)
PhoneDrg = Entry(highlightbackground="gray", bd=4)
PhoneDrg.grid(row=16, column=2)

AddDrg=Entry(gui)
AddDrg=Entry(highlightbackground="gray", bd=4)
AddDrg.grid(row=17, column=2)

buttonName = Button(gui)
buttonName = Button(text='Save', fg='cyan', bg='gray30',
    width=18, command=sendToFile)
buttonName.grid(row=15, column=4)

buttonName = Button(gui)
buttonName = Button(text='Read', fg='cyan', bg='gray30',
    width=18, command=readToFile)
buttonName.grid(row=16, column=4)

buttonQuit = Button(gui)
buttonQuit = Button(text='Quit', fg='cyan', bg='gray30',
    width=18, command=quit)
buttonQuit.grid(row=17, column=4)

gui.mainloop()
