#!/usr/bin/python3
#!-*-encoding:Utf-8-*-


from tkinter import *
import subprocess
import time


root=Tk()
root.title("Histoire de vie")

labelo=Label(root, text="Histoire de vie patient 1",
    font='Times 18 bold italic', fg='navy')
labelo.pack(padx=10, pady=4)

#"1.0","end-1c"
def retrieve_input():
    inputValue = textBox.get("1.0","end-1c")
    print(inputValue)
    file = open('./histv/doc_histv/Hvie_patient1.json', 'a+')
    file.write(textBox.get("1.0","end-1c") + "\n")
    file.close()

def lectureFic():
    file = open('./histv/doc_histv/Hvie_patient1.json', 'r')
    print(file.read())
    file.close()
    subprocess.call('./histv/doc_histv/patient1_read.py')

def effacerText():
    textBox.delete('1.0', END)
    textBox.insert(INSERT, "En date du: ")
    textBox.insert(END, time.strftime("%d/%m/%Y") + "\n")
    textBox.update()

textBox=Text(root, height=20, width=80, font=18)
textBox.insert(INSERT, "En date du: ")
textBox.insert(END, time.strftime("%d/%m/%Y") + "\n")
textBox.pack()

buttonLire=Button(root, text="Read", fg='yellow', bg='gray30',
    activebackground='dark turquoise', command=lectureFic)
buttonLire.pack(side='left', fill='both', expand=True)

buttonEffacer=Button(root, text="1-Add", fg='red', bg='gray30',
    activebackground='red', activeforeground='yellow',
    command=effacerText)
buttonEffacer.pack(side='left', fill='both', expand=True)

buttonEnter=Button(root, text="2-Save", fg='cyan', bg='gray30',
    activebackground='dark turquoise', command=retrieve_input)
buttonEnter.pack(side='left', fill='both', expand=True)

buttonQuitter=Button(root, text="Quit", fg='red', bg='gray30',
    activebackground='red', activeforeground='yellow', command=quit)
buttonQuitter.pack(side='left', fill='both', expand=True)

mainloop()
