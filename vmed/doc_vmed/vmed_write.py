#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
import subprocess
import time
from tkinter import messagebox


def retrieve_input():
    file = open('./vmed/doc_vmed/resultvmed.json', 'a+')
    file.write(textBox.get("1.0", "end-1c"))
    file.write(str('\n\n'))
    file.close()

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
    file = open('./vmed/doc_vmed/resultvmed.json', 'r')
    print(file.read())
    file.close()
    subprocess.call('./vmed/doc_vmed/vmed_read.py')

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

with open('./newpatient/entryfile.txt', 'r') as filename:
    line1=filename.readline()

root=Tk()
root.title("Results of Medical Visit")
root.configure(background='gray17')

# To place side by side labelo + entrylab
top = Frame(root, bg='gray17')
bottom = Frame(root, bg='gray17')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(root, text="Results of Medical Visit patient 1",
    font='Arial 18 bold', fg='cyan', bg='gray17')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

textname=StringVar()
entryName=Entry(root, textvariable=textname)
textname.set(line1)
entryName.pack(in_=top, side=LEFT, padx=10, pady=20)

textBox=Text(root, height=15, width=60, font=18, relief=SUNKEN)
textBox.insert(INSERT, "\nEn date du : ")
textBox.insert(END, time.strftime("%d/%m/%Y à %H:%M:%S :\n"))
textBox.pack(padx=30, pady=30)

buttonLire=Button(root, text="Read", width=8,
    fg='cyan', bg='navy', activebackground='dark turquoise',
    activeforeground='navy', command=lectureFic)
buttonLire.pack(side='left', padx=10, pady=10)

buttonEffacer=Button(root, text="1-Add", width=8,
    fg='yellow', bg='navy', activebackground='dark turquoise',
    activeforeground='navy', command=ajouterText)
buttonEffacer.pack(side='left', padx=10, pady=10)

buttonEnter=Button(root, text="2-Save", width=8, 
    fg='yellow', bg='navy', activebackground='dark turquoise',
    activeforeground='navy', command=messFromSafeButt)
buttonEnter.pack(side='left', padx=10, pady=10)

buttonQuitter=Button(root, text="Quit", width=8,
    fg='cyan', bg='gray30', activebackground='red', 
    activeforeground='navy', command=quit)
buttonQuitter.pack(side='right', padx=10, pady=10)

importationFile('./vmed/doc_vmed/resultvmed.json',
    encodage="Utf-8")

mainloop()
