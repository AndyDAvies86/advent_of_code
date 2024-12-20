# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:46:13 2020

@author: Andy
"""



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

#file = open("2016day4.txt","r")
#start = file.read()
#startlist = start.split("\n")
#
#
#file = open("2016day4test.txt","r")
#startb = file.read()
#testlist = startb.split("\n")

test = 'abc'
start = 'ojvtpuvg'



def check(inputvalue):
    code = ''
    i = 0
    while len(code) < 8:
        test = inputvalue+str(i)
        hashval = hashlib.md5(test.encode()).hexdigest()
        if hashval[0:5] == '00000':
            code += hashval[5]
            print(code)
        i += 1
        if i % 1000000 == 0:
            print(str(int(i/1000000))+'million')
    return code

def check2(inputvalue):
    code = ['#' for x in range(0,8)]
    i = 0
    while '#' in code:
        test = inputvalue+str(i)
        hashval = hashlib.md5(test.encode()).hexdigest()
        if hashval[0:5] == '00000':
            if hashval[5] in [str(x) for x in range(0,8)]:
#                print(code[int(hashval[5])])
                code[int(hashval[5])] = code[int(hashval[5])].replace('#',hashval[6])
                print(''.join(code))
        i += 1
        if i % 1000000 == 0:
            print(str(int(i/1000000))+'million')
    return ''.join(code)


