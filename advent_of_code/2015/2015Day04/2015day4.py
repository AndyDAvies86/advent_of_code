
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

#file = open("2015day4.txt","r")
#start = file.read()
#startlist = start.split("\n")

start = 'ckczppom'

#file = open("2015day1test.txt","r")
#startb = file.read()
#testlist = startb.split("\n")

def part1(inputvalue):
    code = ''
    i = 0
    while len(code) < 8:
        test = inputvalue+str(i)
        hashval = hashlib.md5(test.encode()).hexdigest()
        if hashval[0:5] == '00000':
            return i
        i += 1
        
def part2(inputvalue):
    code = ''
    i = 0
    while len(code) < 8:
        test = inputvalue+str(i)
        hashval = hashlib.md5(test.encode()).hexdigest()
        if hashval[0:6] == '000000':
            return i
        i += 1