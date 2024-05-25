
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

file = open("inputfile.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n")

#%%
def looksayturn(looksay):
    newlooksay = ''
    if len(looksay) == 1:
        newlooksay = '1'+looksay
    else:
        jj = 0
        while jj < len(looksay):
            number = looksay[jj]
            kk = 0
            while looksay[jj+kk] == looksay[jj]:
                if jj + kk == len(looksay)-1:
                    newlooksay += str(kk+1)+looksay[jj]
                    return newlooksay
                else:
                    kk += 1
            newlooksay += str(kk)+looksay[jj]
            jj += kk
    return newlooksay

#%%
def part1(inputlist,turns):
    looksay = inputlist[0]
    for ii in range(0,turns):
        print(looksay)
        looksay = looksayturn(looksay)
    return looksay

   
# %%

def part2(inputlist):
    
    return 
# %%
