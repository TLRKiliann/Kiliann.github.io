#!/usr/bin/python3
#!-*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
#from tkinter import filedialog
#import os
import subprocess


# La ScrollBar in class and preparing for main application !
class ScrollCanvas(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=borderwidth, relief=relief)
        self.can = Canvas(self, width=width, height=height, bd=bd,
            bg=bg, relief=relief)
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW,
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

# Class to menubar
class MenuBar(Frame):
    """Barre menu déroulant"""
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='dim gray', padx=0)
        # 1st menu
        fileMenu = Menubutton(self, text='Menu', fg='white',
            bg='gray30', relief=GROOVE)
        fileMenu.pack(side=LEFT, padx=3)
        # Partie déroulante du menu 1st
        me1 = Menu(fileMenu, tearoff=0)
        me1.add_separator()
        me1.add_command(label='Accueil', underline=0, background='black',
            activebackground='aquamarine',
            foreground='aquamarine', activeforeground='black',
            command=boss.page)
        me1.add_separator()
        me1.add_command(label="Synopsis", underline=0, background='black',
            activebackground='cyan',
            foreground='aquamarine', activeforeground='black',
            command=boss.showsynopsis)
        me1.add_separator()
        me1.add_command(label="Psychotabs", underline=0, background='black', 
            activebackground='cyan',
            foreground='aquamarine', activeforeground='black',
            command=boss.launchPsycho)
        me1.add_separator()
        me1.add_command(label='Installation', background='black',
            activebackground='aquamarine',
            foreground='yellow', activeforeground='black',
            command=boss.instalpy)
        me1.add_separator()
        me1.add_command(label='QUITTER', underline=0, background='black',
            activebackground='red',
            foreground='red', activeforeground='white',
            command=boss.msgExit)
        me1.add_separator()
        # Integration of 1st menu
        fileMenu.configure(activeforeground='black', activebackground='cyan',
            menu=me1)

        # For label below (in me2.add_command)
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1=namefile.readline()
            line2=namefile.readline()
            line3=namefile.readline()
            line4=namefile.readline()
            line5=namefile.readline()
            line6=namefile.readline()
            line7=namefile.readline()
            line8=namefile.readline()
            line9=namefile.readline()
            line10=namefile.readline()
            line11=namefile.readline()
            line12=namefile.readline()
            line13=namefile.readline()
            line14=namefile.readline()
            line15=namefile.readline()
            line16=namefile.readline()
            line17=namefile.readline()
            line18=namefile.readline()
            line19=namefile.readline()

        self.new_text=line1
        self.new_text2=line4
        self.new_text3=line7
        self.new_text4=line10
        self.new_text5=line13
        self.new_text6=line16
        self.new_text7=line19

        # Menu administrative
        self.cmd_Admin=Menubutton(self, text='Admin', fg='cyan', bg='gray30', relief=GROOVE)
        self.cmd_Admin.pack(side=LEFT, padx=3)
        # Partie déroulante du menu administrative
        me2 = Menu(self.cmd_Admin)
        me2.add_command(label=self.new_text, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.adminDir)
        me2.add_separator()
        me2.add_command(label=self.new_text2, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.adminDir2)
        me2.add_separator()
        me2.add_command(label=self.new_text3, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.adminDir3)
        me2.add_separator()
        me2.add_command(label=self.new_text4, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.adminDir4)
        me2.add_separator()
        me2.add_command(label=self.new_text5, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.adminDir5)
        me2.add_separator()
        me2.add_command(label=self.new_text6, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.adminDir6)
        me2.add_separator()
        me2.add_command(label=self.new_text7, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.adminDir7)
        # Integration of menu admin
        self.cmd_Admin.configure(activeforeground='black', activebackground='cyan', menu=me2)

        # Agenda menu
        self.cmd_agenda=Menubutton(self, text='Agenda', fg='cyan', bg='gray30', relief=GROOVE)
        self.cmd_agenda.pack(side=LEFT, padx=3)
        me3 = Menu(self.cmd_agenda)
        # Partie déroulante du menu agenda
        me3.add_command(label=self.new_text, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.patientAgenda)
        me3.add_separator()
        me3.add_command(label=self.new_text2, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.patientAgenda2)
        me3.add_separator()
        me3.add_command(label=self.new_text3, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.patientAgenda3)
        me3.add_separator()
        me3.add_command(label=self.new_text4, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.patientAgenda4)
        me3.add_separator()
        me3.add_command(label=self.new_text5, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.patientAgenda5)
        me3.add_separator()
        me3.add_command(label=self.new_text6, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.patientAgenda6)
        me3.add_separator()
        me3.add_command(label=self.new_text7, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.patientAgenda7)
        me3.add_separator()
        # Integration of agenda menu
        self.cmd_agenda.configure(activeforeground='black', activebackground='cyan', menu=me3)

        # 14 besoins menu
        self.cmd_Besoins=Menubutton(self, text='14 needs', fg='cyan', bg='gray30',
            relief=GROOVE)
        self.cmd_Besoins.pack(side=LEFT, padx=3)
        # Partie déroulante du menu 14b
        me4 = Menu(self.cmd_Besoins)
        me4.add_command(label=self.new_text, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.besoinsCoche)
        me4.add_separator()
        me4.add_command(label=self.new_text2, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.besoins2Coche)
        me4.add_separator()
        me4.add_command(label=self.new_text3, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.besoins3Coche)
        me4.add_separator()
        me4.add_command(label=self.new_text4, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.besoins4Coche)
        me4.add_separator()
        me4.add_command(label=self.new_text5, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.besoins5Coche)
        me4.add_separator()
        me4.add_command(label=self.new_text6, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.besoins6Coche)
        me4.add_separator()
        me4.add_command(label=self.new_text7, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.besoins7Coche)
        me4.add_separator()
        # Integration of 14b menu
        self.cmd_Besoins.configure(activeforeground='black', activebackground='cyan', menu=me4)

        # Helth and care menu
        self.cmd_Soins=Menubutton(self, text='Care and monitoring', fg='cyan', bg='gray30',
            relief=GROOVE)
        self.cmd_Soins.pack(side=LEFT, padx=3)
        # Partie déroulante du menu health and care
        meSoins = Menu(self.cmd_Soins)
        meSoins.add_command(label=self.new_text, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.suiviSoins1)
        meSoins.add_separator()
        meSoins.add_command(label=self.new_text2, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.suiviSoins2)
        meSoins.add_separator()
        meSoins.add_command(label=self.new_text3, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.suiviSoins3)
        meSoins.add_separator()
        meSoins.add_command(label=self.new_text4, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.suiviSoins4)
        meSoins.add_separator()
        meSoins.add_command(label=self.new_text5, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.suiviSoins5)
        meSoins.add_separator()
        meSoins.add_command(label=self.new_text6, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.suiviSoins6)
        meSoins.add_separator()
        meSoins.add_command(label=self.new_text7, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.suiviSoins7)
        meSoins.add_separator()
        # Integration of health and care menu
        self.cmd_Soins.configure(activeforeground='black', activebackground='cyan', menu=meSoins)

        # Treatments
        self.cmd_ttt=Menubutton(self, text='Treatments', fg='cyan', bg='gray30',
            relief=GROOVE)
        self.cmd_ttt.pack(side=LEFT, padx=3)
        # Partie déroulante du menu health and care
        meTtt = Menu(self.cmd_ttt)
        meTtt.add_command(label=self.new_text, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.tttMed1)
        meTtt.add_separator()
        meTtt.add_command(label=self.new_text2, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.tttMed2)
        meTtt.add_separator()
        meTtt.add_command(label=self.new_text3, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.tttMed3)
        meTtt.add_separator()
        meTtt.add_command(label=self.new_text4, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.tttMed4)
        meTtt.add_separator()
        meTtt.add_command(label=self.new_text5, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.tttMed5)
        meTtt.add_separator()
        meTtt.add_command(label=self.new_text6, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.tttMed6)
        meTtt.add_separator()
        meTtt.add_command(label=self.new_text7, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.tttMed7)
        meTtt.add_separator()
        # Integration of health and care menu
        self.cmd_ttt.configure(activeforeground='black', activebackground='cyan',
            menu=meTtt)

        # Vital parameters menu
        self.cmd_Param=Menubutton(self, text='Vital Parameters', fg='cyan', bg='gray30',
            relief=GROOVE)
        self.cmd_Param.pack(side=LEFT, padx=3)
        # Partie déroulante du menu param
        menuParam = Menu(self.cmd_Param)
        menuParam.add_command(label=self.new_text, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.showParam1)
        menuParam.add_separator()
        menuParam.add_command(label=self.new_text2, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.showParam2)
        menuParam.add_separator()
        menuParam.add_command(label=self.new_text3, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.showParam3)
        menuParam.add_separator()
        menuParam.add_command(label=self.new_text4, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.showParam4)
        menuParam.add_separator()
        menuParam.add_command(label=self.new_text5, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.showParam5)
        menuParam.add_separator()
        menuParam.add_command(label=self.new_text6, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.showParam6)
        menuParam.add_separator()
        menuParam.add_command(label=self.new_text7, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.showParam7)
        menuParam.add_separator()
        # Integration of Vital parameters menu
        self.cmd_Param.configure(activeforeground='black', activebackground='cyan',
            menu=menuParam)

        # BMI menu
        self.cmd_BMI=Menubutton(self, text='Body Mass Indice', fg='cyan', bg='gray30',
            relief=GROOVE)
        self.cmd_BMI.pack(side=LEFT, padx=3)
        # drop-down portion of BMI menu
        meBmi = Menu(self.cmd_BMI)
        meBmi.add_command(label=self.new_text, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.calculB)
        meBmi.add_separator()
        meBmi.add_command(label=self.new_text2, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.calculB2)
        meBmi.add_separator()
        meBmi.add_command(label=self.new_text3, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.calculB3)
        meBmi.add_separator()
        meBmi.add_command(label=self.new_text4, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.calculB4)
        meBmi.add_separator()
        meBmi.add_command(label=self.new_text5, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.calculB5)
        meBmi.add_separator()
        meBmi.add_command(label=self.new_text6, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.calculB6)
        meBmi.add_separator()
        meBmi.add_command(label=self.new_text7, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.calculB7)
        meBmi.add_separator()
        # Integration of 3rd menu
        self.cmd_BMI.configure(activeforeground='black', activebackground='cyan', menu=meBmi)

        # Medical Visite
        self.cmd_Vmed=Menubutton(self, text='Medical Visit', fg='cyan', bg='gray30',
            relief=GROOVE)
        self.cmd_Vmed.pack(side=LEFT, padx=3)
        # drop-down portion of vmed
        meVmed = Menu(self.cmd_Vmed)
        meVmed.add_command(label=self.new_text, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.visitMed)
        meVmed.add_separator()
        meVmed.add_command(label=self.new_text2, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.visitMed2)
        meVmed.add_separator()
        meVmed.add_command(label=self.new_text3, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.visitMed3)
        meVmed.add_separator()
        meVmed.add_command(label=self.new_text4, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.visitMed4)
        meVmed.add_separator()
        meVmed.add_command(label=self.new_text5, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.visitMed5)
        meVmed.add_separator()
        meVmed.add_command(label=self.new_text6, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.visitMed6)
        meVmed.add_separator()
        meVmed.add_command(label=self.new_text7, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.visitMed7)
        meVmed.add_separator()
        # Integration of 3rd menu
        self.cmd_Vmed.configure(activeforeground='black', activebackground='cyan', menu=meVmed)

        # Menu for showing all Graphs togather per patient 
        self.cmd_Graph=Menubutton(self, text='Graphics', fg='cyan', bg='gray30', relief=GROOVE)
        self.cmd_Graph.pack(side=LEFT, padx=3)
        # drop-down portion of Graphics menu
        meGraph = Menu(self.cmd_Graph)
        meGraph.add_command(label=self.new_text, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.visualGraph)
        meGraph.add_separator()
        meGraph.add_command(label=self.new_text2, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.visualGraph2)
        meGraph.add_separator()
        meGraph.add_command(label=self.new_text3, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.visualGraph3)
        meGraph.add_separator()
        meGraph.add_command(label=self.new_text4, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.visualGraph4)
        meGraph.add_separator()
        meGraph.add_command(label=self.new_text5, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.visualGraph5)
        meGraph.add_separator()
        meGraph.add_command(label=self.new_text6, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.visualGraph6)
        meGraph.add_separator()
        meGraph.add_command(label=self.new_text7, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.visualGraph7)
        meGraph.add_separator()
        # Integration of Graph menu
        self.cmd_Graph.configure(activeforeground='black', activebackground='cyan',
            menu=meGraph)

        # Nutrition menu for intolerance and hate meals
        self.cmd_Print=Menubutton(self, text='Nutrition', fg='cyan', bg='gray30', relief=GROOVE)
        self.cmd_Print.pack(side=LEFT, padx=3)
        # drop-down portion of nutrition
        mePrint = Menu(self.cmd_Print)
        mePrint.add_command(label=self.new_text, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.nutritionMenu)
        mePrint.add_separator()
        mePrint.add_command(label=self.new_text2, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.nutritionMenu2)
        mePrint.add_separator()
        mePrint.add_command(label=self.new_text3, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.nutritionMenu3)
        mePrint.add_separator()
        mePrint.add_command(label=self.new_text4, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.nutritionMenu4)
        mePrint.add_separator()
        mePrint.add_command(label=self.new_text5, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.nutritionMenu5)
        mePrint.add_separator()
        mePrint.add_command(label=self.new_text6, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.nutritionMenu6)
        mePrint.add_separator()
        mePrint.add_command(label=self.new_text7, background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.nutritionMenu7)
        mePrint.add_separator()
        # Integration of nutrition menu
        self.cmd_Print.configure(activeforeground='black', activebackground='cyan',
            menu=mePrint)

        # Manuals Nurse
        self.cmd_Intext=Menubutton(self, text='Manuals', fg='cyan', bg='gray30', relief=GROOVE)
        self.cmd_Intext.pack(side=LEFT, padx=3)
        # drop-down portion of Manuals Nurse
        meIntext = Menu(self.cmd_Intext)
        meIntext.add_command(label='Click on it', background='black', activebackground='cyan',
                        foreground='cyan', activeforeground='black',
                        command=boss.manualFile)
        # Integration of Manuals Nurse
        self.cmd_Intext.configure(activeforeground='black', activebackground='cyan',
            menu=meIntext)

# Application principale (Main app)
class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='gray22', padx=20, pady=20, relief=GROOVE)
        self.master.title('ANGEL-VISION - Developed by CK - Dec. 2020')
        mBar = MenuBar(self)
        mBar.pack(side=TOP, fill=X, expand=YES)
        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can = Canvas(self, width=1250, height=800, bg='gray18')
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW,
                                  tags="self.frame")
        # Insertion d'une image
        self.photo = PhotoImage(file='./syno_gif/title_syno.gif')
        self.item = self.can.create_image(625, 400, image=self.photo)
        # Insertion du texte
        self.can.create_text(625, 500, anchor=CENTER, 
            text="Python 3.6 - Tkinter 8.6 - GIMP 2.8",
            font=('Times New Roman', 18), fill='aquamarine')
        self.can.create_text(170, 770, anchor=NE, text="Copyright (C) 2020 Inc.",
            font=('Times', 12), fill='white')
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # Création de 2 boutons sur la page d'accueil (main page or intro)
        # Synopsis button
        button2 = Button(self, text="SYNOPSIS", font=70, bg='gray15',
            fg='turquoise',
            anchor = CENTER, command = self.showsynopsis)
        button2.configure(width=15, activebackground='SteelBlue',
            activeforeground='white', relief=GROOVE)
        button2_window = self.can.create_window(450, 580, anchor=CENTER,
            window=button2)
        # Statistiques button
        button3 = Button(self, text="PSYCHOTABS", font=74, bg='gray15',
            fg='turquoise', anchor = CENTER, command = self.launchPsycho)
        button3.configure(width=15, activebackground='SteelBlue',
            activeforeground='white', relief=GROOVE)
        button3_window = self.can.create_window(790, 580, anchor=CENTER,
            window=button3)
        self.pack()

    # Méthode pour reconfigurer la scrollbar à chaque fois
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def effacer(self):
        '''Reinitialize canvas when we pass to another'''
        self.can.delete(ALL)

    def msgExit(self):
        MsgBox = messagebox.askyesno('Quit system', 'Do you want to quit ?')
        if MsgBox == 1:
            self.master.destroy()
        else:
            NoforQ = messagebox.showinfo('Return', 'You will now return to the'
                'application screen')

    # Admin
    def adminDir(self):
        subprocess.call('./admin/fic_admin1.py')

    def adminDir2(self):
        subprocess.call('./admin/fic_admin2.py')

    def adminDir3(self):
        subprocess.call('./admin/fic_admin3.py')

    def adminDir4(self):
        subprocess.call('./admin/fic_admin4.py')

    def adminDir5(self):
        subprocess.call('./admin/fic_admin5.py')

    def adminDir6(self):
        subprocess.call('./admin/fic_admin6.py')

    def adminDir7(self):
        subprocess.call('./admin/fic_admin7.py')

    # CheckBox 14 besoins
    def besoinsCoche(self):
        subprocess.call('./14besoins/checkb.py')

    def besoins2Coche(self):
        subprocess.call('./14besoins/checkb2.py')

    def besoins3Coche(self):
        subprocess.call('./14besoins/checkb3.py')

    def besoins4Coche(self):
        subprocess.call('./14besoins/checkb4.py')

    def besoins5Coche(self):
        subprocess.call('./14besoins/checkb5.py')

    def besoins6Coche(self):
        subprocess.call('./14besoins/checkb6.py')

    def besoins7Coche(self):
        subprocess.call('./14besoins/checkb7.py')


    def launchPsycho(self):
        subprocess.call('./psychotabs.py')
    # Agenda
    def patientAgenda(self):
        subprocess.call('./patient_agenda/origin_agenda.py')

    def patientAgenda2(self):
        subprocess.call('./patient_agenda/origin2_agenda2.py')

    def patientAgenda3(self):
        subprocess.call('./patient_agenda/origin3_agenda3.py')

    def patientAgenda4(self):
        subprocess.call('./patient_agenda/origin4_agenda4.py')

    def patientAgenda5(self):
        subprocess.call('./patient_agenda/origin5_agenda5.py')

    def patientAgenda6(self):
        subprocess.call('./patient_agenda/origin6_agenda6.py')

    def patientAgenda7(self):
        subprocess.call('./patient_agenda/origin7_agenda7.py')

    # Func suivi
    def suiviSoins1(self):
        subprocess.call("./14besoins/suivi_patient_1.py")

    def suiviSoins2(self):
        subprocess.call("./14besoins/suivi_patient_2.py")

    def suiviSoins3(self):
        subprocess.call("./14besoins/suivi_patient_3.py")

    def suiviSoins4(self):
        subprocess.call("./14besoins/suivi_patient_4.py")

    def suiviSoins5(self):
        subprocess.call("./14besoins/suivi_patient_5.py")

    def suiviSoins6(self):
        subprocess.call("./14besoins/suivi_patient_6.py")

    def suiviSoins7(self):
        subprocess.call("./14besoins/suivi_patient_7.py")

    # treatments
    def tttMed1(self):
        subprocess.call("./ttt/patienttt1.py")

    def tttMed2(self):
        subprocess.call("./ttt/patienttt2.py")

    def tttMed3(self):
        subprocess.call("./ttt/patienttt3.py")

    def tttMed4(self):
        subprocess.call("./ttt/patienttt4.py")

    def tttMed5(self):
        subprocess.call("./ttt/patienttt5.py")

    def tttMed6(self):
        subprocess.call("./ttt/patienttt6.py")

    def tttMed7(self):
        subprocess.call("./ttt/patienttt7.py")

    # Func Vital Parameters
    def showParam1(self):
        subprocess.call("./param/fencap.py")

    def showParam2(self):
        subprocess.call("./param/fencap2.py")

    def showParam3(self):
        subprocess.call("./param/fencap3.py")

    def showParam4(self):
        subprocess.call("./param/fencap4.py")

    def showParam5(self):
        subprocess.call("./param/fencap5.py")

    def showParam6(self):
        subprocess.call("./param/fencap6.py")

    def showParam7(self):
        subprocess.call("./param/fencap7.py")

    # Func BMI
    def calculB(self):
        subprocess.call("./calBmi/CalculBmi.py")

    def calculB2(self):
        subprocess.call("./calBmi/CalculBmi2.py")

    def calculB3(self):
        subprocess.call("./calBmi/CalculBmi3.py")

    def calculB4(self):
        subprocess.call("./calBmi/CalculBmi4.py")

    def calculB5(self):
        subprocess.call("./calBmi/CalculBmi5.py")

    def calculB6(self):
        subprocess.call("./calBmi/CalculBmi6.py")

    def calculB7(self):
        subprocess.call("./calBmi/CalculBmi7.py")

    # Func Visit MED
    def visitMed(self):
        subprocess.call("./vmed/vm_patient1.py")
        
    def visitMed2(self):
        subprocess.call("./vmed/vm_patient2.py")
        
    def visitMed3(self):
        subprocess.call("./vmed/vm_patient3.py")
        
    def visitMed4(self):
        subprocess.call("./vmed/vm_patient4.py")
        
    def visitMed5(self):
        subprocess.call("./vmed/vm_patient5.py")
        
    def visitMed6(self):
        subprocess.call("./vmed/vm_patient6.py")
        
    def visitMed7(self):
        subprocess.call("./vmed/vm_patient7.py")    

    # Graphical menu
    def visualGraph(self):
        subprocess.call('./param/aspifile/aspidata.py')
        subprocess.call('./param/aspifile/aspipuls.py')
        subprocess.call('./param/aspifile/aspisat.py')
        subprocess.call('./param/aspifile/aspifreq.py')
        subprocess.call('./param/aspifile/aspitemp.py')
        subprocess.call('./param/aspifile/aspigly.py')
        subprocess.call('./param/aspifile/aspidlr.py')
        subprocess.call('./calBmi/doc_BMI/convert_kg.py')
        subprocess.call('./calBmi/doc_BMI/convert_bmilist.py')

    def visualGraph2(self):
        subprocess.call('./param/aspifile2/aspidata.py')
        subprocess.call('./param/aspifile2/aspipuls.py')
        subprocess.call('./param/aspifile2/aspisat.py')
        subprocess.call('./param/aspifile2/aspifreq.py')
        subprocess.call('./param/aspifile2/aspitemp.py')
        subprocess.call('./param/aspifile2/aspigly.py')
        subprocess.call('./param/aspifile2/aspidlr.py')
        subprocess.call('./calBmi/doc_BMI2/convert_kg.py')
        subprocess.call('./calBmi/doc_BMI2/convert_bmilist.py')

    def visualGraph3(self):
        subprocess.call('./param/aspifile3/aspidata.py')
        subprocess.call('./param/aspifile3/aspipuls.py')
        subprocess.call('./param/aspifile3/aspisat.py')
        subprocess.call('./param/aspifile3/aspifreq.py')
        subprocess.call('./param/aspifile3/aspitemp.py')
        subprocess.call('./param/aspifile3/aspigly.py')
        subprocess.call('./param/aspifile3/aspidlr.py')
        subprocess.call('./calBmi/doc_BMI3/convert_kg.py')
        subprocess.call('./calBmi/doc_BMI3/convert_bmilist.py')

    def visualGraph4(self):
        subprocess.call('./param/aspifile4/aspidata.py')
        subprocess.call('./param/aspifile4/aspipuls.py')
        subprocess.call('./param/aspifile4/aspisat.py')
        subprocess.call('./param/aspifile4/aspifreq.py')
        subprocess.call('./param/aspifile4/aspitemp.py')
        subprocess.call('./param/aspifile4/aspigly.py')
        subprocess.call('./param/aspifile4/aspidlr.py')
        subprocess.call('./calBmi/doc_BMI4/convert_kg.py')
        subprocess.call('./calBmi/doc_BMI4/convert_bmilist.py')

    def visualGraph5(self):
        subprocess.call('./param/aspifile5/aspidata.py')
        subprocess.call('./param/aspifile5/aspipuls.py')
        subprocess.call('./param/aspifile5/aspisat.py')
        subprocess.call('./param/aspifile5/aspifreq.py')
        subprocess.call('./param/aspifile5/aspitemp.py')
        subprocess.call('./param/aspifile5/aspigly.py')
        subprocess.call('./param/aspifile5/aspidlr.py')
        subprocess.call('./calBmi/doc_BMI5/convert_kg.py')
        subprocess.call('./calBmi/doc_BMI5/convert_bmilist.py')

    def visualGraph6(self):
        subprocess.call('./param/aspifile6/aspidata.py')
        subprocess.call('./param/aspifile6/aspipuls.py')
        subprocess.call('./param/aspifile6/aspisat.py')
        subprocess.call('./param/aspifile6/aspifreq.py')
        subprocess.call('./param/aspifile6/aspitemp.py')
        subprocess.call('./param/aspifile6/aspigly.py')
        subprocess.call('./param/aspifile6/aspidlr.py')
        subprocess.call('./calBmi/doc_BMI6/convert_kg.py')
        subprocess.call('./calBmi/doc_BMI6/convert_bmilist.py')

    def visualGraph7(self):
        subprocess.call('./param/aspifile7/aspidata.py')
        subprocess.call('./param/aspifile7/aspipuls.py')
        subprocess.call('./param/aspifile7/aspisat.py')
        subprocess.call('./param/aspifile7/aspifreq.py')
        subprocess.call('./param/aspifile7/aspitemp.py')
        subprocess.call('./param/aspifile7/aspigly.py')
        subprocess.call('./param/aspifile7/aspidlr.py')
        subprocess.call('./calBmi/doc_BMI7/convert_kg.py')
        subprocess.call('./calBmi/doc_BMI7/convert_bmilist.py')

    # Allergy
    def allergyLink(self):
        subprocess.call('./allergy/allerpatient1.py')

    def allergyLink2(self):
        subprocess.call('./allergy/allerpatient2.py')

    def allergyLink3(self):
        subprocess.call('./allergy/allerpatient3.py')

    def allergyLink4(self):
        subprocess.call('./allergy/allerpatient4.py')

    def allergyLink5(self):
        subprocess.call('./allergy/allerpatient5.py')

    def allergyLink6(self):
        subprocess.call('./allergy/allerpatient6.py')

    def allergyLink7(self):
        subprocess.call('./allergy/allerpatient7.py')

    # Func labo
    def laboResult(self):
        subprocess.call('./labo/resultlabo1.py')

    def laboResult2(self):
        subprocess.call('./labo/resultlabo2.py')

    def laboResult3(self):
        subprocess.call('./labo/resultlabo3.py')

    def laboResult4(self):
        subprocess.call('./labo/resultlabo4.py')

    def laboResult5(self):
        subprocess.call('./labo/resultlabo5.py')

    def laboResult6(self):
        subprocess.call('./labo/resultlabo6.py')

    def laboResult7(self):
        subprocess.call('./labo/resultlabo7.py')

    # Func Diagnostic
    def diag1(self):
        subprocess.call("./diag/diag_patient_1.py")

    def diag2(self):
        subprocess.call("./diag/diag_patient_2.py")

    def diag3(self):
        subprocess.call("./diag/diag_patient_3.py")

    def diag4(self):
        subprocess.call("./diag/diag_patient_4.py")

    def diag5(self):
        subprocess.call("./diag/diag_patient_5.py")

    def diag6(self):
        subprocess.call("./diag/diag_patient_6.py")

    def diag7(self):
        subprocess.call("./diag/diag_patient_7.py")

    # Func Medical Visit
    def showvm1(self):
        subprocess.call("./vmMacro/vm_ae.py")

    def showvm2(self):
        subprocess.call("./vmMacro/vm_ae.py")

    def showvm3(self):
        subprocess.call("./vmMacro/vm_ae.py")

    def showvm4(self):
        subprocess.call("./vmMacro/vm_ae.py")

    def showvm5(self):
        subprocess.call("./vmMacro/vm_ae.py")

    def showvm6(self):
        subprocess.call("./vmMacro/vm_ae.py")

    def showvm7(self):
        subprocess.call("./vmMacro/vm_ae.py")

    # Manual nurse
    def manualFile(self):
        subprocess.call('./manual/pdfopenmanual.py')

    # Func histoire de vie
    def histv1(self):
        subprocess.call("./histv/patient1_histv.py")

    def histv2(self):
        subprocess.call("./histv/patient1_histv2.py")

    def histv3(self):
        subprocess.call("./histv/patient1_histv3.py")

    def histv4(self):
        subprocess.call("./histv/patient1_histv4.py")

    def histv5(self):
        subprocess.call("./histv/patient1_histv5.py")

    def histv6(self):
        subprocess.call("./histv/patient1_histv6.py")

    def histv7(self):
        subprocess.call("./histv/patient1_histv6.py")

    #Moyens aux
    def moyaux(self):
        subprocess.call("./auxsrc/auxsrc_patient1.py")

    def moyaux2(self):
        subprocess.call("./auxsrc/auxsrc_patient2.py")

    def moyaux3(self):
        subprocess.call("./auxsrc/auxsrc_patient3.py")

    def moyaux4(self):
        subprocess.call("./auxsrc/auxsrc_patient4.py")

    def moyaux5(self):
        subprocess.call("./auxsrc/auxsrc_patient5.py")

    def moyaux6(self):
        subprocess.call("./auxsrc/auxsrc_patient6.py")

    def moyaux7(self):
        subprocess.call("./auxsrc/auxsrc_patient7.py")

    # External stakeholders
    def extStake(self):
        subprocess.call('./stackeholders/exstacke_patient1.py')

    def extStake2(self):
        subprocess.call('./stackeholders/exstacke_patient2.py')

    def extStake3(self):
        subprocess.call('./stackeholders/exstacke_patient3.py')

    def extStake4(self):
        subprocess.call('./stackeholders/exstacke_patient4.py')

    def extStake5(self):
        subprocess.call('./stackeholders/exstacke_patient5.py')

    def extStake6(self):
        subprocess.call('./stackeholders/exstacke_patient6.py')

    def extStake7(self):
        subprocess.call('./stackeholders/exstacke_patient7.py')

    # Menu print
    def nutritionMenu(self):
        subprocess.call('./nutrition/nutrit_patient1.py')

    def nutritionMenu2(self):
        subprocess.call('./nutrition/nutrit_patient2.py')

    def nutritionMenu3(self):
        subprocess.call('./nutrition/nutrit_patient3.py')

    def nutritionMenu4(self):
        subprocess.call('./nutrition/nutrit_patient4.py')

    def nutritionMenu5(self):
        subprocess.call('./nutrition/nutrit_patient5.py')

    def nutritionMenu6(self):
        subprocess.call('./nutrition/nutrit_patient6.py')

    def nutritionMenu7(self):
        subprocess.call('./nutrition/nutrit_patient7.py')

    # For new entry
    def callPatient1(self):
        subprocess.call('./newpatient/entrypytientfile.py')

    # Second page intro (a copy from the main app juste above)
    def page(self):
        self.can.delete(ALL)
        # Insertion d'une image
        self.photo=PhotoImage(file='./syno_gif/title_syno.gif')
        self.item=self.can.create_image(625, 400, image=self.photo)
        # Insertion du texte
        self.can.create_text(625, 500, anchor=CENTER, 
            text="Python 3.6 - Tkinter 8.6 - GIMP 2.8",
                    font=('Times New Roman', 18), fill='aquamarine')
        self.can.create_text(170, 770, anchor=NE, text="Copyright (C) 2020 Inc.",
                    font=('Times', 12), fill='white')
        self.can.pack(side=RIGHT, fill=BOTH, expand=YES)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # Création des 3 boutons
        button2 = Button(self, text="SYNOPSIS", font=70, bg='gray15', 
            fg='turquoise',
            anchor = CENTER, command = self.showsynopsis)
        button2.configure(width=15, activebackground='SteelBlue',
            activeforeground='white', relief=GROOVE)
        button2_window = self.can.create_window(450, 580, anchor=CENTER,
            window=button2) 

        button3 = Button(self, text="PSYCHOTABS", font=74, bg='gray15',
            fg='turquoise',
            anchor = CENTER, command = self.launchPsycho)
        button3.configure(width=15, activebackground='SteelBlue', 
            activeforeground='white', relief=GROOVE)
        button3_window = self.can.create_window(790, 580, anchor=CENTER, 
            window=button3)

        self.can.configure(scrollregion=self.can.bbox(ALL)) 

    # Installation of python and tkinter page
    def instalpy(self):
        self.can.delete(ALL)
        self.photo=PhotoImage(file='./syno_gif/pyt.gif')
        self.item=self.can.create_image(700, 400, image=self.photo)
        self.can.create_text(500, 20, anchor=NW, 
            text="-INSTALLATION DU PROGRAMME-\n\n"
            "Linux (Xubuntu):\n\n"

            "Ouvrir le terminal.\n"
            "Vérifier version python (si version 2.7 ou 3 et plus)\n"
            "en tapant dans le terminal: python -V ou python3 -V ou python --version.\n"
            "Sinon, télécharger python 3.5 en ligne de commande:\n"
            "sudo apt-get update && apt-get upgrade.\n"
            "sudo apt-get install python3-tk (avec tkinter pour la GUI).\n"
            "Aller sous le dossier où il a été téléchargé et taper (ex: cd /Documents/psychotabs.py)\n"
            "et tapez ./psychotabs.py pour ouvrir l'application.\n"
            "Je vous conseille de regarder sur le net en fonction de la version linux.\n\n"

            "**************************************************************\n\n"

            "Mac OS:\n\n"

            "Ouvrir le terminal.\n"
            "Vérifier version python (si version 2.7 ou 3 et plus)\n"
            "en tapant dans le terminal: python --version.\n"
            "Rendez-vous sur python.org pour télécharger la version correspondante à votre Mac.\n"
            "A partir du Terminal, allez sous le dossier où il a été téléchargé et taper (ex: cd\n" 
            "/Documents/dossier) et taper (python3 psychotabs.py dans le terminal) pour ouvrir l'application.\n\n"

            "**************************************************************\n\n"

            "Windows:\n\n"

            "Rendez-vous sur la page python.org télécharger un version de python\n"
            "supérieur à 3.5 (dernière version stable).\n"
            "Ensuite quelques manipulation sont indispensable pour la création d'un\n"
            "'stand-alone' avec pyinstaller2. Rendez-vous sur ce site :\n"
            "https://wwww.XXXXXXXXXXXXXXXXXXXX.com\n"
            "et sur ce lui-ci :\n"
            "https://www.ZZZZZZZZZZZZ.com\n"
            "Pour toutes questions, vous pouvez me joindre à l'adresse mail :\n"
            "philogenie@protonmail.com",
            font=('Times', 13), fill='aquamarine')
        self.can.configure(scrollregion=self.can.bbox(ALL))

    # Synopsis page
    def showsynopsis(self):
        self.can.delete()
        self.can.create_text(625, 80, anchor=CENTER, text="Synopsis",
            font=('Times New Roman', 40), fill='aquamarine')

        # To introduce a new pytient
        self.x1, self.y1 = 120, 50
        self.b=Button(self.can, width=10, font=16, bg='gray17', fg='cyan',
            activebackground='cyan',
            activeforeground='black',
            text="New Entry",
            command=self.callPatient1)
        self.fb=self.can.create_window(self.x1, self.y1, window=self.b)
        
        # To refresh page with new entry patient
        self.x101, self.y101 = 270, 50
        self.b2=Button(self.can, width=10, font=16, bg='gray17', fg='gold',
            activebackground='cyan',
            activeforeground='black',
            text="Refresh",
            command=self.showsynopsis)
        self.fb2=self.can.create_window(self.x101, self.y101, window=self.b2)
        
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1=(namefile.readline())
            
        self.new_text=line1

        self.x2, self.y2 = 129, 200
        self.Data_write=Entry(self.can)
        self.new_text=StringVar()
        self.Data_write=Entry(textvariable=self.new_text,
            highlightbackground='gray', bd=4)
        self.new_text.set(line1)
        self.Data_write=self.can.create_window(self.x2, self.y2,
            window=self.Data_write)

        self.x3, self.y3 = 271, 200
        self.b=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Allergy",
            command=self.allergyLink)
        self.fb=self.can.create_window(self.x3, self.y3, window=self.b)

        self.x3, self.y3 = 429, 200
        self.b=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Diagnostic + ATCD",
            command=self.diag1)
        self.fb=self.can.create_window(self.x3, self.y3, window=self.b)

        self.x4, self.y4 = 597, 200
        self.b4=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Laboratory",
            command=self.laboResult)
        self.fb4=self.can.create_window(self.x4, self.y4, window=self.b4)
        #769
        self.x5, self.y5 = 725, 200
        self.b5=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Exams",
            command=self.suiviSoins1)
        self.fb5=self.can.create_window(self.x5, self.y5, window=self.b5)
        #896
        self.x6, self.y6 = 853, 200
        self.b6=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Life story",
            command=self.histv1)
        self.fb6=self.can.create_window(self.x6, self.y6, window=self.b6)

        self.x7, self.y7 = 981, 200
        self.b7=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Aux. resrc.",
            command=self.moyaux)
        self.fb7=self.can.create_window(self.x7, self.y7, window=self.b7)

        self.x8, self.y8 = 1109, 200
        self.b8=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Ext. stacke.",
            command=self.extStake)
        self.fb8=self.can.create_window(self.x8, self.y8, window=self.b8)

        # Patient 2
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1=(namefile.readline())
            line2=(namefile.readline())
            line3=(namefile.readline())
            line4=(namefile.readline())

        self.new_text=line4

        self.x9, self.y9 = 129, 232
        self.Data_write=Entry(self.can)
        self.new_text=StringVar()
        self.Data_write=Entry(textvariable=self.new_text,
          highlightbackground='gray', bd=4)
        self.new_text.set(line4)
        self.Data_write=self.can.create_window(self.x9, self.y9,
          window=self.Data_write)

        self.x10, self.y10 = 271, 232
        self.b10=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Allergy",
            command=self.diag2)
        self.fb10=self.can.create_window(self.x10, self.y10, window=self.b10)

        self.x13, self.y13 = 429, 232
        self.b13=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Diagnostic + ATCD",
            command=self.showParam2)
        self.fb13=self.can.create_window(self.x13, self.y13, window=self.b13)

        self.x14, self.y14 = 597, 232
        self.b14=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Laboratory",
            command=self.suiviSoins2)
        self.fb14=self.can.create_window(self.x14, self.y14, window=self.b14)

        self.x15, self.y15 = 725, 232
        self.b15=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Exams",
            command=self.showvm1)
        self.fb15=self.can.create_window(self.x15, self.y15, window=self.b15)

        self.x16, self.y16 = 853, 232
        self.b16=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Life story",
            command=self.histv2)
        self.fb16=self.can.create_window(self.x16, self.y16, window=self.b16)

        self.x17, self.y17 = 981, 232
        self.b17=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Aux. resrc.",
            command=self.diag2)
        self.fb17=self.can.create_window(self.x17, self.y17, window=self.b17)

        self.x171, self.y171 = 1109, 232
        self.b171=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Ext. stacke.",
            command=self.moyaux)
        self.fb171=self.can.create_window(self.x171, self.y171, window=self.b171)

        # Patient 2
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1=(namefile.readline())
            line2=(namefile.readline())
            line3=(namefile.readline())
            line4=(namefile.readline())
            line5=(namefile.readline())
            line6=(namefile.readline())
            line7=(namefile.readline())
        self.new_text=line7
        self.x18, self.y18 = 129, 264
        self.Data_write=Entry(self.can)
        self.new_text=StringVar()
        self.Data_write=Entry(textvariable=self.new_text,
          highlightbackground='gray', bd=4)
        self.new_text.set(line7)
        self.Data_write=self.can.create_window(self.x18, self.y18,
          window=self.Data_write)

        self.x19, self.y19 = 271, 264
        self.b19=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Allergy",
            command=self.diag3)
        self.fb19=self.can.create_window(self.x19, self.y19, window=self.b19)

        self.x22, self.y22 = 429, 264
        self.b22=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Diagnostic + ATCD",
            command=self.showParam3)
        self.fb22=self.can.create_window(self.x22, self.y22, window=self.b22)

        self.x23, self.y23 = 597, 264
        self.b23=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Laboratory",
            command=self.suiviSoins3)
        self.fb23=self.can.create_window(self.x23, self.y23, window=self.b23)

        self.x24, self.y24 = 725, 264
        self.b24=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Exams",
            command=self.showvm3)
        self.fb24=self.can.create_window(self.x24, self.y24, window=self.b24)

        self.x25, self.y25 = 853, 264
        self.b25=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Life story",
            command=self.histv3)
        self.fb25=self.can.create_window(self.x25, self.y25, window=self.b25)

        self.x26, self.y26 = 981, 264
        self.b26=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Aux. resrc.",
            command=self.diag3)
        self.fb26=self.can.create_window(self.x26, self.y26, window=self.b26)

        self.x8, self.y8 = 1109, 264
        self.b8=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Ext. stacke.",
            command=self.moyaux)
        self.fb8=self.can.create_window(self.x8, self.y8, window=self.b8)

        # 4ème personne Synopsis - Page
                # Patient 2
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1=(namefile.readline())
            line2=(namefile.readline())
            line3=(namefile.readline())
            line4=(namefile.readline())
            line5=(namefile.readline())
            line6=(namefile.readline())
            line7=(namefile.readline())
            line8=(namefile.readline())
            line9=(namefile.readline())
            line10=(namefile.readline())
        self.new_text=line10
        self.x27, self.y27 = 129, 296
        self.Data_write=Entry(self.can)
        self.new_text=StringVar()
        self.Data_write=Entry(textvariable=self.new_text,
          highlightbackground='gray', bd=4)
        self.new_text.set(line10)
        self.Data_write=self.can.create_window(self.x27, self.y27,
          window=self.Data_write)

        self.x28, self.y28 = 271, 296
        self.b28=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Allergy",
            command=self.diag4)
        self.fb28=self.can.create_window(self.x28, self.y28, window=self.b28)

        self.x31, self.y31 = 429, 296
        self.b31=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Diagnostic + ATCD",
            command=self.showParam4)
        self.fb31=self.can.create_window(self.x31, self.y31, window=self.b31)

        self.x32, self.y32 = 597, 296
        self.b32=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Laboratory",
            command=self.suiviSoins4)
        self.fb32=self.can.create_window(self.x32, self.y32, window=self.b32)

        self.x33, self.y33 = 725, 296
        self.b33=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Exams",
            command=self.showvm4)
        self.fb33=self.can.create_window(self.x33, self.y33, window=self.b33)

        self.x34, self.y34 = 853, 296
        self.b34=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Life story",
            command=self.histv4)
        self.fb34=self.can.create_window(self.x34, self.y34, window=self.b34)

        self.x35, self.y35 = 981, 296
        self.b35=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Aux. resrc.",
            command=self.diag4)
        self.fb35=self.can.create_window(self.x35, self.y35, window=self.b35)

        self.x351, self.y351 = 1109, 296
        self.b351=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Ext. stacke.",
            command=self.moyaux)
        self.fb351=self.can.create_window(self.x351, self.y351, window=self.b351)

        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1=(namefile.readline())
            line2=(namefile.readline())
            line3=(namefile.readline())
            line4=(namefile.readline())
            line5=(namefile.readline())
            line6=(namefile.readline())
            line7=(namefile.readline())
            line8=(namefile.readline())
            line9=(namefile.readline())
            line10=(namefile.readline())
            line11=(namefile.readline())
            line12=(namefile.readline())
            line13=(namefile.readline())
        self.new_text=line13
        self.x36, self.y36 = 129, 328
        self.Data_write=Entry(self.can)
        self.new_text=StringVar()
        self.Data_write=Entry(textvariable=self.new_text,
          highlightbackground='gray', bd=4)
        self.new_text.set(line13)
        self.Data_write=self.can.create_window(self.x36, self.y36,
          window=self.Data_write)

        self.x37, self.y37 = 271, 328
        self.b37=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Allergy",
            command=self.diag5)
        self.fb37=self.can.create_window(self.x37, self.y37, window=self.b37)

        self.x40, self.y40 = 429, 328
        self.b40=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Diagnostic + ATCD",
            command=self.showParam5)
        self.fb40=self.can.create_window(self.x40, self.y40, window=self.b40)

        self.x41, self.y41 = 597, 328
        self.b41=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Laboratory",
            command=self.suiviSoins5)
        self.fb41=self.can.create_window(self.x41, self.y41, window=self.b41)

        self.x42, self.y42 = 725, 328
        self.b42=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Exams",
            command=self.showvm5)
        self.fb42=self.can.create_window(self.x42, self.y42, window=self.b42)

        self.x43, self.y43 = 853, 328
        self.b43=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Life story",
            command=self.histv5)
        self.fb43=self.can.create_window(self.x43, self.y43, window=self.b43)

        self.x44, self.y44 = 981, 328
        self.b44=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Aux. resrc.",
            command=self.diag5)
        self.fb44=self.can.create_window(self.x44, self.y44, window=self.b44)

        self.x441, self.y441 = 1109, 328
        self.b441=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Ext. stacke.",
            command=self.moyaux)
        self.fb441=self.can.create_window(self.x441, self.y441, window=self.b441)

        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1=(namefile.readline())
            line2=(namefile.readline())
            line3=(namefile.readline())
            line4=(namefile.readline())
            line5=(namefile.readline())
            line6=(namefile.readline())
            line7=(namefile.readline())
            line8=(namefile.readline())
            line9=(namefile.readline())
            line10=(namefile.readline())
            line11=(namefile.readline())
            line12=(namefile.readline())
            line13=(namefile.readline())
            line14=(namefile.readline())
            line15=(namefile.readline())
            line16=(namefile.readline())
        self.new_text=line16
        self.x45, self.y45 = 129, 360
        self.Data_write=Entry(self.can)
        self.new_text=StringVar()
        self.Data_write=Entry(textvariable=self.new_text,
          highlightbackground='gray', bd=4)
        self.new_text.set(line16)
        self.Data_write=self.can.create_window(self.x45, self.y45,
          window=self.Data_write)

        self.x46, self.y46 = 271, 360
        self.b46=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Allergy",
            command=self.diag6)
        self.fb46=self.can.create_window(self.x46, self.y46, window=self.b46)

        self.x49, self.y49 = 429, 360
        self.b49=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Diagnostic + ATCD",
            command=self.showParam6)
        self.fb49=self.can.create_window(self.x49, self.y49, window=self.b49)

        self.x50, self.y50 = 597, 360
        self.b50=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Laboratory",
            command=self.suiviSoins6)
        self.fb50=self.can.create_window(self.x50, self.y50, window=self.b50)

        self.x51, self.y51 = 725, 360
        self.b51=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Exams",
            command=self.showvm6)
        self.fb51=self.can.create_window(self.x51, self.y51, window=self.b51)

        self.x52, self.y52 = 853, 360
        self.b52=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Life story",
            command=self.histv6)
        self.fb52=self.can.create_window(self.x52, self.y52, window=self.b52)

        self.x53, self.y53 = 981, 360
        self.b53=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Aux. resrc.",
            command=self.diag6)
        self.fb53=self.can.create_window(self.x53, self.y53, window=self.b53)

        self.x531, self.y531 = 1109, 360
        self.b531=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Ext. stacke.",
            command=self.moyaux)
        self.fb531=self.can.create_window(self.x531, self.y531, window=self.b531)

        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1=(namefile.readline())
            line2=(namefile.readline())
            line3=(namefile.readline())
            line4=(namefile.readline())
            line5=(namefile.readline())
            line6=(namefile.readline())
            line7=(namefile.readline())
            line8=(namefile.readline())
            line9=(namefile.readline())
            line10=(namefile.readline())
            line11=(namefile.readline())
            line12=(namefile.readline())
            line13=(namefile.readline())
            line14=(namefile.readline())
            line15=(namefile.readline())
            line16=(namefile.readline())
            line17=(namefile.readline())
            line18=(namefile.readline())
            line19=(namefile.readline())
        self.new_text=line19
        self.x54, self.y54 = 129, 392
        self.Data_write=Entry(self.can)
        self.new_text=StringVar()
        self.Data_write=Entry(textvariable=self.new_text,
          highlightbackground='gray', bd=4)
        self.new_text.set(line19)
        self.Data_write=self.can.create_window(self.x54, self.y54,
          window=self.Data_write)

        self.x54, self.y54 = 271, 392
        self.b54=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Allergy",
            command=self.diag7)
        self.fb54=self.can.create_window(self.x54, self.y54, window=self.b54)

        self.x57, self.y57 = 429, 392
        self.b57=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Diagnostic + ATCD",
            command=self.showParam7)
        self.fb57=self.can.create_window(self.x57, self.y57, window=self.b57)

        self.x58, self.y58 = 597, 392
        self.b58=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Laboratory",
            command=self.suiviSoins7)
        self.fb58=self.can.create_window(self.x58, self.y58, window=self.b58)

        self.x59, self.y59 = 725, 392
        self.b59=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Exams",
            command=self.showvm7)
        self.fb59=self.can.create_window(self.x59, self.y59, window=self.b59)

        self.x60, self.y60 = 853, 392
        self.b60=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Life story",
            command=self.histv7)
        self.fb60=self.can.create_window(self.x60, self.y60, window=self.b60)

        self.x61, self.y61 = 981, 392
        self.b61=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Aux. resrc.",
            command=self.diag7)
        self.fb61=self.can.create_window(self.x61, self.y61, window=self.b61)

        self.x62, self.y62 = 1109, 392
        self.b62=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise',
            activeforeground='black',
            text="Ext. stacke.",
            command=self.moyaux)
        self.fb62=self.can.create_window(self.x62, self.y62, window=self.b62)

        self.can.configure(scrollregion=self.can.bbox(ALL))

if __name__=='__main__':
    app = Application()
    app.mainloop()
