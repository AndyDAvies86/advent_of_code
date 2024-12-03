
#%%
import pandas as pd
import numpy as np
import re
import math
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
    return int(inputlist[0])
    
#%%

def getfactors(number):
    factors = []
    # print(factors)
    for ii in range(1,int(number**0.5)):
         if number % ii == 0:
            factors.append(ii)
            factors.append(number//ii)
    if int(number**0.5)**2 == number:
        factors.append(int(number**0.5))
    return factors

def part1(inputlist):
    target = parselist(inputlist)//10
    # print(target)
    house = 1
    matched = False
    while not matched:
        # print(house,sum(getfactors(house)))
        if sum(getfactors(house)) >= target:
            matched = True
        else:
            house = house+1
    return house

    


#%%

def p2factors(number):
    factors = []
    # print(factors)
    for ii in range(1,51):
         if number % ii == 0:
            if number<ii*50:
                factors.append(ii)
            if number<number//ii*50:
                factors.append(number//ii)
    if int(number**0.5)**2 == number and number <= 2500:
        factors.append(int(number**0.5))
    return factors


def part2(inputlist):
    target = parselist(inputlist)//11

    house = 1
    matched = False
    while not matched:
        # print(house,sum(getfactors(house)))
        if sum(p2factors(house)) >= target:
            matched = True
        else:
            house = house+1
    return house
#%%