
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
startlist = start.split("\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n")


#%%

def parselist(inputlist):
    pass
#%%

def wall(pos,fav):
    x = pos[0]
    y = pos[1]
    test = x*x+3*x+2*x*y+y+y*y+fav
    b_test = bin(test)[2:]
    new = [int(x) for x in b_test]
    return sum(new)%2

def fillboard(board,t,fav):
    for ii in range(0,t[1]+4):
        for jj in range(0,t[0]+4):
            if wall([jj,ii],fav) == 0:
                if ii == 0 and jj == 0:
                    temp = min([board[ii+1][jj],board[ii][jj+1]])
                elif ii == 0:
                    temp = min([board[ii+1][jj],board[ii][jj-1],board[ii][jj+1]])
                elif jj == 0:
                    temp = min([board[ii-1][jj],board[ii+1][jj],board[ii][jj+1]])
                else:
                    temp = min([board[ii-1][jj],board[ii+1][jj],board[ii][jj-1],board[ii][jj+1]])
                board[ii][jj] = min(board[ii][jj],temp+1)
    return board

def part1(inputlist,t):
    fav = int(inputlist[0])
    pos = [1,1]
    board = [[999+wall([x,y],fav) for x in range(0,t[0]+5)] for y in range(0,t[1]+5)]
    board[pos[0]][pos[1]] = 0
    # print(board)
    # newboard = [[1000 for x in range(0,t[0]+5)] for y in range(0,t[1]+5)]
    go = True
    a=0
    while go:
        a=a+1
        newboard = copy.deepcopy(board)
        newboard = fillboard(newboard,t,fav)
        if newboard == board:
            return newboard[t[1]][t[0]]
        board = copy.deepcopy(newboard)
            
    return board[t[1]][t[0]]
    


#%%

def part2(inputlist):
    fav = int(inputlist[0])
    pos = [1,1]
    board = [[999+wall([x,y],fav) for x in range(0,60)] for y in range(0,60)]
    board[pos[0]][pos[1]] = 0
    # print(board)
    # newboard = [[1000 for x in range(0,t[0]+5)] for y in range(0,t[1]+5)]
    go = True
    a=0
    while go:
        a=a+1
        newboard = copy.deepcopy(board)
        newboard = fillboard(newboard,[51,51],fav)
        if newboard == board:
            return sum([sum([x<=50 for x in y]) for y in newboard])
        board = copy.deepcopy(newboard)
            
    return board[t[1]][t[0]]
    
#%%