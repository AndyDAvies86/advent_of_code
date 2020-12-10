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


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2020day10.txt","r")
start = file.read()
startlist = start.split("\n")
startint = [int(x) for x in startlist]

file = open("2020day10test.txt","r")
startb = file.read()
testlist = startb.split("\n")
testint = [int(x) for x in testlist]

file = open("2020day10testsm.txt","r")
startc = file.read()
testlistsm = startc.split("\n")
testsmint = [int(x) for x in testlistsm]

def fulljolts(inputlist):
    inputlist.append(max(inputlist)+3)
    inputlist.append(0)
    inputlist.sort()
    return inputlist

def countgaps(inputlist):
    count = [0,0,0]
    for i in range(0,len(inputlist)-1):
        diff = inputlist[i+1] - inputlist[i]
        count[diff-1] += 1
    return count

def part1sol(inputlist):
    count = countgaps(fulljolts(inputlist))
    return count[0]*count[2]

def part2sol(inputlist):
    fulljoltlist = fulljolts(inputlist)
    lengtharray = {x : 0 for x in range(0,fulljoltlist[-1])}
    lengtharray[fulljoltlist[-1]] = 1
    for j in range(1,len(inputlist)):
         k = len(inputlist)-j-1
         a = inputlist[k]

         lengtharray[a] = lengtharray[a+1] + lengtharray[a+2] + lengtharray[a+3]
    return lengtharray[0]
        