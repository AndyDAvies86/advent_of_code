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
import anytree
import networkx

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2020day8.txt","r")
start = file.read()
startlist = start.split("\n")


file = open("2020day8test.txt","r")
startb = file.read()
testlist = startb.split("\n")

def splitlist(inputlist):
    codelist = []
    for row in inputlist:
        temprow = row.split(" ")
        codelist.append([temprow[0],int(temprow[1])])
    return codelist


def runcode(codelist):
       
    accumulator = 0
    
    i=0
    lines = set([])
    while i not in lines and i < len(codelist):
#        print(i)
        lines.add(i)
        row = codelist[i]
        if row[0] == 'acc':
            accumulator += row[1]
            i += 1
        if row[0] == 'jmp':
            i += row[1]
        if row[0] == 'nop':
            i += 1
    return i,accumulator

def runcodepart1(inputlist) :
    steps, accum = runcode(splitlist(inputlist))
    return steps, accum

def runcodepart2(inputlist):
    codelist = splitlist(inputlist)
    
#    print(codelist[0])
    
    i = 0
    while i < len(codelist):
        stop = 0
        templist = []
#        print(templist[0])
        
        for j in range(0,len(codelist)):
            if i != j:
                templist.append(codelist[j])
            else:
                if codelist[j][0] == 'jmp':
                    templist.append(['nop',codelist[j][1]])
                elif codelist[j][0] == 'nop':
                    templist.append(['jmp',codelist[j][1]])
                else:
                    templist.append(codelist[j])
                
            
        step,accum = runcode(templist)
#        print((templist[0],codelist[0],i,step,accum))
        if step == len (codelist):
            return step, accum
        i += 1 
        
        