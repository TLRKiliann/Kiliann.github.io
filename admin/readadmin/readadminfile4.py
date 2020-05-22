#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *


def importationFile(fichier):
    file = open(fichier, 'r')
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

fen=Tk()
fen.title("Admininstrative Statement")
fen.configure(background='#82193e')

labelo=Label(fen, text="Admininstrative Statement",
    font='Arial 18 bold', fg='turquoise', bg='#82193e')
labelo.pack(pady=10)

textBox=Text(fen, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", width=10, bd=3,
    fg='white', bg='navy', activebackground='dark turquoise',
    highlightbackground='#82193e', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

importationFile('./admin/readadmin/fileAdmin4.txt')

fen.mainloop()