
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

file = open("2018day8.txt","r")
start = file.read()
startlist = start.split(" ")
startint = []
for row in startlist:
    startint.append(int(row))


file = open("2018day8test.txt","r")
startb = file.read()
testlist = startb.split(" ")
testint = []
for row in testlist:
    testint.append(int(row))
testiter = iter(testint)
#%%

def scoretrees(intlist):
    children = intlist[0]
    metas = intlist[1]
    rest = intlist[2:]
    scores = 0
    values = []
    # print('o',children,metas,len(rest))

    for ii in range(0,children):
        score,value,rest = scoretrees(rest)
        scores = scores+score
        values.append(value)
        # scores.append(score)
        # print('for',ii,score,scores,rest)
    scores = scores + sum(rest[:metas])

    if children == 0:
        remaining = rest[metas:]
        value = sum(rest[:metas])
        # print('if',children,score,remaining)
        return scores,value,remaining
    else:
        # score = sum(scores[k - 1] for k in rest[:metas] if k > 0 and k <= len(scores))
        value = sum(values[k-1] for k in rest[:metas] if k > 0 and k <= len(values))
        remaining = rest[metas:]
        # print('else',children,score,remaining)
        return scores,value,remaining
    



#%%

def part1(intlist):
    answer = scoretrees(intlist)[0]
    print(answer)

def part2(intlist):
    answer = scoretrees(intlist)[1]
    print(answer)