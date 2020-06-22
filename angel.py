#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import time
import datetime
import os
import itertools
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
        Frame.__init__(self, borderwidth=5, bg='dim grey', padx=0)
        # 1st menu
        fileMenu = Menubutton(self, text='Menu', fg='white',
            font=("Times 14"), bg='grey30', relief=GROOVE)
        new_text=StringVar()
        new_text2=StringVar()
        new_text3=StringVar()
        new_text4=StringVar()
        new_text5=StringVar()
        new_text6=StringVar()
        new_text7=StringVar()

        fileMenu.pack(side=LEFT, padx=3)
        # Partie déroulante du menu 1st
        me1 = Menu(fileMenu, tearoff=0)
        me1.add_command(label='Accueil', underline=0, font=("Times 14 bold"),
            background='black',activebackground='aquamarine',
            foreground='aquamarine', activeforeground='black',
            command=boss.secondPage)
        me1.add_command(label="Synopsis", underline=0, font=("Times 14 bold"),
            background='black', activebackground='cyan',
            foreground='aquamarine', activeforeground='black',
            command=boss.showsynopsis)
        me1.add_command(label="Psychotabs", underline=0, font=("Times 14 bold"),
            background='black',  activebackground='cyan',
            foreground='aquamarine', activeforeground='black',
            command=boss.launchPsycho)
        me1.add_command(label='MapApp', font=("Times 14 bold"),
            background='black', activebackground='aquamarine',
            foreground='yellow', activeforeground='black',
            command=boss.instalpy)
        me1.add_command(label='Quit', font=("Times 14 bold"),
            background='black', activebackground='red',
            foreground='red', activeforeground='white',
            command=boss.msgExit)
        # Integration of 1st menu
        fileMenu.configure(activeforeground='black', activebackground='cyan',
            menu=me1)
        
        # For label below (in me2.add_command)
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1=namefile.readline()
                new_text=line1
        except FileNotFoundError as fileout:
            print("No file entryfile.txt exist", fileout)

        try:
            with open('./newpatient/entryfile2.txt', 'r') as namefile:
                line2=namefile.readline()
                new_text2=line2
        except FileNotFoundError as fileout2:
            print("No file entryfile2.txt exist", fileout2)

        try:
            with open('./newpatient/entryfile3.txt', 'r') as namefile:
                line3=namefile.readline()
                new_text3=line3
        except FileNotFoundError as fileout3:
            print("No file entryfile3.txt exist", fileout3)

        try:
            with open('./newpatient/entryfile4.txt', 'r') as namefile:
                line4=namefile.readline()
                new_text4=line4
        except FileNotFoundError as fileout4:
            print("No file entryfile4.txt exist", fileout4)

        try:
            with open('./newpatient/entryfile5.txt', 'r') as namefile:
                line5=namefile.readline()
                new_text5=line5
        except FileNotFoundError as fileout5:
            print("No file entryfile5.txt exist", fileout5)

        try:
            with open('./newpatient/entryfile6.txt', 'r') as namefile:
                line6=namefile.readline()
                new_text6=line6
        except FileNotFoundError as fileout6:
            print("No file entryfile6.txt exist", fileout6)

        try:
            with open('./newpatient/entryfile7.txt', 'r') as namefile:
                line7=namefile.readline()
                new_text7=line7
        except FileNotFoundError as fileout7:
            print("No file entryfile7.txt exist", fileout7)

        # Menu administrative
        self.cmd_Admin=Menubutton(self, text='Admin', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_Admin.pack(side=LEFT, padx=3)
        # Partie déroulante du menu administrative
        me2 = Menu(self.cmd_Admin)
        self.new_text=StringVar()
        me2.add_command(label=new_text, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.adminDir)
        me2.add_separator()
        me2.add_command(label=new_text2, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.adminDir2)
        me2.add_separator()
        me2.add_command(label=new_text3, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.adminDir3)
        me2.add_separator()
        me2.add_command(label=new_text4, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.adminDir4)
        me2.add_separator()
        me2.add_command(label=new_text5, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.adminDir5)
        me2.add_separator()
        me2.add_command(label=new_text6, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.adminDir6)
        me2.add_separator()
        me2.add_command(label=new_text7, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.adminDir7)
        # Integration of menu admin
        self.cmd_Admin.configure(activeforeground='black', activebackground='cyan',
            menu=me2)

        # Agenda menu
        self.cmd_agenda=Menubutton(self, text='Agenda', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_agenda.pack(side=LEFT, padx=3)
        me3 = Menu(self.cmd_agenda)
        # Partie déroulante du menu agenda
        me3.add_command(label=new_text, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda)
        me3.add_separator()
        me3.add_command(label=new_text2, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda2)
        me3.add_separator()
        me3.add_command(label=new_text3, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda3)
        me3.add_separator()
        me3.add_command(label=new_text4, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda4)
        me3.add_separator()
        me3.add_command(label=new_text5, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda5)
        me3.add_separator()
        me3.add_command(label=new_text6, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda6)
        me3.add_separator()
        me3.add_command(label=new_text7, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda7)
        # Integration of agenda menu
        self.cmd_agenda.configure(activeforeground='black', activebackground='cyan', 
            menu=me3)

        # 14 besoins menu
        self.cmd_Besoins=Menubutton(self, text='14 Needs', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_Besoins.pack(side=LEFT, padx=3)
        # Partie déroulante du menu 14b
        me4 = Menu(self.cmd_Besoins)
        me4.add_command(label=new_text, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoinsCoche)
        me4.add_separator()
        me4.add_command(label=new_text2, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins2Coche)
        me4.add_separator()
        me4.add_command(label=new_text3, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins3Coche)
        me4.add_separator()
        me4.add_command(label=new_text4, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins4Coche)
        me4.add_separator()
        me4.add_command(label=new_text5, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins5Coche)
        me4.add_separator()
        me4.add_command(label=new_text6, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins6Coche)
        me4.add_separator()
        me4.add_command(label=new_text7, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins7Coche)
        # Integration of 14b menu
        self.cmd_Besoins.configure(activeforeground='black', activebackground='cyan',
            menu=me4)

        # Helth and care menu
        self.cmd_Soins=Menubutton(self, text='Care and monitoring', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_Soins.pack(side=LEFT, padx=3)
        # Partie déroulante du menu health and care
        meSoins = Menu(self.cmd_Soins)
        meSoins.add_command(label=new_text, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins1)
        meSoins.add_separator()
        meSoins.add_command(label=new_text2, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins2)
        meSoins.add_separator()
        meSoins.add_command(label=new_text3, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins3)
        meSoins.add_separator()
        meSoins.add_command(label=new_text4, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins4)
        meSoins.add_separator()
        meSoins.add_command(label=new_text5, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins5)
        meSoins.add_separator()
        meSoins.add_command(label=new_text6, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins6)
        meSoins.add_separator()
        meSoins.add_command(label=new_text7, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins7)
        # Integration of health and care menu
        self.cmd_Soins.configure(activeforeground='black', activebackground='cyan',
            menu=meSoins)

        # Treatments
        self.cmd_ttt=Menubutton(self, text='Treatments', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_ttt.pack(side=LEFT, padx=3)
        # Partie déroulante du menu health and care
        meTtt = Menu(self.cmd_ttt)
        meTtt.add_command(label=new_text, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed1)
        meTtt.add_separator()
        meTtt.add_command(label=new_text2, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed2)
        meTtt.add_separator()
        meTtt.add_command(label=new_text3, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed3)
        meTtt.add_separator()
        meTtt.add_command(label=new_text4, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed4)
        meTtt.add_separator()
        meTtt.add_command(label=new_text5, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed5)
        meTtt.add_separator()
        meTtt.add_command(label=new_text6, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed6)
        meTtt.add_separator()
        meTtt.add_command(label=new_text7, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed7)
        # Integration of health and care menu
        self.cmd_ttt.configure(activeforeground='black', activebackground='cyan',
            menu=meTtt)

        # Vital parameters menu
        self.cmd_Param=Menubutton(self, text='Vital Parameters', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_Param.pack(side=LEFT, padx=3)
        # Partie déroulante du menu param
        menuParam = Menu(self.cmd_Param)
        menuParam.add_command(label=new_text, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam1)
        menuParam.add_separator()
        menuParam.add_command(label=new_text2, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam2)
        menuParam.add_separator()
        menuParam.add_command(label=new_text3, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam3)
        menuParam.add_separator()
        menuParam.add_command(label=new_text4, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam4)
        menuParam.add_separator()
        menuParam.add_command(label=new_text5, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam5)
        menuParam.add_separator()
        menuParam.add_command(label=new_text6, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam6)
        menuParam.add_separator()
        menuParam.add_command(label=new_text7, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam7)
        # Integration of Vital parameters menu
        self.cmd_Param.configure(activeforeground='black', activebackground='cyan',
            menu=menuParam)

        # BMI menu
        self.cmd_BMI=Menubutton(self, text='Body Mass Indice', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_BMI.pack(side=LEFT, padx=3)
        # drop-down portion of BMI menu
        meBmi = Menu(self.cmd_BMI)
        meBmi.add_command(label=new_text, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB)
        meBmi.add_separator()
        meBmi.add_command(label=new_text2, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB2)
        meBmi.add_separator()
        meBmi.add_command(label=new_text3, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB3)
        meBmi.add_separator()
        meBmi.add_command(label=new_text4, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB4)
        meBmi.add_separator()
        meBmi.add_command(label=new_text5, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB5)
        meBmi.add_separator()
        meBmi.add_command(label=new_text6, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB6)
        meBmi.add_separator()
        meBmi.add_command(label=new_text7, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB7)
        # Integration of 3rd menu
        self.cmd_BMI.configure(activeforeground='black', activebackground='cyan',
            menu=meBmi)

        # Medical Visite
        self.cmd_Vmed=Menubutton(self, text='Medical Visit', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_Vmed.pack(side=LEFT, padx=3)
        # drop-down portion of vmed
        meVmed = Menu(self.cmd_Vmed)
        meVmed.add_command(label=new_text, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed)
        meVmed.add_separator()
        meVmed.add_command(label=new_text2, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed2)
        meVmed.add_separator()
        meVmed.add_command(label=new_text3, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed3)
        meVmed.add_separator()
        meVmed.add_command(label=new_text4, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed4)
        meVmed.add_separator()
        meVmed.add_command(label=new_text5, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed5)
        meVmed.add_separator()
        meVmed.add_command(label=new_text6, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed6)
        meVmed.add_separator()
        meVmed.add_command(label=new_text7, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed7)
        # Integration of 3rd menu
        self.cmd_Vmed.configure(activeforeground='black', activebackground='cyan',
            menu=meVmed)

        # Nutrition menu for intolerance and hate meals
        self.cmd_Print=Menubutton(self, text='Intolerance All.', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_Print.pack(side=LEFT, padx=3)
        # drop-down portion of nutrition
        mePrint = Menu(self.cmd_Print)
        mePrint.add_command(label=new_text, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu)
        mePrint.add_separator()
        mePrint.add_command(label=new_text2, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu2)
        mePrint.add_separator()
        mePrint.add_command(label=new_text3, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu3)
        mePrint.add_separator()
        mePrint.add_command(label=new_text4, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu4)
        mePrint.add_separator()
        mePrint.add_command(label=new_text5, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu5)
        mePrint.add_separator()
        mePrint.add_command(label=new_text6, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu6)
        mePrint.add_separator()
        mePrint.add_command(label=new_text7, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu7)
        # Integration of nutrition menu
        self.cmd_Print.configure(activeforeground='black', activebackground='cyan',
            menu=mePrint)

        # Menu for showing all Graphs togather per patient 
        self.cmd_Graph=Menubutton(self, text='Global', font=("Times 14"), fg='cyan',
            bg='grey30', relief=GROOVE)
        self.cmd_Graph.pack(side=LEFT, padx=3)
        # drop-down portion of Graphics menu
        me1 = Menu(self.cmd_Graph)
        me2=Menu(me1)
        me2.add_command(label='All Files.txt', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup)
        me2.add_command(label='Graphics', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.visualGraph)
        me2.add_command(label='Angel Eye', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.globEye)
        me2.add_command(label='Angel Vision', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.globVision)
        me1.add_cascade(label=new_text, underline=0, font=('Times 16'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me2)
        me1.add_separator()

        me3=Menu(me1)
        me3.add_command(label='All Files.txt', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup2)
        me3.add_command(label='Graphics', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.visualGraph2)
        me3.add_command(label='Angel Eye', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.globEye2)
        me3.add_command(label='Angel Vision', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.globVision2)
        me1.add_cascade(label=new_text2, underline=0, font=('Times 16'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me3)
        me1.add_separator()

        me4=Menu(me1)
        me4.add_command(label='All Files.txt', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup3)
        me4.add_command(label='Graphics', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.visualGraph3)
        me4.add_command(label='Angel Eye', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.globEye3)
        me4.add_command(label='Angel Vision', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.globVision3)
        me1.add_cascade(label=new_text3, underline=0, font=('Times 16'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me4)
        me1.add_separator()

        me5=Menu(me1)
        me5.add_command(label='All Files.txt', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup4)
        me5.add_command(label='Graphics', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.visualGraph4)
        me5.add_command(label='Angel Eye', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.globEye4)
        me5.add_command(label='Angel Vision', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.globVision4)
        me1.add_cascade(label=new_text4, underline=0, font=('Times 16'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me5)
        me1.add_separator()

        me6=Menu(me1)
        me6.add_command(label='All Files.txt', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup5)
        me6.add_command(label='Graphics', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.visualGraph5)
        me6.add_command(label='Angel Eye', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.globEye5)
        me6.add_command(label='Angel Vision', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.globVision5)
        me1.add_cascade(label=new_text5, underline=0, font=('Times 16'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me6)
        me1.add_separator()

        me7=Menu(me1)
        me7.add_command(label='All Files.txt', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup6)
        me7.add_command(label='Graphics', underline=0, font=('Times 16'), 
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.visualGraph6)
        me7.add_command(label='Angel Eye', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.globEye6)
        me7.add_command(label='Angel Vision', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.globVision6)
        me1.add_cascade(label=new_text6, underline=0, font=('Times 16'), 
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me7)
        me1.add_separator()

        # Menu cascade extraordinaire !!!
        me8=Menu(me1)
        me8.add_command(label='All Files.txt', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup7)
        me8.add_command(label='Graphics', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.visualGraph7)
        me8.add_command(label='Angel Eye', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.globEye7)
        me8.add_command(label='Angel Vision', underline=0, font=('Times 16'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.globVision7)
        # Integration of sub-menu
        me1.add_cascade(label=new_text7, underline=0, font=('Times 16'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me8)
        # Integration of Graph menu
        self.cmd_Graph.configure(activeforeground='black', activebackground='cyan', menu=me1)

        # Manuals Nurse
        self.cmd_Intext=Menubutton(self, text='Manuals', font=('Times 14'), fg='cyan',
            bg='grey30', relief=GROOVE)
        self.cmd_Intext.pack(side=LEFT, padx=3)
        # drop-down portion of Manuals Nurse
        meIntext = Menu(self.cmd_Intext)
        meIntext.add_command(label='Click on it', font=('Times 16'), 
            background='black', activebackground='cyan', foreground='cyan',
            activeforeground='black', command=boss.manualFile)
        # Integration of Manuals Nurse
        self.cmd_Intext.configure(activeforeground='black', activebackground='cyan',
            menu=meIntext)

# Application principale (Main app)
class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='grey22', padx=20, pady=20, relief=GROOVE)
        self.master.title('ANGEL-VISION - Developed by ko@l@tr33 - 2020')
        mBar = MenuBar(self)
        mBar.pack(side=TOP, fill=X, expand=YES)
        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can = Canvas(self, width=1250, height=800, bg='grey18')
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW, tags="self.frame")
        # Insertion of picture
        self.photo = PhotoImage(file='./syno_gif/fondcolorbg.png')
        self.item = self.can.create_image(625, 400, image=self.photo)
        # Insertion of text
        self.can.create_text(625, 420, anchor=CENTER, 
            text="Python 3.6 - Tkinter 8.6 - GIMP 2.8",
            font=('Times New Roman', 18, 'bold'), fill='turquoise')
        self.can.create_text(1240, 770, anchor=NE, text="ko@l@tr33",
            font=('Times', 12), fill='turquoise')
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # 3 buttons on welcome page.
        # Info button
        self.button1 = Button(self, text="Info", font=('Times 14 bold'),
            bg='RoyalBlue3', fg='cyan', command = self.frameInfo)
        self.button1.configure(width=10, bd=3, highlightbackground='#82193e',
            activebackground='dark turquoise')
        self.button1_window = self.can.create_window(75, 30, anchor=CENTER,
            window=self.button1)
        # Synopsis button
        self.button2 = Button(self, text="SYNOPSIS", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='cyan', command = self.showsynopsis)
        self.button2.configure(width=15, bd=3, highlightbackground='#82193e',
            activebackground='dark turquoise')
        self.button2_window = self.can.create_window(450, 550, anchor=CENTER,
            window=self.button2)
        # Psychotabs button
        self.button3 = Button(self, text="PSYCHOTABS", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='cyan', command = self.launchPsycho)
        self.button3.configure(width=15, bd=3, highlightbackground='#82193e', 
            activebackground='dark turquoise')
        self.button3_window = self.can.create_window(790, 550, anchor=CENTER,
            window=self.button3)
        self.pack()
        
        # To check onto agenda if an appointment exist.
        self.agendaDateSearch()
        # To check onto ttt if a ttt is stopped today.
        self.tttDataSearch()
        # To check onto ttt if a reserve (ttt) is stopped today.
        self.reserveDataSearch()

    # Method to reconfigure scrollbar every time.
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def effacer(self):
        '''Reinitialize canvas when we pass through another'''
        self.can.delete(ALL)

    # Second page intro (a copy from the main app juste above)
    def secondPage(self):
        self.can.delete(ALL)
        # Insertion d'une image
        self.photo=PhotoImage(file='./syno_gif/angelbg.png')
        self.item=self.can.create_image(625, 400, image=self.photo)
        # Insertion du texte
        self.can.create_text(625, 420, anchor=CENTER,
            text="Python 3.6 - Tkinter 8.6 - GIMP 2.8",
            font=('Times New Roman', 18), fill='turquoise')
        self.can.create_text(1240, 770, anchor=NE, text="ko@l@tr33",
            font=('Times', 12), fill='turquoise')
        self.can.pack(side=RIGHT, fill=BOTH, expand=YES)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # 3 buttons on welcome page.
        # Info button
        self.button1 = Button(self, text="Info", font=('Times 14 bold'),
            bg='RoyalBlue3', fg='cyan', command = self.frameInfo)
        self.button1.configure(width=10, bd=3, highlightbackground='#82193e',
            activebackground='dark turquoise')
        self.button1_window = self.can.create_window(75, 30, anchor=CENTER,
            window=self.button1)
        # Synopsis button
        self.button2 = Button(self, text="SYNOPSIS", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='cyan', command = self.showsynopsis)
        self.button2.configure(width=15, bd=3, highlightbackground='#82193e',
            activebackground='dark turquoise')
        self.button2_window = self.can.create_window(450, 550, anchor=CENTER,
            window=self.button2)
        # Statistics button
        self.button3 = Button(self, text="PSYCHOTABS", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='cyan', command = self.launchPsycho)
        self.button3.configure(width=15, bd=3, highlightbackground='#82193e',
            activebackground='dark turquoise')
        self.button3_window = self.can.create_window(790, 550, anchor=CENTER,
            window=self.button3)

        self.can.configure(scrollregion=self.can.bbox(ALL)) 

    def msgExit(self):
        MsgBox = messagebox.askyesno('Quit system', 'Do you want to quit ?')
        if MsgBox == 1:
            self.master.destroy()
        else:
            NoforQ = messagebox.showinfo('Return', 'You will now return to the'
                'application screen')

    # Installation of python and tkinter page
    def instalpy(self):
        self.can.delete(ALL)
        self.photo=PhotoImage(file='./syno_gif/pyt.gif')
        self.item=self.can.create_image(700, 400, image=self.photo)
        self.can.create_text(500, 20, anchor=NW,
            text="- MAPAPP -\n\n"

            "BACKUP and AGENDA :\n"
            "--------------------------------\n"
            "---> Backup has been programed for every first day of each month\n"
            "---> Agenda is verified every day and pop-up\n"
            "to show you if an appointment is fixed for tomorrow.\n\n"

            "SYNOPSIS\n\n"
            "Entry + Add patient ---> Allergy + Intolerance ---> 14 Needs ---> Care and Monitoring :\n"
            "---------------------------------------------------------------------------------------------------------\n"
            "Use 'Entry' button to enter for first time new patient. Use 'Add "
            "patient' once time all patients were enter \n"
            "(button to replace a patient who's left with delete button).\n"
            "Once time, patient had added use 'allergy' button to enter an allaergy "
            "if none, enter none!\n"
            "You can also use 'Intolerance' in the Menu Bar to complete 'allergy'.\n"
            "After it, Care and Monitoring is available only if you have entered one "
            "or more needs of patient.\n"
            "1 ---> 14 Needs\n"
            "2 ---> Care and monitoring\n\n"

            "Care and monitoring retrieve all data from :\n"
            "----------------------------------------------------\n"
            "+ Labo + Comburtest (urinary stix)\n"
            "+ ttt and R\n"
            "+ 14 Needs\n"
            "+ Externals Stackeholders\n\n"

            "Global :\n"
            "----------\n"
            "---> All txt files are consultable and accessibles\n"
            "---> Graphics : all Graphics open them-self to show you "
            "BMI, Weight(kg), TA, Puls, SaO2, FR, T°C,\n" 
            "and level of Pain\n"
            "---> Angel Eye : tetra vision about : BMI, Vital parameters, Visit "
            "Medical and Care and Monitoring.\n"
            "---> Global Vision : tetra vision about : Diagnosis, Agenda, Auxiliary "
            "resources and Story Life.\n\n"
            "PSYCHOTABS\n\n"
            "Psychotabs is an application only for consulting neurleptics treatments.\n\n"
            "\nDevelopped on Linux Xubuntu (xfce4) Voyager 18.04 by Cédric Kuchen - alias ko@l@tr33\n",
            font=('Times', 13), fill='aquamarine')
        self.can.configure(scrollregion=self.can.bbox(ALL))

    # Synopsis page
    def showsynopsis(self):
        self.can.delete(ALL)
        self.photo=PhotoImage(file='./syno_gif/fondcolor2.png')
        self.item=self.can.create_image(625, 400, image=self.photo)
        self.can.create_text(625, 80, anchor=CENTER, text="SYNOPSIS",
            font=('Times New Roman', 40), fill='turquoise')

        self.x1, self.y1 = 1100, 50
        self.Date_write=Entry(self.can)
        self.data_time=StringVar()
        self.Date_write=Entry(textvariable=self.data_time, width=10,
            highlightbackground='grey', bd=4)
        self.data_time.set(time.strftime("%d/%m/%Y"))
        self.Date_write=self.can.create_window(self.x1, self.y1,
            window=self.Date_write)

        # To backup
        self.updateFiletxt()

        # To check agenda
        # self.agendaDateSearch()

        # Static time
        self.x2, self.y2 = 1100, 100
        self.Date_write2 = Entry(self.can)
        self.data_time2 = StringVar()
        self.Date_write2 = Entry(width=10, textvariable=self.data_time2,
            highlightbackground='grey', bd=4)
        self.data_time2.set(time.strftime("%H:%M:%S %p"))
        self.Date_write2=self.can.create_window(self.x2, self.y2,
            window=self.Date_write2)
        # To display time dynamically

        # To introduce a new pytient
        self.x100, self.y100 = 130, 50
        self.b100=Button(self.can, width=10, font=16, bd=3, highlightbackground='#82193e',
            bg='RoyalBlue3', fg='white', activebackground='dark turquoise',
            text="New Entry", command=self.callPatient1)
        self.fb100=self.can.create_window(self.x100, self.y100, window=self.b100)
        
        # To refresh canvas + menu bar
        self.x101, self.y101 = 270, 50
        self.b101=Button(self.can, width=10, font=16, bd=3, highlightbackground='#82193e',
            bg='RoyalBlue3', fg='SpringGreen2', activebackground='yellow', activeforeground='blue',
            text="Refresh", command=self.upDateAll)
        self.fb101=self.can.create_window(self.x101, self.y101, window=self.b101)

        # To delete one patient and all files
        self.x200, self.y200 = 130, 100
        self.b200=Button(self.can, width=10, font=16, bd=3, highlightbackground='#82193e',
            bg='RoyalBlue3', fg='coral', activebackground='black', activeforeground='red',
            text="Delete patient", command=self.delEverPat)
        self.fb200=self.can.create_window(self.x200, self.y200, window=self.b200)

        # To add one patient and files
        self.x200, self.y200 = 270, 100
        self.b200=Button(self.can, width=10, font=16, bd=3, highlightbackground='#82193e',
            bg='RoyalBlue3', fg='cyan', activebackground='dark turquoise', 
            text="Add patient", command=self.addPatientAfter)
        self.fb200=self.can.create_window(self.x200, self.y200, window=self.b200)

        #Patient1
        # For label below (in me2.add_command)
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1=namefile.readline()
        except FileNotFoundError as callfile:
            print("File entryfile.txt doen't exist !", callfile)

        self.data_time=line1
        self.x2, self.y2 = 129, 200
        self.Data_write=Entry(self.can)
        self.new_data1=StringVar()
        self.Data_write=Entry(textvariable=self.new_data1,
            highlightbackground='grey', bd=4)
        self.new_data1.set(line1)
        self.Data_write=self.can.create_window(self.x2, self.y2,
            window=self.Data_write)

        self.x3, self.y3 = 271, 200
        self.b=Button(self.can, width=8, font=16, bg='grey30', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink)
        self.fb=self.can.create_window(self.x3, self.y3, window=self.b)

        self.x3, self.y3 = 429, 200
        self.b=Button(self.can, width=18, font=16, bg='grey30', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag1)
        self.fb=self.can.create_window(self.x3, self.y3, window=self.b)

        self.x4, self.y4 = 597, 200
        self.b4=Button(self.can, width=10, font=16, bg='grey30', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult)
        self.fb4=self.can.create_window(self.x4, self.y4, window=self.b4)
        #769
        self.x5, self.y5 = 725, 200
        self.b5=Button(self.can, width=10, font=16, bg='grey30', fg='cyan',
            activebackground='dark turquoise', text="Exams",
            command=self.suiviSoins1)
        self.fb5=self.can.create_window(self.x5, self.y5, window=self.b5)
        #896
        self.x6, self.y6 = 853, 200
        self.b6=Button(self.can, width=10, font=16, bg='grey30', fg='cyan',
            activebackground='dark turquoise', text="Life story",
            command=self.histv1)
        self.fb6=self.can.create_window(self.x6, self.y6, window=self.b6)

        self.x7, self.y7 = 981, 200
        self.b7=Button(self.can, width=10, font=16, bg='grey30', fg='cyan',
            activebackground='dark turquoise', text="Aux. resrc.",
            command=self.moyaux)
        self.fb7=self.can.create_window(self.x7, self.y7, window=self.b7)

        self.x8, self.y8 = 1109, 200
        self.b8=Button(self.can, width=10, font=16, bg='grey30', fg='cyan',
            activebackground='dark turquoise', text="Ext. stacke.",
            command=self.extStake)
        self.fb8=self.can.create_window(self.x8, self.y8, window=self.b8)

        # Patient 2
        try:
            with open('./newpatient/entryfile2.txt', 'r') as namefile:
                line2=namefile.readline()
        except FileNotFoundError as callfile2:
            print("File entryfile2.txt doen't exist !", callfile2)

        self.new_data2=line2
        self.x9, self.y9 = 129, 232
        self.Data_write=Entry(self.can)
        self.new_data2=StringVar()
        self.Data_write=Entry(textvariable=self.new_data2,
          highlightbackground='grey', bd=4)
        self.new_data2.set(line2)
        self.Data_write=self.can.create_window(self.x9, self.y9,
          window=self.Data_write)

        self.x10, self.y10 = 271, 232
        self.b10=Button(self.can, width=8, font=16, bg='grey25', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink2)
        self.fb10=self.can.create_window(self.x10, self.y10, window=self.b10)

        self.x13, self.y13 = 429, 232
        self.b13=Button(self.can, width=18, font=16, bg='grey25', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag2)
        self.fb13=self.can.create_window(self.x13, self.y13, window=self.b13)

        self.x14, self.y14 = 597, 232
        self.b14=Button(self.can, width=10, font=16, bg='grey25', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult2)
        self.fb14=self.can.create_window(self.x14, self.y14, window=self.b14)

        self.x15, self.y15 = 725, 232
        self.b15=Button(self.can, width=10, font=16, bg='grey25', fg='cyan',
            activebackground='dark turquoise', text="Exams",
            command=self.showvm1)
        self.fb15=self.can.create_window(self.x15, self.y15, window=self.b15)

        self.x16, self.y16 = 853, 232
        self.b16=Button(self.can, width=10, font=16, bg='grey25', fg='cyan',
            activebackground='dark turquoise', text="Life story",
            command=self.histv2)
        self.fb16=self.can.create_window(self.x16, self.y16, window=self.b16)

        self.x17, self.y17 = 981, 232
        self.b17=Button(self.can, width=10, font=16, bg='grey25', fg='cyan',
            activebackground='dark turquoise', text="Aux. resrc.",
            command=self.moyaux2)
        self.fb17=self.can.create_window(self.x17, self.y17, window=self.b17)

        self.x171, self.y171 = 1109, 232
        self.b171=Button(self.can, width=10, font=16, bg='grey25', fg='cyan',
            activebackground='dark turquoise', text="Ext. stacke.",
            command=self.extStake2)
        self.fb171=self.can.create_window(self.x171, self.y171, window=self.b171)

        # Patient 3
        try:
            with open('./newpatient/entryfile3.txt', 'r') as namefile:
                line3=namefile.readline()
        except FileNotFoundError as callfile3:
            print("File entryfile3.txt doen't exist !", callfile3)

        self.new_data3=line3
        self.x18, self.y18 = 129, 264
        self.Data_write=Entry(self.can)
        self.new_data3=StringVar()
        self.Data_write=Entry(textvariable=self.new_data3,
          highlightbackground='grey', bd=4)
        self.new_data3.set(line3)
        self.Data_write=self.can.create_window(self.x18, self.y18,
          window=self.Data_write)

        self.x19, self.y19 = 271, 264
        self.b19=Button(self.can, width=8, font=16, bg='grey20', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink3)
        self.fb19=self.can.create_window(self.x19, self.y19, window=self.b19)

        self.x22, self.y22 = 429, 264
        self.b22=Button(self.can, width=18, font=16, bg='grey20', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag3)
        self.fb22=self.can.create_window(self.x22, self.y22, window=self.b22)

        self.x23, self.y23 = 597, 264
        self.b23=Button(self.can, width=10, font=16, bg='grey20', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult3)
        self.fb23=self.can.create_window(self.x23, self.y23, window=self.b23)

        self.x24, self.y24 = 725, 264
        self.b24=Button(self.can, width=10, font=16, bg='grey20', fg='cyan',
            activebackground='dark turquoise', text="Exams",
            command=self.showvm3)
        self.fb24=self.can.create_window(self.x24, self.y24, window=self.b24)

        self.x25, self.y25 = 853, 264
        self.b25=Button(self.can, width=10, font=16, bg='grey20', fg='cyan',
            activebackground='dark turquoise', text="Life story",
            command=self.histv3)
        self.fb25=self.can.create_window(self.x25, self.y25, window=self.b25)

        self.x26, self.y26 = 981, 264
        self.b26=Button(self.can, width=10, font=16, bg='grey20', fg='cyan',
            activebackground='dark turquoise', text="Aux. resrc.",
            command=self.moyaux3)
        self.fb26=self.can.create_window(self.x26, self.y26, window=self.b26)

        self.x8, self.y8 = 1109, 264
        self.b8=Button(self.can, width=10, font=16, bg='grey20', fg='cyan',
            activebackground='dark turquoise', text="Ext. stacke.",
            command=self.extStake3)
        self.fb8=self.can.create_window(self.x8, self.y8, window=self.b8)

        # Patient 4
        try:
            with open('./newpatient/entryfile4.txt', 'r') as namefile:
                line4=namefile.readline()
        except FileNotFoundError as callfile4:
            print("File entryfile4.txt doen't exist !", callfile4)

        self.new_data4=line4
        self.x27, self.y27 = 129, 296
        self.Data_write=Entry(self.can)
        self.new_data4=StringVar()
        self.Data_write=Entry(textvariable=self.new_data4,
          highlightbackground='grey', bd=4)
        self.new_data4.set(line4)
        self.Data_write=self.can.create_window(self.x27, self.y27,
          window=self.Data_write)

        self.x28, self.y28 = 271, 296
        self.b28=Button(self.can, width=8, font=16, bg='grey18', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink4)
        self.fb28=self.can.create_window(self.x28, self.y28, window=self.b28)

        self.x31, self.y31 = 429, 296
        self.b31=Button(self.can, width=18, font=16, bg='grey18', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag4)
        self.fb31=self.can.create_window(self.x31, self.y31, window=self.b31)

        self.x32, self.y32 = 597, 296
        self.b32=Button(self.can, width=10, font=16, bg='grey18', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult4)
        self.fb32=self.can.create_window(self.x32, self.y32, window=self.b32)

        self.x33, self.y33 = 725, 296
        self.b33=Button(self.can, width=10, font=16, bg='grey18', fg='cyan',
            activebackground='dark turquoise', text="Exams",
            command=self.showvm4)
        self.fb33=self.can.create_window(self.x33, self.y33, window=self.b33)

        self.x34, self.y34 = 853, 296
        self.b34=Button(self.can, width=10, font=16, bg='grey18', fg='cyan',
            activebackground='dark turquoise', text="Life story",
            command=self.histv4)
        self.fb34=self.can.create_window(self.x34, self.y34, window=self.b34)

        self.x35, self.y35 = 981, 296
        self.b35=Button(self.can, width=10, font=16, bg='grey18', fg='cyan',
            activebackground='dark turquoise', text="Aux. resrc.",
            command=self.moyaux4)
        self.fb35=self.can.create_window(self.x35, self.y35, window=self.b35)

        self.x351, self.y351 = 1109, 296
        self.b351=Button(self.can, width=10, font=16, bg='grey18', fg='cyan',
            activebackground='dark turquoise', text="Ext. stacke.",
            command=self.extStake4)
        self.fb351=self.can.create_window(self.x351, self.y351, window=self.b351)

        #patient5
        try:
            with open('./newpatient/entryfile5.txt', 'r') as namefile:
                line5=namefile.readline()
        except FileNotFoundError as callfile5:
            print("File entryfile5.txt doen't exist !", callfile5)

        self.new_data5=line5
        self.x36, self.y36 = 129, 328
        self.Data_write=Entry(self.can)
        self.new_data5=StringVar()
        self.Data_write=Entry(textvariable=self.new_data5,
          highlightbackground='grey', bd=4)
        self.new_data5.set(line5)
        self.Data_write=self.can.create_window(self.x36, self.y36,
          window=self.Data_write)

        self.x37, self.y37 = 271, 328
        self.b37=Button(self.can, width=8, font=16, bg='grey15', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink5)
        self.fb37=self.can.create_window(self.x37, self.y37, window=self.b37)

        self.x40, self.y40 = 429, 328
        self.b40=Button(self.can, width=18, font=16, bg='grey15', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag5)
        self.fb40=self.can.create_window(self.x40, self.y40, window=self.b40)

        self.x41, self.y41 = 597, 328
        self.b41=Button(self.can, width=10, font=16, bg='grey15', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult5)
        self.fb41=self.can.create_window(self.x41, self.y41, window=self.b41)

        self.x42, self.y42 = 725, 328
        self.b42=Button(self.can, width=10, font=16, bg='grey15', fg='cyan',
            activebackground='dark turquoise', text="Exams",
            command=self.showvm5)
        self.fb42=self.can.create_window(self.x42, self.y42, window=self.b42)

        self.x43, self.y43 = 853, 328
        self.b43=Button(self.can, width=10, font=16, bg='grey15', fg='cyan',
            activebackground='dark turquoise', text="Life story",
            command=self.histv5)
        self.fb43=self.can.create_window(self.x43, self.y43, window=self.b43)

        self.x44, self.y44 = 981, 328
        self.b44=Button(self.can, width=10, font=16, bg='grey15', fg='cyan',
            activebackground='dark turquoise', text="Aux. resrc.",
            command=self.moyaux5)
        self.fb44=self.can.create_window(self.x44, self.y44, window=self.b44)

        self.x441, self.y441 = 1109, 328
        self.b441=Button(self.can, width=10, font=16, bg='grey15', fg='cyan',
            activebackground='dark turquoise', text="Ext. stacke.",
            command=self.extStake5)
        self.fb441=self.can.create_window(self.x441, self.y441, window=self.b441)

        #patient6
        try:
            with open('./newpatient/entryfile6.txt', 'r') as namefile:
                line6=namefile.readline()
        except FileNotFoundError as callfile6:
            print("File entryfile6.txt doen't exist !", callfile6)

        self.new_data6=line6
        self.x45, self.y45 = 129, 360
        self.Data_write=Entry(self.can)
        self.new_data6=StringVar()
        self.Data_write=Entry(textvariable=self.new_data6,
          highlightbackground='grey', bd=4)
        self.new_data6.set(line6)
        self.Data_write=self.can.create_window(self.x45, self.y45,
          window=self.Data_write)

        self.x46, self.y46 = 271, 360
        self.b46=Button(self.can, width=8, font=16, bg='grey12', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink6)
        self.fb46=self.can.create_window(self.x46, self.y46, window=self.b46)

        self.x49, self.y49 = 429, 360
        self.b49=Button(self.can, width=18, font=16, bg='grey12', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag6)
        self.fb49=self.can.create_window(self.x49, self.y49, window=self.b49)

        self.x50, self.y50 = 597, 360
        self.b50=Button(self.can, width=10, font=16, bg='grey12', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult6)
        self.fb50=self.can.create_window(self.x50, self.y50, window=self.b50)

        self.x51, self.y51 = 725, 360
        self.b51=Button(self.can, width=10, font=16, bg='grey12', fg='cyan',
            activebackground='dark turquoise', text="Exams",
            command=self.showvm6)
        self.fb51=self.can.create_window(self.x51, self.y51, window=self.b51)

        self.x52, self.y52 = 853, 360
        self.b52=Button(self.can, width=10, font=16, bg='grey12', fg='cyan',
            activebackground='dark turquoise', text="Life story",
            command=self.histv6)
        self.fb52=self.can.create_window(self.x52, self.y52, window=self.b52)

        self.x53, self.y53 = 981, 360
        self.b53=Button(self.can, width=10, font=16, bg='grey12', fg='cyan',
            activebackground='dark turquoise', text="Aux. resrc.",
            command=self.moyaux6)
        self.fb53=self.can.create_window(self.x53, self.y53, window=self.b53)

        self.x531, self.y531 = 1109, 360
        self.b531=Button(self.can, width=10, font=16, bg='grey12', fg='cyan',
            activebackground='dark turquoise', text="Ext. stacke.",
            command=self.extStake6)
        self.fb531=self.can.create_window(self.x531, self.y531, window=self.b531)
        
        #patient7
        try:
            with open('./newpatient/entryfile7.txt', 'r') as namefile:
                line7=namefile.readline()
        except FileNotFoundError as callfile7:
            print("File entryfile7.txt doen't exist !", callfile7)

        self.new_data7=line7
        self.x54, self.y54 = 129, 392
        self.Data_write=Entry(self.can)
        self.new_data7=StringVar()
        self.Data_write=Entry(textvariable=self.new_data7,
          highlightbackground='grey', bd=4)
        self.new_data7.set(line7)
        self.Data_write=self.can.create_window(self.x54, self.y54,
          window=self.Data_write)

        self.x54, self.y54 = 271, 392
        self.b54=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink7)
        self.fb54=self.can.create_window(self.x54, self.y54, window=self.b54)

        self.x57, self.y57 = 429, 392
        self.b57=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag7)
        self.fb57=self.can.create_window(self.x57, self.y57, window=self.b57)

        self.x58, self.y58 = 597, 392
        self.b58=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult7)
        self.fb58=self.can.create_window(self.x58, self.y58, window=self.b58)

        self.x59, self.y59 = 725, 392
        self.b59=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Exams",
            command=self.showvm7)
        self.fb59=self.can.create_window(self.x59, self.y59, window=self.b59)

        self.x60, self.y60 = 853, 392
        self.b60=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Life story",
            command=self.histv7)
        self.fb60=self.can.create_window(self.x60, self.y60, window=self.b60)

        self.x61, self.y61 = 981, 392
        self.b61=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Aux. resrc.",
            command=self.moyaux7)
        self.fb61=self.can.create_window(self.x61, self.y61, window=self.b61)

        self.x62, self.y62 = 1109, 392
        self.b62=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Ext. stacke.",
            command=self.extStake7)
        self.fb62=self.can.create_window(self.x62, self.y62, window=self.b62)

        # TextBox
        self.x63, self.y63 = 625, 600
        self.t63=Text(self.can, height=15, width=60, font=18, relief=SUNKEN)
        self.t63.insert(INSERT, "Previously (yesterday) : ")
        self.t63.insert(END, time.strftime("%d/%m/%Y at %H:%M:%S :\n"))
        self.ft63=self.can.create_window(self.x63, self.y63, window=self.t63)

        # Display text in textbox from 14 Needs files
        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n--- Patient 1 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, lines[i+3])
                        self.t63.insert(INSERT, lines[i+4])
                        self.t63.insert(INSERT, lines[i+5])
                        self.t63.insert(INSERT, lines[i+6])
                    else:
                        pass
        except FileNotFoundError as infofileout:
            print("File 1 has not been found", infofileout)
        except IndexError as inforange:
            print("List 1 got less than 6 lines", inforange)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi2/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 2 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, lines[i+3])
                        self.t63.insert(INSERT, lines[i+4])
                        self.t63.insert(INSERT, lines[i+5])
                        self.t63.insert(INSERT, lines[i+6])
                    else:
                        pass
        except FileNotFoundError as infofileout1:
            print("File 2 has not been found", infofileout1)
        except IndexError as inforange2:
            print("List 2 got less than 6 lines", inforange2)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi3/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 3 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, lines[i+3])
                        self.t63.insert(INSERT, lines[i+4])
                        self.t63.insert(INSERT, lines[i+5])
                        self.t63.insert(INSERT, lines[i+6])
                    else:
                        pass
        except FileNotFoundError as infofileout3:
            print("File 3 has not been found", infofileout3)
        except IndexError as inforange3:
            print("List 3 got less than 6 lines", inforange3)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi4/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 4 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, lines[i+3])
                        self.t63.insert(INSERT, lines[i+4])
                        self.t63.insert(INSERT, lines[i+5])
                        self.t63.insert(INSERT, lines[i+6])
                    else:
                        pass
        except FileNotFoundError as infofileout4:
            print("File 4 has not been found", infofileout4)
        except IndexError as inforange4:
            print("List 4 got less than 6 lines", inforange4)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi5/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 5 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, lines[i+3])
                        self.t63.insert(INSERT, lines[i+4])
                        self.t63.insert(INSERT, lines[i+5])
                        self.t63.insert(INSERT, lines[i+6])
                    else:
                        pass
        except FileNotFoundError as infofileout5:
            print("File 5 has not been found", infofileout5)
        except IndexError as inforange5:
            print("List 5 got less than 6 lines", inforange5)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi6/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 6 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, lines[i+3])
                        self.t63.insert(INSERT, lines[i+4])
                        self.t63.insert(INSERT, lines[i+5])
                        self.t63.insert(INSERT, lines[i+6])
                    else:
                        pass
        except FileNotFoundError as infofileout6:
            print("File 6 has not been found", infofileout6)
        except IndexError as inforange6:
            print("List 6 got less than 6 lines", inforange6)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi7/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 7 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, lines[i+3])
                        self.t63.insert(INSERT, lines[i+4])
                        self.t63.insert(INSERT, lines[i+5])
                        self.t63.insert(INSERT, lines[i+6])
                    else:
                        pass
        except FileNotFoundError as infofileout7:
            print("File 7 has not been found", infofileout7)
        except IndexError as inforange7:
            print("List 7 got less than 6 lines", inforange7)
        else:
            ("Error unknow")

    def agendaDateSearch(self):
        """
        Display agenda if an appointment 
        has been fixed for tomorrow:
        """
        print("Hello, let's see if appointment has been fixed for tomorrow...")
        time.sleep(1)
        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./patient_agenda/events/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSB2 = messagebox.showwarning('Info',
                            'Look at AGENDA,there is an appointment for patient 1!')
                    else:
                        pass
        except FileNotFoundError as infofile1:
            print("File 1 has not been found", infofile1)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./patient_agenda/events2/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSB2 = messagebox.showwarning('Info',
                            'Look at AGENDA, there is an appointment for patient 2!')
                    else:
                        pass
        except FileNotFoundError as infofile2:
            print("File 2 has not been found", infofile2)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./patient_agenda/events3/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSB2 = messagebox.showwarning('Info',
                            'Look at AGENDA, there is an appointment for patient 3!')
                    else:
                        pass
        except FileNotFoundError as infofile3:
            print("File 3 has not been found", infofile3)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./patient_agenda/events4/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSB2 = messagebox.showwarning('Info',
                            'Look at AGENDA, there is an appointment for patient 4!')
                    else:
                        pass
        except FileNotFoundError as infofile4:
            print("File 4 has not been found", infofile4)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./patient_agenda/events5/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSB2 = messagebox.showwarning('Info',
                            'Look at AGENDA, there is an appointment for patient 5!')
                    else:
                        pass
        except FileNotFoundError as infofile5:
            print("File 5 has not been found", infofile5)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./patient_agenda/events6/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSB2 = messagebox.showwarning('Info',
                            'Look at AGENDA, there is an appointment for patient 6!')
                    else:
                        pass
        except FileNotFoundError as infofile6:
            print("File 6 has not been found", infofile6)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./patient_agenda/events7/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSB2 = messagebox.showwarning('Info',
                            'Look at AGENDA, there is an appointment for patient 7!')
                    else:
                        pass
        except FileNotFoundError as infofile7:
            print("File 7 has not been found", infofile7)
        else:
            ("Error unknow")

    def tttDataSearch(self):
        """
        To search the date of the end into the file of ttt.
        There is 3 dates into this file, I have to resolve that !
        Warning with the format of date into ttt_file !!!
        Error was in file patient_ttt.py with a faul format date...
        """
        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            initword = "Date of end : "
            with open('./ttt/doc_ttt/convode.json', 'r') as filedate:
                lines = filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBTTT2 = messagebox.showwarning('Info',
                                'Look at TTT, there is a ttt for patient \
                                 1 which is stopped today!')
        except FileNotFoundError as info_ttt:
            print("File intro_ttt (patient 1) has not been found", info_ttt)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            initword = "Date of end : "
            with open('./ttt/doc_ttt2/convode.json', 'r') as filedate:
                lines = filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBTTT2 = messagebox.showwarning('Info',
                                'Look at TTT, there is a ttt for patient \
                                 2 which is stopped today!')
        except FileNotFoundError as info_ttt:
            print("File intro_ttt (patient 2) has not been found", info_ttt)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            initword = "Date of end : "
            with open('./ttt/doc_ttt3/convode.json', 'r') as filedate:
                lines = filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBTTT2 = messagebox.showwarning('Info',
                                'Look at TTT, there is a ttt for patient \
                                 3 which is stopped today!')
        except FileNotFoundError as info_ttt:
            print("File intro_ttt (patient 3) has not been found", info_ttt)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            initword = "Date of end : "
            with open('./ttt/doc_ttt4/convode.json', 'r') as filedate:
                lines = filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBTTT2 = messagebox.showwarning('Info',
                                'Look at TTT, there is a ttt for patient \
                                 4 which is stopped today!')
        except FileNotFoundError as info_ttt:
            print("File intro_ttt (patient 4) has not been found", info_ttt)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            initword = "Date of end : "
            with open('./ttt/doc_ttt5/convode.json', 'r') as filedate:
                lines = filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBTTT2 = messagebox.showwarning('Info',
                                'Look at TTT, there is a ttt for patient \
                                 5 which is stopped today!')
        except FileNotFoundError as info_ttt:
            print("File intro_ttt (patient 5) has not been found", info_ttt)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            initword = "Date of end : "
            with open('./ttt/doc_ttt6/convode.json', 'r') as filedate:
                lines = filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBTTT2 = messagebox.showwarning('Info',
                                'Look at TTT, there is a ttt for patient \
                                 6 which is stopped today!')
        except FileNotFoundError as info_ttt:
            print("File intro_ttt (patient 6) has not been found", info_ttt)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            initword = "Date of end : "
            with open('./ttt/doc_ttt7/convode.json', 'r') as filedate:
                lines = filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBTTT2 = messagebox.showwarning('Info',
                                'Look at TTT, there is a ttt for patient \
                                 7 which is stopped today!')
        except FileNotFoundError as info_ttt:
            print("File intro_ttt (patient 7) has not been found", info_ttt)
        else:
            ("Error unknow")

    def reserveDataSearch(self):
        """
        To search the date of the end into the file of reserve.
        There is 3 dates into this file, I have to resolve that !
        """
        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            with open('./ttt/doc_ttt/intro_res.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE for patient 1 which is stopped today!')
                    else:
                        pass
        except FileNotFoundError as info_res1:
            print("File intro_ttt has not been found", info_res1)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            with open('./ttt/doc_ttt2/intro_res.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE for patient 2 which is stopped today!')
                    else:
                        pass
        except FileNotFoundError as info_res2:
            print("File intro_ttt has not been found", info_res2)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            with open('./ttt/doc_ttt3/intro_res.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE for patient 3 which is stopped today!')
                    else:
                        pass
        except FileNotFoundError as info_res3:
            print("File intro_ttt has not been found", info_res3)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            with open('./ttt/doc_ttt4/intro_res.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE for patient 4 which is stopped today!')
                    else:
                        pass
        except FileNotFoundError as info_res4:
            print("File intro_ttt has not been found", info_res4)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            with open('./ttt/doc_ttt5/intro_res.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE for patient 5 which is stopped today!')
                    else:
                        pass
        except FileNotFoundError as info_res5:
            print("File intro_ttt has not been found", info_res5)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            with open('./ttt/doc_ttt6/intro_res.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE for patient 6 which is stopped today!')
                    else:
                        pass
        except FileNotFoundError as info_res6:
            print("File intro_ttt has not been found", info_res6)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            with open('./ttt/doc_ttt7/intro_res.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE for patient 7 which is stopped today!')
                    else:
                        pass
        except FileNotFoundError as info_res7:
            print("File intro_ttt has not been found", info_res7)
        else:
            ("Error unknow")

    def frameInfo(self):
        """
        Info for button on first page
        """
        self.lab=Tk()
        self.lab.title("ATCD")
        self.lab.configure(bg="grey22")

        self.labFra=LabelFrame(self.lab, text="\nWelcome !",
            font=("Arial 12"),fg='cyan', bg='grey22')
        self.labFra.pack(padx=5, pady=5)
        self.separator = Frame(self.labFra, height=2, bd=1,
            relief=SUNKEN)

        self.lab4=Label(self.labFra, text="\nInfo",
            font=('Times 16 bold'), fg='cyan', bg='grey22').pack()
        self.separator = Frame(self.labFra, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=100, pady=3)

        self.lab5=Label(self.labFra, justify=LEFT, fg='cyan',
            bg='grey22', font=('Times', 14),
            text="\nMenu Bar and Synopsis are the most usefull skills\n"
            "to perform onto this app ! If you need help, you\n" 
            "can go to MapApp to access map of this app and\n" 
            "understand how the app is used.\n\n"
            "Enjoy it ! ;)\n").pack(padx=10)
        self.separator = Frame(self.labFra, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=30, pady=3)
        self.lab6=Label(self.labFra, justify=LEFT, fg='cyan',
            bg='grey22', font=('Times', 14),
            text="Path : Menu Bar --> Menu --> MapApp").pack(padx=10, pady=10)

    # For new entry
    def callPatient1(self):
        subprocess.call('./newpatient/entrypytientfile.py')

    def delEverPat(self):
        subprocess.call('./deletepatient/deleverything.py')

    def addPatientAfter(self):
        messagebox.showwarning("Warning", "Don't forget to enter allergy too ! ;)")
        subprocess.call('./newpatient/torecord.py')
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
    # CheckBox 14 needs OK
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
        subprocess.call('./patient_agenda/origin_agenda2.py')

    def patientAgenda3(self):
        subprocess.call('./patient_agenda/origin_agenda3.py')

    def patientAgenda4(self):
        subprocess.call('./patient_agenda/origin_agenda4.py')

    def patientAgenda5(self):
        subprocess.call('./patient_agenda/origin_agenda5.py')

    def patientAgenda6(self):
        subprocess.call('./patient_agenda/origin_agenda6.py')

    def patientAgenda7(self):
        subprocess.call('./patient_agenda/origin_agenda7.py')
    # Func 14 needs suivi OK
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

    # Allergy OK
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
        subprocess.call("./diag/diag_patient1.py")

    def diag2(self):
        subprocess.call("./diag/diag_patient2.py")

    def diag3(self):
        subprocess.call("./diag/diag_patient3.py")

    def diag4(self):
        subprocess.call("./diag/diag_patient4.py")

    def diag5(self):
        subprocess.call("./diag/diag_patient5.py")

    def diag6(self):
        subprocess.call("./diag/diag_patient6.py")

    def diag7(self):
        subprocess.call("./diag/diag_patient7.py")

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
        subprocess.call("./histv/patient2_histv.py")

    def histv3(self):
        subprocess.call("./histv/patient3_histv.py")

    def histv4(self):
        subprocess.call("./histv/patient4_histv.py")

    def histv5(self):
        subprocess.call("./histv/patient5_histv.py")

    def histv6(self):
        subprocess.call("./histv/patient6_histv.py")

    def histv7(self):
        subprocess.call("./histv/patient7_histv.py")

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

    # Backup
    def allFilesBackup(self):
        self.label=Tk()
        self.label.title("Search File")
        filepath = filedialog.askopenfilename(initialdir = "./Backup/Files1",
            title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
        print(filepath)
        with open(filepath, 'r') as fichier:
            content = fichier.read()

        # I have to try with Text (else no scrollbar)
        self.label=Label(self.label, justify=LEFT, font=('Times 14'),
            bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

    # Backup
    def allFilesBackup2(self):
        self.label=Tk()
        self.label.title("Search File")
        filepath = filedialog.askopenfilename(initialdir = "./Backup/Files2",
            title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
        print(filepath)
        with open(filepath, 'r') as fichier:
            content = fichier.read()

        self.label=Label(self.label, justify=LEFT, font=('Times 14'),
            bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

    # Backup
    def allFilesBackup3(self):
        self.label=Tk()
        self.label.title("Search File")
        filepath = filedialog.askopenfilename(initialdir = "./Backup/Files3",
            title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
        print(filepath)
        with open(filepath, 'r') as fichier:
            content = fichier.read()

        self.label=Label(self.label, justify=LEFT, font=('Times 14'),
            bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

    # Backup
    def allFilesBackup4(self):
        self.label=Tk()
        self.label.title("Search File")
        filepath = filedialog.askopenfilename(initialdir = "./Backup/Files4",
            title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
        print(filepath)
        with open(filepath, 'r') as fichier:
            content = fichier.read()

        self.label=Label(self.label, justify=LEFT, font=('Times 14'),
            bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

    # Backup
    def allFilesBackup5(self):
        self.label=Tk()
        self.label.title("Search File")
        filepath = filedialog.askopenfilename(initialdir = "./Backup/Files5",
            title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
        print(filepath)
        with open(filepath, 'r') as fichier:
            content = fichier.read()

        self.label=Label(self.label, justify=LEFT, font=('Times 14'),
            bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

    # Backup
    def allFilesBackup6(self):
        self.label=Tk()
        self.label.title("Search File")
        filepath = filedialog.askopenfilename(initialdir = "./Backup/Files6",
            title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
        print(filepath)
        with open(filepath, 'r') as fichier:
            content = fichier.read()

        self.label=Label(self.label, justify=LEFT, font=('Times 14'),
            bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

    # Backup
    def allFilesBackup7(self):
        self.label=Tk()
        self.label.title("Search File")
        filepath = filedialog.askopenfilename(initialdir = "./Backup/Files7",
            title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
        print(filepath)
        with open(filepath, 'r') as fichier:
            content = fichier.read()

        self.label=Label(self.label, justify=LEFT, font=('Times 14'),
            bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

    def globEye(self):
        subprocess.call('./global_eye/angel_eye1.py')

    def globEye2(self):
        subprocess.call('./global_eye/angel_eye2.py')

    def globEye3(self):
        subprocess.call('./global_eye/angel_eye3.py')

    def globEye4(self):
        subprocess.call('./global_eye/angel_eye4.py')

    def globEye5(self):
        subprocess.call('./global_eye/angel_eye5.py')

    def globEye6(self):
        subprocess.call('./global_eye/angel_eye6.py')

    def globEye7(self):
        subprocess.call('./global_eye/angel_eye7.py')

    # 4 frames in one
    def globVision(self):
        subprocess.call('./global_vision/global_vision1.py')

    def globVision2(self):
        subprocess.call('./global_vision/global_vision2.py')

    def globVision3(self):
        subprocess.call('./global_vision/global_vision3.py')

    def globVision4(self):
        subprocess.call('./global_vision/global_vision4.py')

    def globVision5(self):
        subprocess.call('./global_vision/global_vision5.py')

    def globVision6(self):
        subprocess.call('./global_vision/global_vision6.py')

    def globVision7(self):
        subprocess.call('./global_vision/global_vision7.py')

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

    def newsTextBox(self):
        self.can.textBox = Text(app, text = "")

    def updateFiletxt(self):
        # To backup all files
        listeDate = ["01/05/2020", "18/06/2020", "01/07/2020",
        "01/08/2020", "01/09/2020", "01/10/2020", "01/11/2020",
        "01/12/2020"]
        
        for i in listeDate:
            try:
                if time.strftime("%d/%m/%Y") == i:
                    MSB = messagebox.showinfo('Info', 'Backup is done at the first of each month')
                    subprocess.call('./Backup/backupfile.py')
                    print("+ Backup is done !")
            except FileNotFoundError as errout:
                print("+ It is not the right date for backup, next will" \
                    "be at the first of next month)", errout)

        self.can.configure(scrollregion=self.can.bbox(ALL))

    def upDateAll(self):
        self.master.destroy()
        subprocess.call('./angel.py')

if __name__=='__main__':
    app = Application()
    app.mainloop()
