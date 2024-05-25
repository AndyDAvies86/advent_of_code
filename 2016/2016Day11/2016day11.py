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

file = open("2016day11.txt","r")
start = file.read()

startlist = start.split("\n")

file = open("2016day11test.txt","r")
startb = file.read()
testlist = startb.split("\n")

def begin(inputlist):
    clean = []
    for row in inputlist:
        newrow = row.replace('The ','').replace('floor contains ','').replace('a ','').replace(',','').replace('and ','').replace('-compatible','').replace(' nothing relevant.','')
        splitrow = newrow.split(" ")
        shortrow = splitrow[1:]
        print(shortrow)
        briefrow = [x[0] for x in shortrow]
        cleanrow = [briefrow[i]+briefrow[i+1] for i in range(0,len(briefrow),2)]
        clean.append(cleanrow)
    return clean

def part1(inputlist):
    E = 1
    floorstate = begin(inputlist)
    
