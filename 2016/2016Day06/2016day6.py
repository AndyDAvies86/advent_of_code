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
import hashlib

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2016day6.txt","r")
start = file.read()
startlist = start.split("\n")


file = open("2016day6test.txt","r")
startb = file.read()
testlist = startb.split("\n")

def colcount(inputlist):
    cols = ['' for x in range(0,len(inputlist[0]))]
    for row in inputlist:
        cols = [cols[x] + row[x] for x in range(0,len(inputlist[0]))]
#    print(cols)
    word =''
    for row in cols:
        maxcount = 0
        maxletter = ''
        for char in alphabet:
            if row.count(char) > maxcount:
                maxcount = row.count(char)
                maxletter=char
        word += maxletter
        print(word)
    

def colcount2(inputlist):
    cols = ['' for x in range(0,len(inputlist[0]))]
    for row in inputlist:
        cols = [cols[x] + row[x] for x in range(0,len(inputlist[0]))]
#    print(cols)
    word =''
    for row in cols:
        maxcount = 9999999
        maxletter = ''
        for char in alphabet:
            if 0 < row.count(char) < maxcount:
                maxcount = row.count(char)
                maxletter=char
        word += maxletter
        print(word)
    
