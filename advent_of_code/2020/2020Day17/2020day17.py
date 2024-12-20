
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2020day17.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("2020day17test.txt","r")
startb = file.read()
testlist = startb.split("\n")

#file = open("2020day16test2.txt","r")
#startc = file.read()
#testlist = startb.split("\n")
#
def setup(inputlist,cycles):
    print((len(inputlist)+2*cycles,len(inputlist[0])+2*cycles,2*cycles+1))
    field = np.zeros((len(inputlist)+2*cycles,len(inputlist[0])+2*cycles,2*cycles+1), dtype = int)
    for i in range(0,len(inputlist)):
        for j in range(0,len(inputlist[0])):
            if inputlist[i][j] == '#':
                field[i+cycles][j+cycles][cycles] = 1
    return field

def turn(inputfield):
    field = copy.deepcopy(inputfield)
    x = len(field)
    y = len(field[0])
    z = len(field[0][0])
    for i in range(0,x):
        for j in range(0,y):
            for k in range(0,z):
                adjacency = -inputfield[i][j][k]
                for ii in range(max(0,i-1),min(x,i+2)):
                    for jj in range(max(0,j-1),min(y,j+2)):
                        for kk in range(max(0,k-1),min(z,k+2)):
                            adjacency += inputfield[ii,jj,kk]
                if adjacency not in [2,3] and inputfield[i][j][k] == 1:
                    field[i][j][k] = 0
                elif adjacency == 3 and inputfield[i][j][k] == 0:
                    field[i][j][k] = 1
    return field

def part1(inputlist,cycles):
    field = setup(inputlist,cycles)
    for i in range(0,cycles):
        field = turn(field)
    return field, np.sum(field)
                            
def setup2(inputlist,cycles):
    print((len(inputlist)+2*cycles,len(inputlist[0])+2*cycles,2*cycles+1))
    field = np.zeros((len(inputlist)+2*cycles,len(inputlist[0])+2*cycles,2*cycles+1,2*cycles+1), dtype = int)
    for i in range(0,len(inputlist)):
        for j in range(0,len(inputlist[0])):
            if inputlist[i][j] == '#':
                field[i+cycles][j+cycles][cycles][cycles] = 1
    return field

def turn2(inputfield):
    field = copy.deepcopy(inputfield)
    x = len(field)
    y = len(field[0])
    z = len(field[0][0])
    w = len(field[0][0][0])
    for i in range(0,x):
        for j in range(0,y):
            for k in range(0,z):
                for l in range(0,w):
                    adjacency = -inputfield[i][j][k][l]
                    for ii in range(max(0,i-1),min(x,i+2)):
                        for jj in range(max(0,j-1),min(y,j+2)):
                            for kk in range(max(0,k-1),min(z,k+2)):
                                for ll in range(max(0,l-1),min(w,l+2)):
                                    adjacency += inputfield[ii,jj,kk,ll]
                    if adjacency not in [2,3] and inputfield[i][j][k][l] == 1:
                        field[i][j][k][l] = 0
                    elif adjacency == 3 and inputfield[i][j][k][l] == 0:
                        field[i][j][k][l] = 1
    return field

def part2(inputlist,cycles):
    field = setup2(inputlist,cycles)
    for i in range(0,cycles):
        field = turn2(field)
    return field, np.sum(field)
                            