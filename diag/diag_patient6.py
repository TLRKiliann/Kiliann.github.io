#!/usr/bin/python3
#!-*-encoding:Utf-8-*-


from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from tkinter import filedialog
import subprocess
import os


# La ScrollBar en class! Préparation pour l'application.
class ScrollCanvas(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=borderwidth, relief=relief)
        self.can=Canvas(self, width=width, height=height, bd=bd, bg=bg,
            relief=relief)
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
        But=Button(self, text ="Close", fg='cyan', bg='gray30',
            activebackground='cyan', command=boss.quit).pack(side=LEFT,
            padx=3)

# Application principale
class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self)
        self.master.title('ANGEL-VISION - Developed by CK - Dec. 2018')
        mBar=MenuBar(self)
        mBar.pack(side=TOP, fill=X, expand=1)
        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can=Canvas(self, width=600, height=400, bg='gray17')
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW, 
                                  tags="self.frame")
        # Insertion du texte
        self.can.create_text(300, 150, anchor=CENTER, text="Diagnostics and ATCD",
                    font=('Times New Roman', 28), fill='aquamarine')
        self.can.create_text(170, 770, anchor=NE, text="Copyright (C) 2018 Inc.",
                    font=('Times', 12), fill='white') 
        self.can.pack(side=LEFT, fill=BOTH, expand=1)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # Création des boutons
        self.x, self.y = 200, 250
        self.b=Button(self.can, width=10, font=16, bg='navy', fg='gold', 
                      activebackground='dark turquoise', 
                      activeforeground='black', 
                      text="Add", 
                      command=self.Frame_Ap1)
        self.fb=self.can.create_window(self.x, self.y, window=self.b)

        self.x, self.y = 400, 250
        self.b=Button(self.can, width=10, font=16, bg='navy', fg='gold', 
                      activebackground='dark turquoise', 
                      activeforeground='black', 
                      text="Read", 
                      command=self.Frame_Ap2)
        self.fb=self.can.create_window(self.x, self.y, window=self.b)
        self.pack()

    # Méthode pour reconfigurer la scrollbar à chaque fois
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def Frame_Ap1(self):
        subprocess.call('./diag/doc_diag6/diag_write.py')

    def Frame_Ap2(self):
        subprocess.call('./diag/doc_diag6/diag_read.py')


if __name__=='__main__':
    app = Application()
    app.mainloop()
    