
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()
numbers = '1234567890'

file = open("2020day22.txt","r")
start = file.read()
startlist = start.split("\n\n")

file = open("2020day22test.txt","r")
startb = file.read()
testlist = startb.split("\n\n")

def hands(inputlist):
    handlist = []
    for row in inputlist:
        temprow = row.split("\n")
        newrow = [int(x) for x in temprow[1:]]
        handlist.append(newrow)
    return handlist

def turn(handlist):
    play = [handlist[0][0],handlist[1][0]]
    handlist[0] = handlist[0][1:]
    handlist[1] = handlist[1][1:]
    winner = play.index(max(play))
    handlist[winner] += [max(play),min(play)]
    return handlist

def part1(inputlist):
    handlist = hands(inputlist)
    maxlist = len(handlist[0]+handlist[1])
    i = 0
    while 0 < len(handlist[0]) < maxlist:
        handlist = turn(handlist)
        i += 1
#        print(i)
    winning = handlist[0] + handlist[1]
    score = 0
    for card in winning:
        score += (maxlist-winning.index(card)) * card
    return score

def game(inhandlist,i):
    handlist = copy.deepcopy(inhandlist)
    listofstates = []
#    print(i)
    i += 1
    while 0 < len(handlist[0]) < len(handlist[0])+len(handlist[1]):
#        print('len',len(listofstates))
        play = [handlist[0][0],handlist[1][0]]  
        if handlist in listofstates:
#            print('Full',handlist)
            return 0
        elif len(handlist[0]) <= play[0] or len(handlist[1]) <= play[1] :
#            print('turn', handlist)
            listofstates.append(copy.deepcopy(handlist))
            handlist = turn(handlist)
        else:
#            print('game',handlist)
            listofstates.append(copy.deepcopy(handlist))
            winner = game([handlist[0][1:play[0]+1],handlist[1][1:play[1]]],i)            
#            print(winner)
            handlist[winner] = handlist[winner][1:]+[play[winner],play[1-winner]]
            handlist[1-winner] = handlist[1-winner][1:]
#        print(len(handlist[0]),len(handlist[1]))
        if len(handlist[0]) == 0:
            return 1
        elif len(handlist[1]) == 0:
            return 0
#    print(handlist)
    if len(handlist[0]) == 0:
            return 1
    elif len(handlist[1]) == 0:
            return 0
    

def part2(inputlist):
    handlist = hands(inputlist)
    maxlist = len(handlist[0]+handlist[1])
    i = 0
#    game(handlist,0)
    listofstates = []
    i = 0
    while 0 < len(handlist[0]) < maxlist:
        play = [handlist[0][0],handlist[1][0]]  
        if handlist in listofstates:
            return handlist
        elif len(handlist[0]) <= play[0] or len(handlist[1]) <= play[1] :
            listofstates.append(copy.deepcopy(handlist))
            handlist = turn(handlist)
        else:     
#            print(handlist)
            listofstates.append(copy.deepcopy(handlist))
            winner = game([handlist[0][1:play[0]+1],handlist[1][1:play[1]+1]],0)            
            handlist[winner] = handlist[winner][1:]+[play[winner],play[1-winner]]
            handlist[1-winner] = handlist[1-winner][1:]
    winning = handlist[0] + handlist[1]
    score = 0
    for card in winning:
        score += (maxlist-winning.index(card)) * card
    return score
