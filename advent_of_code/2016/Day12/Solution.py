
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
    pass
#%%

def part1(inputlist):
    reg = {'a':0,'b':0,'c':0,'d':0}
    step = 0
    a = 0
    # for row in inputlist:
    while step < len(inputlist):
        a = a+1
        row = inputlist[step]
        inst = row.split(" ")
        # print(inst)
        if inst[0] == 'cpy':
            if inst[1] in ('a','b','c','d'):
                reg[inst[2]] = reg[inst[1]]
            else:
                reg[inst[2]] = int(inst[1])
            step = step + 1
        elif inst[0] == 'inc':
            reg[inst[1]] = reg[inst[1]] + 1
            step = step+1
        elif inst[0] == 'dec':
            reg[inst[1]] = reg[inst[1]] - 1
            step = step+1
        else:
            if inst[1] in ('a','b','c','d'):
                if reg[inst[1]] == 0:
                    step = step + 1
                else:
                    step = step + int(inst[2])
            else:
                if int(inst[1]) == 0:
                    step = step + 1
                else:
                    step = step + int(inst[2])
        # print(reg)
    return reg['a']

#%%

def part2(inputlist):
    reg = {'a':0,'b':0,'c':1,'d':0}
    step = 0
    a = 0
    # for row in inputlist:
    while step < len(inputlist):
        a = a+1
        row = inputlist[step]
        inst = row.split(" ")
        # print(inst)
        if inst[0] == 'cpy':
            if inst[1] in ('a','b','c','d'):
                reg[inst[2]] = reg[inst[1]]
            else:
                reg[inst[2]] = int(inst[1])
            step = step + 1
        elif inst[0] == 'inc':
            reg[inst[1]] = reg[inst[1]] + 1
            step = step+1
        elif inst[0] == 'dec':
            reg[inst[1]] = reg[inst[1]] - 1
            step = step+1
        else:
            if inst[1] in ('a','b','c','d'):
                if reg[inst[1]] == 0:
                    step = step + 1
                else:
                    step = step + int(inst[2])
            else:
                if int(inst[1]) == 0:
                    step = step + 1
                else:
                    step = step + int(inst[2])
        # print(reg)
    return reg['a']
#%%