# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 09:46:31 2020

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

file = open("2017day24.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("2017day24test.txt","r")
startb = file.read()
testlist = startb.split("\n")

#file = open("2020day14test2.txt","r")
startc = file.read()
testlist2 = startc.split("\n")

def cleanlist(inputlist):
    outlist = []
    for row in inputlist:
        newrow = row.split("/")
        outlist.append([int(x) for x in newrow])
    return outlist

full = []
for row in cleanlist(startlist):
    full += row
counts = [full.count(x) for x in range(0,max(full)+1)]fab
    
