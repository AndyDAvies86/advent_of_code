
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2015day2.txt","r")
start = file.read()
startlist = start.split("\n")

#file = open("2015day1test.txt","r")
#startb = file.read()
#testlist = startb.split("\n")

def part1(inputlist):
    templist = [x.split("x") for x in inputlist]
    intlist = [[int(x) for x in row] for row in templist]
    paper = 0
    for row in intlist:
        areas = [row[0]*row[1],row[1]*row[2],row[0]*row[2]]
        paper += 2*(sum(areas)) + min(areas)
    return paper

def part2(inputlist):
    templist = [x.split("x") for x in inputlist]
    intlist = [[int(x) for x in row] for row in templist]
    ribbon = 0
    for row in intlist:
        ribbon += 2*sum(row)-2*max(row)+row[0]*row[1]*row[2]
    return ribbon