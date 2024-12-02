
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
    sue_dict = {}
    for row in inputlist:
        to_dict = row.replace(",","").replace(":","").split(" ")
        sue_dict[int(to_dict[1])] = {}
        for ii in range(2,len(to_dict),2):
            sue_dict[int(to_dict[1])][to_dict[ii]] = int(to_dict[ii+1])
    return sue_dict


#%%

def testsues(test_sue,list_sue):
    for x in test_sue:
        if x in list_sue:
            if test_sue[x] != list_sue[x]:
                return 0
    return 1

def part1(inputlist):
    sue_dict = parselist(inputlist)
    test_sue = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    for ii in range(1,len(sue_dict)+1):
        test = testsues(test_sue,sue_dict[ii])
        if test == 1:
            return ii
    return "Error"
        
#%%

def p2testsues(test_sue,list_sue):
    for x in test_sue:
        if x in list_sue:
            if x in ['cats','trees']:
                if test_sue[x] > list_sue[x]:
                    return 0
            elif x in ['pomeranians','goldfish']:
                if test_sue[x] < list_sue[x]:
                    return 0
            else:
                if test_sue[x] != list_sue[x]:
                    return 0
    return 1

def part2(inputlist):
    sue_dict = parselist(inputlist)
    test_sue = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    for ii in range(1,len(sue_dict)+1):
        test = p2testsues(test_sue,sue_dict[ii])
        if test == 1:
            return ii
    return "Error"
#%%