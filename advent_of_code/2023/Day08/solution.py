
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import json
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

def parse(inputlist):
    instructions = [0 if x == 'L' else 1 for x in inputlist[0]]
    steps = {}
    for row in inputlist[1].split("\n"):
        steps[row[0:3]] = [row[7:10],row[12:15]]
    return instructions,steps

def find_A(steps):
    A_pos = []
    for step in steps:
        # print(step)
        if step[2] == 'A':
            A_pos.append(step)
    return A_pos



#%%        

def part1(inputlist):
    instructions,steps=parse(inputlist)
    circ = len(instructions)
    num = 0
    pos = 'AAA'
    while pos != 'ZZZ':
        # print(pos,num,circ)
        pos = steps[pos][instructions[num%circ]]
        # print(pos)
        num = num+1
    return num



def part2(inputlist):
    instructions,steps=parse(inputlist)
    circ = len(instructions)
    A_pos = find_A(steps)
    # print(A_pos)
    Z_cycle = []
    for pos in A_pos:
        num = 0
        while pos[2] != 'Z':
            pos = steps[pos][instructions[num%circ]]
            num = num+1
        Z_cycle.append(num)
    return math.lcm(*Z_cycle)

    # num = 0
    # Z_pos = 0
    # while (Z_pos != len(A_pos)):
    #     A_pos = [steps[pos][instructions[num%circ]] for pos in A_pos]
    #     num = num+1
    #     Z_pos = sum([1 if x[2] == 'Z' else 0 for x in A_pos])
        # print(num,Z_pos,A_pos)
    # return num




#%%