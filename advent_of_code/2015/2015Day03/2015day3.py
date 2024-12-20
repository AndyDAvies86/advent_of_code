
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2015day3.txt","r")
start = file.read()
startlist = start.split("\n")

#file = open("2015day1test.txt","r")
#startb = file.read()
#testlist = startb.split("\n")

def part1(inputlist):
    dirs = {'v':np.array([0,-1]), '^':np.array([0,1]), '<':np.array([-1,0]), '>': np.array([1,0])}
    pos = np.array([0,0])
    houses = set()
    print(pos)
    houses.add((pos[0],pos[1]))
    print(houses)
    for step in inputlist:
        pos += dirs[step]
        houses.add((pos[0],pos[1]))
    return len(houses)

def part2(inputlist):
    dirs = {'v':np.array([0,-1]), '^':np.array([0,1]), '<':np.array([-1,0]), '>': np.array([1,0])}
    pos1 = np.array([0,0])
    pos2 = np.array([0,0])
    houses = set()
    houses.add((pos1[0],pos1[1]))
    for i in range(0,len(inputlist)):
        if i % 2 == 1:
            pos1 += dirs[inputlist[i]]
            houses.add((pos1[0],pos1[1]))
        else:
            pos2 += dirs[inputlist[i]]
            houses.add((pos2[0],pos2[1]))
    return len(houses)
    