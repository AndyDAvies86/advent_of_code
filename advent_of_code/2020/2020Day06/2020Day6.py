# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 09:38:38 2020

@author: Andy
"""


import pandas as pd
import numpy as np
import re
import datetime as dt

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2020day6.txt","r")
start = file.read()
startlist = start.split("\n\n")


file = open("2020day6test.txt","r")
startb = file.read()
testlist = startb.split("\n\n")

def combinepeople(inlist):
    newlist =[]
    for row in inlist:
        cleanrow = row.replace('\n',"")
        newrow = ''
        for char in cleanrow:
            if char not in newrow:
                newrow = newrow + char
        newlist.append(newrow)
    return newlist

def sumcounts(inlist):
    score = 0
    for row in inlist:
        score = score + len(row)
    return score

print("Part 1: " + str(sumcounts(combinepeople(startlist))))

def splitpeople(inlist):
    newlist =[]
    for row in inlist:
        splitrow = row.split('\n')
        newlist.append(splitrow)
    return newlist

def ifallanswered(inlist):
    newlist =splitpeople(inlist)
    outlist = []
    for row in newlist:
        allans = alphabet
        for person in row:
            newans = ''        
            for char in person:
                if char in allans:
                    newans = newans + char
            allans = newans
#            print(newans)
        allans = newans
        outlist.append(allans)
    return outlist

print("Part 2: " + str(sumcounts(ifallanswered(startlist))))

splitstart = splitpeople(startlist)

allstartans = ifallanswered(startlist)

count = [len(x) for x in allstartans]

countrep = 0
for row in allstartans:
    test = ''.join(sorted(row))
    for i in range(0,len(test)-1) :
        if test[i] == test[i+1]:
            countrep += 1

    