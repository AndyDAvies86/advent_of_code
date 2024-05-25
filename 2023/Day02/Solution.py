
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
def gamelist(biglist):
    games = {}
    for x in biglist:
        # print(x)
        colon = x.find(':')
        gamenum=int(x[5:colon])
        game = x[colon+2:]
        moves = game.split("; ")
        movelist = []
        for move in moves:
            # print(move)
            groups = move.split(", ")
            grouplist = {}
            for group in groups:
                # print(group)
                space = group.split(" ")
                # print(space)
                cubenum = int(space[0])
                cubecol = space[1]
                grouplist[cubecol] = cubenum
            movelist.append(grouplist)
        games[gamenum] = movelist


    return games


#%%
def findmax(game):
    maxlist = {'blue':0,'red':0, 'green':0}
    for turn in game:
        # print(turn)
        for col in turn:
            # print(col)
            # print (turn[col])
            if turn[col] > maxlist[col]:
                maxlist[col] = turn[col]
    return maxlist


def checkgames(games):
    idnum = 0
    for ii in range (1,len(games)+1):
        gamemaxlist = findmax(games[ii])
        if gamemaxlist['red'] <= 12 and gamemaxlist['green'] <= 13 and gamemaxlist['blue'] <= 14:
            idnum = idnum + ii
    return idnum        

def part1(biglist):
    games = gamelist(biglist)
    return checkgames(games)


print("Test part 1: "+str(part1(testlist)))
print("Puzzle part 1: "+str(part1(startlist)))

#%%

def part2(biglist):
    games = gamelist(biglist)
    power = 0
    for ii in range (1,len(games)+1):
        game=games[ii]
        # print(game)
        gamemaxlist = findmax(game)
        # print(gamemaxlist)
        poweradd = gamemaxlist['red']*gamemaxlist['green']*gamemaxlist['blue']
        power = power + poweradd
    return power

print("Test part 2: "+str(part2(testlist)))
print("Puzzle part 2: "+str(part2(startlist)))

#%%