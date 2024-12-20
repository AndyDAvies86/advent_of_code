# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:46:13 2020

@author: Andy
"""



import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2016day7.txt","r")
start = file.read()
startlist = start.split("\n")


file = open("2016day7test.txt","r")
startb = file.read()
testlist = startb.split("\n")

def cleanlist(inputlist):
    cleanlist = []
    for row in inputlist:
#        print(row)
        row = row.replace("[","]")
#        print(row)
        row = row.split("]")
#        print(row)
        cleanlist.append(row)
            
#        cleanlist.append([newrow[0],newrow[1][0],newrow[1][1]])
    return cleanlist

def abba(inputstring):
    check = False
    if len(inputstring) >= 4:
        for i in range(0,len(inputstring)-3):
            if inputstring[i] == inputstring[i+3] and inputstring[i+1] == inputstring[i+2] and inputstring[i] != inputstring[i+1]:
                check = True
    return check
    
def checkall(inputlist):
    splitlist = cleanlist(inputlist)
    count = 0
    for row in splitlist:
        abbacheck = [abba(x) for x in row]
        fail = False
        countind = 0
#        print(abbacheck)
        for i in range(1,len(row),2):
            if abbacheck[i]:
                fail = True
        if not fail:
            for i in range(0,len(row),2):
                if abbacheck[i]:
                    countind = 1
        count += countind
    return count
    

def aba(inputstring):
    abalist = []
    for i in range(0,len(inputstring)):
        for j in range(0,len(inputstring[i])-2):
            if inputstring[i][j] == inputstring[i][j+2] and inputstring[i][j] != inputstring[i][j+1]:
                abalist.append(inputstring[i][j:j+2])
    return abalist
        

def part2(inputlist):
    splitlist = cleanlist(inputlist)
    count = 0
    for row in splitlist:
        int_row = []
        out_row = []
        for i in range(0,len(row)):
            if i % 2 == 1:
                int_row.append(row[i])
            else:
                out_row.append(row[i])
        abaint = aba(int_row)
        abaout = aba(out_row)
        babint =  [x[::-1] for x in abaint]
        if len(set(babint).intersection(abaout)) > 0:
            count += 1
    return count
        
        