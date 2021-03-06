#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *


def importationFile(fichier, encodage="Utf-8"):
    with open(fichier, 'r', encoding=encodage) as filer:
        content = filer.readlines()
        for li in content:
            textBox.insert(END, li)

fen=Tk()
fen.title("Auxiliary resources")
fen.configure(background='#82193e')

# To place side by side labelo + entrylab
top = Frame(fen, bg='#82193e')
bottom = Frame(fen, bg='#82193e')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="Auxiliary resources : ",
    font='Arial 18 bold', fg='cyan', bg='#82193e')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

with open('./newpatient/entryfile4.txt', 'r') as filename:
    line1=filename.readline()
    
entrytext=StringVar()
entrytext.set(line1)
entryName=Entry(fen, textvariable=entrytext)
entryName.pack(in_=top, side=LEFT, padx=10, pady=20)

textBox=Text(fen, height=15, width=60, font=18, relief=SUNKEN)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", width=8, bd=3,
    fg='white', bg='navy', activebackground='dark turquoise', 
    highlightbackground='grey17', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

importationFile('./auxsrc/doc_auxsrc4/auxsrcfile4.txt',
    encodage="Utf-8")

fen.mainloop()
