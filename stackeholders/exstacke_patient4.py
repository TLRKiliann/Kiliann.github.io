#!/usr/bin/python3
# -*-encoding:Utf-8-*-


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
        But2=Button(self, text ="Close", fg='cyan', bg='gray30', relief=GROOVE,
            activebackground='cyan', command=boss.quit).pack(side=LEFT, padx=3)

# Application principale
class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self)
        self.master.title('ANGEL-VISION - Developed by CK - 2020')
        mBar=MenuBar(self)
        mBar.pack(side=TOP, fill=X, expand=1)
        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can=Canvas(self, width=600, height=600, bg='gray17')
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW,
            tags="self.frame")
        # Insertion du texte
        self.can.create_text(280, 50, anchor=CENTER, text="External Stackeholders",
            font=('Times New Roman', 28), fill='aquamarine')

        self.can.create_text(350, 150, anchor='w', text="Diabetologia",
            font=('Times New Roman', 18), fill='cyan')
        self.can.create_text(350, 200, anchor='w', text="Oncology",
            font=('Times New Roman', 18), fill='cyan')
        self.can.create_text(350, 250, anchor='w', text="Ophtalmology",
            font=('Times New Roman', 18), fill='cyan')
        self.can.create_text(350, 300, anchor='w', text="Dentist",
            font=('Times New Roman', 18), fill='cyan')
        self.can.create_text(350, 350, anchor='w', text="Stomatherapy",
            font=('Times New Roman', 18), fill='cyan')
        self.can.create_text(350, 400, anchor='w', text="Aromatherapy",
            font=('Times New Roman', 18), fill='cyan')
        self.can.create_text(350, 450, anchor='w', text="Physiotherapy",
            font=('Times New Roman', 18), fill='cyan')
        self.can.create_text(350, 500, anchor='w', text="Ergotherapy",
            font=('Times New Roman', 18), fill='cyan')
        self.can.create_text(350, 550, anchor='w', text="Podology",
            font=('Times New Roman', 18), fill='cyan')
        self.can.pack(side=LEFT, fill=BOTH, expand=1)

        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        
        # Button to add Diabetologia
        self.x1, self.y1 = 100, 150
        self.b1=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Add",
            command=self.lienDirect)
        self.fb1=self.can.create_window(self.x1, self.y1, window=self.b1)
        
        # Button to read Diabetologia
        self.x2, self.y2 = 250, 150
        self.b2=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Read",
            command=self.lectureFic)
        self.fb2=self.can.create_window(self.x2, self.y2, window=self.b2)
        self.pack()

        # Button2 to add2 Oncology
        self.x3, self.y3 = 100, 200
        self.b3=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Add",
            command=self.lienDirect)
        self.fb3=self.can.create_window(self.x3, self.y3, window=self.b3)
        
        # Button2 to read2 Oncology
        self.x4, self.y4 = 250, 200
        self.b4=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Read",
            command=self.lectureFic)
        self.fb4=self.can.create_window(self.x4, self.y4, window=self.b4)
        self.pack()

        # Button3 to add3 Ophtalmology
        self.x5, self.y5 = 100, 250
        self.b5=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Add",
            command=self.lienDirect)
        self.fb5=self.can.create_window(self.x5, self.y5, window=self.b5)
        
        # Button3 to read3 Ophtalmology
        self.x6, self.y6 = 250, 250
        self.b6=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Read",
            command=self.lectureFic)
        self.fb6=self.can.create_window(self.x6, self.y6, window=self.b6)
        self.pack()

        # Button4 to add4 Dentist
        self.x7, self.y7 = 100, 300
        self.b7=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Add",
            command=self.lienDirect)
        self.fb7=self.can.create_window(self.x7, self.y7, window=self.b7)
        
        # Button4 to read4 Dentist
        self.x8, self.y8 = 250, 300
        self.b8=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Read",
            command=self.lectureFic)
        self.fb8=self.can.create_window(self.x8, self.y8, window=self.b8)
        self.pack()

        # Button5 to add5 Stomatherapy
        self.x9, self.y9 = 100, 350
        self.b9=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Add",
            command=self.lienDirect)
        self.fb9=self.can.create_window(self.x9, self.y9, window=self.b9)
        
        # Button5 to read5 Stomatherapy
        self.x10, self.y10 = 250, 350
        self.b10=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Read",
            command=self.lectureFic)
        self.fb10=self.can.create_window(self.x10, self.y10, window=self.b10)
        self.pack()

        # Button6 to add6 Aromatherapy
        self.x11, self.y11 = 100, 400
        self.b11=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Add",
            command=self.linkNeeds)
        self.fb11=self.can.create_window(self.x11, self.y11, window=self.b11)
        
        # Button6 to read6 Aromatherapy
        self.x12, self.y12 = 250, 400
        self.b12=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Read",
            command=self.readFileNeeds)
        self.fb12=self.can.create_window(self.x12, self.y12, window=self.b12)
        self.pack()

        # Button7 to add7 Physiotherapy
        self.x11, self.y11 = 100, 450
        self.b11=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Add",
            command=self.lienDirect)
        self.fb11=self.can.create_window(self.x11, self.y11, window=self.b11)
        
        # Button7 to read7 Physiotherapy
        self.x12, self.y12 = 250, 450
        self.b12=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Read",
            command=self.lectureFic)
        self.fb12=self.can.create_window(self.x12, self.y12, window=self.b12)
        self.pack()

        # Button8 to add8 Ergotherapy
        self.x13, self.y13 = 100, 500
        self.b13=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Add",
            command=self.lienDirect)
        self.fb13=self.can.create_window(self.x13, self.y13, window=self.b13)
        
        # Button8 to read8 Ergotherapy
        self.x14, self.y14 = 250, 500
        self.b14=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Read",
            command=self.lectureFic)
        self.fb14=self.can.create_window(self.x14, self.y14, window=self.b14)
        self.pack()

        # Button9 to add9 Podology
        self.x15, self.y15 = 100, 550
        self.b15=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Add",
            command=self.linkNeeds)
        self.fb15=self.can.create_window(self.x15, self.y15, window=self.b15)
        
        # Button9 to read9 Podology
        self.x16, self.y16 = 250, 550
        self.b16=Button(self.can, width=10, font=16, bg='navy', fg='gold',
            activebackground='dark turquoise',
            activeforeground='black', text="Read",
            command=self.readFileNeeds)
        self.fb16=self.can.create_window(self.x16, self.y16, window=self.b16)
        self.pack()

    # Méthode pour reconfigurer la scrollbar à chaque fois
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    # Func to add
    def lienDirect(self):
        try:
            if os.path.getsize('./vmed/doc_vmed4/resultvmed.txt'):
                print("+ File 'VMED4' exist (add)!")
                subprocess.call('./vmed/doc_vmed4/vmed_write.py')
        except FileNotFoundError as outmsg:
            print("+ Sorry, file 'VMED4' not exist !", outmsg)
            print("+ File 'VMED4' created !")
            self.confRec()

    # Func to read
    def lectureFic(self):
        try:
            if os.path.getsize('./vmed/doc_vmed4/resultvmed.txt'):
                print("+ File 'VMED4' exist (read)!")
                subprocess.call('./vmed/doc_vmed4/vmed_read.py')
        except FileNotFoundError as outcom:
            print("+ Sorry, file 'VMED4' not exist !", outcom)
            self.confRec()

    def linkNeeds(self):
        try:
            if os.path.getsize('./14besoins/doc_suivi4/patient4_14b.txt'):
                print("+ File '14Needs4' exist (add)!")
                subprocess.call('./14besoins/doc_suivi4/patient4_write.py')
        except FileNotFoundError as outmsg2:
            print("+ Sorry, file '14Needs4' not exist !", outmsg2)
            print("+ File 14Needs4 created !")
            self.confRec()

    # Func to read
    def readFileNeeds(self):
        try:
            if os.path.getsize('./14besoins/doc_suivi4/patient4_14b.txt'):
                print("+ File '14Needs4' exist (read)!")
                subprocess.call('./14besoins/doc_suivi4/patient4_read.py')
        except FileNotFoundError as outcom2:
            print("+ Sorry, file '14Needs4' not exist !", outcom2)
            self.confRec()

    def confRec(self):
        self.MsgBox2msg = messagebox.showinfo("Warning", "File 'VMED4'"
            "was not created. No Medical Visit has been checked !")

if __name__=='__main__':
    app = Application()
    app.mainloop()
