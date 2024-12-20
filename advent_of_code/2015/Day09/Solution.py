
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
def distances(inputlist):
    distancelist = {}
    citylist = []
    for row in inputlist:
        rowsplit = row.split(" ")
        distancelist[str([rowsplit[0],rowsplit[2]])] = int(rowsplit[4])
        distancelist[str([rowsplit[2],rowsplit[0]])] = int(rowsplit[4])
        citylist.append(rowsplit[0])
        citylist.append(rowsplit[2])
    cities = list(set(citylist))
    return distancelist,cities

#%%
def part1(inputlist):
    distancelist,cities = distances(inputlist)
    cityorders = list(it.permutations(cities))
    mindistance = 999999999
    for row in cityorders:
        distance = 0
        for ii in range(0,len(row)-1):
            distance += distancelist[(str([row[ii],row[ii+1]]))]
        #print (row, distance)
        if distance < mindistance:
            mindistance = distance
    return mindistance
   
# %%

def part2(inputlist):
    distancelist,cities = distances(inputlist)
    cityorders = list(it.permutations(cities))
    maxdistance = 0
    for row in cityorders:
        distance = 0
        for ii in range(0,len(row)-1):
            distance += distancelist[(str([row[ii],row[ii+1]]))]
        #print (row, distance)
        if distance > maxdistance:
            maxdistance = distance
    return maxdistance