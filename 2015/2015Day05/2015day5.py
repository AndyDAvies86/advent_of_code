
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

file = open("2015day5.txt","r")
start = file.read()
startlist = start.split("\n")


#file = open("2015day1test.txt","r")
#startb = file.read()
#testlist = startb.split("\n")

def nice(inputvalue):
    pattern1 = '[aeiou].*[aeiou].*[aeiou]'
    pattern2 = ''.join([x+x+'|' for x in alphabet[:-1]]+['zz'])
#    print(pattern2)
    pattern3 = 'ab|cd|pq|xy'
    match1 = bool(re.search(pattern1,inputvalue))
    match2 = bool(re.search(pattern2,inputvalue))
    match3 = bool(re.search(pattern3,inputvalue))
    return match1 and match2 and not match3
   
def part1(inputlist):
    count = 0
    for row in inputlist:
        if nice(row):
            count += 1
    return count

def nice2(inputvalue):
    pattern1 = '([a-z][a-z]).*\\1'
    pattern2 = ''.join([x+'[a-z]'+x+'|' for x in alphabet[:-1]]+['z[a-z]z'])
#    print(pattern2)
    match1 = bool(re.search(pattern1,inputvalue))
    match2 = bool(re.search(pattern2,inputvalue))
    return match1 and match2

def part2(inputlist):
    count = 0
    for row in inputlist:
        if nice2(row):
            count += 1
    return count