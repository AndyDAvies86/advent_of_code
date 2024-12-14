
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import math

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
    games = []
    for row in inputlist:
        settings = row.split("\n")
        a_in = settings[0].replace(',','').split()[2:]
        a = [int(x[1:]) for x in a_in]
        b_in = settings[1].replace(',','').split()[2:]
        b = [int(x[1:]) for x in b_in]
        prize_in = settings[2].replace(',','').split()[1:]
        prize = [int(x[2:]) for x in prize_in]
        games.append([np.array([[a[0],b[0]],[a[1],b[1]]]),np.array(prize)])
    return games
        
#%%

def solve(game):
    try:
        inverse = np.linalg.inv(game[0])
        solution = inverse@game[1]
        if solution[0] % 1 == 0 and solution[1] % 1 == 0:
            return solution
        if solution[0] % 1 != 0 or solution[1] % 1 == 0:
            print('no',game)
            return np.array([0,0])            
    except:
        inversea = inverse = np.linalg.inv(game[0][0])
        inverseb = inverse = np.linalg.inv(game[0][1])
        print('ex',game,inversea,inverseb)

    return np.array([0,0])

def quicksolve(game):
    puzz = game[0]
    det = round(np.linalg.det(puzz),0)
    flip = np.array([[puzz[1][1],-puzz[0][1]],[-puzz[1][0],puzz[0][0]]])
    # print(puzz,det,flip)
    if det != 0 :
        solution = flip@game[1]
        # print('sol',solution,solution//det)
        if solution[0] % det == 0 and solution[1] % det == 0:
            # print('yay')
            return solution//det
        # else:
        #     print('nay')
    else:
        # print('det',game)
        return np.array([0,0])
    return np.array([0,0])


def part1(inputlist):
    games = parselist(inputlist)
    press = 0
    for game in games:
        solution = quicksolve(game)
        # print(game,solution)
        press = press+sum(np.array([3,1])*solution)
    return press
#%%

def part2(inputlist):
    games = parselist(inputlist)
    press = 0
    for game in games:
        game[1] = [game[1][x] + 10000000000000 for x in range(0,2)]
        solution = quicksolve(game)
        # print(game,solution)
        press = press+sum(np.array([3,1])*solution)
    return press
#%%