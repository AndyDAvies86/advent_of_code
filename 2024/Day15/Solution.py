
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
    inst = inputlist[1]
    board = inputlist[0].split('\n')
    # board = [[y for y in x] for x in inputlist[0].split('\n')]
    # pieces = {'#':9,'@':5,'O':1,'.':0}
    # board = np.array([[pieces[x] for x in y] for y in inputlist[0].split('\n')])
    # walls = [[ii,jj] for ii in range(0,len(b_def)) for jj in range(0,len(b_def[0])) if b_def[ii][jj]=='#']
    # boxes = [[ii,jj] for ii in range(0,len(b_def)) for jj in range(0,len(b_def[0])) if b_def[ii][jj]=='O']
    # robot = [[ii,jj] for ii in range(0,len(b_def)) for jj in range(0,len(b_def[0])) if b_def[ii][jj]=='@'][0]
    return inst,board
#%%
def move(board,robot,d):
    points = {'<':[0,-1],'>':[0,1],'^':[-1,0],'V':[1,0]}
    shove = points[d]
    l = 0
    # while  



def part1(inputlist):
    pass
#%%

def part2(inputlist):
    pass
#%%