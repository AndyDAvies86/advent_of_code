
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import hashlib

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2015day6.txt","r")
start = file.read()
startlist = start.split("\n")


#file = open("2015day1test.txt","r")
#startb = file.read()
#testlist = startb.split("\n")

def cleanlist(inputlist):
    newlist = []
    for row in inputlist:
        temprow = row.replace("turn ","").replace("through ","")
        splitrow = temprow.split(" ")
#        print(splitrow)
        newrow = [splitrow[0],[int(x) for x in splitrow[1].split(',')],[int(x) for x in splitrow[2].split(',')]]
        newlist.append(newrow)
    return newlist

def part1(inputlist):
    instructions = cleanlist(inputlist)
    field = [[0 for x in range(0,1000)] for y in range(0,1000)]
    for row in instructions:
#        print(row)
        if row[0] == ("on"):
            for i in range(row[1][0],row[2][0]+1):
                for j in range(row[1][1],row[2][1]+1):
                    field[i][j] = 1
        if row[0] == ("off"):
            for i in range(row[1][0],row[2][0]+1):
                for j in range(row[1][1],row[2][1]+1):
                    field[i][j] = 0
        if row[0] == ("toggle"):
            for i in range(row[1][0],row[2][0]+1):
                for j in range(row[1][1],row[2][1]+1):
                    field[i][j] = 1-field[i][j]
#        print(sum(sum(x) for x in field))
    return sum(sum(x) for x in field)
        
def part2(inputlist):
    instructions = cleanlist(inputlist)
    field = [[0 for x in range(0,1000)] for y in range(0,1000)]
    for row in instructions:
#        print(row)
        if row[0] == ("on"):
            for i in range(row[1][0],row[2][0]+1):
                for j in range(row[1][1],row[2][1]+1):
                    field[i][j] += 1
        if row[0] == ("off"):
            for i in range(row[1][0],row[2][0]+1):
                for j in range(row[1][1],row[2][1]+1):
                    field[i][j] = max(0,field[i][j]-1)
        if row[0] == ("toggle"):
            for i in range(row[1][0],row[2][0]+1):
                for j in range(row[1][1],row[2][1]+1):
                    field[i][j] += 2
#        print(sum(sum(x) for x in field))
    return sum(sum(x) for x in field)
        