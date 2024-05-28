
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import json

#%%
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()
#%%
file = open("inputfile.txt","r")
start = file.read()
startlist = start.split(",")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split(",")

#%%

def parse(inputlist):
    return[int(x) for x in inputlist]

def op1(inputlist,i1,i2,o):
    inputlist[o] = inputlist[i1]+inputlist[i2]
    return inputlist

def op2(inputlist,i1,i2,o):
    inputlist[o] = inputlist[i1]*inputlist[i2]
    return inputlist

def oprun(inputlist,oc,i1,i2,o):
    if oc == 1:
        return op1(inputlist,i1,i2,o)
    if oc==2:
        return op2(inputlist,i1,i2,o)
    # else:
    #     return inputlist

def intcode(program):
    pos = 0
    while True:
        if program[pos] == 99:
            return program
        # print(program[pos:pos+4])
        oc = program[pos]
        i1 = program[pos+1]
        i2 = program[pos+2]
        o = program[pos+3]
        program = oprun(program,oc,i1,i2,o)
        pos=pos+4


#%%        

def part1(inputlist):
    program = parse(inputlist)
    # print(program)
    program[1] = 12
    program[2] = 2
    program = intcode(program)
    return program[0]




def part2(inputlist):
    for noun in range(0,100):
        for verb in range(0,100):
            program = parse(inputlist)
            program[1] = noun
            program[2] = verb
            # print(program)
            test = intcode(program)
            if test[0] == 19690720:
                return 100*noun+verb



#%%