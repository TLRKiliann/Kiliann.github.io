#!/usr/bin/python3
#!-*-encoding:Utf-8-*-

from tkinter import *


def importationFile(fichier):
    file = open(fichier, 'r')
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

def saveData():         
    with open('./patient_agenda/events3/doc_events/fix_agenda/modifrdv.txt', 'w') as textfile2:
        textfile2.writelines(textBox.get('0.0', '12.0'))

with open('./newpatient/entryfile.txt', 'r') as filename:
    line1=filename.readline()

fen=Tk()
fen.title("RDV have changed")
fen.configure(background='gray17')

# To place side by side labelo + entrylab
top=Frame(fen, bg='gray17')
bottom=Frame(fen, bg='gray17')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="RDV have changed",
    font='Arial 18 bold', fg='turquoise', bg='gray17')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

textname=StringVar()
entryName=Entry(fen, textvariable=textname)
textname.set(line1)
entryName.pack(in_=top, side=LEFT, padx=10, pady=20)

textBox=Text(fen, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

buttonSave=Button(fen, text="Save", fg='yellow', bg='navy',
    width=8, activebackground='dark turquoise', 
    activeforeground='navy', command=saveData)
buttonSave.pack(side='left', padx=10, pady=10)

buttonClose=Button(fen, text="Quit", fg='cyan', bg='gray30', width=8,
    activebackground='dark turquoise', activeforeground='navy', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

importationFile('./patient_agenda/events3/doc_events/fix_agenda/modifrdv.txt')

fen.mainloop()
