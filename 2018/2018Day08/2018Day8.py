# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:46:13 2020

@author: Andy
"""



import pandas as pd
import numpy as np
import re
import datetime as dt

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2018day8.txt","r")
start = file.read()
startlist = start.split(" ")
startint = []
for row in startlist:
    startint.append(int(row))


file = open("2018day8test.txt","r")
startb = file.read()
testlist = startb.split(" ")
testint = []
for row in testlist:
    testint.append(int(row))

def summeta(inlist):
    nodestofind = [0]
    metasum = 0
    metatofind = [0]
    for pos in inlist:
        if sum(nodestofind) + sum(metatofind) == 0:
            nodestofind[0] = pos
            break
        if sum(nodestofind) == 0:
            metasum += pos
            for i in range(0,len(metatofind)):
                if metatofind[-(1+i)] > 0:
                    metatofind[-(-1+i)] -= 1
                    break
        
        
        
