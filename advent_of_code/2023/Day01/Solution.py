
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
numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
numlist = [str(x) for x in range(0,10)]
#%%
file = open("inputfile.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n")

file = open("inputtest2.txt","r")
startc = file.read()
test2list = startc.split("\n")

#%%
def firstlastnum(word):
    numlist= ''
    for x in word:
        if x.isnumeric():
            numlist = numlist + x
    outnum =  10*int(numlist[0])+int(numlist[-1])
    return outnum

def sumcodes(biglist):
    cumul = 0
    for word in biglist:
        cumul += firstlastnum(word)
    return cumul

print("Test part 1: "+str(sumcodes(testlist)))
print("Puzzle part 1: "+str(sumcodes(startlist)))

#%%
def numstringlist(word):
    numpos = [word.rfind(x) for x in numlist]
    numwordpos = [word.rfind(x) for x in numbers]
    minnumpos = [999 if word.find(x) == -1 else word.find(x) for x in numlist]
    minnumwordpos = [999 if word.find(x) == -1 else word.find(x) for x in numbers]
    maxposlist = []
    minposlist = []
    for ii in range (0,10):
        maxposlist.append(max(numpos[ii],numwordpos[ii]))
        minposlist.append(min(minnumpos[ii],minnumwordpos[ii]))
    score = maxposlist.index(max(maxposlist))+10*minposlist.index(min(minposlist))
    return score

def sumpt2cals(biglist):
    cumul = 0
    for word in biglist:
        # print(word)
        # print(numstringlist(word))
        cumul += numstringlist(word)
    return cumul

print("Test part 2: "+str(sumpt2cals(test2list)))
print("Puzzle part 2: "+str(sumpt2cals(startlist)))

#%%