# -*- coding: utf-8 -*-
"""


@author: Andy
"""

import pandas as pd
import numpy as np

filetest = open("2021day9test.txt","r")
starttest = filetest.read()
test = starttest.split("\n")


file = open("2021day9input.txt","r")
start = file.read()
startlist = start.split("\n")

def definemap(inputlist):
    prefloormap = [[10]+[int(x) for x in y] + [10] for y in inputlist]
    floormap = [[10 for x in range(0,len(prefloormap[0]))]] + prefloormap +[[10 for x in range(0,len(prefloormap[0]))]]
    return floormap

def lowpoints(inputlist):
    floormap = definemap(inputlist)    
    width = len(floormap[0])
    height = len(floormap)
    risk = 0
    for ii in range(1,height-1):
        for jj in range(1,width-1):
            neighbours = [floormap[ii+x][jj+y] for (x,y) in ((0,1),(1,0),(-1,0),(0,-1))]
            minneighbour = min(neighbours)
            if floormap[ii][jj] < minneighbour:
#                print(ii,jj,floormap[ii][jj],neighbours)
                risk += floormap[ii][jj]+1
    return risk

def findlow(floormap):   
    width = len(floormap[0])
    height = len(floormap)
    lows = []
    for ii in range(1,height-1):
        for jj in range(1,width-1):
            neighbours = [floormap[ii+x][jj+y] for (x,y) in ((0,1),(1,0),(-1,0),(0,-1))]
            minneighbour = min(neighbours)
            if floormap[ii][jj] < minneighbour:
#                print(ii,jj,floormap[ii][jj],neighbours)
                lows.append((ii,jj))
    return lows
    
            
def buildbasinstep(floormap,basin):
    width = len(floormap[0])
    height = len(floormap)
    for ii in range(1,height-1):
        for jj in range(1,width-1):
            if basin[ii][jj] == 0 and floormap[ii][jj] !=9:
                neighbours = [(ii+x,jj+y) for (x,y) in ((0,1),(1,0),(-1,0),(0,-1))]
                for neighbour in neighbours:
                    if basin[neighbour[0]][neighbour[1]] != 0 and floormap[neighbour[0]][neighbour[1]] < floormap[ii][jj]:
                        basin[ii][jj] = basin[neighbour[0]][neighbour[1]]
    return basin

def buildbasins(floormap,basinmap) :      
    a = 0
    while a == 0:
        basincount = sum([sum(x) for x in basinmap])
        newbasinmap = buildbasinstep(floormap,basinmap)
        if sum([sum(x) for x in basinmap]) == basincount:
            return basinmap
        basinmap = newbasinmap
        
def basins(inputlist):
    floormap = definemap(inputlist)
    basinmap = [[0 for x in floormap[0]] for y in floormap]
    lowlist = findlow(floormap)
#    print(lowlist)
    for ii in range(0,len(lowlist)):
        basinmap[lowlist[ii][0]][lowlist[ii][1]] = ii+1
    basinmap = buildbasins(floormap,basinmap)
    basinlist = [x for y in basinmap for x in y] 
    basindict = {}
    for ii in range(0,len(lowlist)):
        basindict[ii+1] = basinlist.count(ii+1)
#    print(basindict)
    basinsort = [k for k, v in sorted(basindict.items(), key=lambda item: item[1])]
#    print(basinsort)
    basinscorelist = [basindict[x] for x in basinsort[-3:]]
#    print(basinscorelist)
    basinscore = basinscorelist[0]*basinscorelist[1]*basinscorelist[2]
    return basinscore
        