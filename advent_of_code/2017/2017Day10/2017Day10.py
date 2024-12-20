# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:27:09 2020

@author: Andy
"""





import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it


#alphabet = 'abcdefghijklmnopqrstuvwxyz'
#alphaup = alphabet.upper()

file = open("2017day10.txt","r")
start = file.read()
startlist = start.split(",")
startint = [int(x) for x in startlist]

testint = [3,4,1,5]
#
#file = open("2017day14test.txt","r")
#startb = file.read()
#testlist = startb.split("\n")


def twist(numlist,length,skipsize,pos):
    numlength = len(numlist)
    twistslice = deque(it.islice(numlist,length))
    fixslice = deque(it.islice(numlist,length,numlength))
    twistslice.reverse()
    newnumlist = twistslice+fixslice
    newnumlist.rotate(-length-skipsize)
    pos = pos - length - skipsize
    skipsize += 1
    return newnumlist,skipsize,pos
    
    
    pass


def knothash(listlength,inputlist):
    numlist = deque(range(listlength))
    skipsize = 0
    pos = 0
    for entry in inputlist:
#        print(numlist)
        if entry <= listlength:
            numlist,skipsize,pos = twist(numlist,entry,skipsize,pos)
        else:
            print("Length out of range")
#    print(numlist,pos)
    return numlist[pos%listlength]*numlist[(pos+1)%listlength]







