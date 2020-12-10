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

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2018day10.txt","r")
start = file.read()
startlist = start.split("\n")
startinput = []
for row in startlist:
    startinput.append(row.split(" "))



file = open("2018day10test.txt","r")
startb = file.read()
testlist = startb.split("\n")
testinput = []
for row in testlist:
    testinput.append(row.split(" "))
