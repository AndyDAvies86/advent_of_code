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

file = open("2017day21.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("2017day21test.txt","r")
startb = file.read()
testlist = startb.split("\n")

#file = open("2017day20test2.txt","r")
#startc = file.read()
#testlist2 = startc.split("\n")

begin = ['.#.','..#','###']

def instructions(inputlist):
    outlist = {}
    for row in inputlist:
        newrow = row.replace("/","").split(" => ")
        print(newrow)
        outlist[newrow[0]] = newrow[1]
        if len(newrow[0]) == 9:
            maniprow = [newrow[0][3*x:3*x+3] for x in range(0,3)]
            revrow = ''.join([maniprow[x][::-1] for x in range(0,3)])
            print(revrow)
            for j in range(0,3):
                rotrow = maniprow[j]
#            for j in rnage(0,4)
                
        
    return outlist


def split(screen,lookup):
    newscreen = []    
    if len(screen) % 2 == 0:
        for i in range (0,len(screen),2):
            newscreen += ['','','']
            for j in range (0,len(screen),2):
                compare = screen[i][j:j+2]+screen[i+1][j:j+2]
                toadd = lookup[compare]
                newscreen[int(3*i/2)] += toadd[0:3]
                newscreen[int(3*i/2+1)] += toadd[3:6]
                newscreen[int(3*i/2+2)] += toadd[6:9]
    if len(screen) % 3 == 0:
        for i in range (0,len(screen),3):
            newscreen += ['','','','']
            for j in range (0,len(screen),3):
                compare = screen[i][j:j+3]+screen[i+1][j:j+3]+screen[i+2][j:j+3]
                print(compare)
                toadd = lookup[compare]
                print(toadd)
                newscreen[int(4*i/3)] += toadd[0:4]
                newscreen[int(4*i/3+1)] += toadd[4:8]
                newscreen[int(4*i/3+2)] += toadd[8:12]
                newscreen[int(4*i/3+3)] += toadd[12:16]
        return newscreen
                

def part1(inputlist):
    lookup = instructions(inputlist)
    screen = ['.#.','..#','###']
    screen = split(screen,lookup)
    print(str(screen).replace(',','\n'))