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

file = open("2017day22.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("2017day22test.txt","r")
startb = file.read()
testlist = startb.split("\n")

#file = open("2017day20test2.txt","r")
#startc = file.read()
#testlist2 = startc.split("\n")


#if infected turn right else turn left
#if clean become infected else become clean
#forward 1 in direction

def setup(inputlist):
    length = len(inputlist)
    gridsize = int((length-1)/2)
    infected = []
    for i in range(0,length):
        for j in range(0,length):
            if inputlist[i][j] == '#':
                infected.append((j-gridsize,gridsize-i))
    return infected

def part1(inputlist,time):
    startinfected = setup(inputlist)
    infected = copy.deepcopy(startinfected)
    pos = np.array((0,0))
    directions = deque([np.array((1,0)),np.array((0,1)),np.array((-1,0)), np.array((0,-1))])
    directions.rotate(-1)
    t = 0
    count = 0
    print((t,len(infected),count))
    while t < time:
        infind = ((pos[0],pos[1]) in infected)
        if infind:
            directions.rotate(1)
            infected.remove((pos[0],pos[1]))
            pos = pos + directions[0]
        else:
            directions.rotate(-1)
            infected.append((pos[0],pos[1]))
            pos = pos + directions[0]
            count += 1
        t += 1
    return count
    
    
def part2repeat(inputlist,time):
    startinfected = setup(inputlist)
    infected = copy.deepcopy(startinfected)
    weakened = []
    flagged = []
    pos = np.array((0,0))
    directions = deque([np.array((1,0)),np.array((0,1)),np.array((-1,0)), np.array((0,-1))])
    directions.rotate(-1)
    t = 0
    count = 0
    history = [[infected,weakened,flagged,(pos[0],pos[1]),(directions[0][0],directions[0][1])]]
#    print((t,len(infected),count))
    while t < time:
        infind = ((pos[0],pos[1]) in infected)
        weakind = ((pos[0],pos[1]) in weakened)
        flagind = ((pos[0],pos[1]) in flagged)
        if infind:
            directions.rotate(1)
            infected.remove((pos[0],pos[1]))
            flagged.append((pos[0],pos[1]))
            pos = pos + directions[0]
        elif weakind:
            weakened.remove((pos[0],pos[1]))
            infected.append((pos[0],pos[1]))
            pos = pos + directions[0]
            count += 1
        elif flagind:
            directions.rotate(2)
            flagged.remove((pos[0],pos[1]))
            pos = pos + directions[0]
        else:
            directions.rotate(-1)
            weakened.append((pos[0],pos[1]))
            pos = pos + directions[0]
        t += 1
#        if t in [1,22]:
#            print('W'+str(weakened))
#            print('F'+str(flagged))
#            print('I'+str(infected))
#            print ('P'+str(pos))
#            print('D'+str(directions[0]))
        if [set(infected),set(weakened),set(flagged),(pos[0],pos[1]),(directions[0][0],directions[0][1])] in history:
            print("Repeat")
            return t,history.index([infected,weakened,flagged]),count
        history.append([set(infected),set(weakened),set(flagged),(pos[0],pos[1]),(directions[0][0],directions[0][1])])
    return t,0,count

def part2(inputlist,time):
    end,start,count = part2repeat(inputlist,time)
    print(end,start,count)
#    leadin = start
    remain = time-start
    loop = end-start
    leadout = remain % loop
    outcount = 0
    if leadout+start > 0:
        outcount = part2repeat(inputlist,leadout+start)
    cycles = int((remain-leadout)/loop)*count + outcount
    return cycles
        
def part2test(inputlist,time):
    startinfected = setup(inputlist)
    infected = copy.deepcopy(startinfected)
    weakened = []
    flagged = []
    pos = np.array((0,0))
    directions = deque([np.array((1,0)),np.array((0,1)),np.array((-1,0)), np.array((0,-1))])
    directions.rotate(-1)
    t = 0
    count = 0
    history = [[infected,weakened,flagged,(pos[0],pos[1]),(directions[0][0],directions[0][1])]]
#    print((t,len(infected),count))
    while t < time:
        infind = ((pos[0],pos[1]) in infected)
        weakind = ((pos[0],pos[1]) in weakened)
        flagind = ((pos[0],pos[1]) in flagged)
        if infind:
            directions.rotate(1)
            infected.remove((pos[0],pos[1]))
            flagged.append((pos[0],pos[1]))
            pos = pos + directions[0]
        elif weakind:
            weakened.remove((pos[0],pos[1]))
            infected.append((pos[0],pos[1]))
            pos = pos + directions[0]
            count += 1
        elif flagind:
            directions.rotate(2)
            flagged.remove((pos[0],pos[1]))
            pos = pos + directions[0]
        else:
            directions.rotate(-1)
            weakened.append((pos[0],pos[1]))
            pos = pos + directions[0]
        t += 1
        if t % 100000 == 0:
            print(int(t/100000))
#        if [infected,weakened,flagged,(pos[0],pos[1]),(directions[0][0],directions[0][1])] in history:
#            print("Repeat")
#            return t,history.index([infected,weakened,flagged]),count
#        history.append([infected,weakened,flagged])
    return t,0,count

resultlist = [part2test(testlist,x)[2] for x in range(0,100)]
resultchange = []
for i in range(0,99):
    if resultlist[i+1] > resultlist[i]:
        resultchange.append(i)
        
# C W I F 
       
def part2again(inputlist,time):
    count = 0
    infected = setup(inputlist)
    status = {}    
    pos = np.array((0,0))
    directions = deque([np.array((1,0)),np.array((0,1)),np.array((-1,0)), np.array((0,-1))])
    directions.rotate(-1)
    for point in infected:
        status[point] = 'I'
    t = 0
    while t < time:        
        point = (pos[0],pos[1])        
        if (pos[0],pos[1]) not in status:
            directions.rotate(-1)
            status[point] = 'W'
            pos = pos + directions[0]
        elif status[point] == 'I':
            directions.rotate(1)
            status[point] = 'F'
            pos = pos + directions[0]
        elif status[point] == 'W':
            status[point] = 'I'
            pos = pos + directions[0]
            count += 1
        elif status[point] == 'F':
            directions.rotate(2)
            status[point] = 'C'
            pos = pos + directions[0]
        else:
            directions.rotate(-1)
            status[point] = 'W'
            pos = pos + directions[0]
        
        t += 1
#        print((point,t,status[point]))
    return count