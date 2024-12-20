
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
startlist = start.split("\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n")

#%%

def parse(inputlist):
   return [[int(x) for x in y.split(" ")] for y in inputlist]

def pred_next(numlist):
    diffs =[numlist[x]-numlist[x-1] for x in range(1,len(numlist))]
    # print(numlist)
    # print(diffs)
    if sum([abs(x) for x in diffs]) == 0:
        return numlist+[numlist[-1]]
    else: 
        return numlist+[numlist[-1]+pred_next(diffs)[-1]]
    

#%%        

def part1(inputlist):
    num_lists = parse(inputlist)
    scores = 0
    for num_list in num_lists:
        # print(pred_next(num_list))
        score = pred_next(num_list)[-1]
        # print(score)
        scores = scores+score
    return scores
    



def part2(inputlist):
    old_num_lists = parse(inputlist)
    num_lists = [list(reversed(x)) for x in old_num_lists]
    scores = 0
    for num_list in num_lists:
        # print(pred_next(num_list))
        score = pred_next(num_list)[-1]
        # print(score)
        scores = scores+score
    return scores


#%%