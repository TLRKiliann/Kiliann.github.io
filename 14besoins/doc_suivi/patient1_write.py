#!/usr/bin/python3
# -*-encoding:Utf-8-*-


import tkinter
from tkinter import *
import subprocess
import os
import time
from tkinter import messagebox


def retrieve_input():
    try:        
        if os.path.getsize('./14besoins/doc_suivi/patient1_14b.txt'):
            print("+ File 'patient1_14b.txt' exist !")
            with open('./14besoins/doc_suivi/patient1_14b.txt', 'a+') as namefile:
                namefile.write(str('\n\n'))
                namefile.write(textBox.get("1.0", "end-1c" + '\n'))
    except FileNotFoundError as outcom:
        print("+ Sorry, file 'patient1_14b.txt' not exist !")
        print(str(outcom))
        print("+ File 'patient1_14b.txt' created !")
        with open('./14besoins/doc_suivi/patient1_14b.txt', 'a+') as namefile:
            namefile.write(str('\n\n'))
            namefile.write(textBox.get("1.0", "end-1c" + '\n'))

def messFromSafeButt():
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        retrieve_input()
        textBox.insert(INSERT, "\n---Data saved !---")
        print("+ Data saved !")
    else:
        textBox.insert(INSERT, "Nothing has been saved !")
        print("+ Nothing has been saved !")

def lectureFic():
    with open('./14besoins/doc_suivi/patient1_14b.txt', 'r') as f1read:
        with open('./labo/doc_labo/result.json', 'r') as f2read:
            print(f1read.read())
            print(f2read.read())
    subprocess.call('./14besoins/doc_suivi/patient1_read.py')

def ajouterText():
    textBox.delete('1.0', END)
    textBox.insert(INSERT, "En date du : ")
    textBox.insert(END, time.strftime("%d/%m/%Y à %H:%M:%S :") + '\n')
    textBox.update()

def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

def importationFilejson(fichier2):
    file = open(fichier2, 'r')
    content2=file.readlines()
    file.close()
    for li in content2:
        textBox.insert(END, li)

# To read name in Entry widget
with open('./newpatient/entryfile.txt', 'r') as filename:
    line1=filename.readline()

# To read allergy in Entry widget
with open('./allergy/allergyfile.txt', 'r') as allerfile:
    lineA1=allerfile.readline()
    lineA2=allerfile.readline()
    lineA3=allerfile.readline()
    lineA4=allerfile.readline()
    lineA5=allerfile.readline()

root=Tk()
root.title("Care and monitoring")
root.configure(background='gray17')

# To place side by side labelo + entrylab
top = Frame(root, bg='gray17')
bottom = Frame(root, bg='gray17')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(root, text="Care and monitoring : ",
    font='Times 18 bold', fg='cyan', bg='gray17')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

labelallergy=Label(root, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='gray17')
labelallergy.pack(padx=5, pady=5)

text_name=StringVar()
Entryname=Entry(root, textvariable=text_name)
text_name.set(line1)
Entryname.pack(in_=top, side=LEFT, padx=10, pady=20)

text_aller=StringVar()
text_aller.set(lineA1 + ', ' + lineA3 + ', ' + lineA5)
Entryaller=Entry(root, textvariable=text_aller, width=60)
Entryaller.pack(padx=10, pady=5)

textBox=Text(root, height=15, width=60, font=18, relief=SUNKEN)
textBox.insert(INSERT, "\nEn date du : ")
textBox.insert(END, time.strftime("%d/%m/%Y à %H:%M:%S :\n"))
textBox.pack(padx=30, pady=30)

buttonLire=Button(root, text="Read", fg='cyan', bg='gray30',
    activebackground='dark turquoise', activeforeground='navy',
    command=lectureFic)
buttonLire.pack(side='left', padx=10, pady=10)

buttonAjouter=Button(root, text="1-Add", fg='yellow', bg='gray30',
    activebackground='dark turquoise', activeforeground='navy',
    command=ajouterText)
buttonAjouter.pack(side='left', padx=10, pady=10)

buttonEnter=Button(root, text="2-Save", fg='yellow', bg='gray30',
    activebackground='dark turquoise', activeforeground='navy',
    command=messFromSafeButt)
buttonEnter.pack(side='left', padx=10, pady=10)

buttonQuitter=Button(root, text="Quit", fg='cyan', bg='gray30',
    width=10, activebackground='cyan', activeforeground='navy',
    command=quit)
buttonQuitter.pack(side='right', padx=10, pady=10)

importationFile('./14besoins/doc_suivi/patient1_14b.txt',
    encodage="Utf-8")

importationFilejson('./labo/doc_labo/result.json')

mainloop()
