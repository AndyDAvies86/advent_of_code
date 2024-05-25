#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2018day10.txt","r")
start = file.read()
startlist = start.split("\n")
startinput = []
for row in startlist:
    startinput.append(row.split(" "))



file = open("2018day10test.txt","r")
startb = file.read()
testlist = startb.split("\n")
testinput = []
for row in testlist:
    testinput.append(row.split(" "))
#%%%

def parselist(inputlist):
    poslist = []
    vellist = []
    for row in inputlist:
        posstart = row.find("<")+1
        posend = row.find(">")
        posrow = row[posstart:posend]
        # print(posrow)
        poslist.append([int(x) for x in posrow.split(',')])
        velstart = row.find("vel")+10
        velrow = row[velstart:-1]
        # print(velrow)
        vellist.append([int(x) for x in velrow.split(",")])
    return poslist,vellist
#%%

def new_positions(inputlist,time):
    poslist,vellist=parselist(inputlist)
    nowpos = []
    for ii in range(0,len(poslist)):
        newpos = [
            poslist[ii][0]+time*vellist[ii][0],
            poslist[ii][1]+time*vellist[ii][1],
            ]
        nowpos.append(newpos)
    return nowpos

def create_array(nowpos,xmax,ymax):
    array = (" "*(xmax+1)+"\n")*(ymax+1)
    # print(array)
    for pos in nowpos:
        # print(pos)
        flick = pos[0]+(xmax+2)*pos[1]
        # print(flick,len(array))
        array = array[:flick]+'#'+array[flick+1:]
        # print(array)
    print(array)
#%%

def find_smallest(inputlist,max_time):
    xmax = 999999
    ymax = 999999
    minx = 0
    miny = 0
    for time in range(0,max_time):
        newpos=new_positions(inputlist,time)
        x=[]
        y=[]
        for pos in newpos:
            x.append(pos[0])
            y.append(pos[1])
        x_range = max(x)-min(x)
        y_range = max(y)-min(y)
        if x_range < xmax:
            xmax=x_range
            x_start=min(x)
            minx = time
        if y_range < ymax:
            ymax=y_range
            y_start = min(y)
            miny = time
    return xmax,ymax,minx,miny,x_start,y_start

    

#%%
def part1(inputlist,max_time):
    xmax,ymax,minx,miny,x_start,y_start = find_smallest(inputlist,max_time)
    print(xmax,ymax,minx,miny,x_start,y_start)
    for time in range(min(minx,miny),max(minx,miny)+1):
        print(time)
        nowpos = new_positions(inputlist,time)
        newpos = []
        for pos in nowpos:
            movepos=[pos[0]-x_start,pos[1]-y_start]
            newpos.append(movepos)
        create_array(newpos,xmax,ymax)

#%%
    
def part2(inputlist,max_time):
    return find_smallest(inputlist,max_time)[2]

#%%