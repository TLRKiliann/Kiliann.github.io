#!/usr/bin/python3
# -*- coding:utf-8 -*-


import subprocess
import json


file = open('./param/aspifile/dlr.json')
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
    print("Douleurs: " + str(value[0]["Douleurs"]))
    print("\n")
    print("Date: " + str(value[1]["Date"]))
    print("Douleurs: " + str(value[1]["Douleurs"]))
    
print("\nList of dates\n")

data_list1 = []
for value in zip(value):
    data_list1.append(value[0]['Date'])
    print(value[0]['Date'])

print("\nThat seems ok!\n")

with open('./param/aspifile/data_datedlr.json', 'a+') as datafile:
    json.dump(data_list1, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList of pain\n")

data_list2 = []
for value in zip(value):
    data_list2.append(value[0]['Douleurs'])
    print(value[0]['Douleurs'])

print("\nThat seems correct!\n")

with open('./param/aspifile/data_dlr.json', 'a+') as datafile:
    json.dump(data_list2, datafile, indent=4)

print("\nDownloading 'plot_prog.py'...")

subprocess.call('./param/aspifile/plot/plot_dlr.py')
