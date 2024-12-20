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

file = open("2016day4.txt","r")
start = file.read()
startlist = start.split("\n")


file = open("2016day4test.txt","r")
startb = file.read()
testlist = startb.split("\n")

def cleanlist(inputlist):
    splitlist = [row.split("-") for row in inputlist]    
    cleanedlist = []
    for row in splitlist:
        newrow = [''.join(row[:-1])]+row[-1].replace(']','').split('[')
        cleanedlist.append(newrow)
    return cleanedlist

def createhash(inputlist):
    countlist = []
    for char in alphabet:
#        print(row[0],char,row[0].count(char))
        countlist.append([-(inputlist[0].count(char)),char])
#    print(countlist)
    countlist.sort()
#    print(countlist)
    hashout = ''.join([row[1] for row in countlist[0:5]])
    return hashout

def checkrooms(inputlist):
    cleanedlist=cleanlist(inputlist)
    idsum = 0
    newlist = []
    for row in cleanedlist:
#        print(row,createhash(row))
        if row[2] == createhash(row):
            idsum += int(row[1])
            newlist.append(row)
#            print(idsum)
    return idsum,newlist


def crack(inputlist):
    shortlist = checkrooms(inputlist)[1]
#    shortlist = cleanlist(inputlist)
#    spincypher = deque(alphabet)
    for row in shortlist:
        decrypt = ''
        for char in row[0]:
#            (((ord(char)-96)+int(row[1])) % 26) + 96)
            decrypt += chr(((ord(char)+int(row[1])-97) % 26) + 97)            
#        print(decrypt)
        if 'pole' in decrypt:
            return row[1]
            
            
