#!/usr/bin/python3
#!-*-encoding:Utf-8-*-


from tkinter import *


def importationFile(fichier):
    file = open(fichier, 'r')
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

fen=Tk()
fen.title("Admininstrative Statement")
fen.configure(background='gray17')

labelo=Label(fen, text="Admininstrative Statement",
    font='Arial 18 bold', fg='turquoise', bg='gray17')
labelo.pack(pady=10)

textBox=Text(fen, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quitter", fg='cyan', bg='gray30',
    activebackground='dark turquoise', activeforeground='navy', command=quit)
buttonClose.pack(side='right')

importationFile('./admin/readadmin/fileAdmin1.txt')

fen.mainloop()