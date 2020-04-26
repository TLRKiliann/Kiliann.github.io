#!/usr/bin/python3
#!-*-encoding:Utf-8-*-

from tkinter import *


def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

fen=Tk()
fen.title("Histoire de vie")

labelo=Label(fen, text="Histoire de vie patient 1",
    font='Times 18 bold italic', fg='navy')
labelo.pack(padx=10, pady=4)

textBox=Text(fen, height=20, width=80, font=18)
textBox.pack()

buttonClose=Button(fen, text="Quit", fg='yellow', bg='gray25',
    activebackground='dark turquoise', command=quit)
buttonClose.pack(side='left', fill='both', expand=True)

importationFile('./histv/doc_histv/Hvie_patient1.json',
    encodage="Utf-8")

fen.mainloop()
