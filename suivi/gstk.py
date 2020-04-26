#!/usr/bin/python3
#!-*-encoding:Utf-8-*-


import tkinter
from tkinter import *


class ScrolledText(Frame): 
    """Widget composite, associant un widget Text et une barre de défilement"""
    def __init__(self, boss, baseFont="Times", width=50, height=25):
        Frame.__init__(self, boss, bd=2, relief=SUNKEN)
        self.text=Text(self, font=baseFont, bg='ivory', bd=1, width=width, height=height)      
        scroll=Scrollbar(self, bd=1, command=self.text.yview)

        self.text.configure(yscrollcommand=scroll.set)
        self.text.pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2)

        scroll.pack(side=RIGHT, expand=NO, fill=Y, padx=2, pady=2)

    def importFichier(self):
            fichier=open('suivi_patient_1/sui_07.01.19_AE.txt', 'r')
            fichier.read()
            fichier.close()

fen=Tk()
fen.title("Patient 1")
lib=Label(fen, text="Médication de X 1",
font="Times 14 bold italic", fg="navy")
lib.pack(padx=10, pady=4)

st=ScrolledText(fen, baseFont="Helvetica 12 normal", width=60, height=25)
st.pack(expand=YES, fill=BOTH, padx=8, pady=8)

st.importFichier()

fen.mainloop()
