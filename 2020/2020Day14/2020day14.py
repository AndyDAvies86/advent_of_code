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

file = open("2020day14.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("2020day14test.txt","r")
startb = file.read()
testlist = startb.split("\n")

file = open("2020day14test2.txt","r")
startc = file.read()
testlist2 = startc.split("\n")

def cleanlist(inputlist):
    outputlist = []
    for row in inputlist:
        newrow = row.split(" ")
        outputlist.append([newrow[0],newrow[2]])
    return outputlist

def part1 (inputlist):
    clean = cleanlist(inputlist)
    mem = {}
    mask = 'X'*36
    for row in clean:
        if row[0] == 'mask':
            mask = row[1]
        if row[0][0:3] == 'mem':
            lookup = int(row[0][4:-1])
#            print(lookup)
            valuepre = bin(2**36+int(row[1]))[3:]
#            print(valuepre)
#            print(len(valuepre))
            valueout = ''
            for i in range(0,36):
                if mask[i] == "X":
                    valueout += valuepre[i]
                else:
                    valueout += mask[i]
            value = int(valueout,2)
#            print(value)
            mem[lookup] = value
    return sum(mem.values())
            

def splitx(maskin,lookup):
    lookupstart = bin(2**36+lookup)[3:]
    firstpass = ''
    for i in range(0,36):
        if maskin[i] == "1":
            firstpass += '1'
        else:
            firstpass += lookupstart[i]               
    outlist = [firstpass]
    print(outlist)
    for i in range(0,36):
        tempout = []
        for row in outlist:
#            maskval = ''
            if maskin[i] == "X":
                tempout += [row[:i]+'0'+row[i+1:],row[:i]+'1'+row[i+1:]]
            else:
                tempout.append(row)
        outlist = copy.deepcopy(tempout)
    outvalues = [int(x,2) for x in outlist]
    print(outvalues)
    return outvalues
            
        

def part2 (inputlist):
    clean = cleanlist(inputlist)
    mem = {}
    mask = []
    for row in clean:
#        print(row)
        if row[0] == 'mask':
            mask = row[1]
        if row[0][0:3] == 'mem':
            lookupstart = int(row[0][4:-1])
#            print(lookup)
            lookuplist = splitx(mask,lookupstart)
            for l in lookuplist:
                mem[l] = int(row[1])
#    full = []
#    for key in mem.keys():
#        full += mem[key]
#    print(mem)
    return sum(mem.values())
        
            