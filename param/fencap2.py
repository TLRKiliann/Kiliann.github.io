#!/usr/bin/python3
#!-*-encoding:utf-8-*-

"""
this script is made to develop
other butons with functions
"""

import tkinter
from tkinter import *
from tkinter import messagebox
import json
import os
import subprocess
import time
import io
import sys


def writeData():
    """
    To export data in a json file
    and launching aspiFile.py
    """
    file = open('./param/Main2.json', 'a+')
    file.write(str("Date: "))
    file.write(textDate.get() + '\n')
    file.write(str("Heure: "))
    file.write(textHour.get() + '\n')
    file.write(str("Prenom et Nom: "))
    file.write(textName.get() + '\n')
    file.write(str("TA: "))
    file.write(textTa.get() + " mmHg\n")
    file.write(str("Puls: "))
    file.write(textPuls.get() + "/min\n")
    file.write(str("SaO2: "))
    file.write(textSa.get() + "%\n")
    file.write(str("FR: "))
    file.write(textFr.get() + "/min\n")
    file.write(str("Temperature: "))
    file.write(textTemp.get() + "°C\n")
    file.write(str("Glycemie: "))
    file.write(textHgt.get() + " mmol/l\n")
    file.write(str("Douleurs: "))
    file.write(textDlrs.get() +"/10\n\n")
    file.close()

    try:
        if os.path.getsize('./param/aspifile2/tensor.json'):
            print("+ File 'tensor' exist !")
            with open('./param/aspifile2/tensor.json', 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataTa = datastore
            dataTa['data'].append({'Date' : textDate.get(), 'Tension' : textTa.get()})
            if textTa.get() == "":
                print("---Pas de VALEUR 'Tension' entrée---")
            else:
                print("---Ok VALEUR 'Tension' entrée---")
                with open('./param/aspifile2/tensor.json', 'w') as datafile2:
                    json.dump(dataTa, datafile2, indent=4)
    except FileNotFoundError as outcom:
        print('+ Sorry, file tensor.json not exist !')
        print(str(outcom))
        print("+ File tensor.json created !")
        dataTa = {}
        dataTa['data'] = []
        dataTa['data'].append({'Date' : textDate.get(), 'Tension' : textTa.get()})
        if textTa.get() == "":
            print("---Pas de VALEUR 'Tension' entrée---")
        else:
            print("---Ok VALEUR 'Tension' entrée---")
            with open('./param/aspifile2/tensor.json', 'w') as datafile:
                json.dump(dataTa, datafile, indent=4)

    try:
        if os.path.getsize('./param/aspifile2/puls.json'):
            print("+ File 'puls' exist !")
            with open('./param/aspifile2/puls.json', 'r') as datapuls:
                datastore = json.load(datapuls)
                print(datastore)
            dataP = datastore
            dataP['data'].append({'Date' : textDate.get(), 'Puls' : textPuls.get()})
            if textPuls.get() == "":
                print("---Pas de VALEUR 'Puls' entrée---")
            else:
                print("---Ok VALEUR 'Puls' entrée---")
                with open('./param/aspifile2/puls.json', 'w') as datapuls2:
                    json.dump(dataP, datapuls2, indent=4)
    except FileNotFoundError as errorfile1:
        print('+ Sorry, file puls.json not exist !')
        print(str(errorfile1))
        print("+ File puls.json created !")
        dataP = {}
        dataP['data'] = []
        dataP['data'].append({'Date' : textDate.get(), 'Puls' : textPuls.get()})
        if textPuls.get() == "":
            print("---Pas de VALEUR 'Puls' entrée---")
        else:
            print("---Ok VALEUR 'Puls' entrée---")
            with open('./param/aspifile2/puls.json', 'w') as datapuls3:
                json.dump(dataP, datapuls3, indent=4)

    try:
        if os.path.getsize('./param/aspifile2/sat.json'):
            print("+ File 'sat' exist !")
            with open('./param/aspifile2/sat.json', 'r') as datasat:
                datastore = json.load(datasat)
                print(datastore)
            dataS = datastore
            dataS['data'].append({'Date' : textDate.get(), 'SaO2' : textSa.get()})
            if textSa.get() == "":
                print("---Pas de VALEUR 'SaO2' entrée---")
            else:
                print("---Ok VALEUR 'SaO2' entrée---")
                with open('./param/aspifile2/sat.json', 'w') as datasat2:
                    json.dump(dataS, datasat2, indent=4)
    except FileNotFoundError as errorfile2:
        print('+ Sorry, file sat.json not exist !')
        print(str(errorfile2))
        print("+ File sat.json created !")
        dataS = {}
        dataS['data'] = []
        dataS['data'].append({'Date' : textDate.get(), 'SaO2' : textSa.get()})
        if textSa.get() == "":
            print("---Pas de VALEUR 'SaO2' entrée---")
        else:
            print("---Ok VALEUR 'SaO2' entrée---")
            with open('./param/aspifile2/sat.json', 'w') as datasat3:
                json.dump(dataS, datasat3, indent=4)

    try:
        if os.path.getsize('./param/aspifile2/freq.json'):
            print("+ File 'freq' exist !")
            with open('./param/aspifile2/freq.json', 'r') as datafreq:
                datastore = json.load(datafreq)
                print(datastore)
            dataF = datastore
            dataF['data'].append({'Date' : textDate.get(), 'FR' : textFr.get()})
            if textFr.get() == "":
                print("---Pas de VALEUR 'FR' entrée---")
            else:
                print("---Ok VALEUR 'FR' entrée---")
                with open('./param/aspifile2/freq.json', 'w') as datafreq2:
                    json.dump(dataF, datafreq2, indent=4)
    except FileNotFoundError as errorfile3:
        print('+ Sorry, file freq.json not exist !')
        print(str(errorfile3))
        print("+ File freq.json created !")
        dataF = {}
        dataF['data'] = []
        dataF['data'].append({'Date' : textDate.get(), 'FR' : textFr.get()})
        if textFr.get() == "":
            print("---Pas de VALEUR 'FR' entrée---")
        else:
            print("---Ok VALEUR 'FR' entrée---")
            with open('./param/aspifile2/freq.json', 'w') as datafreq3:
                json.dump(dataF, datafreq3, indent=4)

    try:
        if os.path.getsize('./param/aspifile2/temp.json'):
            print("+ File 'temp' exist !")
            with open('./param/aspifile2/temp.json', 'r') as datatemp:
                datastore = json.load(datatemp)
                print(datastore)
            dataTe2 = datastore
            dataTe2['data'].append({'Date' : textDate.get(), 'Temperature' : textTemp.get()})
            if textTemp.get() == "":
                print("---Pas de VALEUR 'Temperature' entrée---")
            else:
                print("---Ok VALEUR 'Temperature' entrée---")
                with open('./param/aspifile2/temp.json', 'w') as datatemp2:
                    json.dump(dataTe2, datatemp2, indent=4)
    except FileNotFoundError as errorfile4:
        print('+ Sorry, file temp.json not exist !')
        print(str(errorfile4))
        print("+ File temp.json created !")
        dataTe2 = {}
        dataTe2['data'] = []
        dataTe2['data'].append({'Date' : textDate.get(), 'Temperature' : textTemp.get()})
        if textTemp.get() == "":
            print("---Pas de VALEUR 'Temperature' entrée---")
        else:
            print("---Ok VALEUR 'Temperature' entrée---")
            with open('./param/aspifile2/temp.json', 'w') as datatemp3:
                json.dump(dataTe2, datatemp3, indent=4)

    try:
        if os.path.getsize('./param/aspifile2/gly.json'):
            print("+ File 'gly' exist !")
            with open('./param/aspifile2/gly.json', 'r') as datagly:
                datastore = json.load(datagly)
                print(datastore)
            dataG = datastore
            dataG['data'].append({'Date' : textDate.get(), 'Glycemie' : textHgt.get()})
            if textHgt.get() == "":
                print("---Pas de VALEUR 'Glycemie' entrée---")
            else:
                print("---Ok VALEUR 'Glycemie' entrée---")
                with open('./param/aspifile2/gly.json', 'w') as datagly2:
                    json.dump(dataG, datagly2, indent=4)
    except FileNotFoundError as errorfile5:
        print('+ Sorry, file gly.json not exist !')
        print(str(errorfile5))
        print("+ File gly.json created !")
        dataG = {}
        dataG['data'] = []
        dataG['data'].append({'Date' : textDate.get(), 'Glycemie' : textHgt.get()})
        if textHgt.get() == "":
            print("---Pas de VALEUR 'Glycemie' entrée---")
        else:
            print("---Ok VALEUR 'Glycemie' entrée---")
            with open('./param/aspifile2/gly.json', 'w') as datagly3:
                json.dump(dataG, datagly3, indent=4)

    try:
        if os.path.getsize('./param/aspifile2/dlr.json'):
            print("+ File 'dlr' exist !")
            with open('./param/aspifile2/dlr.json', 'r') as datadlr:
                datastore = json.load(datadlr)
                print(datastore)
            dataD = datastore
            dataD['data'].append({'Date' : textDate.get(), 'Douleurs' : textDlrs.get()})
            if textDlrs.get() == "":
                print("---Pas de VALEUR 'Douleurs' entrée---")
            else:
                print("---Ok VALEUR 'Douleurs' entrée---")
                with open('./param/aspifile2/dlr.json', 'w') as datadlr2:
                    json.dump(dataD, datadlr2, indent=4)
    except FileNotFoundError as errorfile6:
        print('+ Sorry, file dlr.json not exist !')
        print(str(errorfile6))
        print("+ File dlr.json created !")
        dataD = {}
        dataD['data'] = []
        dataD['data'].append({'Date' : textDate.get(), 'Douleurs' : textDlrs.get()})
        if textDlrs.get() == "":
            print("---Pas de VALEUR 'Douleurs' entrée---")
        else:
            print("---Ok VALEUR 'Douleurs' entrée---")
            with open('./param/aspifile2/dlr.json', 'w') as datadlr3:
                json.dump(dataD, datadlr3, indent=4)

    label['text'] = ("Date: " + textDate.get() +" -- "+ "Nom: " + textName.get() + 
        "\nTension: " + textTa.get() +" -- "+ "Puls: " + textPuls.get() +
        "\nSaO2: " + textSa.get() +" -- "+ "FR: " + textFr.get() +
        "\nTemperature: " + textTemp.get() +
        "\nGlycemie: " + textHgt.get() +
        "\nDouleurs: " + textDlrs.get() +
        "\nAll data have been added in json files !")

def appelTens():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile2/tensor.json'):
            subprocess.call('./param/aspifile2/aspidata.py', shell=True)
            label['text'] = ("Date: " + textDate.get() +" -- "+ "Nom: " + textName.get() +
                "\nTension: " + textTa.get())
    except FileNotFoundError as errorgraph1:
        print('+ Sorry the TA plot doesn\'t work ! Data missing !', errorgraph1)
        label['text'] = "Sorry the TA plot doesn\'t work ! Data missing !"

def appelPuls():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile2/puls.json'):
            subprocess.call('./param/aspifile2/aspipuls.py', shell=True)
            label['text'] = ("Date: " + textDate.get() +" -- "+ "Nom: " + textName.get() +
                "\nPulsations: " + textPuls.get())
    except FileNotFoundError as errorgraph2:
        print('+ Sorry the Puls plot doesn\'t work ! Data missing !', errorgraph2)
        label['text'] = "Sorry the Puls plot doesn\'t work ! Data missing !"

def appelSat():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile2/sat.json'):
            subprocess.call('./param/aspifile2/aspisat.py', shell=True)
            label['text'] = ("Date: " + textDate.get() +" -- "+ "Nom: " + textName.get() +
                "\nSaO2: " + textSa.get())
    except FileNotFoundError as errorgraph3:
        print('+ Sorry the SaO2 plot doesn\'t work ! Data missing !', errorgraph3)
        label['text'] = "Sorry the SaO2 plot doesn\'t work ! Data missing !"

def appelFreq():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile2/freq.json'):
            subprocess.call('./param/aspifile2/aspifreq.py', shell=True)
            label['text'] = ("Date: " + textDate.get() +" -- "+ "Nom: " + textName.get() +
                "\nFréqu. resp.: " + textFr.get())
    except FileNotFoundError as errorgraph4:
        print('+ Sorry the FR plot doesn\'t work ! Data missing !', errorgraph4)
        label['text'] = "Sorry the FR plot doesn\'t work ! Data missing !"

def appelTemp():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile2/temp.json'):
            subprocess.call('./param/aspifile2/aspitemp.py', shell=True)
            label['text'] = ("Date: " + textDate.get() +" -- "+ "Nom: " + textName.get() +
                "\nTempérature: " + textTemp.get())
    except FileNotFoundError as errorgraph5:
        print('+ Sorry the Temp plot doesn\'t work ! Data missing !', errorgraph5)
        label['text'] = "Sorry the Temp plot doesn\'t work ! Data missing !"

def appelGly():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile2/gly.json'):
            subprocess.call('./param/aspifile2/aspigly.py', shell=True)
            label['text'] = ("Date: " + textDate.get() +" -- "+ "Nom: " + textName.get() +
                "\nGlycémie: " + textHgt.get())
    except FileNotFoundError as errorgraph6:
        print('+ Sorry the Hgt plot doesn\'t work ! Data missing !', errorgraph6)
        label['text'] = "Sorry the Hgt plot doesn\'t work ! Data missing !"

def appelDlr():
    """
    to call aspidata.py for recapt data
    and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile2/dlr.json'):
            subprocess.call('./param/aspifile2/aspidlr.py', shell=True)
            label['text'] = ("Date: " + textDate.get() +" -- "+ "Nom: " + textName.get() +
                "\nDouleurs: " + textDlrs.get())
    except FileNotFoundError as errorgraph7:
        print('Sorry the Dlrs plot doesn\'t work ! Data missing !', errorgraph7)
        label['text'] = "Sorry the Dlrs plot doesn\'t work ! Data missing !"

def delMain():
    """
    To earase Main2.json
    """
    Main_MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will delete Main2.json with all data !!!")
    if Main_MsgBox == 'yes':
        try:
            if os.path.getsize('./param/Main2.json'):
                os.remove('./param/Main2.json')
                label['text'] = "File Main2.json has been deleted !"
                print("+ File Main2.json has been deleted !")
        except FileNotFoundError:
            label['text'] = "Sorry, file asked not exist !"
            print('+ Sorry, file asked not exist !')
    else:
        print("+ Nothing has changed !")
        label['text'] = "Nothing has changed !"

def delTA():
    """
    To earase tensor.json
    """
    try:
        if os.path.getsize('./param/aspifile2/tensor.json'):
            os.remove('./param/aspifile2/tensor.json')
            label['text'] = "File tensor.json has been deleted !"
            print("+ File tensor.json has been deleted !")
    except FileNotFoundError:
        label['text'] = "Sorry, file asked not exist !"
        print('+ Sorry, file asked not exist !')

def delPuls():
    """
    To earase puls.json
    """
    try:
        if os.path.getsize('./param/aspifile2/puls.json'):
            os.remove('./param/aspifile2/puls.json')
            label['text'] = "File puls.json has been deleted !"
            print("+ File puls.json has been deleted !")
    except FileNotFoundError:
        label['text'] = "Sorry, file asked not exist !"
        print("+ Sorry, file asked not exist !")

def delSat():
    """
    To earase sat.json
    """
    try:
        if os.path.getsize('./param/aspifile2/sat.json'):
            os.remove('./param/aspifile2/sat.json')
            label['text'] = "File sat.json has been deleted !"
            print("+ File sat.json has been deleted !")
    except FileNotFoundError:
        label['text'] = "Sorry, file asked not exist !"
        print('+ Sorry, file asked not exist !')

def delFreq():
    """
    To earase file
    """
    try:
        if os.path.getsize('./param/aspifile2/freq.json'):
            os.remove('./param/aspifile2/freq.json')
            label['text'] = "File freq.json has been deleted !"
            print("+ File freq.json has been deleted !")
    except FileNotFoundError:
        label['text'] = "Sorry, file asked not exist !"
        print('+ Sorry, file asked not exist !')

def delTemp():
    """
    To earase temp.json
    """
    try:
        if os.path.getsize('./param/aspifile2/temp.json'):
            os.remove('./param/aspifile2/temp.json')
            label['text'] = "File temp.json has been deleted !"
            print("+ File temp.json has been deleted !")
    except FileNotFoundError:
        label['text'] = "Sorry, file asked not exist !"
        print('+ Sorry, file asked not exist !')

def delGly():
    """
    To earase gly.json
    """
    try:
        if os.path.getsize('./param/aspifile2/gly.json'):
            os.remove('./param/aspifile2/gly.json')
            label['text'] = "File gly.json has been deleted !"
            print("+ File gly.json has been deleted !")
    except FileNotFoundError:
        label['text'] = "Sorry, file asked not exist !"
        print('+ Sorry, file asked not exist !')

def delDlr():
    """
    To earase dlr.json
    """
    try:
        if os.path.getsize('./param/aspifile2/dlr.json'):
            os.remove('./param/aspifile2/dlr.json')
            label['text'] = "File dlr.json has been deleted !"
            print("+ File dlr.json has been deleted !")
    except FileNotFoundError:
        label['text'] = "Sorry, file asked not exist !"
        print('+ Sorry, file asked not exist !')

def delEvery():
    """
    To delete all json files
    """
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will delete all files with all data !!!")
    if MsgBox == 'yes':
        delTA()
        delPuls()
        delSat()
        delFreq()
        delTemp()
        delGly()
        delDlr()
        label['text'] = "All json files have been deleted !"
        print("All json files have been deleted !")
    else:
        label['text'] = "Nothing has been deleted !"
        print("+ Nothing has been deleted !")

gui = Tk()
gui.title("Paramètres vitaux")
gui.configure(background='gray30')
gui.geometry('650x560')

# Labels
labelTitle = Label(gui, text="Paramètres Vitaux", font=('Times', 18), bg='gray30', fg='aquamarine')
labelTitle.grid(row=0, column=2)

label = Label(gui)
label = Label(text='Date :', font=('Times', 14), fg='aquamarine', bg='gray30', width=15)
label.grid(row=1, column=1)

label = Label(gui)
label = Label(text='Heure :', font=('Times', 14), fg='aquamarine', bg='gray30', width=15)
label.grid(row=2, column=1)

label1 = Label(gui)
label1 = Label(text='Entrer le Nom :', font=('Times', 14), fg='aquamarine', bg='gray30', width=15)
label1.grid(row=3, column=1)

label2 = Label(gui)
label2 = Label(text='Entrer la TA :', font=('Times', 14), fg='aquamarine', bg='gray30', width=15)
label2.grid(row=4, column=1)

label3 = Label(gui)
label3 = Label(text='Entrer les Puls :', font=('Times', 14), fg='aquamarine', bg='gray30', width=15)
label3.grid(row=5, column=1)

label4 = Label(gui)
label4 = Label(text='Entrer la SaO2 :', font=('Times', 14), fg='aquamarine', bg='gray30', width=15)
label4.grid(row=6, column=1)

label5 = Label(gui)
label5 = Label(text='Entrer la FR :', font=('Times', 14), fg='aquamarine', bg='gray30', width=15)
label5.grid(row=7, column=1)

label6 = Label(gui)
label6 = Label(text='Entrer la T°C :', font=('Times', 14), fg='aquamarine', bg='gray30', width=15)
label6.grid(row=8, column=1)

label7 = Label(gui)
label7 = Label(text='Entrer la Hgt :', font=('Times', 14), fg='aquamarine', bg='gray30', width=15)
label7.grid(row=9, column=1)

label8 = Label(gui)
label8 = Label(text='Eva des Dlrs :', font=('Times', 14), fg='aquamarine', bg='gray30', width=15)
label8.grid(row=10, column=1)

textDate = Entry(gui)
time_string = IntVar()
textDate = Entry(textvariable=time_string, highlightbackground='gray', bd=4)
time_string.set(time.strftime("%d/%m/%Y"))
textDate.grid(row=1, column=2)

textHour = Entry(gui)
time_Htring = IntVar()
textHour = Entry(textvariable=time_Htring, highlightbackground='gray', bd=4)
time_Htring.set(time.strftime("%H:%M:%S"))
textHour.grid(row=2, column=2)

textName = Entry(gui)
name_text = StringVar()
textName = Entry(textvariable=name_text, highlightbackground='gray', bd=4)
name_text.set("Nom du patient 2")
textName.grid(row=3, column=2)

# Entry
textTa = Entry(gui)
textTa = Entry(highlightbackground='gray', bd=4)
textTa.grid(row=4, column=2)

textPuls = Entry(gui)
textPuls = Entry(highlightbackground='gray', bd=4)
textPuls.grid(row=5, column=2)

textSa = Entry(gui)
textSa = Entry(highlightbackground='gray', bd=4)
textSa.grid(row=6, column=2)

textFr = Entry(gui)
textFr = Entry(highlightbackground='gray', bd=4)
textFr.grid(row=7, column=2)

textTemp = Entry(gui)
textTemp = Entry(highlightbackground='gray', bd=4)
textTemp.grid(row=8, column=2)

textHgt = Entry(gui)
textHgt = Entry(highlightbackground='gray', bd=4)
textHgt.grid(row=9, column=2)

textDlrs = Entry(gui)
textDlrs = Entry(highlightbackground='gray', bd=4)
textDlrs.grid(row=10, column=2)

button2Write = Button(gui)
button2Write.config(text='Quitter', width=15, bg='gray40', fg='aquamarine',
    activeforeground='red', command=quit)
button2Write.grid(row=1, column=3)

buttonDel = Button(gui)
buttonDel.config(text='Tout réinitialiser !!!', width=15, bg='gray40', fg='yellow',
    activeforeground='red', command=delEvery)
buttonDel.grid(row=1, column=4)

buttonWrite = Button(gui)
buttonWrite.config(text='Saisir les données', width=15, bg='gray40', fg='aquamarine',
    activebackground='dark turquoise', activeforeground='blue', command=writeData)
buttonWrite.grid(row=2, column=3)

buttonDel = Button(gui)
buttonDel.config(text='Supprimer Main2', width=15, bg='coral', fg='yellow',
    activeforeground='red', command=delMain)
buttonDel.grid(row=2, column=4)

# Buttons
button3Write = Button(gui)
button3Write.config(text='Graph TA', width=15, bg='lightblue', fg='blue2', command=appelTens)
button3Write.grid(row=4, column=3)

button4Write = Button(gui)
button4Write.config(text='Graph Puls', width=15, bg='lightblue', fg='blue2', command=appelPuls)
button4Write.grid(row=5, column=3)

button5Write = Button(gui)
button5Write.config(text='Graph SaO2', width=15, bg='lightblue', fg='blue2', command=appelSat)
button5Write.grid(row=6, column=3)

button6Write = Button(gui)
button6Write.config(text='Graph FR', width=15, bg='lightblue', fg='blue2', command=appelFreq)
button6Write.grid(row=7, column=3)

button7Write = Button(gui)
button7Write.config(text='Graph T°C', width=15, bg='lightblue', fg='blue2', command=appelTemp)
button7Write.grid(row=8, column=3)

button8Write = Button(gui)
button8Write.config(text='Graph Hgt', width=15, bg='lightblue', fg='blue2', command=appelGly)
button8Write.grid(row=9, column=3)

button9Write = Button(gui)
button9Write.config(text='Graph Dlrs', width=15, bg='lightblue', fg='blue2', command=appelDlr)
button9Write.grid(row=10, column=3)

button1Del = Button(gui)
button1Del.config(text='Supprimer TA', width=15, bg='coral', fg='yellow',
    activeforeground='blue2', command=delTA)
button1Del.grid(row=4, column=4)

button2Del = Button(gui)
button2Del.config(text='Supprimer Puls', width=15, bg='coral', fg='yellow',
    activeforeground='blue2', command=delPuls)
button2Del.grid(row=5, column=4)

button3Del = Button(gui)
button3Del.config(text='Supprimer SaO2', width=15, bg='coral', fg='yellow',
    activeforeground='blue2', command=delSat)
button3Del.grid(row=6, column=4)

button4Del = Button(gui)
button4Del.config(text='Supprimer FR', width=15, bg='coral', fg='yellow',
    activeforeground='blue2', command=delFreq)
button4Del.grid(row=7, column=4)

button5Del = Button(gui)
button5Del.config(text='Supprimer T°C', width=15, bg='coral', fg='yellow',
    activeforeground='blue2', command=delTemp)
button5Del.grid(row=8, column=4)

button6Del = Button(gui)
button6Del.config(text='Supprimer Hgt', width=15, bg='coral', fg='yellow',
    activeforeground='blue2', command=delGly)
button6Del.grid(row=9, column=4)

button7Del = Button(gui)
button7Del.config(text='Supprimer Dlrs', width=15, bg='coral', fg='yellow',
    activeforeground='blue2', command=delDlr)
button7Del.grid(row=10, column=4)

lower_frame = Frame(gui, bg='#88c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.65, relwidth=0.95, relheight=0.3, anchor='n')

label = Label(lower_frame, text=" ", font=('Times', 11), bg='white', anchor='nw', justify='left')
label.place(relwidth=1, relheight=1)

gui.mainloop()
