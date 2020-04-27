#!/usr/bin/python3
# -*-coding:Utf-8-*-

"""
with open('filetest.txt', 'r') as filetest:
    lines=filetest.readlines()
    for line in lines:
        print(lines)
        break
"""

# Loop to catch mot magic in line
motmagic="01/04/2020"
with open('filetest.txt', 'r') as filetest:
    lines=filetest.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        if motmagic in line:
            print(lines[i])
            print(lines[i+1])
            print(lines[i+2])
            break

# Only one line was fired...
motmagic="01/04/2020"
with open('filetest.txt', 'r') as filetest:
    lines=filetest.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        if not motmagic in line:
            print(line)
            if motmagic in line:
                print(line)
                break
               