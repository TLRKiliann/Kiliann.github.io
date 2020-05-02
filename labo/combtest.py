#!/usr/bin/python3
# -*-coding:utf-8-*-


from tkinter import *
import tkinter as tk 
from tkinter import ttk 


app = tk.Tk()
app.title("Stix")
app.configure(bg='gray17')


ttk.Label(app, text="Stix : ").grid(row=0, column=2)


# ttk.Label 
ttk.Label(app, text="pH :",
        font=("Times New Roman", 10), width=5).grid(column=1,
        row=1, padx=10)
  
n = tk.StringVar()
phchoosen = ttk.Combobox(app, width = 5, textvariable = n)
  
# Adding ttk.combobox drop down list
phchoosen['values'] = (' 0',
    ' 1', 
    ' 2', 
    ' 3', 
    ' 4', 
    ' 5',  
    ' 6',  
    ' 7',  
    ' 8',  
    ' 9',  
    ' 10') 
  
phchoosen.grid(row=2, column=1)
phchoosen.current(0)

ttk.Label(app, text="Leu :",  
        font=("Times New Roman", 10), width=5).grid(column=2,
        row=1, padx=10)

Leuco = tk.StringVar()
Leuchoosen = ttk.Combobox(app, width = 5, textvariable = Leuco)
Leuchoosen['values'] = (' 0',
    ' +1', 
    ' +2', 
    ' +3') 
  
Leuchoosen.grid(row=2, column=2)
Leuchoosen.current(0)

ttk.Label(app, text="Nit :",  
        font=("Times New Roman", 10), width=5).grid(column=3,
        row=1, padx=10)

Nit = tk.StringVar()
Nitchoosen = ttk.Combobox(app, width = 5, textvariable = Nit)
Nitchoosen['values'] = (' ', ' -', ' +')
  
Nitchoosen.grid(row=2, column=3)
Nitchoosen.current(0)

ttk.Label(app, text="Pro :",  
        font=("Times New Roman", 10), width=5).grid(column=4,
        row=1, padx=10)

Pro = tk.StringVar()
Prochoosen = ttk.Combobox(app, width = 5, textvariable = Pro)
Prochoosen['values'] = (' 0', ' +1', ' +2', ' +3')
  
Prochoosen.grid(row=2, column=4)
Prochoosen.current(0)

ttk.Label(app, text="Glu :",  
        font=("Times New Roman", 10), width=5).grid(column=5,
        row=1, padx=10)

Glu = tk.StringVar()
Gluchoosen = ttk.Combobox(app, width = 5, textvariable = Glu)
Gluchoosen['values'] = (' 0', ' +1', ' +2', ' +3')
  
Gluchoosen.grid(row=2, column=5)
Gluchoosen.current(0)

ttk.Label(app, text="Ket :",  
        font=("Times New Roman", 10), width=5).grid(column=6,
        row=1, padx=10)

Ket = tk.StringVar()
Ketchoosen = ttk.Combobox(app, width = 5, textvariable = Ket)
Ketchoosen['values'] = (' 0', ' +1', ' +2', ' +3')
  
Ketchoosen.grid(row=2, column=6)
Ketchoosen.current(0)

ttk.Label(app, text="Ubg :",  
        font=("Times New Roman", 10), width=5).grid(column=7,
        row=1, padx=10)

UBG = tk.StringVar()
UBGchoosen = ttk.Combobox(app, width = 5, textvariable = UBG)
UBGchoosen['values'] = (' 0', ' +1', ' +2', ' +3')
  
UBGchoosen.grid(row=2, column=7)
UBGchoosen.current(0)

ttk.Label(app, text="Bul :",  
        font=("Times New Roman", 10), width=5).grid(column=8,
        row=1, padx=10)

Bul = tk.StringVar()
Bulchoosen = ttk.Combobox(app, width = 5, textvariable = Bul)
  
# Adding ttk.combobox drop down list
Bulchoosen['values'] = (' 0',
    ' 1', 
    ' 2', 
    ' 3', 
    ' 4', 
    ' 5',  
    ' 6',  
    ' 7',  
    ' 8',  
    ' 9',  
    ' 10') 
  
Bulchoosen.grid(row=2, column=8)
Bulchoosen.current(0)

ttk.Label(app, text="Hb :",  
        font=("Times New Roman", 10), width=5).grid(column=9,
        row=1, padx=10)

Hb = tk.StringVar()
Hbchoosen = ttk.Combobox(app, width = 5, textvariable = Hb)
  
# Adding ttk.combobox drop down list
Hbchoosen['values'] = (' 0',
    ' 1', 
    ' 2', 
    ' 3', 
    ' 4', 
    ' 5',  
    ' 6',  
    ' 7',  
    ' 8',  
    ' 9',  
    ' 10') 
  
Hbchoosen.grid(row=2, column=9)
Hbchoosen.current(0)

ttk.Label(app, text="Ery :",  
        font=("Times New Roman", 10), width=5).grid(column=10,
        row=1, padx=10)

Ery = tk.StringVar()
Erychoosen = ttk.Combobox(app, width = 5, textvariable = Ery)

Erychoosen['values'] = (' 0',
    ' 1', 
    ' 2', 
    ' 3', 
    ' 4', 
    ' 5',  
    ' 6',  
    ' 7',  
    ' 8',  
    ' 9',  
    ' 10') 
  
Erychoosen.grid(row=2, column=10)
Erychoosen.current(0)

app.mainloop()
