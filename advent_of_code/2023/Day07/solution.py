
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import json
import collections

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

card_rank = '23456789TJQKA'
card_rank_p2 = 'J23456789TQKA'
hand_rank = 'H2T3F45'

def parse(inputlist):
   return {x[0:5]:int(x[5:]) for x in inputlist}

def rank_hands(handlist):
    hand_score = {}
    for hand in handlist:
        # print(hand)
        h_count =  collections.Counter(hand).most_common()
        if len(h_count) == 1:
            h_score=5*(10**11)
        else:
            h_score = h_count[0][1]*(10**11)+h_count[1][1]*(3*10**10)
        c_score = (card_rank.index(hand[0])*(10**8)
        +card_rank.index(hand[1])*(10**6)
        +card_rank.index(hand[2])*(10**4)
        +card_rank.index(hand[3])*(10**2)
        +card_rank.index(hand[4]))
        hand_score[hand] = h_score+c_score
    # print(hand_score)
    return [x[0] for x in sorted(hand_score.items(), key=lambda key_val:key_val[1])]
    # return sorted(hand_score)


def rank_hands_p2(handlist):
    hand_score = {}
    for hand in handlist:
        # print(hand)
        old_h_count =  collections.Counter(hand).most_common()
        if old_h_count[0][0] == 'J' and old_h_count[0][1] == 5:
            newhand='AAAAA'
        elif old_h_count[0][0] == 'J':
            newhand = hand.replace("J",old_h_count[1][0])
        else:
            newhand = hand.replace("J",old_h_count[0][0])
        h_count =  collections.Counter(newhand).most_common()
        if len(h_count) == 1:
            h_score=5*(10**11)
        else:
            h_score = h_count[0][1]*(10**11)+h_count[1][1]*(3*10**10)
        c_score = (card_rank_p2.index(hand[0])*(10**8)
        +card_rank_p2.index(hand[1])*(10**6)
        +card_rank_p2.index(hand[2])*(10**4)
        +card_rank_p2.index(hand[3])*(10**2)
        +card_rank_p2.index(hand[4]))
        hand_score[hand] = h_score+c_score
    # print(hand_score)
    return [x[0] for x in sorted(hand_score.items(), key=lambda key_val:key_val[1])]
    # return sorted(hand_score)


#%%        

def part1(inputlist):
    handlist = parse(inputlist)
    hand_ranks = rank_hands(handlist)
    # print(hand_ranks)
    scores = 0
    for hand in handlist:
        score = handlist[hand]*(1+hand_ranks.index(hand))
        scores = scores+ score
        # print(hand,handlist[hand],hand_ranks.index(hand),score)
    return scores



def part2(inputlist):
    handlist = parse(inputlist)
    hand_ranks = rank_hands_p2(handlist)
    # print(hand_ranks)
    scores = 0
    for hand in handlist:
        score = handlist[hand]*(1+hand_ranks.index(hand))
        scores = scores+ score
        # print(hand,handlist[hand],hand_ranks.index(hand),score)
    return scores






#%%