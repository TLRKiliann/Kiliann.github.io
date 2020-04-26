#!/usr/bin/python3
#!-*-encoding:utf-8-*-

from tkinter import *


def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

fen=Tk()
fen.title("Paramètres")
fen.configure(background='gray17')

labelo=Label(fen, text="Paramètres Vitaux patient 1",
    font='Arial 18 bold', fg='cyan', bg='gray17')
labelo.pack(pady=10)

textBox=Text(fen, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", fg='cyan', 
	bg='gray30', activebackground='dark turquoise', 
    activeforeground='navy', command=quit)
buttonClose.pack(side='right')

importationFile('./param/Main.json',
    encodage="Utf-8")

fen.mainloop()
