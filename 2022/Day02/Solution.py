
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy

#%%
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()
#%%
file = open("inputfile.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n")

#%%
def listfull(inputlist):
    fullturns =[]
    turndict = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}
    for row in inputlist:
        fullturns.append([turndict[x] for x in row.split(" ")])
    return fullturns

#%%

def part1(inputlist):
    scoresthrow = [x[1] for x in listfull(inputlist)]
    scoreswin = [(x[1]-x[0]+1)%3 for x in listfull(inputlist)]
    return sum(scoresthrow)+sum(scoreswin)*3

#%%

def listfull2(inputlist):
    fullturns =[]
    turndict = {"A":1, "B":2, "C":3}
    windict = {"X":-1, "Y":0, "Z":1}
    for row in inputlist:
        splitrow = row.split(" ")
        #print(splitrow)
        methrow = turndict[splitrow[0]]+windict[splitrow[1]]
        newthrow = (methrow-1)%3 + 1
        newrow = [turndict[splitrow[0]],newthrow]
        fullturns.append(newrow)
    print(fullturns)
    return fullturns
#%%

def part2(inputlist):
    scoresthrow = [x[1] for x in listfull2(inputlist)]
    scoreswin = [(x[1]-x[0]+1)%3 for x in listfull2(inputlist)]
    print(scoreswin)
    print(scoresthrow)
    return sum(scoresthrow)+sum(scoreswin)*3
#%%