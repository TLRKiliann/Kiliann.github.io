#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
import time
import shutil


# To backup all files
listeDate = ["30/05/2020", "01/06/2020", "01/07/2020",
"01/08/2020", "01/09/2020", "01/10/2020", "01/11/2020",
"01/12/2020"]

for i in listeDate:
    if time.strftime("%d/%m/%Y") == i:
        try:
            print("Backup of Main files !")
            shutil.copy('./param/Main.txt', './Backup/Files1/Backup_Mainparam.txt')
        except FileNotFoundError as outinfo:
            print("File Main.txt not found", outinfo)
            pass
        try:
            shutil.copy('./param/Main2.txt', './Backup/Files2/Backup_Mainparam2.txt')
        except FileNotFoundError as outinfo2:
            print("File Main2.txt not found", outinfo2)
            pass
        try:
            shutil.copy('./param/Main3.txt', './Backup/Files3/Backup_Mainparam3.txt')
        except FileNotFoundError as outinfo3:
            print("File Main3.txt not found", outinfo3)
            pass
        try:
            shutil.copy('./param/Main4.txt', './Backup/Files4/Backup_Mainparam4.txt')
        except FileNotFoundError as outinfo4:
            print("File Main4.txt not found", outinfo4)
            pass
        try:
            shutil.copy('./param/Main5.txt', './Backup/Files5/Backup_Mainparam5.txt')
        except FileNotFoundError as outinfo5:
            print("File Main5.txt not found", outinfo5)
            pass
        try:
            shutil.copy('./param/Main6.txt', './Backup/Files6/Backup_Mainparam6.txt')
        except FileNotFoundError as outinfo6:
            print("File Main6.txt not found", outinfo6)
            pass
        try:
            shutil.copy('./param/Main7.txt', './Backup/Files7/Backup_Mainparam7.txt')
        except FileNotFoundError as outinfo7:
            print("File Main7.txt not found", outinfo7)
            pass
        try:
            print("Backup of Bmi files !")
            shutil.copy('./calBmi/bmi.txt', './Backup/Files1/Backup_Bmi.txt')
        except FileNotFoundError as outinfo8:
            print("File bmi.txt not found", outinfo8)
            pass
        try:
            shutil.copy('./calBmi/bmi2.txt', './Backup/Files2/Backup_Bmi2.txt')
        except FileNotFoundError as outinfo9:
            print("File bmi2.txt not found", outinfo9)
            pass
        try:
            shutil.copy('./calBmi/bmi3.txt', './Backup/Files3/Backup_Bmi3.txt')
        except FileNotFoundError as outinfo10:
            print("File bmi3.txt not found", outinfo10)
            pass
        try:
            shutil.copy('./calBmi/bmi4.txt', './Backup/Files4/Backup_Bmi4.txt')
        except FileNotFoundError as outinfo11:
            print("File bmi4.txt not found", outinfo11)
            pass
        try:
            shutil.copy('./calBmi/bmi5.txt', './Backup/Files5/Backup_Bmi5.txt')
        except FileNotFoundError as outinfo12:
            print("File bmi5.txt not found", outinfo12)
            pass
        try:
            shutil.copy('./calBmi/bmi6.txt', './Backup/Files6/Backup_Bmi6.txt')
        except FileNotFoundError as outinfo13:
            print("File bmi6.txt not found", outinfo13)
            pass
        try:
            shutil.copy('./calBmi/bmi7.txt', './Backup/Files7/Backup_Bmi7.txt')
        except FileNotFoundError as outinfo14:
            print("File bmi7.txt not found", outinfo14)
            pass
        try:
            print("Backup of Treatments files !")
            shutil.copy('./ttt/doc_ttt/intro_ttt.txt', './Backup/Files1/Backup_ttt.txt')
        except FileNotFoundError as outinfo15:
            print("File intro_ttt.txt not found", outinfo15)
            pass
        try:
            shutil.copy('./ttt/doc_ttt2/intro_ttt.txt', './Backup/Files2/Backup_ttt2.txt')
        except FileNotFoundError as outinfo17:
            print("File intro_ttt2.txt not found", outinfo17)
            pass
        try:
            shutil.copy('./ttt/doc_ttt3/intro_ttt.txt', './Backup/Files3/Backup_ttt3.txt')
        except FileNotFoundError as outinfo18:
            print("File intro_ttt3.txt not found", outinfo18)
            pass
        try:
            shutil.copy('./ttt/doc_ttt4/intro_ttt.txt', './Backup/Files4/Backup_ttt4.txt')
        except FileNotFoundError as outinfo19:
            print("File intro_ttt4.txt not found", outinfo19)
            pass
        try:
            shutil.copy('./ttt/doc_ttt5/intro_ttt.txt', './Backup/Files5/Backup_ttt5.txt')
        except FileNotFoundError as outinfo20:
            print("File intro_ttt5.txt not found", outinfo20)
            pass
        try:
            shutil.copy('./ttt/doc_ttt6/intro_ttt.txt', './Backup/Files6/Backup_ttt6.txt')
        except FileNotFoundError as outinfo21:
            print("File intro_ttt6.txt not found", outinfo21)
            pass
        try:
            shutil.copy('./ttt/doc_ttt7/intro_ttt.txt', './Backup/Files7/Backup_ttt7.txt')
        except FileNotFoundError as outinfo22:
            print("File intro_ttt7.txt not found", outinfo22)
            pass
        try:
            print("Backup of Reserves files !")
            shutil.copy('./ttt/doc_ttt/intro_res.txt', './Backup/Files1/Backup_res.txt')
        except FileNotFoundError as outinfo23:
            print("File intro_res.txt not found", outinfo23)
            pass
        try:
            shutil.copy('./ttt/doc_ttt2/intro_res.txt', './Backup/Files2/Backup_res2.txt')
        except FileNotFoundError as outinfo24:
            print("File intro_res2.txt not found", outinfo24)
            pass
        try:
            shutil.copy('./ttt/doc_ttt3/intro_res.txt', './Backup/Files3/Backup_res3.txt')
        except FileNotFoundError as outinfo25:
            print("File intro_res3.txt not found", outinfo25)
            pass
        try:
            shutil.copy('./ttt/doc_ttt4/intro_res.txt', './Backup/Files4/Backup_res4.txt')
        except FileNotFoundError as outinfo26:
            print("File intro_res4.txt not found", outinfo26)
            pass
        try:
            shutil.copy('./ttt/doc_ttt5/intro_res.txt', './Backup/Files5/Backup_res5.txt')
        except FileNotFoundError as outinfo27:
            print("File intro_res5.txt not found", outinfo27)
            pass
        try:
            shutil.copy('./ttt/doc_ttt6/intro_res.txt', './Backup/Files6/Backup_res6.txt')
        except FileNotFoundError as outinfo28:
            print("File intro_res6.txt not found", outinfo28)
            pass
        try:
            shutil.copy('./ttt/doc_ttt7/intro_res.txt', './Backup/Files7/Backup_res7.txt')
        except FileNotFoundError as outinfo29:
            print("File intro_res7.txt not found", outinfo29)
            pass
        try:
            print("Backup of Diagnosis files !")
            shutil.copy('./diag/doc_diag/diagrecap.txt', './Backup/Files1/Backup_diag.txt')
        except FileNotFoundError as outinfo30:
            print("File diagrecap.txt not found", outinfo30)
            pass
        try:
            shutil.copy('./diag/doc_diag2/diagrecap.txt', './Backup/Files2/Backup_diag2.txt')
        except FileNotFoundError as outinfo31:
            print("File diagrecap2.txt not found", outinfo31)
            pass
        try:
            shutil.copy('./diag/doc_diag3/diagrecap.txt', './Backup/Files3/Backup_diag3.txt')
        except FileNotFoundError as outinfo32:
            print("File diagrecap3.txt not found", outinfo32)
            pass
        try:
            shutil.copy('./diag/doc_diag4/diagrecap.txt', './Backup/Files4/Backup_diag4.txt')
        except FileNotFoundError as outinfo33:
            print("File diagrecap4.txt not found", outinfo33)
            pass
        try:
            shutil.copy('./diag/doc_diag5/diagrecap.txt', './Backup/Files5/Backup_diag5.txt')
        except FileNotFoundError as outinfo34:
            print("File diagrecap5.txt not found", outinfo34)
            pass
        try:
            shutil.copy('./diag/doc_diag6/diagrecap.txt', './Backup/Files6/Backup_diag6.txt')
        except FileNotFoundError as outinfo35:
            print("File diagrecap6.txt not found", outinfo35)
            pass
        try:
            shutil.copy('./diag/doc_diag7/diagrecap.txt', './Backup/Files7/Backup_diag7.txt')
        except FileNotFoundError as outinfo36:
            print("File diagrecap7.txt not found", outinfo36)
            pass
        try:
            print("Backup of Visit Med files !")
            shutil.copy('./vmed/doc_vmed/resultvmed.txt', './Backup/Files1/Backupv_med.txt')
        except FileNotFoundError as outinfo37:
            print("File resultvmed.txt not found", outinfo37)
            pass
        try:
            shutil.copy('./vmed/doc_vmed2/resultvmed.txt', './Backup/Files2/Backupv_med2.txt')
        except FileNotFoundError as outinfo38:
            print("File resultvmed2.txt not found", outinfo38)
            pass
        try:
            shutil.copy('./vmed/doc_vmed3/resultvmed.txt', './Backup/Files3/Backupv_med3.txt')
        except FileNotFoundError as outinfo39:
            print("File resultvmed3.txt not found", outinfo39)
            pass
        try:
            shutil.copy('./vmed/doc_vmed4/resultvmed.txt', './Backup/Files4/Backupv_med4.txt')
        except FileNotFoundError as outinfo40:
            print("File resultvmed4.txt not found", outinfo40)
            pass
        try:
            shutil.copy('./vmed/doc_vmed5/resultvmed.txt', './Backup/Files5/Backupv_med5.txt')
        except FileNotFoundError as outinfo41:
            print("File resultvmed5.txt not found", outinfo41)
            pass
        try:
            shutil.copy('./vmed/doc_vmed6/resultvmed.txt', './Backup/Files6/Backupv_med6.txt')
        except FileNotFoundError as outinfo42:
            print("File resultvmed6.txt not found", outinfo42)
            pass
        try:
            shutil.copy('./vmed/doc_vmed7/resultvmed.txt', './Backup/Files7/Backupv_med7.txt')
        except FileNotFoundError as outinfo43:
            print("File resultvmed7.txt not found", outinfo43)
            pass
        try:
            print("Backup of Care and Monitoring files !")
            shutil.copy('./14besoins/doc_suivi/patient1_14b.txt', './Backup/Files1/Backup_careneeds.txt')
        except FileNotFoundError as outinfo44:
            print("File patient1_14b.txt not found", outinfo44)
            pass
        try:
            shutil.copy('./14besoins/doc_suivi2/patient2_14b.txt', './Backup/Files2/Backup_careneeds2.txt')
        except FileNotFoundError as outinfo45:
            print("File patient2_14b.txt not found", outinfo45)
            pass
        try:
            shutil.copy('./14besoins/doc_suivi3/patient3_14b.txt', './Backup/Files3/Backup_careneeds3.txt')
        except FileNotFoundError as outinfo46:
            print("File patient3_14b.txt not found", outinfo46)
            pass
        try:
            shutil.copy('./14besoins/doc_suivi4/patient4_14b.txt', './Backup/Files4/Backup_careneeds4.txt')
        except FileNotFoundError as outinfo47:
            print("File patient4_14b.txt not found", outinfo47)
            pass
        try:
            shutil.copy('./14besoins/doc_suivi5/patient5_14b.txt', './Backup/Files5/Backup_careneeds5.txt')
        except FileNotFoundError as outinfo48:
            print("File patient5_14b.txt not found", outinfo48)
            pass
        try:
            shutil.copy('./14besoins/doc_suivi6/patient6_14b.txt', './Backup/Files6/Backup_careneeds6.txt')
        except FileNotFoundError as outinfo49:
            print("File patient6_14b.txt not found", outinfo49)
            pass
        try:
            shutil.copy('./14besoins/doc_suivi7/patient7_14b.txt', './Backup/Files7/Backup_careneeds7.txt')
        except FileNotFoundError as outinfo50:
            print("File patient7_14b.txt not found", outinfo50)
            pass
        try:
            print("Backup of Aux. Res. files !")
            shutil.copy('./auxsrc/doc_auxsrc/auxsrcfile1.txt', './Backup/Files1/Backup_auxsrc.txt')
        except FileNotFoundError as outinfo51:
            print("File auxsrcfile1.txt not found", outinfo51)
            pass
        try:
            shutil.copy('./auxsrc/doc_auxsrc2/auxsrcfile2.txt', './Backup/Files2/Backup_auxsrc2.txt')
        except FileNotFoundError as outinfo52:
            print("File auxsrcfile2.txt not found", outinfo52)
            pass
        try:
            shutil.copy('./auxsrc/doc_auxsrc3/auxsrcfile3.txt', './Backup/Files3/Backup_auxsrc3.txt')
        except FileNotFoundError as outinfo53:
            print("File auxsrcfile3.txt not found", outinfo53)
            pass
        try:
            shutil.copy('./auxsrc/doc_auxsrc4/auxsrcfile4.txt', './Backup/Files4/Backup_auxsrc4.txt')
        except FileNotFoundError as outinfo54:
            print("File auxsrcfile4.txt not found", outinfo54)
            pass
        try:
            shutil.copy('./auxsrc/doc_auxsrc5/auxsrcfile5.txt', './Backup/Files5/Backup_auxsrc5.txt')
        except FileNotFoundError as outinfo55:
            print("File auxsrcfile5.txt not found", outinfo55)
            pass
        try:
            shutil.copy('./auxsrc/doc_auxsrc6/auxsrcfile6.txt', './Backup/Files6/Backup_auxsrc6.txt')
        except FileNotFoundError as outinfo56:
            print("File auxsrcfile6.txt not found", outinfo56)
            pass
        try:
            shutil.copy('./auxsrc/doc_auxsrc7/auxsrcfile7.txt', './Backup/Files7/Backup_auxsrc7.txt')
        except FileNotFoundError as outinfo57:
            print("File auxsrcfile7.txt not found", outinfo57)
            pass
        try:
            print("Backup of Story Life files !")
            shutil.copy('./histv/doc_histv/Hvie_patient1.txt', './Backup/Files1/Back_upstory.txt')
        except FileNotFoundError as outinfo58:
            print("File Hvie_patient1.txt not found", outinfo58)
            pass
        try:
            shutil.copy('./histv/doc_histv2/Hvie_patient1.txt', './Backup/Files2/Back_upstory2.txt')
        except FileNotFoundError as outinfo59:
            print("File Hvie_patient2.txt not found", outinfo59)
            pass
        try:
            shutil.copy('./histv/doc_histv3/Hvie_patient1.txt', './Backup/Files3/Back_upstory3.txt')
        except FileNotFoundError as outinfo60:
            print("File Hvie_patient3.txt not found", outinfo60)
            pass
        try:
            shutil.copy('./histv/doc_histv4/Hvie_patient1.txt', './Backup/Files4/Back_upstory4.txt')
        except FileNotFoundError as outinfo61:
            print("File Hvie_patient4.txt not found", outinfo61)
            pass
        try:
            shutil.copy('./histv/doc_histv5/Hvie_patient1.txt', './Backup/Files5/Back_upstory5.txt')
        except FileNotFoundError as outinfo62:
            print("File Hvie_patient5.txt not found", outinfo62)
            pass
        try:
            shutil.copy('./histv/doc_histv6/Hvie_patient1.txt', './Backup/Files6/Back_upstory6.txt')
        except FileNotFoundError as outinfo63:
            print("File Hvie_patient6.txt not found", outinfo63)
            pass
        try:
            shutil.copy('./histv/doc_histv7/Hvie_patient1.txt', './Backup/Files7/Back_upstory7.txt')
        except FileNotFoundError as outinfo64:
            print("File Hvie_patient7.txt not found", outinfo64)
            pass
        print("+ End of backup !")
    else:
        print("+ No backup has been made !")
        break
