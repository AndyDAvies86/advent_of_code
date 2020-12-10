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
import anytree
import networkx

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2020day9.txt","r")
start = file.read()
startlist = start.split("\n")
startint = [int(x) for x in startlist]

file = open("2020day9test.txt","r")
startb = file.read()
testlist = startb.split("\n")
testint = [int(x) for x in testlist]

def nextdigitcheck(checklist,checkdigit):
    for i in range(0,25):
        for j in range(0,25):
            if i !=j:
                if checklist[i] + checklist[j] == checkdigit:
                    return 1
    return 0

def finderror(inputlist):
    for check in range (25,len(inputlist)):
       digitcheck = nextdigitcheck(inputlist[check-25:check],inputlist[check])
       if digitcheck == 0:
           return inputlist[check],check
    print("Error")
    
def solvepart2(inputlist):
    errordigit,errorpos = finderror(inputlist)
    for i in range(0,errorpos):
        for j in range(i,errorpos):
#            print(inputlist[i:j+1])
            if errordigit == sum(inputlist[i:j+1]):
                return (min(inputlist[i:j+1])+max(inputlist[i:j+1]))
    print("Error")
                    
                    