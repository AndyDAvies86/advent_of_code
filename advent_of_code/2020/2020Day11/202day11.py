# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 08:54:23 2020

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

file = open("2020day11.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("2020day11test.txt","r")
startb = file.read()
testlist = startb.split("\n")


def setup(inputlist):
    seatlist = []
    for row in inputlist:
        seatlist.append([x for x in row])    
    return seatlist

def seatswap(seatlist):
    newlist = copy.deepcopy(seatlist)
    for i in range(0,len(seatlist)):
        for j in range(0,len(seatlist[i])):            
            if seatlist[i][j] != '.':
                adjacency = []
                for x in range(max(0,i-1),min(len(seatlist),i+2)):
                    for y in range(max(0,j-1),min(len(seatlist[i]),j+2)):
#                        if i == 0 and j == 8:
#                            print((x,y))
                        adjacency.append(seatlist[x][y]) 
#                if i == 0 and j == 2:
#                    print(adjacency)
                adjcount = adjacency.count('#')-seatlist[i][j].count('#')
                if adjcount == 0:
                    newlist[i][j] = "#"
                if adjcount >= 4:
                    newlist[i][j] = "L"
    return newlist

def findstable(inputlist):
    seatlist = setup(inputlist)
    stop = 0
    while stop == 0:
        newlist = seatswap(seatlist)
        if newlist == seatlist:
            stop = 1
        seatlist = newlist
    seatsfilled = 0
    for row in seatlist:
        seatsfilled += row.count('#')
    return seatsfilled


def seatswap2(seatlist):
    newlist = copy.deepcopy(seatlist)
    directions = [[x,y] for x in range(-1,2) for y in range(-1,2)]
    directions.remove([0,0])
    for i in range(0,len(seatlist)):
        for j in range(0,len(seatlist[i])):            
            if seatlist[i][j] != '.':
                adjacency = []
                for direct in directions:
                    x = i + direct[0]
                    y = j + direct[1]
                    stop = 0
#                    print(direct,i,j)
                    while x in range(0,len(seatlist)) and y in range(0,len(seatlist[i])) and stop == 0:
#                        if i == 0 and j == 2:
#                            print(adjacency,x,y)
#                        print((x,y))
                        if seatlist[x][y] != ".":
                            stop = 1
                            adjacency.append(seatlist[x][y])
                        x = x + direct[0]
                        y = y + direct[1]
#                        if i == 0 and j == 8:
#                            print((x,y))
#                if i == 0 and j == 2:
#                    print(adjacency)
                adjcount = adjacency.count('#')
                if adjcount == 0:
                    newlist[i][j] = "#"
                if adjcount >=5:
                    newlist[i][j] = "L"
    return newlist
        

def findstable2(inputlist):
    seatlist = setup(inputlist)
    stop = 0
    step = 0
    while stop == 0:
        newlist = seatswap2(seatlist)
        print(sum([row.count('#') for row in setup(newlist)]),step)
        step += 1
        if newlist == seatlist:
            stop = 1
        seatlist = newlist
    seatsfilled = 0
    for row in seatlist:
        seatsfilled += row.count('#')
    return seatsfilled,seatlist