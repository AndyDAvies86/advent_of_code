
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
    times = [int(x) for x in re.split(r'\s+',inputlist[0])[1:]]
    distances = [int(x) for x in re.split(r'\s+',inputlist[1])[1:]]
    races = []
    for ii in range (0,len(times)):
        races.append([times[ii],distances[ii]])
    return races

def parse_p2(inputlist):
    midlist = [x.replace(' ','') for x in inputlist]
    race = [int(x.split(':')[1]) for x in midlist]
    return race


def total_distance(race,button_time):
    distance = (race[0]-button_time)*button_time
    return distance


#%%        

def part1(inputlist):
    races = parse(inputlist)
    records = 1
    for race in races:
        wins = [total_distance(race,x) > race[1] for x in range(0,race[0])]
        records = records * sum(wins)
    return records



def part2(inputlist):
    race=parse_p2(inputlist)
    button = 0
    losses = 0
    while button >= 0:
        # print (race,button)
        if total_distance(race,button)>race[1]:
            return race[0]-2*losses+1
        losses = losses + 1
        button = button + 1




#%%