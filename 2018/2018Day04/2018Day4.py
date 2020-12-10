# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:46:13 2020

@author: Andy
"""



import pandas as pd
import numpy as np
import re
import datetime as dt

file = open("2018day4.txt","r")
start = file.read()
startlist = start.split("\n")

cleanlist = []
for word in startlist:
    activity = word[19:]
    moment = dt.datetime.strptime(word[1:17], '%Y-%m-%d %H:%M')
    newword = [moment, activity]
    cleanlist.append(newword)

sortedlist = sorted(cleanlist, key=lambda x: (x[0]))

        
deltaday = dt.timedelta(days=1)
deltamin = dt.timedelta(minutes=1)

guards = {}
guardnum=0
guardlist =[]
for word in sortedlist:
    if word[1][0:5] == "Guard":
        newword = word[1].split(" ")
        guardnum = newword[1].replace("#"," ")
        guards[guardnum] = 0
    outword=[word[0],word[1],guardnum]
    guardlist.append(outword)

fallasleep = []
wakesup = []
for word in guardlist:
    if word[1] == 'falls asleep':
        fallasleep.append([word[0],word[2]])
    if word[1] == 'wakes up':
        wakesup.append([word[0], word[2]])

for i in range (0,len(fallasleep)):
    time = int((wakesup[i][0]-fallasleep[i][0])/deltamin)
    guards[fallasleep[i][1]] += time

sleepyguard =  max(guards, key=guards.get)

sleepminute = {}
for i in range(0,60):
    sleepminute[i] = 0

for i in range (0,len(fallasleep)):
    if fallasleep[i][1] == sleepyguard:
        for j in range(fallasleep[i][0].minute,wakesup[i][0].minute):
            sleepminute[j] += 1

sleepyminute =  max(sleepminute, key=sleepminute.get)

print("Part 1: " + str(int(sleepyguard)*sleepyminute))


sleepminuteb = {}
for guard in list(guards.keys()):
    for i in range(0,60):
        sleepminuteb[(guard,i)] = 0


for i in range (0,len(fallasleep)):
    time = int((wakesup[i][0]-fallasleep[i][0])/deltamin)
    for j in range (0,time):
        sleepminuteb[(fallasleep[i][1],fallasleep[i][0].minute + j)] += 1

sleepyminuteb = max(sleepminuteb, key=sleepminuteb.get)
    
print("Part 2: " + str(int(sleepyminuteb[0])*sleepyminuteb[1]))   




"""
guard = {}b
for word in cleanlist:
    if word[3][0:5] == "Guard":
        manipword = word[3].split(" ")
        guardnum = int(manipword[1].replace("#", ""))
        guard[(int(word[0]),int(word[1]),int(word[2]))] = guardnum
"""        