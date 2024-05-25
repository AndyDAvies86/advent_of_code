
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
startlist = start

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb


#%%
#%%
def part1(inputlist):
    pos = 0
    stop = 0
    while stop < 1:
        if len(set([x for x in inputlist[pos:pos+4]])) == 4:
            stop = 1
        pos += 1
    return pos+3
#%%

def part2(inputlist):
    pos = 0
    stop = 0
    while stop < 1:
        if len(set([x for x in inputlist[pos:pos+14]])) == 14:
            stop = 1
        pos += 1
    return pos+13

#%%