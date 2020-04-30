#!/usr/bin/python3
# -*- coding:utf-8 -*-


from tkinter import *


def saveCheck():
    pass

# To read name in Entry widget
with open('./newpatient/entryfile.txt', 'r') as filename:
    line1=filename.readline()

gui = Tk()
gui.title("Intolerances")
gui.configure(bg='gray17')

Intolabel = Label(gui, text="Intolerances : ", font="Times 18 bold",
    width=14, fg='aquamarine', bg='gray17', anchor='e')
Intolabel.grid(sticky='w', row=0, column=0, pady=10)

text_entry = StringVar()
text_entry.set(line1)
Intoentry = Entry(gui, textvariable=text_entry)
Intoentry.grid(sticky='e', row=0, column=0, pady=10)

CheckVar1 = IntVar()
C1 = Checkbutton(gui, text="Gluten", fg='navy', 
    bg='dark turquoise', variable=CheckVar1, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C1.grid(row=2, column=0)

CheckVar2 = IntVar()
C2 = Checkbutton(gui, text="Lactose", fg='navy', 
    bg='dark turquoise', variable=CheckVar2, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C2.grid(row=3, column=0)

CheckVar3 = IntVar()
C3 = Checkbutton(gui, text="Saccharose", fg='navy', 
    bg='dark turquoise', variable=CheckVar3, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C3.grid(row=4, column=0)

CheckVar4 = IntVar()
C4 = Checkbutton(gui, text="Fructose", fg='navy', 
    bg='dark turquoise', variable=CheckVar4, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C4.grid(row=5, column=0)

#Les allergies d’origine animale : 
animallabel = Label(gui, text="Animal allergy", font="Times 18 bold",
    fg='aquamarine', bg='gray17')
animallabel.grid(row=6, column=0, pady=10)  

CheckVar5 = IntVar()
C5 = Checkbutton(gui, text="Eggs", fg='navy', 
    bg='dark turquoise', variable=CheckVar5, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C5.grid(row=7, column=0)

CheckVar6 = IntVar()
C6 = Checkbutton(gui, text="Fish", fg='navy', 
    bg='dark turquoise', variable=CheckVar6, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C6.grid(row=8, column=0)


CheckVar7 = IntVar()
C7 = Checkbutton(gui, text="Shellfish", fg='navy', 
    bg='dark turquoise', variable=CheckVar7, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C7.grid(row=9, column=0)

CheckVar8 = IntVar()
C8 = Checkbutton(gui, text="Molluscs", fg='navy', 
    bg='dark turquoise', variable=CheckVar8, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C8.grid(row=10, column=0)

#Les allergies d’origine végétale : 
vegetallabel = Label(gui, text="Vegetable allergy",
    font="Times 18 bold", fg='aquamarine', bg='gray17')
vegetallabel.grid(row=11, column=0, pady=10)  

CheckVar9 = IntVar()
C9 = Checkbutton(gui, text="Groundnut", fg='navy', 
    bg='dark turquoise', variable=CheckVar9, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C9.grid(row=12, column=0)

CheckVar10 = IntVar()
C10 = Checkbutton(gui, text="Oleaginous fruits", fg='navy', 
    bg='dark turquoise', variable=CheckVar10, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C10.grid(row=13, column=0)

CheckVar11 = IntVar()
C11 = Checkbutton(gui, text="Sesame", fg='navy', 
    bg='dark turquoise', variable=CheckVar11, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C11.grid(row=14, column=0)

CheckVar12 = IntVar()
C12 = Checkbutton(gui, text="Soya", fg='navy', 
    bg='dark turquoise', variable=CheckVar12, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C12.grid(row=15, column=0)

CheckVar13 = IntVar()
C13 = Checkbutton(gui, text="Cereals (wheat, rye)", fg='navy', 
    bg='dark turquoise', variable=CheckVar13, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C13.grid(row=16, column=0)

CheckVar14 = IntVar()
C14 = Checkbutton(gui, text="Latex fruits", fg='navy', 
    bg='dark turquoise', variable=CheckVar14, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C14.grid(row=17, column=0)

latexlabel = Label(gui, text="Latex fruits = avocado, banana, kiwi,"
    "fig, chestnut, etc.", font="Times 12", fg='aquamarine',
    bg='gray17')
latexlabel.grid(row=18, column=0, pady=10)  

CheckVar15 = IntVar()
C15 = Checkbutton(gui, text="Rosacea",
    fg='navy', bg='dark turquoise', variable=CheckVar15, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C15.grid(row=19, column=0)

rosaclabel = Label(gui, text="Rosacea = apricot, cherry, strawberry, etc.",
    font="Times 12", fg='aquamarine', bg='gray17')
rosaclabel.grid(row=20, column=0, pady=10)  

CheckVar16 = IntVar()
C16 = Checkbutton(gui, text="Umbellifers", fg='navy', 
    bg='dark turquoise', variable=CheckVar16, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C16.grid(row=21, column=0)

ombellabel = Label(gui, text="Umbellifers = dill, carrot, celery,"
    "fennel, parsley, etc.",
    font="Times 12", fg='aquamarine', bg='gray17')
ombellabel.grid(row=22, column=0, pady=10)  

buttSave = Button(gui, text="Save", width=10, fg='yellow',
    bg='navy', command=saveCheck)
buttSave.grid(sticky='w', row=23, column=0, padx=20, pady=10)

buttQuit = Button(gui, text='Quit', width=10, fg='cyan',
    bg='gray17', command=quit)
buttQuit.grid(sticky='e', row=23, column=0, padx=20, pady=10)

gui.mainloop()
