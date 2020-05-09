#!/usr/bin/python3
# -*- coding:utf-8 -*-


import subprocess
import json


file = open('./param/aspifile7/gly.json')
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
    print("Glycemie: " + str(value[0]["Glycemie"]))
    print("\n")
    print("Date: " + str(value[1]["Date"]))
    print("Glycemie: " + str(value[1]["Glycemie"]))
    
print("\nList of dates\n")

data_list1 = []
for value in zip(value):
    data_list1.append(value[0]['Date'])
    print(value[0]['Date'])

print("\nThat seems ok!\n")

with open('./param/aspifile7/data_dategly.json', 'a+') as datafile:
    json.dump(data_list1, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList of glycemia\n")

data_list2 = []
for value in zip(value):
    data_list2.append(value[0]['Glycemie'])
    print(value[0]['Glycemie'])

print("\nThat seems correct!\n")

with open('./param/aspifile7/data_gly.json', 'a+') as datafile:
    json.dump(data_list2, datafile, indent=4)

print("\nDownloading 'plot_prog.py'...")

subprocess.call('./param/aspifile7/plot/plot_gly.py')
