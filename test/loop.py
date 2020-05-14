#!/usr/bin/python3
# -*-coding:Utf-8-*-

import os
import time
import datetime
import subprocess

try:
    datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
    with open('main_14b.txt', 'r') as filedate:
        lines=filedate.readlines()
        print(lines)
        for i in range(0, len(lines)):
            line = lines[i]
            if datesearch in line:
                print("\n\n---Patient2---\n")
                print(line)
                print(lines[i+1])
                print(lines[i+2])
                print(lines[i+3])
except FileNotFoundError as infousr2:
    print("File has not been found", infousr2)

try:
    datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
    with open('main_14b2.txt', 'r') as filedate:
        lines=filedate.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if datesearch in line:
                print("\n\n---Patient3---\n")
                print(line)
                print(lines[i+1])
                print(lines[i+2])
                print(lines[i+3])
            else:
                pass
except FileNotFoundError as infousr3:
    print("File has not been found", infousr3)
