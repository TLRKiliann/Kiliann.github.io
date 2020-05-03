#!/usr/bin/python3
#!-*-encoding:Utf-8-*-


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import os
import json
import subprocess


def callbackDay(event):
    print(comboDay.get())

def callbackMonth(event):
    print(comboMonth.get())

def callbackYear(event):
    print(comboYear.get())

def callbackFinishDay(event):
    print(comboFinishDay.get())

def callbackFinishMonth(event):
    print(comboFinishMonth.get())

def callbackFinishYear(event):
    print(comboFinishYear.get())

def showTreat():
    subprocess.call('./ttt/doc_ttt7/tabs.py')

def copyFunc():
    """
    MessageBox to ensure if it's well done.
    """
    MsgBox = messagebox.askyesno('Record', 'Do you want to save ?')
    if MsgBox == 1:
        print("Ok ça passe")
        copyToFile()
        #app.destroy()
    else:
        messagebox.showinfo('Return', 'You will return to the application')

def deleteTreatment():
    """
    To earase one line in array
    for one entry
    """
    MSB = messagebox.askyesno('Delete ttt', 'Are you sure ?')
    if MSB == 1:
        print("Ok, ttt has been ejected !")
        messagebox.showinfo('info BOX', 'Treatment is away !')
        try:
            if os.path.getsize('./ttt/doc_ttt7/convdose.json'):
                print("+ File 'convdose' exist !")
                with open('./ttt/doc_ttt7/convdose.json', 'r') as datafile:
                    datastore = json.load(datafile)
                
                dataDose = datastore
                for key, value in dataDose.items():
                    if deleteTreat.get() == value[0]['Traitement']:
                        print(key)
                        print("value3c1", value[0]['Traitement'])
                        del value[0]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[1]['Traitement']:
                        print(key)
                        print("value3c2", value[1]['Traitement'])
                        del value[1]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[2]['Traitement']:
                        print(key)
                        print("value3c3", value[2]['Traitement'])
                        del value[2]
                        print("+ TTT earased !")
                    elif deleteTreat.get() == value[3]['Traitement']:
                        print(key)
                        print("value3c4", value[3]['Traitement'])
                        del value[3]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[4]['Traitement']:
                        print(key)
                        print("value3c4", value[4]['Traitement'])
                        del value[4]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[5]['Traitement']:
                        print(key)
                        print("value3c4", value[5]['Traitement'])
                        del value[5]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[6]['Traitement']:
                        print(key)
                        print("value3c4", value[6]['Traitement'])
                        del value[6]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[7]['Traitement']:
                        print(key)
                        print("value3c4", value[7]['Traitement'])
                        del value[7]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[8]['Traitement']:
                        print(key)
                        print("value3c4", value[8]['Traitement'])
                        del value[8]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[9]['Traitement']:
                        print(key)
                        print("value3c4", value[9]['Traitement'])
                        del value[9]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[10]['Traitement']:
                        print(key)
                        print("value3c4", value[10]['Traitement'])
                        del value[10]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[11]['Traitement']:
                        print(key)
                        print("value3c4", value[11]['Traitement'])
                        del value[11]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[12]['Traitement']:
                        print(key)
                        print("value3c4", value[12]['Traitement'])
                        del value[12]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[13]['Traitement']:
                        print(key)
                        print("value3c4", value[13]['Traitement'])
                        del value[13]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[14]['Traitement']:
                        print(key)
                        print("value3c4", value[14]['Traitement'])
                        del value[14]
                        print("+ TTT earased !")
                    else:
                        print("Treatment is not present into medication")

                    if deleteTreat.get() == '':
                        print("None treatment checked")
                    else:
                        print("---Ok VALEUR 'Traitement' entrée---")
                        with open('./ttt/doc_ttt7/convdose.json', 'w') as datafile2:
                            json.dump(dataDose, datafile2, indent=4)
        except FileNotFoundError as outcom:
            print('+ Sorry, file convdose.json not exist !', outcom)
    else:           
        NoforQ = messagebox.showinfo('Return', 'Treatment not earased')
def copyToFile():
    """
    To write all data to intro_ttt.json
    to reuse them after.
    """
    with open('./ttt/doc_ttt7/intro_ttt.txt', '+a') as file:
        file.write(str("Date : "))
        file.write(textDate.get() + '\n')
        file.write(str("Heure : "))
        file.write(textHour.get() + '\n')
        file.write(str("Name : "))
        file.write(textName.get() + '\n')
        file.write(str("Date of introduction : "))
        file.write(comboDay.get())
        file.write(comboMonth.get())
        file.write(comboYear.get())
        file.write(str('\n'))
        file.write(str("Nom du ttt : "))
        file.write(textTreat.get() + '\n')
        file.write(str("Dosage du ttt : "))
        file.write(textDosage.get() + '\n')
        if CheckVarMatin.get()==1:
            file.write(str("Matin : "))
        file.write(Entmatin.get() + '\n')
        if CheckVarMidi.get()==1:
            file.write(str("Midi : "))
        file.write(Entmidi.get() + '\n')
        if CheckVarSoir.get()==1:
            file.write(str("Soir : "))
        file.write(Entsoir.get() + '\n')
        if CheckVarNuit.get()==1:
            file.write(str("Nuit : "))
        file.write(Entnuit.get() + '\n')
        if CheckVar1.get()==1:
            file.write(str("Réserve : "))
            file.write(str("Oui\n"))
        if CheckVar2.get()==1:
            file.write(str("1ère intention : "))
            file.write(str("Oui\n"))
        if CheckVar3.get()==1:
            file.write(str("2ème intention : "))
            file.write(str("Oui\n"))
        if Rnbre.get()=='':
            print("Pas de réserves!")
        else:
            file.write(str("Nbre de réserve/24h : "))
            file.write(Rnbre.get() + '\n')
        file.write(str("Date of end : "))
        file.write(comboFinishDay.get())
        file.write(comboFinishMonth.get())
        file.write(comboFinishYear.get())
        file.write(str('\n'))
        file.write(str("Signature : "))
        file.write(textSign.get())
        file.write(str('\n\n'))

    try:
        if os.path.getsize('./ttt/doc_ttt7/convdose.json'):
            print("+ File 'convdose' exist !")
            with open('./ttt/doc_ttt7/convdose.json', 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataDose = datastore
            dataDose['data'].append({'Date' : textDate.get(),
                'Date of introduction' : comboDay.get() + comboMonth.get() +
                comboYear.get(), 'Date of end' : comboFinishDay.get() +
                comboFinishMonth.get() + comboFinishYear.get(),
                'Traitement' : textTreat.get(), 'Dosage' : textDosage.get(),
                'Matin' : Entmatin.get(), 'Midi' : Entmidi.get(),
                'Soir' : Entsoir.get(), 'Nuit' : Entnuit.get()})
            if textTreat.get() == "":
                print("---Pas de VALEUR 'Traitement' entrée---")
            else:
                print("---Ok VALEUR 'Traitement' entrée---")
                with open('./ttt/doc_ttt7/convdose.json', 'w') as datafile2:
                    json.dump(dataDose, datafile2, indent=4)
    except FileNotFoundError as outcom:
        print('+ Sorry, file convdose.json not exist !')
        print(str(outcom))
        print("+ File convdose.json created !")
        dataDose = {}
        dataDose['data'] = []
        dataDose['data'].append({'Date' : textDate.get(),
            'Date of introduction' : comboDay.get() + comboMonth.get() +
            comboYear.get(), 'Date of end' : comboFinishDay.get() +
            comboFinishMonth.get() + comboFinishYear.get(),
            'Traitement' : textTreat.get(), 'Dosage' : textDosage.get(),
            'Matin' : Entmatin.get(), 'Midi' : Entmidi.get(),
            'Soir' : Entsoir.get(), 'Nuit' : Entnuit.get()})
        if textTreat.get() == "":
            print("---Pas de VALEUR 'Traitement' entrée---")
        else:
            print("---Ok VALEUR 'Traitement' entrée---")
            with open('./ttt/doc_ttt7/convdose.json', 'w') as datafile:
                json.dump(dataDose, datafile, indent=4)

app = tk.Tk()
app.title("Introduction of treatement (ttt)")
app.configure(bg='gray17')

textLab = tk.Label(app, text="Introduction of treatement (ttt)",
    font=('Times 22 bold'), fg='aquamarine', bg='gray17')
textLab.grid(row=0, column=0, columnspan=3, pady=10)

labelallergy=tk.Label(app, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='gray17')
labelallergy.grid(row=1, column=0, columnspan=3)

# To read allergy for entry widget
with open('./allergy/allergyfile7.txt', 'r') as filename2:
    line1=filename2.readline()
    line2=filename2.readline()
    line3=filename2.readline()
    line4=filename2.readline()
    line5=filename2.readline()
    line6=filename2.readline()
    line7=filename2.readline()

entrytext=tk.StringVar()
entrytext.set(line1 + ', ' + line3 + ', ' + line5 + ', ' + line7)
entryName=tk.Entry(app, textvariable=entrytext, width=60)
entryName.grid(row=2, column=0, columnspan=3, pady=10)

LabDate = tk.Label(app, text="Date : ", width=20, font=12,
    fg='cyan', bg='gray17', anchor='e')
LabDate.grid(row=3, column=0)

LabHour = tk.Label(app, text="Hour : ", width=20, font=12,
    fg='cyan', bg='gray17', anchor='e')
LabHour.grid(row=4, column=0)

LabName = tk.Label(app, text="Patient's name : ", width=20, font=12,
    fg='cyan', bg='gray17', anchor='e')
LabName.grid(row=5, column=0)

LabTreat = tk.Label(app, text='Name of drug : ', width=20, 
    font=12, fg='cyan', bg='gray17', anchor='e')
LabTreat.grid(row=6, column=0)

LabDose = tk.Label(app, text="Dose : ", width=20, font=12,
    fg='cyan', bg='gray17', anchor='e')
LabDose.grid(row=7, column=0)

textDate = tk.Entry(app)
time_string = tk.IntVar()
textDate = tk.Entry(textvariable=time_string,
    highlightbackground='gray', bd=4)
time_string.set(time.strftime("%d/%m/%Y"))
textDate.grid(row=3, column=1)

textHour = tk.Entry(app)
time_Htring = tk.IntVar()
textHour = tk.Entry(textvariable=time_Htring,
    highlightbackground='gray', bd=4)
time_Htring.set(time.strftime("%H:%M:%S"))
textHour.grid(row=4, column=1)

# To read name of patient for entry widget
with open('./newpatient/entryfile.txt', 'r') as filename:
    line1=filename.readline()
    line2=filename.readline()
    line3=filename.readline()
    line4=filename.readline()
    line5=filename.readline()
    line6=filename.readline()
    line7=filename.readline()
    line8=filename.readline()
    line9=filename.readline()
    line10=filename.readline()
    line11=filename.readline()
    line12=filename.readline()
    line13=filename.readline()
    line14=filename.readline()
    line15=filename.readline()
    line16=filename.readline()
    line17=filename.readline()
    line18=filename.readline()
    line19=filename.readline()

textName = tk.Entry(app)
name_text = tk.StringVar()
textName = tk.Entry(textvariable=name_text,
    highlightbackground='gray', bd=4)
name_text.set(line19)
textName.grid(row=5, column=1)

textTreat = tk.Entry(app)
ttt_name = tk.StringVar()
textTreat = tk.Entry(textvariable=ttt_name,
    highlightbackground='gray', bd=4)
ttt_name.set("Drug")
textTreat.grid(row=6, column=1)

textDosage = tk.Entry(app)
tttDosage = tk.StringVar()
textDosage = tk.Entry(textvariable=tttDosage,
    highlightbackground='gray', bd=4)
tttDosage.set("mcg/ml/mg/UI/gttes")
textDosage.grid(row=7, column=1)

textDateS = tk.Label(app, text="Processing start date :", 
    font=('Arial 14 bold'), fg='aquamarine', bg='gray17', width=40, anchor='w')
textDateS.grid(row=8, column=0, columnspan=2, pady=10)

def changeDay():
    comboDay["values"] = ['01', '02', '03', '04',
                          '05', '06', '07', '08',
                          '09', '10', '11', '12',
                          '13', '14', '15', '15',
                          '16', '17', '18', '19',
                          '20', '21', '22', '23',
                          '24', '25', '26', '27',
                          '28', '29', '30', '31']

labelDay = tk.Label(app,
    text = "Choose the day :", font=12, fg='cyan', bg='gray17')
labelDay.grid(row=9, column=0)

comboDay = ttk.Combobox(app,
    values=['01', '02', '03', '04',
            '05', '06', '07', '08',
            '09', '10', '11', '12',
            '13', '14', '15', '15',
            '16', '17', '18', '19',
            '20', '21', '22', '23',
            '24', '25', '26', '27',
            '28', '29', '30', '31'], postcommand=changeDay)
comboDay.bind("<<ComboboxSelected>>", callbackDay)
comboDay.grid(row=10, column=0, pady=10)

def changeMonth():
    comboMonth["values"] = [' January',  
                          ' February', 
                          ' March', 
                          ' April', 
                          ' May', 
                          ' June', 
                          ' July', 
                          ' August', 
                          ' September', 
                          ' October', 
                          ' November', 
                          ' December']

labelMonth = tk.Label(app,
    text = "Choose the month :", font=12, fg='cyan', bg='gray17')
labelMonth.grid(row=9, column=1)

comboMonth = ttk.Combobox(app,
    values=[' January',  
          ' February', 
          ' March', 
          ' April', 
          ' May', 
          ' June', 
          ' July', 
          ' August', 
          ' September', 
          ' October', 
          ' November', 
          ' December'], postcommand=changeMonth)
comboMonth.bind("<<ComboboxSelected>>", callbackMonth)
comboMonth.grid(row=10, column=1, pady=10)

def changeYear():
    comboYear["values"] = [' 2000', ' 2001', ' 2002', ' 2003',
                          ' 2004', ' 2005', ' 2006', ' 2007',
                          ' 2008', ' 2009', ' 2010', ' 2011',
                          ' 2012', ' 2013', ' 2014', ' 2015',
                          ' 2016', ' 2017', ' 2018', ' 2019',
                          ' 2020', ' 2021', ' 2022', ' 2023',
                          ' 2024', ' 2025', ' 2026', ' 2027',
                          ' 2028', ' 2029', ' 2030', ' 2031',
                          ' 2032', ' 2033', ' 2034', ' 2035']

labelYear = tk.Label(app,
    text = "Choose the year :", font=12, fg='cyan', bg='gray17')
labelYear.grid(row=9, column=2)

comboYear = ttk.Combobox(app,
    values=[' 2000', ' 2001', ' 2002', ' 2003',
            ' 2004', ' 2005', ' 2006', ' 2007',
            ' 2008', ' 2009', ' 2010', ' 2011',
            ' 2012', ' 2013', ' 2014', ' 2015',
            ' 2016', ' 2017', ' 2018', ' 2019',
            ' 2020', ' 2021', ' 2022', ' 2023',
            ' 2024', ' 2025', ' 2026', ' 2027',
            ' 2028', ' 2029', ' 2030', ' 2031',
            ' 2032', ' 2033', ' 2034', ' 2035'], postcommand=changeYear)
comboYear.bind("<<ComboboxSelected>>", callbackYear)
comboYear.grid(row=10, column=2, pady=10)
comboYear.current(20)

# Date of finish
textDateF = tk.Label(app, text="Processing end date :", 
    font=('Arial 14 bold'), fg='aquamarine', bg='gray17', width=40, anchor='w')
textDateF.grid(row=11, column=0, columnspan=2, pady=10)

def finishDay():
    comboFinishDay["values"] = ['01', '02', '03', '04',
                                '05', '06', '07', '08',
                                '09', '10', '11', '12',
                                '13', '14', '15', '15',
                                '16', '17', '18', '19',
                                '20', '21', '22', '23',
                                '24', '25', '26', '27',
                                '28', '29', '30', '31']

labelFinishDay = tk.Label(app,
    text = "Choose the day :", font=12, fg='cyan', bg='gray17')
labelFinishDay.grid(row=12, column=0)

comboFinishDay = ttk.Combobox(app,
    values=['01', '02', '03', '04',
            '05', '06', '07', '08',
            '09', '10', '11', '12',
            '13', '14', '15', '15',
            '16', '17', '18', '19',
            '20', '21', '22', '23',
            '24', '25', '26', '27',
            '28', '29', '30', '31'], postcommand=finishDay)
comboFinishDay.bind("<<ComboboxSelected>>", callbackFinishDay)
comboFinishDay.grid(row=13, column=0, pady=10)

def finishMonth():
    comboFinishMonth["values"] = [' January',  
                          ' February', 
                          ' March', 
                          ' April', 
                          ' May', 
                          ' June', 
                          ' July', 
                          ' August', 
                          ' September', 
                          ' October', 
                          ' November', 
                          ' December']

labelMonth = tk.Label(app,
    text = "Choose the month :", font=12, fg='cyan', bg='gray17')
labelMonth.grid(row=12, column=1)

comboFinishMonth = ttk.Combobox(app,
    values=[' January',  
          ' February', 
          ' March', 
          ' April', 
          ' May', 
          ' June', 
          ' July', 
          ' August', 
          ' September', 
          ' October', 
          ' November', 
          ' December'], postcommand=finishMonth)
comboFinishMonth.bind("<<ComboboxSelected>>", callbackFinishMonth)
comboFinishMonth.grid(row=13, column=1, pady=10)

def finishYear():
    comboFinishYear["values"] = [' 2020', ' 2021', ' 2022', ' 2023',
                                 ' 2024', ' 2025', ' 2026', ' 2027',
                                 ' 2028', ' 2029', ' 2030', ' 2031',
                                 ' 2032', ' 2033', ' 2034', ' 2035']

labelFinishYear = tk.Label(app,
    text = "Choose the year :", font=12, fg='cyan', bg='gray17')
labelFinishYear.grid(row=12, column=2)

comboFinishYear = ttk.Combobox(app,
    values=[' 2020', ' 2021', ' 2022', ' 2023',
            ' 2024', ' 2025', ' 2026', ' 2027',
            ' 2028', ' 2029', ' 2030', ' 2031',
            ' 2032', ' 2033', ' 2034', ' 2035'], postcommand=finishYear)
comboFinishYear.bind("<<ComboboxSelected>>", callbackFinishYear)
comboFinishYear.grid(row=13, column=2, pady=10)
comboFinishYear.current(0)

checkLab = tk.Label(app, text="Doses :", font=('Arial 14 bold'), 
    fg='aquamarine', bg='gray17')
checkLab.grid(row=14, column=0, pady=10)

DosaLab = tk.Label(app, text="Unity :", font=('Arial 14 bold'), 
    fg='aquamarine', bg='gray17')
DosaLab.grid(row=14, column=2, pady=10)

# CheckBox
CheckVarMatin = tk.IntVar()
Cma = tk.Checkbutton(app, text="Morning --->", fg='navy', 
    bg='cyan', variable=CheckVarMatin, 
    onvalue=1, offvalue=0, height=1, 
    width=15, anchor='w')
Cma.grid(row=16, column=0)

LabDose = tk.Label(app, text='Morning dose : ', font=12,
    width=20, fg='cyan', bg='gray17')
LabDose.grid(row=16, column=1)

Entmatin = tk.Entry(app)
Entmatin = tk.Entry(highlightbackground='gray', bd=4)
Entmatin.grid(row=16, column=2)

CheckVarMidi = tk.IntVar()
Cmi = tk.Checkbutton(app, text="Noon --->", fg='navy', 
    bg='cyan', variable=CheckVarMidi, 
    onvalue=1, offvalue=0, height=1, 
    width=15, anchor='w')
Cmi.grid(row=17, column=0)

LabDose = tk.Label(app, text='Take of noon : ', font=12, 
    width=20, fg='cyan', bg='gray17')
LabDose.grid(row=17, column=1)

Entmidi = tk.Entry(app)
Entmidi = tk.Entry(highlightbackground='gray', bd=4)
Entmidi.grid(row=17, column=2)

CheckVarSoir = tk.IntVar()
Csoir = tk.Checkbutton(app, text="Evening --->", fg='navy', 
    bg='cyan', variable=CheckVarSoir, 
    onvalue=1, offvalue=0, height=1, 
    width=15, anchor='w')
Csoir.grid(row=18, column=0)

LabDose = tk.Label(app, text='Evening outlet : ', font=12,
    width=20, fg='cyan', bg='gray17')
LabDose.grid(row=18, column=1)

Entsoir = tk.Entry(app)
Entsoir = tk.Entry(highlightbackground='gray', bd=4)
Entsoir.grid(row=18, column=2)

CheckVarNuit = tk.IntVar()
Cnuit = tk.Checkbutton(app, text="Night --->", fg='navy', 
    bg='cyan', variable=CheckVarNuit, 
    onvalue=1, offvalue=0, height=1, 
    width=15, anchor='w')
Cnuit.grid(row=19, column=0)

# Entry nbre de x/24h
LabDose = tk.Label(app, text='Take of night : ', font=12,
    width=20, fg='cyan', bg='gray17')
LabDose.grid(row=19, column=1)

Entnuit = tk.Entry(app)
Entnuit = tk.Entry(highlightbackground='gray', bd=4)
Entnuit.grid(row=19, column=2)

CheckVar1 = tk.IntVar()
C1 = tk.Checkbutton(app, text="Reserve", fg='navy', 
    bg='pale green', variable=CheckVar1, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor='w')
C1.grid(row=20, column=0, pady=10)

CheckVar2 = tk.IntVar()
C2 = tk.Checkbutton(app, text="First-line", fg='navy', 
    bg='pale green', variable=CheckVar2, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor='w')
C2.grid(row=20, column=1, pady=10)

CheckVar3 = tk.IntVar()
C3 = tk.Checkbutton(app, text="Second-line", fg='navy', 
    bg='pale green', variable=CheckVar3, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor='w')
C3.grid(row=20, column=2, pady=10)

LabelR = tk.Label(app, text='Number of R/24h : ', font=12, 
    width=20, fg='cyan', bg='gray17')
LabelR.grid(row=21, column=1)

Rnbre = tk.Entry(app)
Rnbre = tk.Entry(highlightbackground='gray', bd=4)
Rnbre.grid(row=21, column=2)

buttStopttt = tk.Button(app, text="Stop ttt", width=10, fg='yellow',
    bg='red', bd=4, command=deleteTreatment)
buttStopttt.grid(row=23, column=0)

deleteTreat = tk.Entry(app)
delete_text = tk.StringVar()
delete_text.set("Enter name of ttt")
deleteTreat = tk.Entry(textvariable=delete_text,
    highlightbackground='red', bd=4)
deleteTreat.grid(row=21, column=0)

LabSign = tk.Label(app, text='Signature :', font=12, 
    width=15, fg='red', bg='pale green')
LabSign.grid(row=23, column=1, pady=10)

textSign = tk.Entry(app)
textSign = tk.Entry(highlightbackground='gray', bd=4)
textSign.grid(row=23, column=2, pady=10)

# Buttons with functions
buttShowttt = tk.Button(app, text="Show ttt", width=10, fg='yellow',
    bg='gray30', bd=4, command=showTreat)
buttShowttt.grid(row=24, column=0, pady=10)

buttCopy = tk.Button(app, text="Save", width=10, fg='yellow',
    bg='gray30', bd=4, command=copyFunc)
buttCopy.grid(row=24, column=1, pady=10)

buttQuit = tk.Button(app, text="Quit", width=10, fg='cyan',
    bg='gray30', bd=4, command=quit)
buttQuit.grid(row=24, column=2, pady=10)

app.mainloop()
