
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
        mapdict[(ii,len(inputlist)+1)] = '.'
    for ii in range(0,len(inputlist[0])+2):
        mapdict[(0,ii)] = '.'
        mapdict[(len(inputlist)+1,ii)] = '.'
    for ii in range(0,len(inputlist)):
        for jj in range(0,len(inputlist[0])):
            mapdict[(ii+1,jj+1)] = inputlist[ii][jj]
    return mapdict
#%%

# def addpoint(mapdict,shapes,pos):
#     for d in NESW:
#         check = (pos[0]+d[0],pos[1]+d[1])
#         for shape in shapes:
#             if check in shape and mapdict[pos] == mapdict[check]:
#                 shape.append(pos)
#                 return shapes
#     return shapes+[[pos]]

def perimeter(shape):
    per = 4*len(shape)
    for pos in shape:
        for d in NESW:
            check = (pos[0]+d[0],pos[1]+d[1])
            if check in shape:
                per = per-1
    return per

# def joins(shapes,mapdict):
#     for ii in range(0,len(shapes)):
#         for jj in range(ii+1,len(shapes)):
#             if mapdict[shapes[ii][0]] == mapdict[shapes[jj][0]]:
#                 for pos in shapes[ii]:
#                     for d in NESW:
#                         check = (pos[0]+d[0],pos[1]+d[1])
#                         if check in shapes[jj]:
#                             return shapes[:ii]+[shapes[ii]+shapes[jj]]+shapes[ii+1:jj]+shapes[jj+1:]
#     return shapes

def firstpos(mapdict):
    h = max([y[0] for y in mapdict])+1
    w = max([y[1] for y in mapdict])+1
    # print(h,w)
    for ii in range(1,h):
        for jj in range(1,w):
            # print(mapdict[(ii,jj)])
            if mapdict[(ii,jj)] != '.':
                # print(ii,jj)
                return (ii,jj)
    return (0,0)

def addpos(shape,sameletter):
    # print('x',shape)
    newshape = copy.deepcopy(shape)
    for pos in sameletter:
        if pos not in newshape:
            for d in NESW:
                # print(pos,d)
                if (pos[0]+d[0],pos[1]+d[1]) in newshape and pos not in newshape:
                    # print(shape)
                    newshape.append(pos)
    return newshape


def newshape(mapdict):
    shape = []
    # print(mapdict)
    pos = firstpos(mapdict)
    # print('e',shape,pos)
    if pos == (0,0):
        return shape
    shape.append(pos)
    # print('a',shape)
    sameletter = [x for x in mapdict if mapdict[x] == mapdict[pos]]
    # print('sl',mapdict[pos],sameletter)
    go = True
    while go:
        # print('pre',mapdict[shape[0]],len(shape))
        newshape = addpos(shape,sameletter)
        # print('check',mapdict[newshape[0]],len(shape),len(newshape))
        if len(shape) == len(newshape):
            # print(mapdict[newshape[0]],'ns',newshape)
            # print('sl',sameletter)
            go = False
        shape = copy.deepcopy(newshape)
    return shape

# def shapes()

def part1(inputlist):
    c = len(inputlist)*len(inputlist[0])
    # print(c)
    mapdict = parselist(inputlist)
    shapes = []
    newmapdict = copy.deepcopy(mapdict)
    while sum([len(x) for x in shapes]) < c:
        shape = newshape(newmapdict)
        shapes.append(shape)
        for pos in shape:
            newmapdict[pos] = '.'
        # print(shape)
        # print(len(shapes),sum([len(x) for x in shapes]),mapdict[shape[0]],len(shape),perimeter(shape))
    area = [len(x) for x in shapes]
    per = [perimeter(x) for x in shapes]
    return sum([area[x]*per[x] for x in range(0,len(area))])

#%%

def corners(pos,shape):
    check = np.zeros((2,2))
    for ii in range(0,2):
        for jj in range(0,2):
            if (pos[0]+ii,pos[1]+jj) in shape:
                check[ii][jj] = 1
    if np.sum(check) in (0,4):
        return 0
    elif np.sum(check) in (1,3):
        return 1
    elif check[0][0] == check[1][1]:
        return 2
    return 0
def sidecount(shape):
    # print(shape)
    top = min([x[0] for x in shape])
    bottom = max([x[0] for x in shape])
    left = min([x[1] for x in shape])
    right = max([x[1] for x in shape])
    # edges = (set(),set(),set(),set())
    shapeside = 0
    for ii in range(top-1,bottom+1):
        for jj in range(left-1,right+1):
            pos = [ii,jj]
            corn = corners(pos,shape)
            # print(pos,corn)
            shapeside = shapeside+corn
    return shapeside

def part2(inputlist):
    c = len(inputlist)*len(inputlist[0])
    # print(c)
    mapdict = parselist(inputlist)
    shapes = []
    newmapdict = copy.deepcopy(mapdict)
    while sum([len(x) for x in shapes]) < c:
        shape = newshape(newmapdict)
        shapes.append(shape)
        for pos in shape:
            newmapdict[pos] = '.'
        # print(shape)
        # print(len(shapes),sum([len(x) for x in shapes]),mapdict[shape[0]],len(shape),perimeter(shape))
    area = [len(x) for x in shapes]

    sides = [sidecount(x) for x in shapes]
    print(len(area),min(area),area)
    print(len(sides),min(sides),sides)
    return sum([area[x]*sides[x] for x in range(0,len(area))])


#%%