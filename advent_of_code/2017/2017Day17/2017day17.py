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

start = 367

test = 3

initialstate = deque([0])

def turnkey(state,inputvalue,turn):
#    print(state)
    state.rotate(-inputvalue)
#    print(state)
    state.append(turn)
#    print(state)
    return state    

def unlockpart1(inputvalue,turns):
    initialstate = deque([0])
    state = initialstate
    for i in range(0,turns):
        state = turnkey(initialstate,inputvalue,i+1)
#        print(state)
    return state[0]

def unlockpart2(inputvalue,turns):
    initialstate = deque([0])
    state = initialstate
    for i in range(0,turns):
        state = turnkey(initialstate,inputvalue,i+1)
#        print(state)
    return state[state.index(0)+1]




