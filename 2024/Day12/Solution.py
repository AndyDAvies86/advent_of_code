
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import functools

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

NESW = [(1,0),(0,1),(-1,0),(0,-1)]

#%%


def parselist(inputlist):
    mapdict = {}
    for ii in range(0,len(inputlist)+2):
        mapdict[(ii,0)] = '.'
    for ii in range(0,len(inputlist[0])+2):
        mapdict[(0,ii)] = '.'
    for ii in range(0,len(inputlist)):
        for jj in range(0,len(inputlist[0])):
            mapdict[(ii+1,jj+1)] = inputlist[ii][jj]
    return mapdict
#%%

def addpoint(mapdict,shapes,pos):
    for d in NESW:
        check = (pos[0]+d[0],pos[1]+d[1])
        for shape in shapes:
            if check in shape and mapdict[pos] == mapdict[check]:
                shape.append(pos)
                return shapes
    return shapes+[[pos]]

def perimeter(shape):
    per = 4*len(shape)
    for pos in shape:
        for d in NESW:
            check = (pos[0]+d[0],pos[1]+d[1])
            if check in shape:
                per = per-1
    return per

def joins(shapes,mapdict):
    for ii in range(0,len(shapes)):
        for jj in range(ii+1,len(shapes)):
            if mapdict[shapes[ii][0]] == mapdict[shapes[jj][0]]:
                for pos in shapes[ii]:
                    for d in NESW:
                        check = (pos[0]+d[0],pos[1]+d[1])
                        if check in shapes[jj]:
                            return shapes[:ii]+[shapes[ii]+shapes[jj]]+shapes[ii+1:jj]+shapes[jj+1:]
    return shapes

def part1(inputlist):
    mapdict = parselist(inputlist)
    shapes = []
    for ii in range(1,len(inputlist)+1):
        for jj in range(1,len(inputlist[0])+1):
            shapes = addpoint(mapdict,shapes,(ii,jj))
    # print('shapes1')
    go = True
    # print(shapes)
    while go:
        print('fix'+str(len(shapes)))
        newshapes = joins(shapes,mapdict)
        # print(newshapes)
        if len(newshapes) == len(shapes):
            go = False
        shapes = copy.deepcopy(newshapes)
    area = [len(x) for x in shapes]
    per = [perimeter(x) for x in shapes]
    # print(per)
    # print(area)
    # for ii in range(0,len(shapes)):
        # print(mapdict[shapes[ii][0]],per[ii],area[ii])
    return sum([area[x]*per[x] for x in range(0,len(area))])
            


#%%

def getshapes(inputlist):
    mapdict = parselist(inputlist)
    shapes = []
    for ii in range(1,len(inputlist)+1):
        for jj in range(1,len(inputlist[0])+1):
            shapes = addpoint(mapdict,shapes,(ii,jj))
    # print('shapes1')
    go = True
    # print(shapes)
    while go:
        print('fix'+str(len(shapes)))
        newshapes = joins(shapes,mapdict)
        # print(newshapes)
        if len(newshapes) == len(shapes):
            go = False
        shapes = copy.deepcopy(newshapes)
    return shapes

def addside(pos,d,mapdict):
    for d in NESW:
        check = (pos[0]+d[0],pos[1]+d[1])

def part2(inputlist):
    mapdict = parselist(inputlist)
    shapes = getshapes(inputlist)
    sides = []
    area = [len(x) for x in shapes]
    for shape in shapes:
        pass
        
    return sum([area[x]*sides[x] for x in range(0,len(area))])


#%%