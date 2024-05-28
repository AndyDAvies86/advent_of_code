
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import json

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

#%%

def parse(inputlist):
    round = []
    cube = []
    for jj in range(0,len(inputlist[0])):
        round.append([jj,[]])
        cube.append([jj,[]])
        for ii in range(0,len(inputlist)):
            if inputlist[ii][jj] == 'O':
                round[jj][1].append(ii)
            if inputlist[ii][jj] == '#':
                cube[jj][1].append(ii)
    return round,cube

def tilt_north(round,cube):
    new_round = []
    for ii in range(0,len(round)):
        new_round.append([ii,[]])
        old_r = round[ii][1]
        old_c = [-1]+cube[ii][1]+[999999]
        for jj in range(1,len(old_c)):
            r_to_fit = [x for x in old_r if (x<old_c[jj] and x>old_c[jj-1])]
            new_r = [old_c[jj-1]+x+1 for x in range(0,len(r_to_fit))]
            # print(r_to_fit,new_r,new_round[ii])
            new_round[ii][1] = new_round[ii][1]+new_r
        # print(ii,old_r,old_c,new_round[ii][1])
    return new_round


def find_cubes(inputlist):
    cubes=[]
    for ii in range(0,len(inputlist)):
        for jj in range(0,len(inputlist[0])):
            cubes.append([ii,jj])
    return cubes

def q_spin(inputlist):
    round,cube=parse(inputlist)
    new_round = tilt_north(round,cube)
    rows = len(inputlist)
    cols = len(inputlist[0])
    # print(new_round)
    # print(cube)
    outlist = ['' for x in range(0,rows)]
    for ii in range(0,cols):
        for jj in range(0,rows):
            # print(new_round[jj],cube[jj])
            if ii in new_round[jj][1]:
                outlist[ii] += 'O'
            elif ii in cube[jj][1]:
                outlist[ii] += '#'
            else:
                outlist[ii] += '.'
    # print(outlist)
    return [''.join(outlist[-1-x][y] for x in range(0,rows))  for y in range(0,cols)]
    # return outlist
    
def spins(inputlist,num_spin):
    for ii in range(0,num_spin):
        inputlist=q_spin(inputlist)
    return inputlist

def cycle_search(inputlist):
    boards = [inputlist]
    state = inputlist
    rds = 0
    repeats=[]
    a = 0
    while a < 1:
        state = spins(state,4)
        if state in boards:
            repeat = boards.index(state)
            # repeats.append([rds,repeat])
            a = a+1
        boards.append(state)
        # rds = rds+1
        # if len(boards) % 1000 == 0:
        #     print(len(boards)//1000)
    return len(boards)-1-repeat,repeat

def cycleb(inputlist):
    a=0
    b=100
    for ii in range(0,1000000):
        if spins(inputlist,b-4)==spins(inputlist,b+4*ii):
            return a
        a = a+1
        print(a)
        if a%1000 == 0:
            print(a//1000)






#%%        

def part1(inputlist):
    round,cube=parse(inputlist)
    new_round = tilt_north(round,cube)
    # return new_round
    score = 0
    for col in new_round:
        score_add = [len(inputlist)-x for x in col[1]]
        score = score + sum(score_add)
    return score



def part2(inputlist):
    cycle_size,first_rep = cycle_search(inputlist)
    state=spins(inputlist,4*(1000000000%cycle_size + cycle_size*((first_rep//cycle_size)+1)))
    round,cube=parse(state)
    score = 0
    for col in round:
        score_add = [len(inputlist)-x for x in col[1]]
        score = score + sum(score_add)
    return score



#%%