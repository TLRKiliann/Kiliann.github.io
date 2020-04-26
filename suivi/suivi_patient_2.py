#!/usr/bin/python3
#!-*-encoding:Utf-8-*-


import tkinter
from tkinter import *
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import subprocess
import os

   
# La ScrollBar en class! Préparation pour l'application.
class ScrollCanvas(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=borderwidth, relief=relief)
        self.can=Canvas(self, width=width, height=height, bd=bd, bg=bg, relief=relief)
        self.frame = Frame(self.can)

        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW,
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

# Class de la barre des menus
class MenuBar(Frame):
    """Barre menu déroulant"""
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='dim gray', padx=0)
        # Bouton pour page d'accueil
        But3=Button(self, text ="Fermer", fg='red', bg='gray30', activebackground='cyan',
            command=boss.quit).pack(side=LEFT, padx=3)

# Application principale
class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self)
        self.master.title('ANGEL-VISION - Developed by CK - 2018-2020')
        mBar=MenuBar(self)
        mBar.pack(side=TOP, fill=X, expand=1)
        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can=Canvas(self, width=1250, height=800, bg='gray17')
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW,
                                  tags="self.frame")
        # Insertion du texte
        self.can.create_text(550, 80, anchor=NW, text="SUIVI",
                    font=('Times New Roman', 26), fill='aquamarine')
        self.can.create_text(1175, 770, anchor=NE, text="Copyright (C) 2018 Inc.",
                    font=('Times', 12), fill='white')
        self.can.pack(side=RIGHT, fill=BOTH, expand=1)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # Création des boutons
        self.can.create_text(20, 150, anchor=NW, text="Suivi: Patient 2",
                    font=('Times', 20), fill='aquamarine')

        self.can.create_text(20, 200, anchor=NW, text="01.01.2019 au 07.01.2019\n",
                    font=('Times', 16), fill='white')

        self.x1, self.y1 = 120, 250
        self.b1=Button(self.can, width=15, font=10, bg='navy', fg='gold',
                      activebackground='dark turquoise',
                      activeforeground='black',
                      text="Ouvrir le fichier",
                      command=self.suivia)
        self.fb1=self.can.create_window(self.x1, self.y1, window=self.b1)

        #Label dans lequel écrire
        self.x2, self.y2 = 610, 250
        self.Data_towrite=Entry(self.can)
        self.new_totext=StringVar()
        self.Data_towrite=Entry(textvariable=self.new_totext,
          highlightbackground='gray', bd=4, width=90)
        self.new_totext.set(" ")
        self.Data_towrite=self.can.create_window(self.x2, self.y2,
          window=self.Data_towrite)

        #ButtonLabel click pour entrer les data
        self.x3, self.y3 = 1100, 250
        self.b3=Button(self.can, width=15, font=10, bg='navy', fg='gold',
                      activebackground='dark turquoise',
                      activeforeground='black',
                      text="Entrer l'écrit",
                      command=self.entrerEcrit1)
        self.fb3=self.can.create_window(self.x3, self.y3, window=self.b3)

        #ButtonLabel click delete
        self.x4, self.y4 = 1100, 290
        self.b4=Button(self.can, width=15, font=10, bg='navy', fg='cyan',
                      activebackground='dark turquoise',
                      activeforeground='black',
                      text="Effacer",
                      command=self.deleteCap1)
        self.fb4=self.can.create_window(self.x4, self.y4, window=self.b4)

        self.can.create_text(20, 300, anchor=NW, text="07.01.2019 au 15.01.2019\n",
                    font=('Times', 16), fill='white')

        self.x5, self.y5 = 120, 350
        self.b5=Button(self.can, width=15, font=10, bg='navy', fg='gold',
                      activebackground='dark turquoise',
                      activeforeground='black',
                      text="Ouvrir le fichier",
                      command=self.suivia2)
        self.fb5=self.can.create_window(self.x5, self.y5, window=self.b5)

        #Label dans lequel écrire
        self.x6, self.y6 = 610, 350
        self.Data_write=Entry(self.can)
        self.new_text=StringVar()
        self.Data_write=Entry(textvariable=self.new_text,
          highlightbackground='gray', bd=4, width=90)
        self.new_text.set(" ")
        self.Data_write=self.can.create_window(self.x6, self.y6,
          window=self.Data_write)

        #ButtonLabel click pour entrer les data
        self.x7, self.y7 = 1100, 350
        self.b7=Button(self.can, width=15, font=10, bg='navy', fg='gold',
                      activebackground='dark turquoise',
                      activeforeground='black',
                      text="Entrer l'écrit",
                      command=self.entrerEcrit2)
        self.fb7=self.can.create_window(self.x7, self.y7, window=self.b7)

        #ButtonLabel click delete
        self.x8, self.y8 = 1100, 390
        self.b8=Button(self.can, width=15, font=10, bg='navy', fg='cyan',
                      activebackground='dark turquoise',
                      activeforeground='black',
                      text="Effacer",
                      command=self.deleteCap2)
        self.fb8=self.can.create_window(self.x8, self.y8, window=self.b8)

        self.can.create_text(20, 400, anchor=NW, text="16.01.2019 au 20.01.2019\n",
                    font=('Times', 16), fill='white')

        self.x9, self.y9 = 120, 450
        self.b9=Button(self.can, width=15, font=10, bg='navy', fg='gold',
                      activebackground='dark turquoise',
                      activeforeground='black',
                      text="Ouvrir le fichier",
                      command=self.suivia3)
        self.fb9=self.can.create_window(self.x9, self.y9, window=self.b9)

        #Label dans lequel écrire
        self.x10, self.y10 = 610, 450
        self.Data_write2=Entry(self.can)
        self.new_text2=StringVar()
        self.Data_write2=Entry(textvariable=self.new_text2,
          highlightbackground='gray', bd=4, width=90)
        self.new_text2.set(" ")
        self.Data_write2=self.can.create_window(self.x10, self.y10,
          window=self.Data_write2)

        #ButtonLabel click pour entrer les data
        self.x11, self.y11 = 1100, 450
        self.b11=Button(self.can, width=15, font=10, bg='navy', fg='gold',
                      activebackground='dark turquoise',
                      activeforeground='black',
                      text="Entrer l'écrit",
                      command=self.entrerEcrit3)
        self.fb11=self.can.create_window(self.x11, self.y11, window=self.b11)

        #ButtonLabel click delete
        self.x12, self.y12 = 1100, 490
        self.b12=Button(self.can, width=15, font=10, bg='navy', fg='cyan',
                      activebackground='dark turquoise',
                      activeforeground='black',
                      text="Effacer",
                      command=self.deleteCap3)
        self.fb12=self.can.create_window(self.x12, self.y12, window=self.b12)

        self.can.create_text(20, 500, anchor=NW, text="20.01.2019 au 30.01.2019\n",
                    font=('Times', 16), fill='white')

        self.x13, self.y13 = 120, 550
        self.b13=Button(self.can, width=15, font=10, bg='navy', fg='gold',
                      activebackground='dark turquoise',
                      activeforeground='black',
                      text="Ouvrir le fichier",
                      command=self.suivia4)
        self.fb13=self.can.create_window(self.x13, self.y13, window=self.b13)

        #Label dans lequel écrire
        self.x14, self.y14 = 610, 550
        self.Data_write3=Entry(self.can)
        self.new_text3=StringVar()
        self.Data_write3=Entry(textvariable=self.new_text3, highlightbackground='gray',
          bd=4, width=90)
        self.new_text3.set(" ")
        self.Data_write3=self.can.create_window(self.x14, self.y14,
          window=self.Data_write3)

        #ButtonLabel click pour entrer les data
        self.x15, self.y15 = 1100, 550
        self.b15=Button(self.can, width=15, font=10, bg='navy', fg='gold',
                      activebackground='dark turquoise',
                      activeforeground='black',
                      text="Entrer l'écrit",
                      command=self.entrerEcrit4)
        self.fb15=self.can.create_window(self.x15, self.y15, window=self.b15)

        #ButtonLabel click delete
        self.x16, self.y16 = 1100, 590
        self.b16=Button(self.can, width=15, font=10, bg='navy', fg='cyan',
                      activebackground='dark turquoise',
                      activeforeground='black',
                      text="Effacer",
                      command=self.deleteCap4)
        self.fb16=self.can.create_window(self.x16, self.y16, window=self.b16)

        self.can.configure(scrollregion=self.can.bbox(ALL))
        self.pack()

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def effacer(self):
        '''Réinitialise le canevas quand on passe d'un à l'autre'''
        self.can.delete(ALL)
    #Fenetre pour ouvrir le fichier de la vma:
    def deleteCap1(self):
        self.new_totext.set(" ")

    def deleteCap2(self):
        self.new_text .set(" ")

    def deleteCap3(self):
        self.new_text2.set(" ")

    def deleteCap4(self):
        self.new_text3.set(" ")

    def suivia(self):
        self.label=Tk()
        self.label.title("VM_01.01.19_au_07.01.19")
        filepath=filedialog.askopenfilename(filetypes=[('./suivi/suivi_doc/suivi_patient_2/sui_01.01.19_AE', '.txt')])
        fichier=open('./suivi/suivi_doc/suivi_patient_2/sui_01.01.19_AE.txt', 'r')
        content=fichier.read()
        fichier.close()
        self.label=Label(self.label, justify=LEFT, font=('Times', 12), bg='gray22', 
            fg='cyan', text=content).pack(padx=10, pady=10)

    def entrerEcrit1(self):
        fichier=open('./suivi/suivi_doc/suivi_patient_2/sui_01.01.19_AE.txt', 'a+')
        fichier.write("\n" + self.new_totext.get())
        fichier.close()

    def suivia2(self):
        self.label=Tk()
        self.label.title("VM_07.01.19_au_15.01.19")
        filepath=filedialog.askopenfilename(filetypes=[('./suivi/suivi_doc/suivi_patient_2/sui_07.01.19_AE', '.txt')])
        fichier=open('./suivi/suivi_doc/suivi_patient_2/sui_07.01.19_AE.txt', 'r')
        content=fichier.read()
        fichier.close()
        self.label=Label(self.label, justify=LEFT, font=('Times', 12), bg='gray22', fg='cyan', 
            text=content).pack(padx=10, pady=10)

    def entrerEcrit2(self):
        fichier=open('./suivi/suivi_doc/suivi_patient_2/sui_07.01.19_AE.txt', 'a+')
        fichier.write("\n" + self.new_text.get())
        fichier.close()

    def suivia3(self):
        self.label=Tk()
        self.label.title("VM_16.01.19_au_15.01.19")
        filepath=filedialog.askopenfilename(filetypes=[('./suivi/suivi_doc/suivi_patient_2/sui_16.01.19_AE', '.txt')])
        fichier=open('./suivi/suivi_doc/suivi_patient_2/sui_16.01.19_AE.txt', 'r')
        content=fichier.read()
        fichier.close()
        self.label=Label(self.label, justify=LEFT, font=('Times', 12), bg='gray22', fg='cyan', 
            text=content).pack(padx=10, pady=10)

    def entrerEcrit3(self):
        fichier=open('./suivi/suivi_doc/suivi_patient_2/sui_16.01.19_AE.txt', 'a+')
        fichier.write("\n" + self.new_text2.get())
        fichier.close()

    def suivia4(self):
        self.label=Tk()
        self.label.title("VM_20.01.19_au_30.01.19")
        filepath=filedialog.askopenfilename(filetypes=[('./suivi/suivi_doc/suivi_patient_2/sui_20.01.19_AE', '.txt')])
        fichier=open('./suivi/suivi_doc/suivi_patient_2/sui_20.01.19_AE.txt', 'r')
        content=fichier.read()
        fichier.close()
        self.label=Label(self.label, justify=LEFT, font=('Times', 12), bg='gray22', fg='cyan', 
            text=content).pack(padx=10, pady=10)
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def entrerEcrit4(self):
        fichier=open('./suivi/suivi_doc/suivi_patient_2/sui_20.01.19_AE.txt', 'a+')
        fichier.write("\n" + self.new_text3.get())
        fichier.close()

if __name__=='__main__':
    app = Application()
    app.mainloop()
