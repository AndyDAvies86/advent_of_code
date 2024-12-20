
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import hashlib

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
    return inputlist[0]
#%%

def findkey(salt,a,patt):
    for ii in range(a+1,a+1001):
        regex = re.escape(patt)+r'{5}'
        x = salt+str(ii)
        y = str(hashlib.md5(x.encode()).hexdigest())
        check = re.search(regex,y)
        if check:
            # print(ii)
            return 1
    return 0


def part1(inputlist):
    salt = parselist(inputlist)
    keys = []
    a = 0
    while len(keys) < 64:
        x = salt+str(a)
        y = str(hashlib.md5(x.encode()).hexdigest())
        check = re.findall(r'([0123456789abcdef])\1{2}',y)
        # print(a,y,check)
        if check:
            # print(a,check)
            # print(findkey(salt,a,check[0]))
            if findkey(salt,a,check[0]) == 1:
                keys.append(a)
        a = a+1
    return keys[-1]
    
#%%

def hashstretch(x):
    for ii in range(0,2017):
        x = str(hashlib.md5(x.encode()).hexdigest())
    return x

def findstretchkey(salt,a,patt):
    for ii in range(a+1,a+1001):
        regex = re.escape(patt)+r'{5}'
        x = salt+str(ii)
        y = hashstretch(x)
        check = re.search(regex,y)
        if check:
            # print(ii)
            return 1
    return 0

def part2(inputlist):
    salt = parselist(inputlist)
    keys = []
    trips = {}
    quins = {}
    a = 0
    while len(keys) < 80:
        x = salt+str(a)
        y = hashstretch(x)
        check = re.findall(r'([0123456789abcdef])\1{2}',y)
        # print(a,y,check)
        if check:
            trips[a] = check[0]
            # print('t',a,check[0])
        check5 = re.findall(r'([0123456789abcdef])\1{4}',y)
        if check5:
            quins[a] = set([z[0] for z in check5])
            # print('q',a,quins[a],quins)
            for ii in range(max(0,a-1000),a):
                if ii in trips:
                    if trips[ii] in quins[a] and ii not in keys:
                        keys.append(ii)
                        print(len(keys),ii,a,check[0])
        a = a+1
    newkeys = sorted(list(set(keys)))
    return newkeys[63]
#%%