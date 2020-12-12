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

file = open("2016day9.txt","r")
start = file.read()
startlist = start.split("\n")

#file = open("2016day9test.txt","r")
#startb = file.read()
#testlist = startb.split("\n")


def decompress(inputstring):
    outstring = ''
    remaining = inputstring
    while len(remaining) > 0:
        if remaining[0] != "(":
            outstring += remaining[0]
            remaining = remaining[1:]
        else:
            pos = remaining.index(")")
            instruction = remaining[1:pos].split("x")
            remaining = remaining[pos+1:]
            outstring += remaining[0:int(instruction[0])]*int(instruction[1])
            remaining = remaining[int(instruction[0]):]
    return len(outstring)

def setupcount(inputstring):
    checker = copy.deepcopy(inputstring)
    countlist = [1 for x in inputstring]
    while "(" in checker:
        start = checker.index("(")
        end = checker.index(")")
        for i in range(start,end+1):
            countlist[i] = 0
            checker = checker[0:start]+"X"*(end-start+1)+checker[end+1:]
    return countlist


def decompress2(inputstring):
    countlist = setupcount(inputstring)
    checker = copy.deepcopy(inputstring)
#    print(checker)
#    print(countlist)
    while "(" in checker:
        start = checker.index("(")
        end = checker.index(")")
        instruction = checker[start+1:end].split("x")
#        print(start,end,instruction)
        for i in range(end+1,end+1+int(instruction[0])):
#            print(countlist[i],instruction[1])
            countlist[i] = countlist[i]*int(instruction[1])
#            print(countlist)
            checker = checker[0:start]+(end-start+1)*"x"+checker[end+1:]
    return (sum(countlist),len(countlist))
            
        
        
    
    
        