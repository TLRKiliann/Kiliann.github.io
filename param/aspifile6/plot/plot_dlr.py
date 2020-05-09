#!/usr/bin/python3
# -*- coding:utf-8 -*-


import json
import matplotlib.pyplot as plt
import os


print("\nListe1 = dates :")
print("--------------")
fileO = open('./param/aspifile6/data_datedlr.json')
list1 = json.load(fileO)
#f.close

for letter in list1:
    print("list1: " + letter)

print("\nList2 = douleurs :")
print("--------------------")

fileO = open('./param/aspifile6/data_dlr.json')
list2 = json.load(fileO)
#f.close

for letter in list2:
    print("List2: " + letter)

dicolist = {}

for list1, list2 in zip(list1, list2):
    dicolist[list1] = list2

print("\nDictionnary display :")
print("---------------------------")
print(dicolist)

list1 = []
list2 = []

for key, value in dicolist.items():
    list1.append(key)
    list2.append(value)
    
print("\nList of date by entry's order :")
print("----------------------------------")
print(list1)
# How to sort data of list1 to correspond whith list2 ???
# And for list2 ??? Is it with array ??? 
print("\nList of pain evaluation :")
print("------------------------")
print(list2)

#list3 = [int(list2) for list2 in list2]
list2 = list(map(int, list2))

show_grid = True
with plt.style.context(('seaborn-darkgrid')):
    plt.plot(list1, list2)
    plt.ylabel('Dlrs')
    plt.xlabel('Dates')
    plt.title('Echelle de la Dlr/10 par date')
    plt.xticks(rotation=45)
    plt.grid(show_grid)
    plt.show()

os.remove('./param/aspifile6/data_datedlr.json')
print("+ File data_datedlr.json removed !")
os.remove('./param/aspifile6/data_dlr.json')
print("+ File data_dlr.json removed !\n")
