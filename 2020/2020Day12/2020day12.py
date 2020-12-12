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

file = open("2020day12.txt","r")
start = file.read()

startlist = start.split("\n")

file = open("2020day12test.txt","r")
startb = file.read()
testlist = startb.split("\n")



def boat(inputlist):
    cleanlist = [[row[0],int(row[1:])] for row in inputlist]
    pos = np.array([0,0])
    E = np.array([1,0])
    N = np.array([0,1])
    W = np.array([-1,0])
    S = np.array([0,-1])
    dircheck = {'N':N,'E':E,'S':S,'W':W}
    direction = deque([E,N,W,S])
    for row in cleanlist:
        if row[0] in dircheck:
            pos += row[1]*dircheck[row[0]]               
        if row[0] == 'R' :
            direction.rotate(int(row[1]/90))
        if row[0] == 'L':
            direction.rotate(int(-row[1]/90))
        if row[0] == 'F':
            pos += row[1]*direction[0]
    return pos,(abs(pos[0])+abs(pos[1]))
 
def boat2(inputlist):
    cleanlist = [[row[0],int(row[1:])] for row in inputlist]
    bpos = np.array([0,0])
    wpos = np.array([10,1])
    E = np.array([1,0])
    N = np.array([0,1])
    W = np.array([-1,0])
    S = np.array([0,-1])
    dircheck = {'N':N,'E':E,'S':S,'W':W}
#    compass = [E,N,W,S]
    for row in cleanlist:
        print(row)
        if row[0] in dircheck:
            wpos += row[1]*dircheck[row[0]]               
        if row[0] == 'R' :
            for i in range(0,int(row[1]/90)):
                wpos = wpos[0]*S + wpos[1]*E
        if row[0] == 'L':
            for i in range(0,int(row[1]/90)):
                wpos = wpos[0]*N + wpos[1]*W
        if row[0] == 'F':
            bpos += row[1]*wpos
        print(bpos,wpos)
    return bpos,(abs(bpos[0])+abs(bpos[1]))
    
    
    
    