#!/usr/bin/python3
#!-*-encoding:Utf-8-*-


from tkinter import *
import subprocess


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
        self.can.create_window((4, 4), window=self.frame, anchor=NW,
            tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

# Class de la barre des menus
class MenuBar(Frame):
    """Barre menu déroulant"""
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='dim gray', padx=0)
        But2=Button(self, text ="Fermer", fg='red', bg='gray30',
            activebackground='cyan', command=boss.quit).pack(side=LEFT, padx=3)

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
        self.can.create_text(625, 280, anchor=CENTER, text="Patient 1\n",
            font=('Times', 36), fill='aquamarine')
        self.can.create_text(625, 370, anchor=CENTER, text="HISTOIRE DE VIE",
            font=('Times New Roman', 28), fill='aquamarine')
        self.can.create_text(170, 770, anchor=NE, text="Copyright (C) 2018 Inc.",
            font=('Times', 12), fill='white') 
        self.can.pack(side=LEFT, fill=BOTH, expand=1)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.x2, self.y2 = 450, 460
        self.b2=Button(self.can, width=15, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Ajouter",
            command=self.lienDirect)
        self.fb2=self.can.create_window(self.x2, self.y2, window=self.b2)

        self.x3, self.y3 = 790, 460
        self.b3=Button(self.can, width=15, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Lire",
            command=self.lectureFic)
        self.fb3=self.can.create_window(self.x3, self.y3, window=self.b3)
        self.pack()

    # Méthode pour reconfigurer la scrollbar à chaque fois
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def lienDirect(self):
        subprocess.call('./histv/doc_histv/patient1write.py')

    def lectureFic(self):
        subprocess.call('./histv/doc_histv/patient1_read.py')

if __name__=='__main__':
    app = Application()
    app.mainloop()
