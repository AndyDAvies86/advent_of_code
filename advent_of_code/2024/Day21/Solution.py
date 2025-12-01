#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque,Counter
import itertools as it
import copy
import networkx as nx
import matplotlib.pyplot as plt
from functools import lru_cache,cache

from advent_of_code.utils.helper_functions import *

#%%
start = lineparse('inputfile.txt')
test = lineparse('inputtest.txt')

#%%

def parselist(inputlist):
    pass
#%%

def numpad():
    nums = {str(x):((x+2)//3,(x+2)%3) for x in range(1,10)}
    nums['0'] = (0,1)
    nums['A'] = (0,2)
    return nums

def dirpad():
    dirs = {
        '^':(1,1),
        '>':(0,2),
        'v':(0,1),
        '<':(0,0),
        'A':(1,2)
    }
    return dirs

@lru_cache
def movedir(x,y,type='d'):
    # if x==y:
    #     return 'A'
    if type == 'n':
        pad = numpad()
    else:
        pad = dirpad()
    xpos = pad[x]
    ypos = pad[y]
    out = ''   
    if xpos[1] < ypos[1]:
        out = out+(ypos[1]-xpos[1])*'>'
    if xpos[0] < ypos[0]:
        out = out+(ypos[0]-xpos[0])*'^'
    if xpos[0] > ypos[0]:
        out = out+(xpos[0]-ypos[0])*'v'
    if xpos[1] > ypos[1]:
        out = out+(xpos[1]-ypos[1])*'<'
    return out

@lru_cache
def nextstep(intuple,p='d'):
    tstring = tuple('A')+intuple
    keyslist = []
    for ii in range(0,len(intuple)):
        newkey = movedir(tstring[ii],tstring[ii+1],p)
        keyslist.append(newkey)
    return keyslist



def keydistance(pad):
    dist ={
        x+y:md(pad[x],pad[y])+1 for x in pad for y in pad
    }
    return dist

def part1(inputlist):
    for code in inputlist:
        digits = nextstep(tuple(code),'n')
        print(code,digits)

        for key in digits:
            print(key,nextstep(key),nextstep(key[::-1]))

    return

    # return sum([presses[x]*int(inputlist[x][:3]) for x in range(len(inputlist))])

     

#%%

def part2(inputlist):
    pass
#%%