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
except IndexError as inforange2:
    print("List 2 less than 6 lines", inforange2)
else:
    ("No problem identified for patient 1")

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
except FileNotFoundError as infofile1:
    print("File 2 has not been found", infofile1)
except IndexError as inforange2:
    print("List 2 less than 6 lines", inforange2)
else:
    ("No problem identified for patient 2")

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
except FileNotFoundError as infofile1:
    print("File 2 has not been found", infofile1)
except IndexError as inforange2:
    print("List 2 less than 6 lines", inforange2)
else:
    ("No problem identified for patient 3")

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
except FileNotFoundError as infofile1:
    print("File 2 has not been found", infofile1)
except IndexError as inforange2:
    print("List 2 less than 6 lines", inforange2)
else:
    ("No problem identified for patient 4")

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
except FileNotFoundError as infofile1:
    print("File 2 has not been found", infofile1)
except IndexError as inforange2:
    print("List 2 less than 6 lines", inforange2)
else:
    ("No problem identified for patient 5")

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
except FileNotFoundError as infofile1:
    print("File 2 has not been found", infofile1)
except IndexError as inforange2:
    print("List 2 less than 6 lines", inforange2)
else:
    ("No problem identified for patient 6")

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
except FileNotFoundError as infofile1:
    print("File 2 has not been found", infofile1)
except IndexError as inforange2:
    print("List 2 less than 6 lines", inforange2)
else:
    ("No problem identified for patient7")
