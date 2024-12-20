
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2015day1.txt","r")
start = file.read()
startlist = start.split(", ")

#file = open("2015day1test.txt","r")
#startb = file.read()
#testlist = startb.split("\n")

def part1(inputlist):
    return inputlist.count("(")-inputlist.count(")")

def part2(inputlist):
    floor = 0
    for i in range(0,len(inputlist)):
        if inputlist[i] == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return i+1
        