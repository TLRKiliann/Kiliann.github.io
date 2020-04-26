#!/usr/bin/python3
# -*- coding:utf-8 -*-


import os
import json
import time


file = open('./param/aspifile4/puls.json')
data = json.load(file)
#file.close

for (key, value) in data.items():
    print("Key: " + key)
    print("Valeur: " + str(value))
    print("\nTo represent the data_get:\n")
    print(data.get("data"))
    print("\n")
    print("Valeur: " + str(value[0]))
    print("Valeur: " + str(value[1]))
    print("\n")
    print("Date: " + str(value[0]["Date"]))
    print("Puls: " + str(value[0]["Puls"]))
    print("\n")
    print("Date: " + str(value[1]["Date"]))
    print("Puls: " + str(value[1]["Puls"]))
    
print("\nList of dates\n")

data_list1 = []
for value in zip(value):
    data_list1.append(value[0]['Date'])
    print(value[0]['Date'])

print("\nThat seems ok!\n")

with open('./param/aspifile4/data_datepuls.json', 'a+') as datafile:
    json.dump(data_list1, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList of puls\n")

data_list2 = []
for value in zip(value):
    data_list2.append(value[0]['Puls'])
    print(value[0]['Puls'])

print("\nThat seems correct!\n")

with open('./param/aspifile4/data_puls.json', 'a+') as datafile:
    json.dump(data_list2, datafile, indent=4)

print("\nDownloading 'plot_prog.py'...")
# Un temps d'attente de 2 sec:
print("Time wait 2 seconds...")
time.sleep(2)
# Lancement du programme plot_puls.py
os.system('./param/aspifile4/plot/plot_puls.py')
