
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import hashlib

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2015day7.txt","r")
start = file.read()
startlist = start.split("\n")


file = open("2015day7test.txt","r")
startb = file.read()
testlist = startb.split("\n")


def cleanlist(inputlist):
    splitlist = [x.split(' -> ') for x in inputlist]
    outlist = [x[0].split(" ") + [x[1]] for x in splitlist]
    return outlist


def instruct(row,register):
#    print(row)
    if len(row) == 2:
        if row[0].isnumeric():
            register[row[-1]] = int(row[0])
        else:
            register[row[-1]] = register[row[0]]
    elif row[0] == 'NOT':
        if row[1].isnumeric():
            inval = int(row[1])
        else:
            inval = register[row[1]]
        register[row[-1]] = ~inval & 2**16 - 1
    elif row[1] == "AND":
        if row[0].isnumeric():
            inval = int(row[0])
        else:
            inval = register[row[0]]
        if row[2].isnumeric():
            inval2 = int(row[2])
        else:
            inval2 = register[row[2]]
        register[row[-1]] = inval & inval2
    elif row[1] == "OR":
        if row[0].isnumeric():
            inval = int(row[0])
        else:
            inval = register[row[0]]
        if row[2].isnumeric():
            inval2 = int(row[2])
        else:
            inval2 = register[row[2]]
        register[row[-1]] = inval | inval2
    elif row[1] == "LSHIFT":
        if row[1].isnumeric():
            inval = int(row[0])
        else:
            inval = register[row[0]]
        if row[2].isnumeric():
            inval2 = int(row[2])
        else:
            inval2 = register[row[2]]
        register[row[-1]] = inval << inval2  
    elif row[1] == "RSHIFT":
        if row[1].isnumeric():
            inval = int(row[0])
        else:
            inval = register[row[0]]
        if row[2].isnumeric():
            inval2 = int(row[2])
        else:
            inval2 = register[row[2]]
        register[row[-1]] = inval >> inval2  
    return register

def passthrough(instructions,register):
    newinstructions = []
    for row in instructions:
        try:
            register = instruct(row,register)
        except:
            newinstructions.append(row)
    return newinstructions,register

def part1(inputlist,check):
    instructions = cleanlist(inputlist)
    register = {}
    while len(instructions) > 0:
#    ii = 0
#    while ii < 1000 :
        instructions,register = passthrough(instructions,register)
#        ii += 1
#        print(instructions)
#        print(register)
#    print(register)
    return register[check]

def removeb(instructions):
    for ii in range(0,len(instructions)):
        if instructions[ii][-1] == 'b' :
            return instructions[0:ii]+instructions[ii+1:]

def part2(inputlist):
    instructions = cleanlist(inputlist)
#    print(len(instructions))
    register = {}
    register['b'] = 46065
    instructions = removeb(instructions)
#    print(len(instructions))
    while len(instructions) > 0:
#        print(len(instructions),register['b'])
        instructions,register = passthrough(instructions,register)
        try:
            return register['a']
        except:
            a=0
    