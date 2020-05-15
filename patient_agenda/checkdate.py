#!/usr/bin/python3
# -*- coding:utf-8 -*-


from tkinter import messagebox
import datetime


try:
    dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
    with open('./patient_agenda/events/doc_events/fix_agenda/read_file.py', 'r') as filedate:
        lines=filedate.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if dateagenda in line:
                MSB2 = messagebox.showinfo('Info', 'Look at AGENDA, there is a rdv to carry on for patient 1!')
            else:
                pass
except FileNotFoundError as infofile1:
    print("File 2 has not been found", infofile1)
else:
    ("Error unknow")

try:
    dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
    with open('./patient_agenda/events2/doc_events/fix_agenda/read_file.py', 'r') as filedate:
        lines=filedate.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if dateagenda in line:
                MSB2 = messagebox.showinfo('Info', 'Look at AGENDA, there is a rdv to carry on for patient 2!')
            else:
                pass
except FileNotFoundError as infofile2:
    print("File 2 has not been found", infofile2)
else:
    ("Error unknow")

try:
    dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
    with open('./patient_agenda/events3/doc_events/fix_agenda/read_file.py', 'r') as filedate:
        lines=filedate.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if dateagenda in line:
                MSB2 = messagebox.showinfo('Info', 'Look at AGENDA, there is a rdv to carry on for patient 3!')
            else:
                pass
except FileNotFoundError as infofile3:
    print("File 2 has not been found", infofile3)
else:
    ("Error unknow")

try:
    dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
    with open('./patient_agenda/events4/doc_events/fix_agenda/read_file.py', 'r') as filedate:
        lines=filedate.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if dateagenda in line:
                MSB2 = messagebox.showinfo('Info', 'Look at AGENDA, there is a rdv to carry on for patient 4!')
            else:
                pass
except FileNotFoundError as infofile4:
    print("File 2 has not been found", infofile4)
else:
    ("Error unknow")

try:
    dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
    with open('./patient_agenda/events5/doc_events/fix_agenda/read_file.py', 'r') as filedate:
        lines=filedate.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if dateagenda in line:
                MSB2 = messagebox.showinfo('Info', 'Look at AGENDA, there is a rdv to carry on for patient 5!')
            else:
                pass
except FileNotFoundError as infofile5:
    print("File 2 has not been found", infofile5)
else:
    ("Error unknow")

try:
    dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
    with open('./patient_agenda/events6/doc_events/fix_agenda/read_file.py', 'r') as filedate:
        lines=filedate.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if dateagenda in line:
                MSB2 = messagebox.showinfo('Info', 'Look at AGENDA, there is a rdv to carry on for patient 6!')
            else:
                pass
except FileNotFoundError as infofile6:
    print("File 2 has not been found", infofile6)
else:
    ("Error unknow")

try:
    dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
    with open('./patient_agenda/events7/doc_events/fix_agenda/read_file.py', 'r') as filedate:
        lines=filedate.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if dateagenda in line:
                MSB2 = messagebox.showinfo('Info', 'Look at AGENDA, there is a rdv to carry on for patient 7!')
            else:
                pass
except FileNotFoundError as infofile7:
    print("File 2 has not been found", infofile7)
else:
    ("Error unknow")
