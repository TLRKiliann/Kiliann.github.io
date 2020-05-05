#!/usr/bin/python3
#!-*-encoding:Utf-8-*-


from tkinter import *


fen=Tk()
fen.title("Global Vision")
fen.configure(background='gray17')

# To place side by side labelo + entrylab
top = Frame(fen, bg='gray17')
bottom = Frame(fen, bg='gray17')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

"""
labelo=Label(fen, text="Life story : ", width=20,
    font='Times 18 bold', fg='cyan', bg='gray17')
labelo.pack(padx=5, pady=20)
"""

def importationFile1(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

textBox=Text(fen, height=15, width=60, font=18, relief=SUNKEN)
textBox.pack(in_=top, side=LEFT, anchor='nw', padx=30, pady=30)

def importationFile2(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox2.insert(END, li)

textBox2=Text(fen, height=15, width=60, font=18, relief=SUNKEN)
textBox2.pack(in_=top, side=LEFT, padx=30, pady=30)

def importationFile3(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox3.insert(END, li)

textBox3=Text(fen, height=15, width=60, font=18, relief=SUNKEN)
textBox3.pack(in_=bottom, side=LEFT, padx=30, pady=30)

def importationFile4(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox4.insert(END, li)

textBox4=Text(fen, height=15, width=60, font=18, relief=SUNKEN)
textBox4.pack(in_=bottom, side=LEFT, padx=30, pady=30)

importationFile1('./calBmi/bmi3.txt',
    encodage="Utf-8")

importationFile2('./param/Main3.txt',
    encodage="Utf-8")

importationFile3('./vmed/doc_vmed3/resultvmed.txt',
    encodage="Utf-8")

importationFile4('./14besoins/doc_suivi3/main_14b.txt',
    encodage="Utf-8")

fen.mainloop()