
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


#%%

def parselist(inputlist):
    oneline = ''.join(inputlist)
    return oneline
#%%

def part1(inputlist):
    inst = parselist(inputlist)
    muls = re.findall(r"mul\([0-9]+\,[0-9]+\)",inst)
    score = 0
    for mul in muls:
        newmul = mul.replace("mul(","").replace(")","").split(",")
        score = score + int(newmul[0])*int(newmul[1])
    return score
#%%

def p2parse(inputlist):
    full = ''.join(inputlist)
    rem = copy.deepcopy(full)
    # ind = 1
    cleaned = ''
    while len(rem) > 0:
        pos = rem.find("don't()")
        if pos == -1:
            cleaned = cleaned + rem
        else:
            cleaned = cleaned + rem[:pos]
        rem = rem[pos:]
        posb = rem.find("do()")
        if posb == -1:
            rem = ''
        else:
            rem = rem[posb:]
    return cleaned

def part2(inputlist):
    inst = p2parse(inputlist)
    muls = re.findall(r"mul\([0-9]+\,[0-9]+\)",inst)
    score = 0
    for mul in muls:
        newmul = mul.replace("mul(","").replace(")","").split(",")
        score = score + int(newmul[0])*int(newmul[1])
    return score
#%%