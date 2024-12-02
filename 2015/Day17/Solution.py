
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
    return [int(x) for x in inputlist]
#%%

def part1(inputlist,vol):
    buckets = np.array(parselist(inputlist))
    good = 0
    max_check = 2**len(buckets)
    for ii in range(0,max_check):
        b_in = np.array([int(x) for x in bin(ii+max_check)[3:]])
        if sum(buckets*b_in) == vol:
            good = good+1
    return good


#%%

def part2(inputlist,vol):
    buckets = np.array(parselist(inputlist))
    good = 0
    max_check = 2**len(buckets)
    min_b = 999
    for ii in range(0,max_check):
        b_in = np.array([int(x) for x in bin(ii+max_check)[3:]])
        if sum(b_in) < min_b:
            if sum(buckets*b_in) == vol:
                min_b = sum(b_in)

    for ii in range(0,max_check):
        b_in = np.array([int(x) for x in bin(ii+max_check)[3:]])
        if sum(b_in) == min_b:
            if sum(buckets*b_in) == vol:
                good = good+1
    return good
#%%