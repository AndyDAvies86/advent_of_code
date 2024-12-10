
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
    prekit = [x.replace(' a ','').replace(' and',',').replace(',,',',')[x.find('contains') + 8:] for x in inputlist][:3]
    kit = [[''.join([a[0] for a in x.split(' ')]) for x in y.split(',')] for y in prekit]
    # kit = [[''.join([z[0] for z in y.split(' a ')[-1].replace('.','').split(' ')]) for y in x.split(',')] for x in inputlist[:-1]]
    # kitdict = {}
    # for ii in range(0,len(kit)):
    print(kit[0])
    print(kit[1])
    print(kit[2])
    return kit
#%%

def part1(inputlist):
    E = 0
    
#%%

def part2(inputlist):
    pass
#%%