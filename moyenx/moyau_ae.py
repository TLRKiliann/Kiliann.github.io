#!/usr/bin/python3
#!-*-encoding:Utf-8-*-

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from tkinter import filedialog
#import subprocess
#import os
  
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
        # FunnyButton=Button(self, text ="Page d'accueil", relief=GROOVE, fg='cyan', bg='gray15', activebackground='cyan', command=boss.frameAp1).pack(side =LEFT, padx=3)
        But=Button(self, text ="Moyens Auxiliaires", fg='cyan', bg='gray30', activebackground='cyan', command=boss.frameMoyen1).pack(side=LEFT, padx=3)
        But2=Button(self, text ="Quitter", fg='red', bg='gray30', activebackground='cyan', command=boss.quit).pack(side=LEFT, padx=3)
        # Menu fichier
        # fileMenu = Menubutton(self, text='Fichier', fg='white', bg='grey30', relief=GROOVE)
        # fileMenu.pack(side=LEFT, padx=3)

# Application principale
class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self)
        self.master.title('ANGEL-VISION - Developed by CK - Dec. 2018-2020')
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
        self.can.create_text(625, 280, anchor=CENTER, text="Alain Exemple\n",
                    font=('Times', 36), fill='aquamarine')
        self.can.create_text(625, 370, anchor=CENTER, text="ANGEL-VISION",
                    font=('Times New Roman', 18), fill='aquamarine')
        self.can.create_text(170, 770, anchor=NE, text="Copyright (C) 2018 Inc.",
                    font=('Times', 12), fill='white') 
        self.can.pack(side=LEFT, fill=BOTH, expand=1)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.x, self.y = 630, 460
        self.b=Button(self.can, width=15, font=16, bg='navy', fg='gold', 
                      activebackground='dark turquoise', 
                      activeforeground='black', 
                      text="Moyens Auxiliaires", 
                      command=self.frameMoyen1)
        self.fb=self.can.create_window(self.x, self.y, window=self.b)

        self.pack()

    # Méthode pour reconfigurer la scrollbar à chaque fois
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def effacer(self):
        '''Réinitialise le canevas quand on passe d'un à l'autre'''
        self.can.delete(ALL)

    def secondFrame(self):
        self.can.delete(ALL)
        # Insertion du texte
        self.can.create_text(625, 280, anchor=CENTER, text="Alain Exemple\n",
                    font=('Times', 36), fill='aquamarine')
        self.can.create_text(625, 370, anchor=CENTER, text="ANGEL-VISION",
                    font=('Times New Roman', 18), fill='aquamarine')
        self.can.create_text(170, 770, anchor=NE, text="Copyright (C) 2018 Inc.",
                    font=('Times', 12), fill='white') 
        self.can.pack(side=LEFT, fill=BOTH, expand=1)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # Création des boutons
        self.x, self.y = 630, 460
        self.b=Button(self.can, width=15, font=16, bg='navy', fg='gold', 
                      activebackground='dark turquoise', 
                      activeforeground='black', 
                      text="Moyens Auxiliaires", 
                      command=self.frameMoyen1)
        self.fb=self.can.create_window(self.x, self.y, window=self.b)

        self.pack()

        self.can.configure(scrollregion=self.can.bbox(ALL)) 

    # Histoire de vie
    def frameMoyen1(self):
        self.can.delete(ALL)

        self.can.create_text(10, 50, anchor=NW, text="-MOYENS AUXILIAIRES-",
                    font=('Times', 22), fill='turquoise')
        self.can.create_text(10, 120, anchor=NW, text="------------------------\n"
                                                      "+ Un fauteuil roulant\n"
                                                      "------------------------\n"
                                                      "+ Un tintébin\n"
                                                      "------------------------\n" 
                                                      "+ Des lunettes\n"
                                                      "------------------------\n"
                                                      "+ Des appareils auditifs\n"
                                                      "------------------------\n",
                    font=('Times', 14), fill='white')

        button16=Button(self, text="<---", bg="gray50", fg='turquoise', command=self.secondFrame, anchor=CENTER)
        button16.configure(width=10, activebackground='snow2', activeforeground='dark gray', relief=GROOVE)
        button16_window = self.can.create_window(8, 0, anchor=NW, window=button16)

        self.can.configure(scrollregion=self.can.bbox(ALL))

if __name__=='__main__':
    app = Application()
    app.mainloop()


