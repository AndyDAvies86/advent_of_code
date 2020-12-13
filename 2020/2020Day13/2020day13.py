# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 09:46:31 2020

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

file = open("2020day13.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("2020day13test.txt","r")
startb = file.read()
testlist = startb.split("\n")

def part1(inputlist):
    start= int(inputlist[0])
    now = start + 0
    buses =[]
    for bus in inputlist[1].split(","):
        if bus != "x":
            buses.append(int(bus))
#    print(now,buses)
    stop = 0
    while stop == 0:
        for bus in buses:
            if now % bus == 0:
                return ((now,now-start,bus,(now-start)*bus))
        now += 1
        
def findnew(mod,rem,buses,i):
    j = 0
    while j >= 0:
        if (rem + j*mod) % buses[i][0] == buses[i][1] % buses[i][0]:
            newmod = mod*buses[i][0]
            newrem = (rem + j*mod) % newmod
            return newrem,newmod
        j += 1
#        print(j)

def part2(inputlist):
    buses = []
    allbus = inputlist[1].split(",")
    for bus in allbus:
        if bus != "x":
            buses.append([int(bus),allbus.index(bus)])
    print(buses)
    ""
    mod = buses[0][0]
    rem = 0
    for i in range(1,len(buses)):
        rem,mod =findnew(mod,rem,buses,i)
        print(rem,mod)
    return mod-rem
                
        
    
#    t = 0
#    while t >= 0:
#        bustest = [(t+bus[1]) % bus[0] == 0 for bus in buses]
#        if False not in bustest:
#            return t
#        if t % 1000000:
#            print(int(t/1000000))
#        t+=1
    