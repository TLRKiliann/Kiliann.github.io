#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
import os


def get(Nompatient, entree):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to delete ?')
    if MsgBox == 1:
        Nompatient = entree.get()
        print(Nompatient)
        if os.path.getsize('./newpatient/entryfile.txt'):
            print("+ File 'entryfile.txt' exist !")
            with open('./newpatient/entryfile.txt', 'r') as file:
                lines = file.readlines()
            for i in range(len(lines)):
                line = lines[i]
                if Nompatient in line:
                    print(line)
                    delFuncFile()
                else:
                    pass
        else:
            print("+ Sorry, file 'entryfile.txt' not exist !")
            pass
        
        if os.path.getsize('./newpatient/entryfile2.txt'):
            print("+ File 'entryfile2.txt' exist !")
            with open('./newpatient/entryfile2.txt', 'r') as file:
                lines = file.readlines()
            for i in range(len(lines)):
                line = lines[i]
                if Nompatient in line:
                    print(line)
                    delFuncFile2()
                else:
                    pass
        else:
            print("+ Sorry, file 'entryfile2.txt' not exist !")
            pass

        if os.path.getsize('./newpatient/entryfile3.txt'):
            print("+ File 'entryfile3.txt' exist !")
            with open('./newpatient/entryfile3.txt', 'r') as file:
                lines = file.readlines()
            for i in range(len(lines)):
                line = lines[i]
                if Nompatient in line:
                    print(line)
                    delFuncFile3()
                else:
                    pass
        else:
            print("+ Sorry, file 'entryfile3.txt' not exist !")
            pass

        if os.path.getsize('./newpatient/entryfile4.txt'):
            print("+ File 'entryfile4.txt' exist !")
            with open('./newpatient/entryfile4.txt', 'r') as file:
                lines = file.readlines()
            for i in range(len(lines)):
                line = lines[i]
                if Nompatient in line:
                    print(line)
                    delFuncFile4()
                else:
                    pass
        else:
            print("+ Sorry, file 'entryfile4.txt' not exist !")
            pass

        if os.path.getsize('./newpatient/entryfile5.txt'):
            print("+ File 'entryfile5.txt' exist !")
            with open('./newpatient/entryfile5.txt', 'r') as file:
                lines = file.readlines()
            for i in range(len(lines)):
                line = lines[i]
                if Nompatient in line:
                    print(line)
                    delFuncFile5()
                else:
                    pass
        else:
            print("+ Sorry, file 'entryfile5.txt' not exist !")
            pass

        if os.path.getsize('./newpatient/entryfile6.txt'):
            print("+ File 'entryfile6.txt' exist !")
            with open('./newpatient/entryfile6.txt', 'r') as file:
                lines = file.readlines()
            for i in range(len(lines)):
                line = lines[i]
                if Nompatient in line:
                    print(line)
                    delFuncFile6()
                else:
                    pass
        else:
            print("+ Sorry, file 'entryfile.txt6' not exist !")
            pass

        if os.path.getsize('./newpatient/entryfile7.txt'):
            print("+ File 'entryfile7.txt' exist !")
            with open('./newpatient/entryfile7.txt', 'r') as file:
                lines = file.readlines()
            for i in range(len(lines)):
                line = lines[i]
                if Nompatient in line:
                    print(line)
                    delFuncFile7()
                else:
                    pass
        else:
            print("+ Sorry, file 'entryfile7.txt' not exist !")
            pass

        gui.destroy()
    else:           
        NoforQ = messagebox.showinfo('Return', 'None file was found !')

def delFuncFile():
    os.remove('./admin/readadmin/fileAdmin1.txt')
    os.remove('./14besoins/doc_suivi/main_14b.txt')
    os.remove('./14besoins/doc_suivi/patient1_14b.txt')
    os.remove('./ttt/doc_ttt/convdose.json')
    os.remove('./ttt/doc_ttt/intro_ttt.txt')
    os.remove('./param/aspifile/dlr.json')
    os.remove('./param/aspifile/freq.json')
    os.remove('./param/aspifile/gly.json')
    os.remove('./param/aspifile/puls.json')
    os.remove('./param/aspifile/sat.json')
    os.remove('./param/aspifile/temp.json')
    os.remove('./param/aspifile/tensor.json')
    os.remove('./param/Main.txt')
    os.remove('./calBmi/doc_BMI/file_bmi.json')
    os.remove('./calBmi/doc_BMI/file_kg.json')
    os.remove('./calBmi/bmi.txt')
    os.remove('./vmed/doc_vmed/resultvmed.txt')
    os.remove('./diag/doc_diag/diagrecap.txt')
    os.remove('./labo/doc_labo/result.txt')
    os.remove('./auxsrc/doc_auxsrc/auxsrcfile1.txt')
    os.remove('./histv/doc_histv/Hvie_patient1.txt')
    os.remove('./patient_agenda/events/doc_events/fix_agenda/fixed_rdv.txt')
    os.remove('./patient_agenda/events/doc_events/fix_agenda/modifrdv.txt')
    os.remove('./patient_agenda/events/doc_events/fix_agenda/patient_value.json')
    os.remove('./patient_agenda/events/doc_events/fix_agenda/patient_rdv.json')
    os.remove('./patient_agenda/events/doc_events/patient_calendar.txt')
    os.remove('./allergy/allergyfile.txt')
    os.remove('./newpatient/entryfile.txt')
    print("+ entryfile.txt found and delete with all files !")

def delFuncFile2():
    os.remove('./admin/readadmin/fileAdmin2.txt')
    os.remove('./14besoins/doc_suivi2/main_14b.txt')
    os.remove('./14besoins/doc_suivi2/patient2_14b.txt')
    os.remove('./ttt/doc_ttt2/convdose.json')
    os.remove('./ttt/doc_ttt2/intro_ttt.txt')
    os.remove('./param/aspifile2/dlr.json')
    os.remove('./param/aspifile2/freq.json')
    os.remove('./param/aspifile2/gly.json')
    os.remove('./param/aspifile2/puls.json')
    os.remove('./param/aspifile2/sat.json')
    os.remove('./param/aspifile2/temp.json')
    os.remove('./param/aspifile2/tensor.json')
    os.remove('./param/Main2.txt')
    os.remove('./calBmi/doc_BMI2/file_bmi.json')
    os.remove('./calBmi/doc_BMI2/file_kg.json')
    os.remove('./calBmi/bmi2.txt')
    os.remove('./vmed/doc_vmed2/resultvmed.txt')
    os.remove('./diag/doc_diag2/diagrecap.txt')
    os.remove('./labo/doc_labo/result2.txt')
    os.remove('./auxsrc/doc_auxsrc2/auxsrcfile2.txt')
    os.remove('./histv/doc_histv2/Hvie_patient2.txt')
    os.remove('./patient_agenda/events2/doc_events/fix_agenda/fixed_rdv.txt')
    os.remove('./patient_agenda/events2/doc_events/fix_agenda/modifrdv.txt')
    os.remove('./patient_agenda/events2/doc_events/fix_agenda/patient_value.json')
    os.remove('./patient_agenda/events2/doc_events/fix_agenda/patient_rdv.json')
    os.remove('./patient_agenda/events2/doc_events/patient_calendar.txt')
    os.remove('./allergy/allergyfile2.txt')
    os.remove('./newpatient/entryfile2.txt')
    print("+ entryfile2.txt found and has deleted all files !")

def delFuncFile3():
    os.remove('./admin/readadmin/fileAdmin3.txt')
    os.remove('./14besoins/doc_suivi3/main_14b.txt')
    os.remove('./14besoins/doc_suivi3/patient3_14b.txt')
    os.remove('./ttt/doc_ttt3/convdose.json')
    os.remove('./ttt/doc_ttt3/intro_ttt.txt')
    os.remove('./param/aspifile3/dlr.json')
    os.remove('./param/aspifile3/freq.json')
    os.remove('./param/aspifile3/gly.json')
    os.remove('./param/aspifile3/puls.json')
    os.remove('./param/aspifile3/sat.json')
    os.remove('./param/aspifile3/temp.json')
    os.remove('./param/aspifile3/tensor.json')
    os.remove('./param/Main3.txt')
    os.remove('./calBmi/doc_BMI3/file_bmi.json')
    os.remove('./calBmi/doc_BMI3/file_kg.json')
    os.remove('./calBmi/bmi3.txt')
    os.remove('./vmed/doc_vmed3/resultvmed.txt')
    os.remove('./diag/doc_diag3/diagrecap.txt')
    os.remove('./labo/doc_labo/result3.txt')
    os.remove('./auxsrc/doc_auxsrc3/auxsrcfile3.txt')
    os.remove('./histv/doc_histv3/Hvie_patient3.txt')
    os.remove('./patient_agenda/events3/doc_events/fix_agenda/fixed_rdv.txt')
    os.remove('./patient_agenda/events3/doc_events/fix_agenda/modifrdv.txt')
    os.remove('./patient_agenda/events3/doc_events/fix_agenda/patient_value.json')
    os.remove('./patient_agenda/events3/doc_events/fix_agenda/patient_rdv.json')
    os.remove('./patient_agenda/events3/doc_events/patient_calendar.txt')
    os.remove('./allergy/allergyfile3.txt')
    os.remove('./newpatient/entryfile3.txt')
    print("+ entryfile3.txt found and has deleted all files !")

def delFuncFile4():
    os.remove('./admin/readadmin/fileAdmin4.txt')
    os.remove('./14besoins/doc_suivi4/main_14b.txt')
    os.remove('./14besoins/doc_suivi4/patient4_14b.txt')
    os.remove('./ttt/doc_ttt4/convdose.json')
    os.remove('./ttt/doc_ttt4/intro_ttt.txt')
    os.remove('./param/aspifile4/dlr.json')
    os.remove('./param/aspifile4/freq.json')
    os.remove('./param/aspifile4/gly.json')
    os.remove('./param/aspifile4/puls.json')
    os.remove('./param/aspifile4/sat.json')
    os.remove('./param/aspifile4/temp.json')
    os.remove('./param/aspifile4/tensor.json')
    os.remove('./param/Main4.txt')
    os.remove('./calBmi/doc_BMI4/file_bmi.json')
    os.remove('./calBmi/doc_BMI4/file_kg.json')
    os.remove('./calBmi/bmi4.txt')
    os.remove('./vmed/doc_vmed4/resultvmed.txt')
    os.remove('./diag/doc_diag4/diagrecap.txt')
    os.remove('./labo/doc_labo/result4.txt')
    os.remove('./auxsrc/doc_auxsrc4/auxsrcfile4.txt')
    os.remove('./histv/doc_histv4/Hvie_patient4.txt')
    os.remove('./patient_agenda/events4/doc_events/fix_agenda/fixed_rdv.txt')
    os.remove('./patient_agenda/events4/doc_events/fix_agenda/modifrdv.txt')
    os.remove('./patient_agenda/events4/doc_events/fix_agenda/patient_value.json')
    os.remove('./patient_agenda/events4/doc_events/fix_agenda/patient_rdv.json')
    os.remove('./patient_agenda/events4/doc_events/patient_calendar.txt')
    os.remove('./allergy/allergyfile4.txt')
    os.remove('./newpatient/entryfile4.txt')
    print("+ entryfile4.txt found and has deleted all files !")

def delFuncFile5():
    os.remove('./admin/readadmin/fileAdmin5.txt')
    os.remove('./14besoins/doc_suivi5/main_14b.txt')
    os.remove('./14besoins/doc_suivi5/patient5_14b.txt')
    os.remove('./ttt/doc_ttt5/convdose.json')
    os.remove('./ttt/doc_ttt5/intro_ttt.txt')
    os.remove('./param/aspifile5/dlr.json')
    os.remove('./param/aspifile5/freq.json')
    os.remove('./param/aspifile5/gly.json')
    os.remove('./param/aspifile5/puls.json')
    os.remove('./param/aspifile5/sat.json')
    os.remove('./param/aspifile5/temp.json')
    os.remove('./param/aspifile5/tensor.json')
    os.remove('./param/Main5.txt')
    os.remove('./calBmi/doc_BMI5/file_bmi.json')
    os.remove('./calBmi/doc_BMI5/file_kg.json')
    os.remove('./calBmi/bmi5.txt')
    os.remove('./vmed/doc_vmed5/resultvmed.txt')
    os.remove('./diag/doc_diag5/diagrecap.txt')
    os.remove('./labo/doc_labo/result5.txt')
    os.remove('./auxsrc/doc_auxsrc5/auxsrcfile5.txt')
    os.remove('./histv/doc_histv5/Hvie_patient5.txt')
    os.remove('./patient_agenda/events5/doc_events/fix_agenda/fixed_rdv.txt')
    os.remove('./patient_agenda/events5/doc_events/fix_agenda/modifrdv.txt')
    os.remove('./patient_agenda/events5/doc_events/fix_agenda/patient_value.json')
    os.remove('./patient_agenda/events5/doc_events/fix_agenda/patient_rdv.json')
    os.remove('./patient_agenda/events5/doc_events/patient_calendar.txt')
    os.remove('./allergy/allergyfile5.txt')
    os.remove('./newpatient/entryfile5.txt')
    print("+ entryfile5.txt found and has deleted all files !")     

def delFuncFile6():
    os.remove('./admin/readadmin/fileAdmin6.txt')
    os.remove('./14besoins/doc_suivi6/main_14b.txt')
    os.remove('./14besoins/doc_suivi6/patient6_14b.txt')
    os.remove('./ttt/doc_ttt6/convdose.json')
    os.remove('./ttt/doc_ttt6/intro_ttt.txt')
    os.remove('./param/aspifile6/dlr.json')
    os.remove('./param/aspifile6/freq.json')
    os.remove('./param/aspifile6/gly.json')
    os.remove('./param/aspifile6/puls.json')
    os.remove('./param/aspifile6/sat.json')
    os.remove('./param/aspifile6/temp.json')
    os.remove('./param/aspifile6/tensor.json')
    os.remove('./param/Main6.txt')
    os.remove('./calBmi/doc_BMI6/file_bmi.json')
    os.remove('./calBmi/doc_BMI6/file_kg.json')
    os.remove('./calBmi/bmi6.txt')
    os.remove('./vmed/doc_vmed6/resultvmed.txt')
    os.remove('./diag/doc_diag6/diagrecap.txt')
    os.remove('./labo/doc_labo/result6.txt')
    os.remove('./auxsrc/doc_auxsrc6/auxsrcfile6.txt')
    os.remove('./histv/doc_histv6/Hvie_patient6.txt')
    os.remove('./patient_agenda/events6/doc_events/fix_agenda/fixed_rdv.txt')
    os.remove('./patient_agenda/events6/doc_events/fix_agenda/modifrdv.txt')
    os.remove('./patient_agenda/events6/doc_events/fix_agenda/patient_value.json')
    os.remove('./patient_agenda/events6/doc_events/fix_agenda/patient_rdv.json')
    os.remove('./patient_agenda/events6/doc_events/patient_calendar.txt')
    os.remove('./allergy/allergyfile6.txt')
    os.remove('./newpatient/entryfile6.txt')
    print("+ entryfile6.txt found and has deleted all files !")  

def delFuncFile7():
    os.remove('./admin/readadmin/fileAdmin7.txt')
    os.remove('./14besoins/doc_suivi7/main_14b.txt')
    os.remove('./14besoins/doc_suivi7/patient7_14b.txt')
    os.remove('./ttt/doc_ttt7/convdose.json')
    os.remove('./ttt/doc_ttt7/intro_ttt.txt')
    os.remove('./param/aspifile7/dlr.json')
    os.remove('./param/aspifile7/freq.json')
    os.remove('./param/aspifile7/gly.json')
    os.remove('./param/aspifile7/puls.json')
    os.remove('./param/aspifile7/sat.json')
    os.remove('./param/aspifile7/temp.json')
    os.remove('./param/aspifile7/tensor.json')
    os.remove('./param/Main7.txt')
    os.remove('./calBmi/doc_BMI7/file_bmi.json')
    os.remove('./calBmi/doc_BMI7/file_kg.json')
    os.remove('./calBmi/bmi7.txt')
    os.remove('./vmed/doc_vmed7/resultvmed.txt')
    os.remove('./diag/doc_diag7/diagrecap.txt')
    os.remove('./labo/doc_labo/result7.txt')
    os.remove('./auxsrc/doc_auxsrc7/auxsrcfile7.txt')
    os.remove('./histv/doc_histv7/Hvie_patient7.txt')
    os.remove('./patient_agenda/events7/doc_events/fix_agenda/fixed_rdv.txt')
    os.remove('./patient_agenda/events7/doc_events/fix_agenda/modifrdv.txt')
    os.remove('./patient_agenda/events7/doc_events/fix_agenda/patient_value.json')
    os.remove('./patient_agenda/events7/doc_events/fix_agenda/patient_rdv.json')
    os.remove('./patient_agenda/events7/doc_events/patient_calendar.txt')
    os.remove('./allergy/allergyfile7.txt')
    os.remove('./newpatient/entryfile7.txt')
    print("+ entryfile7.txt found and has deleted all files !")

gui=Tk()
gui.title("Enter new patient")
gui.configure(bg='gray17')
gui.geometry('300x200')

labelName = Label(gui)
labelName = Label(text='Enter Name to delete : ', font="Times 14 bold", 
    fg='cyan', bg='gray17')
labelName.pack(pady=10)

Nompatient=StringVar()
Nompatient.set('Firstname + Lastname')
entree = Entry(gui, textvariable=Nompatient, highlightbackground='gray', bd=4)
entree.pack()

bouton1 = Button(gui, text="Enter", width=8, fg='yellow', bg='navy',
    command = lambda: get(Nompatient, entree))
bouton1.pack(side=LEFT, padx=30, pady=10)

buttQuit=Button(gui, text="Quit", width=8, fg='cyan', bg='navy', 
    command=quit)
buttQuit.pack(side=LEFT, padx=15, pady=10)

gui.mainloop()
