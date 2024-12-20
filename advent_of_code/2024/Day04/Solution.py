
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy

#%%
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()
numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
numlist = [str(x) for x in range(0,10)]
#%%
file = open("inputfile.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n")


#%%

def parselist(inputlist):
    pass
#%%
def findx(inputlist):
    xlist = []
    for jj in range(0,len(inputlist)):
        for ii in range(0,len(inputlist[jj])):
            if inputlist[jj][ii] == 'X':
                xlist.append(np.array([ii,jj]))
    return xlist

def findwords(xlist):
    directions = []
    for ii in range(-1,2):
        for jj in range(-1,2):
            if ii != 0 or jj != 0:
                directions.append(np.array([ii,jj]))
    words = []
    for x in xlist:
        for point in directions:
            words.append([x + d*point for d in range(0,4)])
    return words

def wordcleanse(inputlsit,words):
    new_words = []
    h = len(inputlsit)
    w = len(inputlsit[0])
    for word in words:
        vert = [0<= word[y][1] < h for y in range(0,4)] 
        horiz = [0<= word[y][0] < w for y in range(0,4)] 
        if sum(vert+horiz) == 8:
            new_words.append(word)
    return new_words



def part1(inputlist):
    xlist = findx(inputlist)
    allwords = findwords(xlist)
    words = wordcleanse(inputlist,allwords)
    counter = 0
    for word in words:
        xmas = ''
        for char in word:
            xmas = xmas+inputlist[char[1]][char[0]]
        if xmas == 'XMAS':
            counter = counter+1
    return counter
#%%

def finda(inputlist):
    alist = []
    for jj in range(1,len(inputlist)-1):
        for ii in range(1,len(inputlist[jj])-1):
            if inputlist[jj][ii] == 'A':
                alist.append([ii,jj])
    return alist

def part2(inputlist):
    alist = finda(inputlist)
    counter = 0
    for a in alist:
        word1 = ''
        word2 = ''
        for ii in range(-1,2):
            word1 = word1+inputlist[a[1]+ii][a[0]+ii]
            word2 = word2+inputlist[a[1]+ii][a[0]-ii]
        if word1 in ['SAM','MAS'] and word2 in ['SAM','MAS']:
            counter = counter+1
    return counter
#%%