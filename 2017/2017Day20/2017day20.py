# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:46:13 2020

@author: Andy
"""



import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2017day20.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("2017day20test.txt","r")
startb = file.read()
testlist = startb.split("\n")

file = open("2017day20test2.txt","r")
startc = file.read()
testlist2 = startc.split("\n")


def cleanlist(inputlist):
    clean = []
    for row in inputlist:
        newrow = row.split(", ")
        splitrow = [x[3:-1].split(",") for x in newrow]
        introw=[]
        for block in splitrow:
#            newblock = [int(x) for x in block]
            introw.append(np.array([int(x) for x in block]))
        clean.append(introw)
    return clean
        

def part1(inputlist):
    state = cleanlist(inputlist)
    alist = [sum(abs(x[2])) for x in state]
    mina = min(alist)
    mincheck = [x == mina for x in alist]
    print(sum([x == mina for x in alist]))
    minalist = []
    for i in range(0,len(state)):
        if mincheck[i]:
            minalist.append(i)
    vlist = [sum(abs(state[x][1])) for x in minalist]
    minv = min(vlist)
    print(sum([x == minv for x in vlist]))
    print(minalist[vlist.index(minv)])
    
def part2(inputlist):
    state = cleanlist(inputlist)
#    dlist = []
#    for i in range(0,len(state)-1):
#        for j in range(i,len(state)):
#            dlist.append(sum(abs(state[i][0]-state[j][0])))
    t = 0
    while t < 1000:
        for i in range(0,len(state)):
#            print(i)
            state[i][1] += state[i][2]
            state[i][0] += state[i][1]
        plist = [list(x[0]) for x in state]
        pcheck = [plist.count(p) for p in plist]
#        print(pcheck)
        prem = []
        for i in range(0,len(pcheck)):
            if pcheck[i] > 1:
                prem = [i]+prem
        for x in prem:
            del state[x]

        if len(state) == 1:
            return 1
        
#        newdlist = []        
#        for i in range(0,len(state)-1):
#            for j in range(i,len(state)):
#                newdlist.append(sum(abs(state[i][0]-state[j][0])))
#        if min(newdlist) > min(dlist) and prem == []:
#            return len(state)
#        dlist = newdlist
        print((t,len(state)))


        t += 1
        
#        print(t)
#        print(set(plist))        
        
        
        vlist = [sum(abs(x[1])) for x in state]
        alist = [sum(abs(x[2])) for x in state]
#        print(plist,vlist,alist)
#        if plist.index(min(plist)) == vlist.index(min(vlist)):
#            if alist.index(min(alist)) == vlist.index(min(vlist)):
#                return plist.index(min(plist))
