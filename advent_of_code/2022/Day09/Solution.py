
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
#%%
file = open("inputfile.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n")

file = open("inputtest2.txt","r")
startc = file.read()
testlist2 = startc.split("\n")


#%%
def instructions(inputlist):
    moves = {'U': [0,1], 'D':[0,-1], 'L':[-1,0], 'R':[1,0]}
    #steps = [[int(x.split(" ")[1])*y for y in moves[x.split(" ")[0]]] for x in inputlist]
    steps = []
    for row in inputlist:
        step = row.split(" ")
        for ii in range(0,int(step[1])):
            steps.append(moves[step[0]])
    return steps
#%%



#%%

#%%
def part1(inputlist):
    tails = set([(0,0)])
    steps = instructions(inputlist)
    H=[0,0]
    T=[0,0]
    for step in steps:
        H = [H[0]+step[0],H[1]+step[1]]
        #print(H)
        if max(abs(H[0]-T[0]),abs(H[1]-T[1])) > 1:
            gap = [H[0]-T[0],H[1]-T[1]]
            if gap[0] == 0:
                T[1] += int(gap[1]/abs(gap[1]))
            elif gap[1] == 0:
                T[0] += int(gap[0]/abs(gap[0]))
            else:
                for move in [[1,1],[-1,1],[1,-1],[-1,-1]]:
                    if max(abs(H[0]-T[0]-move[0]),abs(H[1]-T[1]-move[1])) <= 1:
                        T = [T[0]+move[0],T[1]+move[1]]
                        break
        tails.add((T[0],T[1]))
        #print(H,T)
    return len(tails)
#%%

def part2(inputlist):
    tails = set([(0,0)])
    steps = instructions(inputlist)
    knots = [[0,0] for x in range(0,10)]
    for step in steps:
        knots[0] = [knots[0][0]+step[0],knots[0][1]+step[1]]
        for ii in range(0,9):
            if max(abs(knots[ii][0]-knots[ii+1][0]),abs(knots[ii][1]-knots[ii+1][1])) > 1:
                gap = [knots[ii][0]-knots[ii+1][0],knots[ii][1]-knots[ii+1][1]]
                if gap[0] == 0:
                    knots[ii+1][1] += int(gap[1]/abs(gap[1]))
                elif gap[1] == 0:
                    knots[ii+1][0] += int(gap[0]/abs(gap[0]))
                else:
                    for move in [[1,1],[-1,1],[1,-1],[-1,-1]]:
                        if max(abs(knots[ii][0]-knots[ii+1][0]-move[0]),abs(knots[ii][1]-knots[ii+1][1]-move[1])) <= 1:
                            knots[ii+1] = [knots[ii+1][0]+move[0],knots[ii+1][1]+move[1]]
                            break
        tails.add((knots[9][0],knots[9][1]))
        #print(H,T)
    return len(tails)
#%%