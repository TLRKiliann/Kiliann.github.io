#!/usr/bin/python3
#!-*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
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
        self.can.create_window((4, 4), window=self.frame, anchor=NW,
            tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

# Class de la barre des menus
class MenuBar(Frame):
    """Barre menu déroulant"""
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='dim gray', padx=0)
        But2=Button(self, text ="Close", fg='cyan', bg='navy',
            activebackground='cyan', command=boss.quit).pack(side=LEFT, padx=3)

# Application principale
class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self)
        self.master.title('ANGEL-VISION - Developed by CK - 2020')
        mBar=MenuBar(self)
        mBar.pack(side=TOP, fill=X, expand=1)
        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can=Canvas(self, width=600, height=400, bg='#82193e')
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW,
            tags="self.frame")
        # Insertion du texte
        self.can.create_text(300, 160, anchor=CENTER, text="Life story\n",
            font=('Times New Roman', 32), fill='cyan')
        self.can.create_text(590, 380, anchor=NE, text="ANGEL-VISION",
            font=('Times', 12), fill='white') 
        self.can.pack(side=LEFT, fill=BOTH, expand=1)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # Button to add
        self.x2, self.y2 = 200, 250
        self.b2=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='gold',
            activebackground='dark turquoise', bd=3, highlightbackground='grey17', 
            text="Add", command=self.lienDirect)
        self.fb2=self.can.create_window(self.x2, self.y2, window=self.b2)
        # Button to read
        self.x3, self.y3 = 400, 250
        self.b3=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='gold',
            activebackground='dark turquoise', bd=3, highlightbackground='grey17', 
            text="Read", command=self.lectureFic)
        self.fb3=self.can.create_window(self.x3, self.y3, window=self.b3)
        self.pack()

    # Méthode pour reconfigurer la scrollbar à chaque fois
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def lienDirect(self):
        """
        To verify and write story life
        """
        try:
            if os.path.getsize('./histv/doc_histv5/Hvie_patient5.txt'):
                print("+ File 'Story Life' exist (add)!")
                subprocess.call('./histv/doc_histv5/story_write.py')
        except FileNotFoundError as outmsg:
            print("+ Sorry, file 'Story Life' not exist !", outmsg)
            print("+ File 'Story Life' created !")
            with open('./histv/doc_histv5/Hvie_patient5.txt', 'w') as file:
                file.write(".")
            self.confRec()
            subprocess.call('./histv/doc_histv5/story_write.py')

    def lectureFic(self):
        """
        To verify and read story life
        """
        try:
            if os.path.getsize('./histv/doc_histv5/Hvie_patient5.txt'):
                print("+ File 'Story Life' exist (read)!")
                subprocess.call('./histv/doc_histv5/story_read.py')
        except FileNotFoundError as outcom:
            print("+ Sorry, file 'Story Life' not exist !", outcom)
            self.confRec()

    def confRec(self):
        self.MsgBox2msg = messagebox.showinfo("Warning", "File 'storylife'"
            "was created, but no Story Life has been checked !")

if __name__=='__main__':
    app = Application()
    app.mainloop()
