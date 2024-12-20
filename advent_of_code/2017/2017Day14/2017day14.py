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

#file = open("2017day14.txt","r")
#start = file.read()
#startlist = start.split("\n")
#
#
#file = open("2017day14test.txt","r")
#startb = file.read()
#testlist = startb.split("\n")

start = 'stpzcrnm'

test = 'flqrgnkx'



def twist(numlist,length,skipsize,pos):
    numlength = len(numlist)
    numdeque = deque(numlist)
    numdeque.rotate(-pos)
    twistslice = deque(it.islice(numdeque,length))
    fixslice = deque(it.islice(numdeque,length,numlength))
    twistslice.reverse()
    newnumlist = twistslice+fixslice
    newnumlist.rotate(pos)
    pos = (pos + length + skipsize) % numlength
    skipsize += 1
    numlist = list(newnumlist)
    return numlist,skipsize,pos


def knothash(numlist,inputlist,skipsize,pos):
    listlength=len(numlist)
    for entry in inputlist:
        if entry <= listlength:
            numlist,skipsize,pos = twist(numlist,entry,skipsize,pos)
        else:
            print("Length out of range")
    return numlist,skipsize,pos

def inputcorrect(inputlist):
    newinput = [ord(x) for x in inputlist]
    newinput += [17,31,73,47,23]
    return newinput

def densehashelement(sparsehashlist):
    newhash = sparsehashlist[0]
    for i in range(1,16):
        newhash = newhash ^ sparsehashlist[i]
    return newhash
        

def fullknothash(inputlist):
    pos = 0
    skipsize = 0
    newlist = inputcorrect(inputlist)
    numlist = [x for x in range(0,256)]
    for i in range(0,64):
        numlist,skipsize,pos = knothash(numlist,newlist,skipsize,pos)
    
    densehash = []
    
    for i in range(0,16):
        sparsehash = numlist[16*i:16*(i+1)]
        densehash.append(densehashelement(sparsehash))
    wordout = ''
    for x in densehash:
        wordout += hex(256+x)[3:]
    return wordout

def fullinputlist(inputstring):
    inputset = []
    for i in range(0,128):
        inputset.append(inputstring+'-'+str(i))
    return inputset

def fullgrid(inputstring):
    count = 0
    grid = []
    inputset = fullinputlist(inputstring)
    for inputvalue in inputset:
        word = fullknothash(inputvalue)
        binvalue = bin(2**128+int(word,16))[3:]
        count += binvalue.count('1')
        grid.append([int(x) for x in binvalue])
    return count,grid

def initialfield(inputfield):
    field = [[99999 for x in range(0,130)] for y in range(0,130)]
#    print(field[0][0])
    for i in range(1,129):
        for j in range(1,129):
            field[i][j] = 88888 + (11111*(1-inputfield[i-1][j-1]))
   
    return field

def countregions(inputstring):
    dummy,origfield = fullgrid(inputstring)
    field = initialfield(origfield)
    setofregions = set(x for y in field for x in y)
#    print(setofregions)
    fieldnum = 1
    for i in range(1,129):
        for j in range(1,129):
#            print(fieldnum)
            if field[i][j] < 99999:
#                print(field[i][j])
                field[i][j] = min(field[i-1][j],field[i+1][j],field[i][j-1],field[i][j+1],field[i][j])
                if field [i][j] == 88888:
                    field[i][j] = fieldnum
                    fieldnum += 1
    stop = 0
    while stop == 0:
        oldfield = copy.deepcopy(field)
        for i in range(1,129):
            for j in range(1,129):
                if field[i][j] < 99999:
                    field[i][j] = min(field[i-1][j],field[i+1][j],field[i][j-1],field[i][j+1],field[i][j])
        newset = set(x for y in field for x in y)
        if oldfield == field:
            stop = 1
        else:
            setofregions = newset
#            print(setofregions,len(setofregions))
    return len(setofregions)-1,field

