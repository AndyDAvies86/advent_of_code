
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
    instructions = []
    for instr in inputlist:
        if instr[-1] == '-':
            instructions.append([instr[:-1],-1])
        else:
            pos = instr.find("=")
            instructions.append([instr[:pos],int(instr[pos+1:])])
    return instructions

def p1_hash(inputstring):
    value = 0
    for char in inputstring:
        value = ((value+ord(char))*17) % 256
        # print(char,value,ord(char))
    return value

def lens_actions(instr):
    if instr[1] == -1:
        #TODO remove lens with instr[0] 
        pass
    else:
        pass

def inst_dict(instructions):
    lenses = {}
    for inst in instructions:
        # print(inst)
        if inst[1] == -1:
            lenses.pop(inst[0],None)
        else:
            lenses[inst[0]]=inst[1]
    return lenses

#%%        


def part1(inputlist):
    return sum([p1_hash(x) for x in inputlist])



def part2(inputlist):
    instructions = parse(inputlist)
    lenses = inst_dict(instructions)
    outscore = 0
    for ii in range(0,256):
        scores = []
        for lens in lenses:
            if p1_hash(lens) == ii:
                scores.append(lenses[lens])
                # print(ii,lens,lenses[lens])
        # print(ii,scores)
        score_list = [scores[x]*(x+1)*(ii+1) for x in range(0,len(scores))]
        # print(score_list)
        outscore = outscore+sum(score_list)
    return outscore






#%%