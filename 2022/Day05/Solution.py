
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
startlist = start.split("\n\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n\n")


#%%
def setupboard(inputlist):
    #print(inputlist[0])
    boardstart =  inputlist[0].split("\n")
    columns = len(boardstart[0])//4 + 1
    #print(columns)
    #print(boardstart)
    board = ['' for x in range(0,columns)]
    for row in range(0,columns):
        pos = 4*row + 1
        for ii in range(0,len(boardstart)-1):
            if boardstart[ii][pos] != ' ':
                board[row] = boardstart[ii][pos]+board[row]
    instructions = [[int(x) for x in row.split(" ")[1::2]] for row in inputlist[1].split("\n")]
    return board, instructions

#%%


#%%

def movecrates(board,step):
    #print(board,step)
    tomove = board[step[1]-1][-step[0]:]
    board[step[2]-1] += tomove[::-1]
    board[step[1]-1] = board[step[1]-1][:-step[0]]
    return board

#%%
def part1(inputlist):
    board, instructions = setupboard(inputlist)
    #print(board)
    for step in instructions:
        #print(board)
        newboard = movecrates(board,step)
        board = copy.deepcopy(newboard)
    return ''.join([x[-1] for x in board])
#%%

def part2(inputlist):
    score = [0]
    return sum(score)
#%%