
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
    col_len = len(inputlist)
    row_len = len(inputlist[0])
    rows=[x for x in range(0,col_len) if inputlist[x].count('.') == row_len]
    cols=[x for x in range(0,row_len) if [inputlist[y][x] for y in range(0,col_len)].count('.') == col_len]
    print(rows)
    print(cols)
    for col in list(reversed(cols)):
        inputlist = [x[:col]+'.'+x[col:] for x in inputlist]
    for row in list(reversed(rows)):
        inputlist = inputlist[:row]+['.'*len(inputlist[0])]+inputlist[row:]
    return inputlist


def galaxies(inputlist):
    gal_list = []
    for ii in range(0,len(inputlist)):
        for jj in range(0,len(inputlist[0])):
            if inputlist[ii][jj]=='#':
                gal_list.append([ii,jj])
    return gal_list

def old_rc(inputlist):
    col_len = len(inputlist)
    row_len = len(inputlist[0])
    rows=[x for x in range(0,col_len) if inputlist[x].count('.') == row_len]
    cols=[x for x in range(0,row_len) if [inputlist[y][x] for y in range(0,col_len)].count('.') == col_len]
    return rows,cols

#%%        

def part1(inputlist):
    gal_list=galaxies(parse(inputlist))
    distances = 0
    dist_list=[]
    for gala in gal_list:
        for galb in gal_list:
            distance = (abs(gala[0]-galb[0])+abs(gala[1]-galb[1]))
            # print(distance,gala,galb)
            dist_list.append(distance)
            distances = distances+distance
    return distances//2


def part2(inputlist):
    gal_list=galaxies(inputlist)
    row_list,col_list=old_rc(inputlist)
    print(row_list,col_list)
    distances = 0
    dist_list=[]
    for gala in gal_list:
        for galb in gal_list:
            distance = (abs(gala[0]-galb[0])+abs(gala[1]-galb[1]))
            row_x = set([x for x in range(min([gala[0],galb[0]]),max([gala[0],galb[0]]))]).intersection(set(row_list))
            col_x = set([x for x in range(min([gala[1],galb[1]]),max([gala[1],galb[1]]))]).intersection(set(col_list))
            distanceb=distance+(1000000-1)*(len(row_x)+len(col_x))
            # print(distance,len(row_x),len(col_x),distanceb)
            dist_list.append(distance+len(row_x)+len(col_x))
            distances = distances+distanceb
    return distances//2



#%%