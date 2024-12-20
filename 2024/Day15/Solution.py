
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import networkx as nx
import matplotlib.pyplot as plt

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

file = open("inputtestsm.txt","r")
startc = file.read()
testsmlist = startc.split("\n\n")


#%%

def parselist(inputlist):
    inst = inputlist[1].replace('\n','')
    b_def = inputlist[0].split('\n')
    pieces = {'#':9,'@':5,'O':1,'.':0}
    board = np.array([[pieces[x] for x in y] for y in inputlist[0].split('\n')])
    walls = [(jj,ii) for ii in range(0,len(b_def)) for jj in range(0,len(b_def[0])) if b_def[ii][jj]=='#']
    boxes = [(jj,ii) for ii in range(0,len(b_def)) for jj in range(0,len(b_def[0])) if b_def[ii][jj]=='O']
    robot = [(jj,ii) for ii in range(0,len(b_def)) for jj in range(0,len(b_def[0])) if b_def[ii][jj]=='@'][0]
    return inst,robot,board
#%%

def printmaze(board):
    h,w = np.shape(board)
    wd = {0:'.',1:'O',5:'@',9:'#'}
    nd = {'#':9,'@':5,'O':1,'.':0}
    print('\n'.join([''.join([wd[x] for x in y ]) for y in board]))

def move(board,step,robotin):
    drot = {'>':0,'v':1,'<':2,'^':3}
    newboard = np.rot90(board,drot[step])
    robot = [int(x) for x in np.where(newboard == 5)][::-1]
    row = newboard[robot[1],:]
    strow = ''.join([str(x) for x in row])
    nwall = strow.find('9',robot[0])
    if '0' not in strow[robot[0]:nwall]:
        return board,robotin
    nbot = strow.find('0',robot[0])
    block = [0]+list(newboard[robot[1],robot[0]:nbot])
    newboard[robot[1],robot[0]:nbot+1] = block
    newboard[robot[1],robot[0]] == 0
    newboard = np.rot90(newboard,4-drot[step])
    return newboard,[int(x) for x in np.where(newboard == 5)][::-1]


def part1(inputlist):
    inst,robot,board = parselist(inputlist)
    for ii in range (0,len(inst)):
        board,robot = move(board,inst[ii],robot)
    bottles = np.where(board == 1)
    return 100*sum(bottles[0])+sum(bottles[1])
    
        

    
#%%

def reparse(inputlist):
    inst = inputlist[1].replace('\n','')
    double = {'#':'##','@':'@.','O':'[]','.':'..'}
    pieces = {'#':9,'@':5,'[':1,']':2,'.':0}
    board = np.array([[pieces[double[x]] for x in y] for y in inputlist[0].split('\n')])
    return inst,board

def hmove(board,step,robotin):
    if step == '<':
        newboard = np.flip(board,1)
    else:
        newboard = board
    robot = [int(x) for x in np.where(board == 5)][::-1]
    row = newboard[robot[1],:]
    strow = ''.join([str(x) for x in row])
    nwall = strow.find('9',robot[0])
    if '0' not in strow[robot[0]:nwall]:
        return board,robotin
    nbot = strow.find('0',robot[0])
    block = [0]+list(newboard[robot[1],robot[0]:nbot])
    newboard[robot[1],robot[0]:nbot+1] = block
    newboard[robot[1],robot[0]] == 0
    if step == '<':
        newboard = np.flip(newboard,1)
    return newboard,[int(x) for x in np.where(newboard == 5)][::-1]

# def vmove
    

def part2(inputlist):
    inst,board = parselist(inputlist)

    
#%%