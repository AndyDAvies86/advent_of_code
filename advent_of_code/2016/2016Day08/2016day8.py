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

file = open("2016day8.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("2016day8test.txt","r")
startb = file.read()
testlist = startb.split("\n")

testscreen = [['.' for x in range(0,7)] for y in range(0,4)]

def cleanlist(inputlist):
    cleanlist = []
    for row in inputlist:
        newrow = row.split(" ")
        if newrow[0] == 'rotate':
            cleanlist.append([newrow[0],newrow[2][0],int(newrow[2][2:]), int(newrow[4])])
        if newrow[0] == 'rect': 
            newitem = newrow[1].split("x")
            cleanlist.append([newrow[0],int(newitem[0]),int(newitem[1])])
    return cleanlist

def rect(inputlist,x,y):
    newlist = copy.deepcopy(inputlist)
#    print(x,y)
    for i in range(0,y):
        for j in range(0,x):
#            print(i,j,newlist[i][j])
            newlist[i][j] = '#'
#            print(newlist[i][j])
#            print(newlist)
#            print(inputlist)
#    print(newlist)
    return newlist

def rotate(inputlist,axis,x,y):
    newlist = copy.deepcopy(inputlist)
    if axis == 'x':
        for i in range(0,len(inputlist)):
            newlist[(i+y)%len(inputlist)][x] = inputlist[i][x]
    if axis == 'y':
        for i in range(0,len(inputlist[0])):
            newlist[x][(i+y)%len(inputlist[0])] = inputlist[x][i]
    return newlist
    

def play(inputlist):
    screen = [['.' for x in range(0,50)] for y in range(0,6)]
    instructions = cleanlist(inputlist)
#    print(screen)
    for row in instructions:
#        print(row)
        if row[0] == 'rect':
            screen = rect(screen,row[1],row[2])
        if row[0] == 'rotate':
            screen = rotate(screen,row[1],row[2],row[3])
#        print(screen)
    count = 0
    for row in screen:
        count += row.count('#')
    return count,screen

def display(screen):
    for i in range(0,10):
        for row in screen:
            print(''.join(row[5*i:5*i+5]))
        print("XXXXXXXXXXXXX")
        