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

file = open("2016day2.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("2016day2test.txt","r")
startb = file.read()
testlist = startb.split("\n")


def codelookup(inputlist):
#    keys = np.matrix('1 2 3;4 5 6;7 8 9')
    pos = np.matrix('1 1')
    movedict = {'U' : np.matrix('0 -1'),
                'D' : np.matrix('0 1'),
                'L' : np.matrix('-1 0'),
                'R' : np.matrix('1 0')}
    outcode = ''
    for row in inputlist:
        for char in row:
            pos = pos + movedict[char]
            x = min(2,max(0,pos.item(0)))
            y = min(2,max(0,pos.item(1)))
#            print(pos,x,y,char)
            pos = np.matrix(str(x)+' '+str(y))
        outcode += str(pos.item(1)*3+pos.item(0)+1)
#        print(outcode)
    return outcode

def codelookup2(inputlist):
    keys = '  1   234 56789 ABC   D  '
    pos = np.matrix('-2 0')
    movedict = {'U' : np.matrix('0 -1'),
                'D' : np.matrix('0 1'),
                'L' : np.matrix('-1 0'),
                'R' : np.matrix('1 0')}
    outcode = ''
    for row in inputlist:
        for char in row:
            newpos = pos + movedict[char]
            x = newpos.item(0)
            y = newpos.item(1)
            print(pos,x,y,char)
            if abs(x)+abs(y) <= 2 :
                pos = np.matrix(str(x)+' '+str(y))
        outcode += (keys[pos.item(1)*5+pos.item(0)+12])
        print(outcode)
    return outcode

