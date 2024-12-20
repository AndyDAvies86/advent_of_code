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

file = open("2017day19.txt","r")
start = file.read()

startlist = start.split("\n")

file = open("2017day19test.txt","r")
startb = file.read()
testlist = startb.split("\n")

def straight(inputlist,oldpath,oldpos,direction,allelements,steps):
    path = copy.deepcopy(oldpath)
    pos = copy.deepcopy(oldpos)
#    print((path,pos,direction,inputlist[pos[0]][pos[1]]))#
    pos += direction
#    print(pos)
    steps += 1
#    print(inputlist[pos[0]][pos[1]])
    if inputlist[pos[0]][pos[1]] in alphaup:
        path += inputlist[pos[0]][pos[1]]
        print(path)
        if len(path) == len(allelements):
            return path,pos
    while inputlist[pos[0]][pos[1]] != '+':
        pos += direction
#        print(pos)
        steps+=1
#        print(inputlist[pos[0]][pos[1]])
        if inputlist[pos[0]][pos[1]] in alphaup:
            path += inputlist[pos[0]][pos[1]]
#            print(path)
            if len(path) == len(allelements):
                return path,pos,steps
    return path,pos,steps

def turn(inputlist,pos,direction):
#    print('Direction: '+str(direction))
    directions = [np.array([1,0]),np.array([0,1]),np.array([-1,0]),np.array([0,-1])]
    for point in directions:
#        print('Point: '+str(point))
        if abs(point[0]) != abs(direction[0]) and abs(point[1]) != abs(direction[1]):
#            print("yes")
            trypoint = pos+point
#            print(pos,trypoint)
#            print(inputlist[trypoint[0]][trypoint[1]])
            if (trypoint[0] in range(0,len(inputlist))) and (trypoint[1] in range(0,len(inputlist[trypoint[0]]))):
                if inputlist[trypoint[0]][trypoint[1]] in alphaup+'-|':
                    return point
                    

def solve1(inputlist):
    path =''
    steps = 0
    start = inputlist[0].index('|')
    allelements = set([x for x in ''.join(inputlist)]).intersection(set(alphaup))
#    print(allelements,maxletter)
#    print(start)
    pos = np.array([0,start])
    direction = np.array([1,0])
#    directions = [np.array([1,0]),np.array([0,1]),np.array([-1,0]),np.array([0,-1])]
#    print(pos[0],pos[1])
#    print(inputlist[pos[0]][pos[1]])
    while len(path)<len(allelements):
#    ii = 0
#    while ii < 4:
#        print(pos,direction)
        path,pos,steps = straight(inputlist,path,pos,direction,allelements,steps)
#        print(path)
        direction = turn(inputlist,pos,direction)
#        for point in directions:
#            if (point != direction).all and (point != -direction).all:
#                trypoint = pos+point
##                print(pos,trypoint)
##                print(inputlist[trypoint[0]][trypoint[1]])
#                if (trypoint[0] in range(0,len(inputlist))) and (trypoint[1] in range(0,len(inputlist[trypoint[0]]))):
#                    if inputlist[trypoint[0]][trypoint[1]] in alphaup+'-|':
#                        direction = point
#                        print(direction)
##                        pos += direction
#        ii += 1
#    print("Final:"+str((path,pos)))
#    print(path)
    return path,steps+1
        
    
    