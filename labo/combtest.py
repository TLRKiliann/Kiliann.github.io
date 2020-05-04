#!/usr/bin/python3
# -*-coding:utf-8-*-


from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox


app = tk.Tk()
app.title("Stix")
app.configure(bg='gray17')

def saveMyButt():
    MSB = messagebox.showinfo('Save', 'Data saved !')
    app.destroy()

ttk.Label(app, text="Stix", font=("Times 28 bold"), foreground='aquamarine',
    background='gray17').grid(row=0, column=0, columnspan=9)

# ttk.Label 
ttk.Label(app, text="pH :",
        font=("Times New Roman", 12), foreground='cyan', background='gray17',
        width=5).grid(column=1, row=1, padx=10)
  
n = tk.StringVar()
phchoosen = ttk.Combobox(app, width=5, textvariable = n)
  
# Adding ttk.combobox drop down list
phchoosen['values'] = (' 5', 
    ' 6', 
    ' 7', 
    ' 8', 
    ' 9') 
  
phchoosen.grid(row=2, column=1)
phchoosen.current(0)

ttk.Label(app, text="Leu :",  
        font=("Times New Roman", 12), foreground='cyan', background='gray17', width=5).grid(column=2,
        row=1, padx=10)

Leuco = tk.StringVar()
Leuchoosen = ttk.Combobox(app, width=5, textvariable = Leuco)
Leuchoosen['values'] = (' 0',
    ' +1', 
    ' +2', 
    ' +3') 
  
Leuchoosen.grid(row=2, column=2)
Leuchoosen.current(0)

ttk.Label(app, text="Nit :",  
        font=("Times New Roman", 12), foreground='cyan', background='gray17', width=5).grid(column=3,
        row=1, padx=10)

Nit = tk.StringVar()
Nitchoosen = ttk.Combobox(app, width=5, textvariable = Nit)
Nitchoosen['values'] = (' -', ' +')
  
Nitchoosen.grid(row=2, column=3)
Nitchoosen.current(0)

ttk.Label(app, text="Pro :",  
        font=("Times New Roman", 12), foreground='cyan', background='gray17', width=5).grid(column=4,
        row=1, padx=10)

Pro = tk.StringVar()
Prochoosen = ttk.Combobox(app, width=5, textvariable = Pro)
Prochoosen['values'] = (' neg', ' +1', ' +2', ' +3')
  
Prochoosen.grid(row=2, column=4)
Prochoosen.current(0)

ttk.Label(app, text="Glu :",  
        font=("Times New Roman", 12), foreground='cyan', background='gray17', width=5).grid(column=5,
        row=1, padx=10)

Glu = tk.StringVar()
Gluchoosen = ttk.Combobox(app, width=5, textvariable = Glu)
Gluchoosen['values'] = (' neg', ' +1', ' +2', ' +3', ' +4')
  
Gluchoosen.grid(row=2, column=5)
Gluchoosen.current(0)

ttk.Label(app, text="Ket :",  
        font=("Times New Roman", 12), foreground='cyan', background='gray17', width=5).grid(column=6,
        row=1, padx=10)

Ket = tk.StringVar()
Ketchoosen = ttk.Combobox(app, width=5, textvariable = Ket)
Ketchoosen['values'] = (' neg', ' +1', ' +2', ' +3')
  
Ketchoosen.grid(row=2, column=6)
Ketchoosen.current(0)

ttk.Label(app, text="Ery :",  
        font=("Times New Roman", 12), foreground='cyan', background='gray17', width=5).grid(column=7,
        row=1, padx=10)

Ery = tk.StringVar()
Erychoosen = ttk.Combobox(app, width=5, textvariable = Ery)

Erychoosen['values'] = (' neg',
    ' +1', 
    ' +2', 
    ' +3', 
    ' +4') 
  
Erychoosen.grid(row=2, column=7)
Erychoosen.current(0)

ttk.Label(app, text="Hb :",  
        font=("Times New Roman", 12), foreground='cyan', background='gray17', width=5).grid(column=8,
        row=1, padx=10)

Hb = tk.StringVar()
Hbchoosen = ttk.Combobox(app, width=5, textvariable = Hb)
  
# Adding ttk.combobox drop down list
Hbchoosen['values'] = (' neg',
    ' +1', 
    ' +2', 
    ' +3', 
    ' +4') 
  
Hbchoosen.grid(row=2, column=8)
Hbchoosen.current(0)

buttSave=Button(app, text='Save', width=8, fg='yellow', bg='navy', command=saveMyButt)
buttSave.grid(row=2, column=9, padx=10)

buttQuit=Button(app, text='Quit', width=8, fg='cyan', bg='gray30', command=quit)
buttQuit.grid(row=3, column=9, padx=10, pady=10)

app.mainloop()
