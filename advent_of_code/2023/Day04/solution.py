
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
    cards= []
    c_loc = inputlist[0].find(":")
    p_loc = inputlist[0].find("|")
    wins = int((p_loc-c_loc-2)/3)
    nums = int((len(inputlist[0])-p_loc-1)/3)

    # print (p_loc,c_loc,len(inputlist[0]),wins,nums)
    for row in inputlist:
        winners = [int(row[c_loc+2+x*3:c_loc+4+x*3]) for x in range(0,wins)]
        numbers = [int(row[p_loc+2+x*3:p_loc+4+x*3]) for x in range(0,nums)]
        # card = []
        # win_start = row.find(":")+2
        # win_end = row.find("|")-1
        # num_start = win_end+3
        # print(row[win_start:win_end].split(" "))
        # print(row[num_start:].split())
        # card = [[int(x) for x in row[win_start:win_end].split(" ")],[int(x) for x in row[num_start:].split(" ")]]
        cards.append([winners,numbers])
    return cards



#%%        

def part1(inputlist):
    cards = parse(inputlist)
    score = 0
    for card in cards:
        winner_set = set(card[0]).intersection(set(card[1]))
        # print(winner_set)
        if len(winner_set) > 0:
            score = score + 2**(len(winner_set)-1)
    return score



def part2(inputlist):
    cards = parse(inputlist)
    card_count = [1 for x in inputlist]
    for ii in range(0,len(inputlist)):
        card = cards[ii]
        winner_set = set(card[0]).intersection(set(card[1]))
        winner_count = len(winner_set)
        for jj in range(ii+1,ii+winner_count+1):
            card_count[jj] = card_count[jj]+card_count[ii]

    return sum(card_count)



#%%