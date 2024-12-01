
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import json
import itertools

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

def parseinput(inputlist):
    row_list = []
    for row in inputlist:
        row_list.append([int(x) for x in row.replace(",","").split(" ")[2:11:2]])
    return row_list


#%%
def part1(inputlist):
    ings = parseinput(inputlist)
    combo = list(itertools.combinations([x for x in range(0,100)
    ],len(inputlist)-1))
    max_score = 0
    for y in combo:
        z=(0,0)+y+(100,100)
        x=[z[k]-z[k-1] for k in range(2,len(z)-1)] 
        scores = [sum([x[ii]*ings[ii][jj] for ii in range(0,len(x))]) for jj in range(0,4)]
        score_list = [max(0,x) for x in scores]
        # for ii in range(0,5):
            
        score = 1  
        for val in score_list:
            score = score * val
        # print(x,score_list,score,ings)
        if score > max_score:
            max_score = score
            max_score_list = score_list
            max_combo=x
    return max_score,max_combo,max_score_list

    


#%%

def part1(inputlist):
    ings = parseinput(inputlist)
    combo = list(itertools.combinations([x for x in range(0,100)
    ],len(inputlist)-1))
    max_score = 0
    for y in combo:
        z=(0,0)+y+(100,100)
        x=[z[k]-z[k-1] for k in range(2,len(z)-1)] 
        scores = [sum([x[ii]*ings[ii][jj] for ii in range(0,len(x))]) for jj in range(0,4)]
        score_list = [max(0,x) for x in scores]
        # for ii in range(0,5):
        cals = sum([x[ii]*ings[ii][4] for ii in range(0,len(x))])
            
        score = 1  
        for val in score_list:
            score = score * val
        # print(x,score_list,score,ings)
        if score > max_score and cals == 500:
            max_score = score
            max_score_list = score_list
            max_combo=x
    return max_score,max_combo,max_score_list

    


#%%