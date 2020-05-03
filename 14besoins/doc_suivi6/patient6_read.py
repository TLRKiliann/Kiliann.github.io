#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *


def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

fen=Tk()
fen.title("Care and monitoring")
fen.configure(background='gray17')

# To place side by side labelo + entrylab
top = Frame(fen, bg='gray17')
bottom = Frame(fen, bg='gray17')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="Care and monitoring : ", width=20,
    font='Times 18 bold', fg='cyan', bg='gray17')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

labelallergy=Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='gray17')
labelallergy.pack(padx=5, pady=5)

# To read name in Entry widget
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
    line14=filename.readline()
    line15=filename.readline()
    line16=filename.readline()

text_name=StringVar()
text_name.set(line16)
Entryname=Entry(fen, textvariable=text_name)
Entryname.pack(in_=top, side=LEFT, padx=10, pady=20)

# To read allergy in Entry widget
with open('./allergy/allergyfile6.txt', 'r') as allerfile:
    lineA1=allerfile.readline()
    lineA2=allerfile.readline()
    lineA3=allerfile.readline()
    lineA4=allerfile.readline()
    lineA5=allerfile.readline()
    lineA6=allerfile.readline()
    lineA7=allerfile.readline()

text_all=StringVar()
text_all.set(lineA1 + ', ' + lineA3 + ', ' + lineA5 + ', ' + lineA7)
Entryall=Entry(fen, textvariable=text_all, width=60)
Entryall.pack(padx=10, pady=5)

textBox=Text(fen, height=15, width=60, font=18, relief=SUNKEN)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", fg='cyan', width=10, 
    bg='gray30', activebackground='dark turquoise', 
    activeforeground='navy', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

importationFile('./14besoins/doc_suivi6/main_14b.txt',
    encodage="Utf-8")

fen.mainloop()