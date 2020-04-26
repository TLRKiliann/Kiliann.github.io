#!/usr/bin/python3
# -*- coding:utf-8 -*-


import tkinter
from tkinter import *
import io


def searchExpress():
    mot = regexpi_var.get()
    file = open('textre.txt', 'r')
    for line in file:
        if mot in line:
            print("Nous y voici !")
            print(mot)
            print(file.readline())
            break
        else:
            print("Rien trouvé sur cette ligne...")
    file.close()

def deleteExpress():
    moteff = regexpi_var.get()
    char = ''
    file = open('textre.txt', 'r+')
    file_N = file.readlines()
    file.seek(0)
    for line in file_N:
        if moteff not in line:
            file.write(line)
    file.truncate()
    print("Processus arrivé à terme")

gui = Tk()

gui.title("Recherche d'une date")
gui.configure(bg='gray25')
#gui.geometry('400x400')

labelTit = Label(gui)
labelTit = Label(text="Recherche d'une date", font=("Arial 16 bold"),
    fg='turquoise', bg='gray25')
labelTit.grid(row=0, column=1, columnspan=3)

labelDate = Label(gui)
labelDate = Label(text='Entrer la date recherchée : ', font='12', fg='cyan',
    bg='gray25')
labelDate.grid(row=1, column=1)

reachDate = Entry(gui)
regexpi_var = StringVar()
reachDate = Entry(textvariable=regexpi_var, highlightbackground='gray')
reachDate.grid(row=1, column=2, padx=5)

buttonSearch = Button(gui)
buttonSearch = Button(text='Search', fg='yellow', bg='navy', width=6, command=searchExpress)
buttonSearch.grid(row=1, column=3, padx=5)

buttonDel = Button(gui)
buttonDel = Button(text='Delete', fg='red', bg='navy', width=6, command=deleteExpress)
buttonDel.grid(row=2, column=2, padx=5)

buttonQuit = Button(gui)
buttonQuit = Button(text='Quit', fg='cyan', bg='navy', width=6, command=quit)
buttonQuit.grid(row=2, column=3)

gui.mainloop()
