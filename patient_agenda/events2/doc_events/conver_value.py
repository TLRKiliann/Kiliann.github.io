#!/usr/bin/python3
# -*- coding:utf-8 -*-


import os
import json
import subprocess


file=open('./patient_agenda/events2/doc_events/patient2_rdv.json')
data=json.load(file)
file.close()

for value in data:
    print(value)

data_list1 = []
for value in data:
    data_list1.append(value[1])

dalaFa = data_list1[0]
dalaTrim = data_list1[1]
dalaPeste = data_list1[2]

lalala = "Rendez-vous set up for :"
final_data =  lalala+' '+str(dalaFa)+'/'+str(dalaTrim)+'/'+str(dalaPeste)
print(final_data)

try:
    if os.path.getsize('./patient_agenda/events2/doc_events/fix_agenda/patient_value.json'):
        print("+ File 'value' exist !")   
        with open('./patient_agenda/events2/doc_events/fix_agenda/patient_value.json','w') as partytime:
            json.dump(final_data, partytime)
except FileNotFoundError as msg:
    print("File doesn't exist, but it has been created !")
    with open('./patient_agenda/events2/doc_events/fix_agenda/patient_value.json','w') as partyleft:
    	json.dump(final_data, partyleft)

subprocess.call('./patient_agenda/events2/doc_events/fix_agenda/extend_agenda.py')
