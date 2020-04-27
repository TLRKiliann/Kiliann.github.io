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
fen.configure(background='gray17')

# To place side by side labelo + entrylab
top = Frame(fen, bg='gray17')
bottom = Frame(fen, bg='gray17')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="Auxiliary resources : ",
    font='Arial 18 bold', fg='cyan', bg='gray17')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

with open('./newpatient/entryfile.txt', 'r') as filename:
    line1=filename.readline()
entrytext=StringVar()
entrytext.set(line1)
entryName=Entry(fen, textvariable=entrytext)
entryName.pack(in_=top, side=LEFT, padx=10, pady=20)

labelallergy=Label(fen, text="Allergy",
    font='Arial 18 bold', fg='red', bg='gray17')
labelallergy.pack(padx=5, pady=10)

with open('./allergy/allergyfile.txt', 'r') as filename:
    line1=filename.readline()
    line2=filename.readline()
    line3=filename.readline()
    line4=filename.readline()
    line5=filename.readline()
entrytext=StringVar()
entrytext.set(line1 + ', ' + line3 + ', ' + line5)
entryName=Entry(fen, textvariable=entrytext, width=60)
entryName.pack(padx=10, pady=10)

textBox=Text(fen, height=15, width=60, font=18, relief=SUNKEN)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", width=8, fg='cyan', 
    bg='gray30', activebackground='dark turquoise', 
    activeforeground='navy', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

importationFile('./auxsrc/doc_auxsrc/auxsrcfile1.txt',
    encodage="Utf-8")

fen.mainloop()
