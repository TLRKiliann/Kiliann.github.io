#!/usr/bin/python3
#!-*-encoding:Utf-8-*-


from tkinter import *
import subprocess
import time
from tkinter import messagebox


#"1.0","end-1c"
def saveData():
    inputValue = textBox.get("1.0","end-1c")
    print(inputValue)
    file = open('./histv/doc_histv5/Hvie_patient5.txt', 'a+')
    file.write(textBox.get("1.0","end-1c") + "\n\n")
    file.close()

def messFromSafeButt():
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        saveData()
        textBox.insert(INSERT, "\n---Data saved !---")
        print("+ Data saved !")
    else:
        textBox.insert(INSERT, "Nothing has been saved !")
        print("+ Nothing has been saved !")

def lectureFic():
    subprocess.call('./histv/doc_histv5/story_read.py')

root=Tk()
root.title("Life story")
root.configure(background='gray17')

# To place side by side labelo + entrylab
top = Frame(root, bg='gray17')
bottom = Frame(root, bg='gray17')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(root, text="Life story of : ",
    font='Times 18 bold', fg='cyan', bg='gray17')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

labelallergy=Label(root, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='gray17')
labelallergy.pack(padx=5, pady=5)

# To read name in Entry widget
with open('./newpatient/entryfile5.txt', 'r') as filename:
    line1=filename.readline()

text_name=StringVar()
Entryname=Entry(root, textvariable=text_name)
text_name.set(line1)
Entryname.pack(in_=top, side=LEFT, padx=10, pady=20)

# To read allergy in Entry widget
with open('./allergy/allergyfile5.txt', 'r') as allerfile:
    lineA1=allerfile.readline()
    lineA2=allerfile.readline()
    lineA3=allerfile.readline()
    lineA4=allerfile.readline()
    lineA5=allerfile.readline()
    lineA6=allerfile.readline()
    lineA7=allerfile.readline()

text_aller=StringVar()
text_aller.set(lineA1 + ', ' + lineA3 + ', ' + lineA5 + ', ' + lineA7)
Entryaller=Entry(root, textvariable=text_aller, width=60)
Entryaller.pack(padx=10, pady=5)

textBox=Text(root, height=15, width=60, font=18, relief=SUNKEN)
textBox.insert(INSERT, "Dated : ")
textBox.insert(END, time.strftime("%d/%m/%Y at %H:%M:%S :\n"))
textBox.pack(padx=30, pady=30)

buttonLire=Button(root, text="Read", width=8, fg='cyan', bg='navy',
    activebackground='dark turquoise', activeforeground='navy',
    bd=3, highlightbackground='grey17', command=lectureFic)
buttonLire.pack(side='left', padx=10, pady=10)

buttonEnter=Button(root, text="Save", width=8, fg='yellow', bg='navy',
    activebackground='dark turquoise', activeforeground='navy',
    bd=3, highlightbackground='grey17', command=messFromSafeButt)
buttonEnter.pack(side='left', padx=10, pady=10)

buttonQuitter=Button(root, text="Quit", fg='white', bg='navy',
    width=8, activebackground='cyan', activeforeground='navy',
    bd=3, highlightbackground='grey17', command=quit)
buttonQuitter.pack(side='right', padx=10, pady=10)

mainloop()
