#!/usr/bin/python3
# -*-coding:utf-8-*-


from tkinter import *
from tkinter import messagebox
import os
import subprocess
import platform


def sheetLabo():
    """
    For openning file at pdf 
    format with a bit prog-sys code.
    For Linux, Windows and MAC.
    """
    becall = platform.system()
    print(platform.system())
    
    if becall == 'Linux':
        os.system('gio open "./labo/labosheet.pdf"') # Linux
    elif becall =='Darwin':
        subprocess.call('open', './labo/labosheet.pdf' ) # Mac
    else:
        os.startfile('./labo/labosheet.pdf') # Windows
        
def printLabo():
    """
    Need to be modified in 
    function of platform's 
    user !!! Here, it's 
    for linux ! ;)
    """
    #lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
    #lpr.stdin.write('4.15.0-96-generic')
    pass

def recordTofile():
    MsgBox = messagebox.askyesno('Record', 'Do you want to save ?')

    if MsgBox == 1:
        print("Ok, data saved")
        recordOption()
        confRec()
        fen.destroy()
    else:
        messagebox.showinfo('Return', 'You will return to the application')

def recordOption():
    print("Date : " + time.strftime("%d/%m/%Y"))
    print("Nom du patient : ", entrytext.get())
    file=open('./labo/doc_labo/result.json', 'a+')
    file.write("Nom du patient : ")
    file.write(entrytext.get() + '\n')
    file.close()
    print(CheckVar1.get())
    if CheckVar1.get()==1:
        print("Surveillance respiratoire requise en ajout")
        file=open('./labo/doc_labo/result.json', 'a+')
        file.write("+ Surveillance respiratoire requise\n")
        file.close()
    else:
        print("Rien à faire")
        
    print(CheckVar2.get())
    if CheckVar2.get()==1:
        print("Surveillance de la température requise en ajout")
        file=open('./labo/doc_labo/result.json', 'a+')
        file.write("+ Surveillance de la température requise\n")
        file.close()
    else:
        print("Rien à faire")

    print(CheckVar3.get())
    if CheckVar3.get()==1:
        print("Surveillance alimentaire et/ou hydratation requise en ajout")
        file=open('./labo/doc_labo/result.json', 'a+')
        file.write("+ Surveillance alimentaire et/ou hydratation requise\n")
        file.close()
    else:
        print("Rien à faire")
        
def confRec():
    MsgBox2msg = messagebox.showinfo("Confirmation", "Record confirmed and finished !")


app = Tk()
app.title("Labo check")
app.configure(bg='gray17')

#label_fra = LabelFrame(app, text="Patient 1",
#    font=('Times 16'),bg='yellow', fg='red', height=2, bd=3)
   
labeltite=Label(app, text='Labo check', 
    font="Times 18 bold", width=10,
    height=3, bg='gray17', fg='aquamarine')
labeltite.grid(sticky='e', row=0, column=1, padx=10)

with open('./newpatient/entryfile.txt', 'r') as filename:
    line1 = filename.readline()
entrytext=StringVar()
entrytext.set(line1)
entryname=Entry(app, textvariable=entrytext, width=20)
entryname.grid(sticky='w', row=0, column=2)

# Electrolytes
labelresult=Label(app, text='--- Electrolytes ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='yellow')
labelresult.grid(sticky='w', row=1, column=0, columnspan=2)

CheckVar1 = IntVar()
C1 = Checkbutton(app, text="Na⁺", fg='navy', 
    bg='cyan', variable=CheckVar1, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C1.grid(sticky='w', row=2, column=0)

CheckVar2 = IntVar()
C2 = Checkbutton(app, text="K⁺", fg='navy', 
    bg='cyan', variable=CheckVar2, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C2.grid(sticky='w', row=3, column=0)

CheckVar3 = IntVar()
C3 = Checkbutton(app, text="Ca⁺ (total)", fg='navy', 
    bg='cyan', variable=CheckVar3, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C3.grid(sticky='w', row=2, column=1, padx=20)

CheckVar4 = IntVar()
C4 = Checkbutton(app, text="Mg⁺", fg='navy', 
    bg='cyan', variable=CheckVar4, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C4.grid(sticky='w', row=3, column=1, padx=20)

CheckVar43 = IntVar()
C43 = Checkbutton(app, text="Cl⁻", fg='navy', 
    bg='cyan', variable=CheckVar43, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C43.grid(sticky='w', row=4, column=1, padx=20)

CheckVar41 = IntVar()
C41 = Checkbutton(app, text="Phosphates (HPO4²⁻)", fg='navy', 
    bg='cyan', variable=CheckVar41, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C41.grid(sticky='w', row=4, column=0)

CheckVar42 = IntVar()
C42 = Checkbutton(app, text="Bicarbonates (HCO₃⁻)", fg='navy', 
    bg='cyan', variable=CheckVar42, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C42.grid(sticky='w', row=5, column=0)

# Cardio-vasc
labelcardio=Label(app, text='--- Cardiovascular ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='yellow')
labelcardio.grid(row=1, column=2, columnspan=2)

CheckVar44 = IntVar()
Cardia1 = Checkbutton(app, text="Cardiac workup", fg='navy', 
    bg='cyan', variable=CheckVar44, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Cardia1.grid(sticky='w', row=2, column=2)

CheckVar45 = IntVar()
Cardia2 = Checkbutton(app, text="CK-MB", fg='navy', 
    bg='cyan', variable=CheckVar45, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Cardia2.grid(sticky='w', row=3, column=2)

CheckVar46 = IntVar()
Cardia3 = Checkbutton(app, text="Troponin", fg='navy', 
    bg='cyan', variable=CheckVar46, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Cardia3.grid(sticky='w', row=4, column=2)

# second column
CheckVar47 = IntVar()
Cardia4 = Checkbutton(app, text="Lipid profile", fg='navy', 
    bg='cyan', variable=CheckVar47, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Cardia4.grid(sticky='w', row=2, column=3)

CheckVar48 = IntVar()
Cardia5 = Checkbutton(app, text="Cholesterol total", fg='navy', 
    bg='cyan', variable=CheckVar48, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Cardia5.grid(sticky='w', row=3, column=3)

CheckVar49 = IntVar()
Cardia6 = Checkbutton(app, text="HDL", fg='navy', 
    bg='cyan', variable=CheckVar49, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Cardia6.grid(sticky='w', row=4, column=3)

CheckVar50 = IntVar()
Cardia7 = Checkbutton(app, text="LDL", fg='navy', 
    bg='cyan', variable=CheckVar50, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Cardia7.grid(sticky='w', row=5, column=3)

CheckVar51 = IntVar()
Cardia8 = Checkbutton(app, text="Triglycerides", fg='navy', 
    bg='cyan', variable=CheckVar51, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Cardia8.grid(sticky='w', row=6, column=3)

# Hepatologia
labelresult2=Label(app, text='--- Hepathology ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='yellow')
labelresult2.grid(sticky='w', row=7, column=0, columnspan=2)

#separator = Label(app, height=5, bd=2, relief=SUNKEN)
#separator.grid(sticky='ns', row=2, column=1)

CheckVar5 = IntVar()
C5 = Checkbutton(app, text="ASAT", fg='navy', 
    bg='cyan', variable=CheckVar5, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C5.grid(sticky='w', row=8, column=0)

CheckVar6 = IntVar()
C6 = Checkbutton(app, text="ALAT", fg='navy', 
    bg='cyan', variable=CheckVar6, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C6.grid(sticky='w', row=9, column=0)

CheckVar7 = IntVar()
C7 = Checkbutton(app, text="Gamma-GT", fg='navy', 
    bg='cyan', variable=CheckVar7, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C7.grid(sticky='w', row=10, column=0)

CheckVar8 = IntVar()
C8 = Checkbutton(app, text="Alkaline phosphatase", fg='navy', 
    bg='cyan', variable=CheckVar8, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C8.grid(sticky='w', row=11, column=0)

CheckVar9 = IntVar()
C9 = Checkbutton(app, text="Bilirubin direct", fg='navy', 
    bg='cyan', variable=CheckVar9, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C9.grid(sticky='w', row=10, column=1, padx=20)

CheckVar10 = IntVar()
C10 = Checkbutton(app, text="Bilirubin indirecte", fg='navy', 
    bg='cyan', variable=CheckVar10, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C10.grid(sticky='w', row=11, column=1, padx=20)

CheckVar11 = IntVar()
C11 = Checkbutton(app, text="LDH", fg='navy', 
    bg='cyan', variable=CheckVar11, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C11.grid(sticky='w', row=8, column=1, padx=20)

CheckVar111 = IntVar()
C111 = Checkbutton(app, text="Uric acid", fg='navy', 
    bg='cyan', variable=CheckVar111, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C111.grid(sticky='w', row=9, column=1, padx=20)

# Coagulation
labelresult3=Label(app, text='--- Coagulation ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='yellow')
labelresult3.grid(row=7, column=2, columnspan=2)

CheckVar12 = IntVar()
C12 = Checkbutton(app, text="TP", fg='navy', 
    bg='cyan', variable=CheckVar12, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C12.grid(sticky='w', row=8, column=2)

CheckVar13 = IntVar()
C13 = Checkbutton(app, text="INR", fg='navy', 
    bg='cyan', variable=CheckVar13, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C13.grid(sticky='w', row=9, column=2)

# Glucids
labelgluco=Label(app, text='--- Carbohydrates ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='yellow')
labelgluco.grid(sticky='w', row=12, column=0, columnspan=2)

CheckVar60 = IntVar()
Gluco1 = Checkbutton(app, text="Fasting glucose", fg='navy', 
    bg='cyan', variable=CheckVar60, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Gluco1.grid(sticky='w', row=13, column=0)

CheckVar61 = IntVar()
Gluco2 = Checkbutton(app, text="Postprandial glucose", fg='navy', 
    bg='cyan', variable=CheckVar61, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Gluco2.grid(sticky='w', row=14, column=0)

CheckVar62 = IntVar()
Gluco3 = Checkbutton(app, text="HbA1c", fg='navy', 
    bg='cyan', variable=CheckVar62, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Gluco3.grid(sticky='w', row=15, column=0)

# Anemia
labelanemia=Label(app, text='--- Anemia ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='yellow')
labelanemia.grid(sticky='w', row=12, column=2, columnspan=2)

CheckVar70 = IntVar()
Anem1 = Checkbutton(app, text="Iron", fg='navy', 
    bg='cyan', variable=CheckVar70, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Anem1.grid(sticky='w', row=13, column=2)


CheckVar71 = IntVar()
Anem2 = Checkbutton(app, text="Ferritin", fg='navy', 
    bg='cyan', variable=CheckVar71, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Anem2.grid(sticky='w', row=14, column=2)

CheckVar72 = IntVar()
Anem3 = Checkbutton(app, text="Vitamin B12", fg='navy', 
    bg='cyan', variable=CheckVar72, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Anem3.grid(sticky='w', row=15, column=2)

CheckVar73 = IntVar()
Anem4 = Checkbutton(app, text="Folates (B9)", fg='navy', 
    bg='cyan', variable=CheckVar73, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Anem4.grid(sticky='w', row=16, column=2)

# Reins
labelinf=Label(app, text='--- Renal ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='yellow')
labelinf.grid(sticky='w', row=17, column=0, columnspan=2)

CheckVar80 = IntVar()
Ren1 = Checkbutton(app, text="Urea", fg='navy', 
    bg='cyan', variable=CheckVar80, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Ren1.grid(sticky='w', row=18, column=0)

CheckVar81 = IntVar()
Ren2 = Checkbutton(app, text="Creat.", fg='navy', 
    bg='cyan', variable=CheckVar81, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Ren2.grid(sticky='w', row=19, column=0)

# Inflammation
labelinf=Label(app, text='--- Inflammation ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='yellow')
labelinf.grid(sticky='w', row=17, column=2, columnspan=2)

CheckVar89 = IntVar()
Inf2 = Checkbutton(app, text="Sediment. velocity", fg='navy', 
    bg='cyan', variable=CheckVar89, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Inf2.grid(sticky='w', row=18, column=2)

CheckVar90 = IntVar()
Inf2 = Checkbutton(app, text="C-react. protein", fg='navy', 
    bg='cyan', variable=CheckVar90, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Inf2.grid(sticky='w', row=19, column=2)

CheckVar91 = IntVar()
Inf1 = Checkbutton(app, text="Albumina", fg='navy', 
    bg='cyan', variable=CheckVar91, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Inf1.grid(sticky='w', row=20, column=2)

CheckVar92 = IntVar()
Inf3 = Checkbutton(app, text="Cortisol", fg='navy', 
    bg='cyan', variable=CheckVar92, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Inf3.grid(sticky='w', row=21, column=2)

CheckVar93 = IntVar()
Inf4 = Checkbutton(app, text="ACTH", fg='navy', 
    bg='cyan', variable=CheckVar93, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
Inf4.grid(sticky='w', row=22, column=2)

# Buttons
buttonsheet=Button(app, text="Complete lab sheet", width=15,
    fg='yellow', bg='gray17', command=sheetLabo)
buttonsheet.grid(row=44, column=1,
    pady=10)

buttonsave=Button(app, text="Save", width=10,
    fg='yellow', bg='gray17', command=recordTofile)
buttonsave.grid(row=44, column=2, pady=10)

buttonquit=Button(app, text='Quit', width=10,
    fg='cyan', bg='gray17', command=quit)
buttonquit.grid(row=44, column=3,
    padx=5, pady=10)

#label_fra.grid(padx=10, pady=10)

app.mainloop()
