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

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2018day9.txt","r")
start = file.read()
startlist = start.split(" ")
startint = [int(startlist[0]),int(startlist[-2])]



file = open("2018day9test.txt","r")
startb = file.read()
testlist = startb.split(" ")
testint = [int(testlist[0]),int(testlist[-1])]

turn = 0
currentpos = 0
board = [0]


def setupscore(inputdata):
    scores = []
    for i in range(0,inputdata[0]):
        scores.append(0)
    return scores
    

def placemarble(turn,currentpos,board):
    turn += 1
    size = len(board)
    newpos = (currentpos + 1) % size
    board.insert(newpos+1,turn)
    currentpos = newpos+1
    return turn,currentpos,board

def turn23move(turn,currentpos,board,inputdata,scores):    
    player = turn % inputdata[0]
    size = len(board)
    turn += 1
    scores[player] += turn
    removepos = (currentpos-7) % size
    remscore = board.pop(removepos)
    scores[player] += remscore
    currentpos = removepos % (size-1)
    return turn,currentpos,board,scores

def turns(turn,currentpos,board,numberturns,inputdata,scores):
    for i in range(0,numberturns):
        if (turn + 1) % 23 != 0:
            turn,currentpos,board=placemarble(turn,currentpos,board)
        else:
            turn,currentpos,board,scores=turn23move(turn,currentpos,board,inputdata,scores)
#        print(board)
    return turn,currentpos,board,scores

def playgame(inputdata):
    turn = 0
    currentpos = 0
    board = [0]
    scores = setupscore(inputdata)
    endturn,endcurrentpos,endboard,endscores=turns(turn,currentpos,board,inputdata[1],inputdata,scores)
    maxscore = max(endscores)
    return maxscore
    
print("Part 1: " + str(playgame([405,70953])))    

maxscores = []
for i in range(1,910):
    maxscores.append(playgame([405,i]))
    
changes = []
for j in range(1,len(maxscores)):
    if maxscores[j] > maxscores[j-1]:
        changes.append(j)


