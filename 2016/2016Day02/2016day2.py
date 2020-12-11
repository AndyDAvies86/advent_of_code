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

moves = {}
nudge = {'U':-3, 'D':3, 'L':-1, 'R':1}
for a in range(1,10):
    for step in ['U','D','L','R']:
        moves[(step,a)] = a + nudge[step]
for a in moves:
    if moves[a]>9:
        moves[a] = a[1]
    if moves[a] < 0 :
        moves[a] = a[1]
        


def U(value):
    return [max(value[0]-1,0),value[1]]

def L(value):
    return [value[0],max(value[1]-1,0)]
    
def D(value):
    return [min(value[0]+1,2),value[1]]
    
def R(value):
    return [value[0],min(value[1]+2,0)]




        

def codelookup(inputlist):
    keypad = {}
    addresses = [(x,y) for x in range(0,3) for y in range(0,3)]
    for a in addresses:
#        print(a)
        keypad[a] = a[0]*3+a[1]+1
    start = [1,1]
    outcode = ''
    for row in inputlist:
        for char in row:
            print(char,start)
            exec('start = '+char+'('+str(start)+')')            
            print(start)
#        start = exec(instructions)
        print(start)
#        outcode += str(keypad[tuple(start)])
    return outcode