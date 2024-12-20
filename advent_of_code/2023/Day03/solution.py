
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

def to_lists(inputlist):
    outlist = []
    for row in inputlist:
        outlist.append([x for x in row])
    return outlist

def number_array(inputlist):
    outlist = []
    for row in inputlist:
        outlist.append([int(x) if x.isnumeric() else 0 for x in row])
    return np.array(outlist)

def symbol_array(inputlist):
    outlist = []
    for row in inputlist:
        outlist.append([1 if (x.isnumeric() or x=='.') else 0 for x in row])
    return np.array(outlist)

def touching_zero(inputarray):
    y,x = np.shape(inputarray)
    outarray=np.ones((y,x),dtype=int)
    for ii in range(1,y-1):
        for jj in range(1,y-1):
            if inputarray[jj,ii] == 0:
                outarray[jj-1:jj+2,ii-1:ii+2]=0
    return outarray

def number_list(inputlist):
    locations = []
    location = []
    rows = len(inputlist)
    columns = len(inputlist[0])
    a = 0
    ii = 0
    jj = 0
    while ii < rows:
        # print(ii,jj)
        # if (not ind) and inputlist[ii][jj].isnumeric()
        ind = inputlist[ii][jj].isnumeric()
        if len(location) == 0 and ind:
            location.append(ii)
            location.append(jj)
        if jj == columns-1:
            if len(location) > 0:
                if ind:
                    location.append(jj)
                else:
                    location.append(jj-1)
                locations.append(location)
                location = []
            jj = -1
            ii = ii + 1
        elif len(location) > 0 and (not ind):
            location.append(jj-1)
            locations.append(location)
            location = []
        jj = jj + 1
    return(locations)

def gear_list(inputlist):
    gear_locs = []
    for ii in range(0,len(inputlist)):
        for jj in range(0,len(inputlist[0])):
            if inputlist[ii][jj] == '*':
                gear_locs.append([ii,jj])
    return gear_locs
        
#%%        

def part1(inputlist):
    part_array = touching_zero(symbol_array(inputlist))    
    number_locs = number_list(inputlist)
    # print(number_locs)
    part_locs = []
    partsum = 0
    for number in number_locs:
        # print(part_array[number[0],number[1]:number[2]+1])
        if part_array[number[0],number[1]:number[2]+1].min() == 0:
            part_locs.append(number)
            # print(number)
    for part in part_locs:
        # print(part)
        part_score = inputlist[part[0]][part[1]:part[2]+1]
        # print(part_score)
        partsum = partsum + int(part_score)
    return partsum


def part2(inputlist):
    gear_locs = gear_list(inputlist)
    number_locs = number_list(inputlist)
    all_gears= []
    for gear in gear_locs:
        gear_nums = []
        for num in number_locs:
            if gear[0] == num[0]:
                if gear[1] in (num[1]-1,num[2]+1):
                    gear_nums.append(int(inputlist[num[0]][num[1]:num[2]+1]))
            if abs(gear[0]-num[0]) == 1:
                if gear[1] in range(num[1]-1,num[2]+2):
                    gear_nums.append(int(inputlist[num[0]][num[1]:num[2]+1]))
        all_gears.append(gear_nums)
    
    gear_sum = 0
    for gear in all_gears:
        if len(gear) ==2:
            gear_sum = gear_sum+gear[0]*gear[1]

    return gear_sum

#%%