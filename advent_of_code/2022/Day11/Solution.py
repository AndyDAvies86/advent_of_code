
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import math

#%%
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()
#%%
file = open("inputfile.txt","r")
start = file.read()
startlist = start.split("\n\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n\n")


#%%
def prepinput(inputlist):
    startitems = []
    operations = []
    tests = []
    throws = []
    for monkey in inputlist:
        notes = monkey.split("\n")
        #start items
        monkeystartlist = notes[1].split(": ")[1]
        monkeystart = [int(x) for x in monkeystartlist.split(", ")]
        startitems.append(monkeystart)
        #operations
        operations.append(notes[2].split(": ")[1][6:])
        #Divisible test
        tests.append(int(notes[3].split(" ")[-1]))
        #Throw
        Tthrow = notes[4].split(" ")[-1]
        Fthrow = notes[5].split(" ")[-1]
        throws.append([int(Tthrow),int(Fthrow)])
    return startitems,operations,tests,throws
#%%
def operation(itemlist,operation,tests):
    maxval = np.prod(tests)
    newitemlist = []
    for item in itemlist:
        if operation == 'old * old':
            old = item
            print(item)
            new = item*item
            print(new)
            print(96140*96140)
            newmod = new%maxval
            newitemlist.append(newmod)
        else:
            old = item
            #print(operation,old)
            new = eval(operation)
            #print(old,new,operation)
            newmod = new%maxval
            newitemlist.append(newmod)
        if operation == 'old * old':
            print(item,old,new,operation,maxval)
    return newitemlist


#%%
def throwitems(itemlist,tests,throws,monkey):
    maxval = np.prod(tests)
    for item in itemlist[monkey]:
        #print(throws)
        if item % tests[monkey] == 0:
            itemlist[throws[monkey][0]].append(item%maxval)
        else:
            itemlist[throws[monkey][1]].append(item%maxval)
    itemlist[monkey] = []
    return itemlist
#%%
def part1(inputlist,rounds):
    monkeys = len(inputlist)
    count = [0 for x in range(0,monkeys)]
    itemlist,operations,tests,throws = prepinput(inputlist)
    for ii in range(0,rounds):
        for monkey in range(0,monkeys):
            count[monkey] += len(itemlist[monkey])
            itemlist[monkey] = [x//3 for x in operation(itemlist[monkey],operations[monkey],tests)]
            itemlist = throwitems(itemlist,tests,throws,monkey)

    return sorted(count)[-1]*sorted(count)[-2]
#%%

def part2(inputlist,rounds):
    monkeys = len(inputlist)
    count = [0 for x in range(0,monkeys)]
    itemlist,operations,tests,throws = prepinput(inputlist)
    #print(tests)
    maxvalb = np.prod(tests)
    #print(maxvalb)
    for ii in range(0,rounds):
        print(itemlist)
        for monkey in range(0,monkeys):
            count[monkey] += len(itemlist[monkey])
            itemlist[monkey] = [x for x in operation(itemlist[monkey],operations[monkey],tests)]
            itemlist = throwitems(itemlist,tests,throws,monkey)
    return count,maxvalb
#    return sorted(count)[-1]*sorted(count)[-2]
   
#%%


# %%
