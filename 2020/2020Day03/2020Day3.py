# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:49:48 2020

@author: Andy
"""

import pandas as pd
import numpy as np

inputfile = pd.read_csv("2020day3.txt",header=None)

start=np.array(inputfile)

def split(word): 
    return list(word) 

col = 0
counta = 0
for i in range (0, len(start)):
    if start[i,0][col] == '#' :
        counta = counta + 1
    col = (col + 3) % len(start[0,0])
    if col == len(start[0,0]) :
        col = 0

print(counta)

col = 0
countb = 0
for i in range (0, len(start)):
    if start[i,0][col] == '#' :
        countb = countb + 1
    col = (col + 1) % len(start[0,0])
    if col == len(start[0,0]) :
        col = 0

print(countb)


col = 0
countc = 0
for i in range (0, len(start)):
    if start[i,0][col] == '#' :
        countc = countc + 1
    col = (col + 5) % len(start[0,0])
    if col == len(start[0,0]) :
        col = 0

print(countc)


col = 0
countd = 0
for i in range (0, len(start)):
    if start[i,0][col] == '#' :
        countd = countd + 1
    col = (col + 7) % len(start[0,0])
    if col == len(start[0,0]) :
        col = 0

print(countd)

col = 0
counte = 0
for i in range (0, len(start), 2):
    if start[i,0][col] == '#' :
        counte = counte + 1
    col = (col + 1) % len(start[0,0])
    if col == len(start[0,0]) :
        col = 0

print(counte)

print(counta*countb*countc*countd*counte)