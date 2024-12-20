
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
startlist = start.split("\n\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n\n")


#%%

def parselist(inputlist):
    state = inputlist[0].split(' ')[-1]
    move = {}
    move = {x.split(' => ')[0]:x.split(' => ')[1] for x in inputlist[1].split('\n')}
    return state, move
#%%

def gen(state,move):
    newstate ='..'
    for ii in range(0,len(state)-5):
        if state[ii:ii+5] in move:
            next = move[state[ii:ii+5]]
            newstate = newstate+next
        else:
            newstate = newstate+'.'
    for jj in range(0,5):
        long = state[len(state)+jj-5:]+'.'*(jj)
        # print('e',jj,state[len(state)+jj-5:])
        if long in move:
            newstate = newstate+move[long]  
        else:
            newstate = newstate+'.'
    return newstate

def part1(inputlist):
    state,move = parselist(inputlist)
    # print(state)
    state = '.....'+state
    # print(0,state)
    for tt in range(0,20):
        state = gen(state,move)
        # print(tt+1,state)
    pots = []
    for ii in range(2,len(state)):
        if state[ii] == '#':
            pots.append(ii-5)
    return sum(pots)
#%%

def findloop(state,move):
    last = state.rfind('#')
    state = state[:last+1]
    steps = [state]
    t=0
    match = 0
    go = True
    while go and t<10000:
        t = t+1
        state = gen(state,move)
        last = state.rfind('#')
        state = state[:last+1]
        if state in steps:
            match = steps.index(state)
            go = False
        else:
            steps.append(state)
    return match,t



def part2(inputlist):
    state,move = parselist(inputlist)
    # print(state)
    state = '.....'+state
    # print(0,state)
    scores = []
    pots = []
    for ii in range(2,len(state)):
            if state[ii] == '#':
                pots.append(ii-5)
    scores.append(sum(pots))
    go = True
    tt = 0
    while tt < 500:
        tt = tt+1
        state = gen(state,move)
        last = state.rfind('#')
        state = state[:last+1]
        # print(tt+1,state)
        pots = []
        for ii in range(2,len(state)):
            if state[ii] == '#':
                pots.append(ii-5)
        print(tt,sum(pots))
        scores.append(sum(pots))
        if tt > 10 and scores[-1]-scores[-2] == scores[-2]-scores[-3]:
            go = False
            diff = scores[-1]-scores[-2]
    
    return (50000000000-tt)*diff+scores[-1]
#%%