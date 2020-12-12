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

file = open("2016day3.txt","r")
start = file.read()
startlist = start.split("\n")
startint = [[int(row[2:5]),int(row[7:10]),int(row[12:15])] for row in startlist]

file = open("2016day3test.txt","r")
startb = file.read()
testlist = startb.split("\n")
testint = [[int(row[0:3]),int(row[4:7]),int(row[8:11])] for row in testlist]

def posstris(inputlist):
    countlist = [sum(row) > 2*max(row) for row in inputlist]
    return sum(countlist)

    
def posstris2(inputlist):
    newlist = []
    for i in range(0,len(inputlist),3):
        templist = inputlist[i:i+3]  
        for j in range(0,3):
            newlist.append([templist[0][j],templist[1][j],templist[2][j]])                
    countlist = [sum(row) > 2*max(row) for row in newlist]
    return sum(countlist)