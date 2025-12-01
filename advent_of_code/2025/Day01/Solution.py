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
    num_list = []
    for inst in inputlist:
        if inst[0] == 'L':
            num_list.append(-int(inst[1:]))
        else:
            num_list.append(int(inst[1:]))
    return num_list
#%%


def part1(inputlist):
    dial = 50
    password=0
    for x in parselist(inputlist):
        dial = (dial + x) % 100
        if dial == 0:
            password = password+1
        # print(x,dial,password)
    return password


     

#%%

def part2(inputlist):
    dial = 50
    password=0
    for x in parselist(inputlist):    
        if x > 0 :
            for ii in range(0,x):
                dial = (dial+1) % 100
                if dial == 0:
                    password = password+1
        if x < 0 :
            for ii in range(0,-x):
                dial = (dial-1) % 100 
                if dial == 0:
                    password = password+1
    return password
#%%

def part2_long(inputlist):
    dial = 50
    dialb=50
    password=0
    passwordb = 0
    num_list = parselist(inputlist)
    
    for jj in range(0,len(num_list)):
        x = num_list[jj]
        pre_dial = dialb + x
        dialb = (pre_dial) % 100
        clicks = abs(pre_dial - dialb)//100
        passwordb = passwordb + clicks
        if x > 0 :
            for ii in range(0,x):
                dial = (dial+1) % 100
                if dial == 0:
                    password = password+1
        if x < 0 :
            for ii in range(0,-x):
                dial = (dial-1) % 100 
                if dial == 0:
                    password = password+1#
        if False:
            print(jj,x,dial,password, dialb, passwordb)
    return password