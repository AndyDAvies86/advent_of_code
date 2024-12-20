#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
from math import lcm

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

file = open("test2.txt","r")
startc = file.read()
testlistc = startc.split("\n")

#%%

def parselist(inputlist):
    midlist = [x.replace('<','').replace('>','').replace('x','').replace('y','').replace('z','').replace('=','') for x in inputlist]
    outlist = [[int(y) for y in x.split(',')] for x in midlist]
    return outlist

def vchanges(poslist):
    alist = [[0,0,0] for x in poslist]
    for ii in range(0,3):
        pos_check = [pos[ii] for pos in poslist]
        for jj in range(0,len(poslist)):
            test = poslist[jj][ii]
            alist[jj][ii] = sum([test<pos for pos in pos_check])-sum([test>pos for pos in pos_check])
    return alist

def part1(inputlist,steps):
    poslist = parselist(inputlist)
    vlist = [[0,0,0] for x in poslist]

    for ii in range(0,steps):
        alist = vchanges(poslist)
        vlist = [[vlist[jj][kk]+alist[jj][kk] for kk in range(0,3)] for jj in range(0,len(vlist))]
        poslist = [[vlist[jj][kk]+poslist[jj][kk] for kk in range(0,3)] for jj in range(0,len(poslist))]
        # print(poslist)
        # print(vlist)
    pot_list = [sum([abs(x) for x in pos]) for pos in poslist]
    kin_list = [sum([abs(x) for x in v]) for v in vlist]
    return sum([pot_list[x]*kin_list[x] for x in range(0,len(poslist))])

def loop_check(inputlist):
    steps = 1
    numpos = len(inputlist)
    poslist_start = inputlist
    poslist = inputlist
    vlist = [0 for x in poslist]
    stop = 0
    while stop == 0:
        alist = [sum([test>pos for test in poslist])-sum([test<pos for test in poslist]) for pos in poslist]
        vlist = [vlist[ii]+alist[ii] for ii in range(0,numpos)]
        poslist = [vlist[ii]+poslist[ii] for ii in range(0,numpos)]
        # print(steps,poslist,vlist,alist)
        if poslist == poslist_start:
            stop=1
        steps = steps+1
    return steps

def part2(inputlist):
    poslist = parselist(inputlist)
    x = loop_check([pos[0] for pos in poslist])
    y = loop_check([pos[1] for pos in poslist])
    z = loop_check([pos[2] for pos in poslist])
    print(x,y,z)
    return lcm(x,y,z) 


#%%