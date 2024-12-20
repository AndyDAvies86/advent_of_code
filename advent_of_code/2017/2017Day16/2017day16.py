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
initialstate = deque(alphabet[0:16])
mini = deque(alphabet[0:5])

file = open("2017day16.txt","r")
start = file.read()
startlist = start.split(",")


#
#
#file = open("2017day14test.txt","r")
#startb = file.read()
#testlist = startb.split("\n")

def spin(state,inputvalue):
    state.rotate(inputvalue)
    return state

def exchange(state,value1,value2):
    temp = state[value1]
    state[value1] = state[value2]
    state[value2] = temp
    return state

def partner(state,value1,value2):
    temp = state.index(value1)
    state[state.index(value2)] = value1
    state[temp] = value2
    return state


def part1(state,inputlist):
    for dance in inputlist:
        if dance[0] == 's':
            state = spin(state,int(dance[1:]))
        if dance[0] == 'p':
            state = partner(state,dance[1],dance[3])
        if dance[0] == 'x':
            pos = [int(x) for x in dance[1:].split("/")]
            state = exchange(state,pos[0],pos[1])
    return state


def findloop(state,inputlist):
    rounds = [''.join(state)]
    for i in range(0,999999999):
        state = part1(state,inputlist)
        if ''.join(state) in rounds:
            return i+1,rounds.index(''.join(state))
        rounds.append(''.join(state))

def part2(state,inputlist,rounds):
    looprounds,loopstart = findloop(state,inputlist)
    modrounds = (rounds-loopstart) % looprounds + loopstart
    for i in range(0,modrounds):
        state = part1(state,inputlist)
    return state
