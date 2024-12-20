
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
    pass
#%%

def createnew(recipes,e1,e2):
    recipes = recipes+str(int(recipes[e1])+int(recipes[e2]))
    return recipes



def part1(inputlist):
    e1 = 0
    e2 = 1
    recipes = '37'
    t=int(inputlist)
    for tt in range(0,t+10):
        recipes = createnew(recipes,e1,e2)
        # print(tt,recipes)
        x = len(recipes)
        e1 = (e1+int(recipes[e1])+1)%x
        e2 = (e2+int(recipes[e2])+1)%x
    return recipes[t:t+10]


#%%

def part2(inputlist):
    inputlist = str(inputlist)
    e1 = 0
    e2 = 1
    recipes = '37'
    go = True
    t=0
    while go and t < 30000000:
        # if t%1000000 == 0:
            # print(t,len(recipes),recipes[-len(inputlist):])
        # if t%100000 == 0:
        #     print(t,e1,e2,len(recipes),recipes[t-10:t])
        recipes = recipes+str(int(recipes[e1])+int(recipes[e2]))
        # print(t,recipes)
        e1 = (e1+int(recipes[e1])+1)%len(recipes)
        e2 = (e2+int(recipes[e2])+1)%len(recipes)
        if inputlist in recipes[-len(inputlist)-3:]:
            return recipes.index(inputlist)
        # if len(recipes) in range(20185400,20185440):
            # print(t,len(recipes),recipes[-len(inputlist):])
        t = t+1
#%%