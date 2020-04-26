#!/usr/bin/python3
#!-*-encoding:Utf-8-*-

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from tkinter import filedialog
#import subprocess
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
        # Menu fichier
        But=Button(self, text ="Fermer", fg='red', bg='gray30', activebackground='cyan', 
            command=boss.quit).pack(side=LEFT, padx=3)

# Application principale
class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self)
        self.master.title('ANGEL-VISION - Developed by CK - Dec. 2018')
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
        self.can.create_text(625, 280, anchor=CENTER, text="Patient 5",
                    font=('Times New Roman', 36), fill='aquamarine')
        self.can.create_text(625, 370, anchor=CENTER, text="ANGEL-VISION",
                    font=('Times New Roman', 18), fill='aquamarine')
        self.can.create_text(170, 770, anchor=NE, text="Copyright (C) 2018 Inc.",
                    font=('Times', 12), fill='white') 
        self.can.pack(side=LEFT, fill=BOTH, expand=1)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # Création des boutons
        self.x, self.y = 425, 460
        self.b=Button(self.can, width=15, font=16, bg='navy', fg='gold', 
                      activebackground='dark turquoise', 
                      activeforeground='black', 
                      text="Diagnostics", 
                      command=self.Frame_Ap1)
        self.fb=self.can.create_window(self.x, self.y, window=self.b)

        self.x, self.y = 625, 460
        self.b=Button(self.can, width=15, font=16, bg='navy', fg='gold', 
                      activebackground='dark turquoise', 
                      activeforeground='black', 
                      text="ATCD", 
                      command=self.Frame_Ap2)
        self.fb=self.can.create_window(self.x, self.y, window=self.b)

        self.x, self.y = 825, 460
        self.b=Button(self.can, width=15, font=16, bg='navy', fg='gold', 
                      activebackground='dark turquoise', 
                      activeforeground='black', 
                      text="TTT", 
                      command=self.Frame_Ap3)
        self.fb=self.can.create_window(self.x, self.y, window=self.b)

        self.pack()

    # Méthode pour reconfigurer la scrollbar à chaque fois
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def Frame_Ap1(self):
        self.Lab=Tk()
        self.Lab.title("Diagnostics")
        self.Lab1=Label(self.Lab, text="\nPatient 5").pack()
        self.separator = Frame(self.Lab, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=5, pady=5)

        self.Lab2=Label(self.Lab, text="\nDiagnostics").pack()
        self.separator = Frame(self.Lab, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=5, pady=5)

        self.Lab3=Label(self.Lab, justify=LEFT, font=('Times', 12), text="\nSchzophrénie paranoïde\n"
        "Résection du tractus gastro-intestinale.\n" 
        "Cirrhose hépatique.\n"
        "Cholangite sclérosante primitive.\n").pack()
        self.separator = Frame(self.Lab, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=5, pady=5)

    def Frame_Ap2(self):
        self.Lab=Tk()
        self.Lab.title("ATCD")
        self.Lab3=Label(self.Lab, text="\nPatient 5").pack()
        self.separator = Frame(self.Lab, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=5, pady=5)

        self.Lab4=Label(self.Lab, text="\nATCD").pack()
        self.separator = Frame(self.Lab, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=5, pady=5)

        self.Lab5=Label(self.Lab, justify=LEFT, font=('Times', 12), 
            text="\nEpisodes de maniaco-dépression à répétition, manifestés lors de contexte à fort stress.\n" 
        "Etats confusionnels et d'agitation sévères chez les patients artérioscléreux et lors d'oligophrénie.\n" 
        "Clopixol Acutard: Traitement initial\n" 
        "Effets secondaires fréquents: augmentation de l'appétit, prise de poids, insomnie, dépression, anxiété,\n" 
        "nervosité, rêves étranges, agitation, diminution de la tolérance et diminue donc vite au cours d'un\n" 
        "traitement à long terme.\n").pack()
        self.separator = Frame(self.Lab, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=5, pady=5)

    def Frame_Ap3(self):
        self.Lab=Tk()
        self.Lab.title("TTT\n")
        self.Lab2=Label(self.Lab, text="\nPatient 5").pack()
        self.separator = Frame(self.Lab, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=5, pady=5)

        self.Lab3=Label(self.Lab, text="\nMédication").pack()
        self.separator = Frame(self.Lab, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=5, pady=5)

        self.Lab4=Label(self.Lab, justify=LEFT, text="\nCipralex\n"
        "Xanax\n"
        "Clopixol\n"
        "Zyprexa\n" 
        "Solmucol\n"
        "Omep\n").pack()
        self.separator = Frame(self.Lab, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=5, pady=5)

if __name__=='__main__':
    app = Application()
    app.mainloop()
    