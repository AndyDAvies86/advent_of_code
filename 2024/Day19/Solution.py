
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import networkx as nx
import matplotlib.pyplot as plt
from functools import cache

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
    tests = inputlist[2:]
    patterns = tuple([x for x in inputlist[0].split(', ')])
    return tests,patterns
#%%

@cache
def checks(test,patterns):
    checkout = []
    if len(test) == 0:
        # print('T')
        return [True]
    for pat in patterns:
        l = len(pat)
        # print(test,pat)
        if test.startswith(pat):
            checkout.append(any(checks(test[l:],patterns)))
    # print(test,checkout)
    return checkout


def part1(inputlist):
    tests,patterns = parselist(inputlist)
    score = 0
    for ii in range(0,len(tests)):
        test = tests[ii]
        if ii%10 == 0:
            print(ii)
        if any(checks(test,patterns)):
            score = score+1
        # print(test,score)
    return score
#%%

@cache
def p2checks(test,patterns):
    checkout = []
    if len(test) == 0:
        # print('T')
        return [1]
    for pat in patterns:
        l = len(pat)
        # print(test,pat)
        if test.startswith(pat):
            checkout.append(sum(p2checks(test[l:],patterns)))
        # print(test,pat,checkout)
    # print(test,checkout)
    return checkout

def part2(inputlist):
    tests,patterns = parselist(inputlist)
    score = 0
    for ii in range(0,len(tests)):
        test = tests[ii]
        # if ii%10 == 0:
        #     print(ii)
        score = score+sum(p2checks(test,patterns))
        # print(test,score)
    return score
#%%