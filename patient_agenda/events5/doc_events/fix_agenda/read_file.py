#!/usr/bin/python3
#!-*-encoding:Utf-8-*-

from tkinter import *


def importationFile(fichier):
    file = open(fichier, 'r')
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

with open('./newpatient/entryfile.txt', 'r') as filename:
    line1=filename.readline()
    line2=filename.readline()
    line3=filename.readline()
    line4=filename.readline()
    line5=filename.readline()
    line6=filename.readline()
    line7=filename.readline()
    line8=filename.readline()
    line9=filename.readline()
    line10=filename.readline()
    line11=filename.readline()
    line12=filename.readline()
    line13=filename.readline()

fen=Tk()
fen.title("RDV set up")
fen.configure(background='gray17')

# To place side by side labelo + entrylab
top = Frame(fen, bg='gray17')
bottom = Frame(fen, bg='gray17')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="RDV set up",
    font='Arial 18 bold', fg='turquoise', bg='gray17')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

textentry=StringVar()
textentry.set(line13)
entrylab=Entry(fen, textvariable=textentry)
entrylab.pack(in_=top, side=LEFT, padx=10, pady=20)

textBox=Text(fen, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", fg='cyan', bg='gray30',
    width=8, activebackground='dark turquoise', 
    activeforeground='navy', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

importationFile('./patient_agenda/events5/doc_events/fix_agenda/fixed_rdv.txt')

fen.mainloop()
