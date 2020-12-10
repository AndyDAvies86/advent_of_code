# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:49:48 2020

@author: Andy
"""

import pandas as pd
import numpy as np
import re

file = open("2020day4.txt","r")
start = file.read()

startlist = start.split("\n\n")

cleanlist = []

for item in startlist:
    newliststr = item.replace("\n"," ")
    newlist = newliststr.split(" ")
    templist = []
    for row in newlist:
        newlistb = row.split(":")
        templist.append(newlistb)
    cleanlist.append(templist)


passdict =[]
for person in cleanlist:
    persondict={}
    for row in person:
        persondict[row[0]] = row[1]
    passdict.append(persondict)
    
keys = ['byr','iyr','eyr','hgt', 'hcl', 'ecl', 'pid']
count = 0
safedict =[]
for person in passdict:
    personcount = 0
    for value in keys:
        
        if person.get(value) != None:
            personcount = personcount + 1

        if personcount == 7:
            count = count + 1
            safedict.append(person)
        
print("Part 1:"+str(count))


regexcheck = {
        'byr' : "^19[2-9][0-9]|200[0-2]$",
        'iyr' : "^201[0-9]|2020$",
        'eyr' : "^202[0-9]|2030$",
        'hgt' : "^((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in)$",
        'hcl' : "^#[0-9a-fA-F]{6}$",
        'ecl' : "^amb|blu|brn|gry|grn|hzl|oth$",
        'pid' : "^[0-9]{9}$",
        'cid' : "."
        }

countb = 0
fail=[]
for person in passdict:
    personcount = 0
    for value in keys:
        if person.get(value) != None:
            tocheck = person.get(value)
            p = re.compile(regexcheck[value])      
            if p.match(tocheck) != None:
                personcount = personcount + 1
    if personcount == 7:
        countb = countb + 1
        
print("Part 2:"+str(countb))
