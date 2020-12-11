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

file = open("2016day1.txt","r")
start = file.read()
startlist = start.split(", ")

#file = open("2016day1test.txt","r")
#startb = file.read()
#testlist = startb.split("\n")

direction = deque([(0,1),(-1,0),(0,-1),(1,0)])




def turnstep(pos,step,direction):
    if step[0] == "R":
        direction.rotate(1)
    else:
        direction.rotate(-1)
    pos = (pos[0]+int(step[1:])*direction[0][0],pos[1]+int(step[1:])*direction[0][1])
    return pos,direction


def allsteps1(inputlist):
    direction = deque([(0,1),(-1,0),(0,-1),(1,0)])
    pos = (0,0)
    for step in inputlist:
        pos,direction=turnstep(pos,step,direction)
    return pos

def allsteps2(inputlist):
    direction = deque([(0,1),(-1,0),(0,-1),(1,0)])
    pos = (0,0)
    stop = 0
    poslist=[]
    i = 0
    while stop == 0:
        if inputlist[i][0] == "R":
            direction.rotate(1)
        else:
            direction.rotate(-1)
        for j in range(0,int(inputlist[i][1:])):
            pos = (pos[0]+direction[0][0],pos[1]+direction[0][1])
            print(pos)
            if pos in poslist:
                return pos
            poslist.append(pos)
        
        i = (i+1) % len(inputlist)
        
    
    