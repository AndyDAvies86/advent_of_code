# -*- coding: utf-8 -*-
"""


@author: Andy
"""

import pandas as pd
import numpy as np

filetest = open("2021day7test.txt","r")
starttest = filetest.read()
test = [int(x) for x in starttest.split(",")]

file = open("2021day7input.txt","r")
start = file.read()
startlist = [int(x) for x in start.split(",")]

def distances(inputlist):
    minfuel = sum([abs(x-max(test)) for x in inputlist])
    optpos = 0
    for ii in range(min(inputlist),max(inputlist)):
        fuel = sum([abs(x-ii) for x in inputlist])
        if fuel < minfuel:
            minfuel = fuel
            optpos = ii
    return minfuel

def distances2(inputlist):
    minfuel = sum([int((abs(x-max(test))*abs(x-max(test))+abs(x-max(test)))/2) for x in inputlist])
    optpos = 0
    for ii in range(min(inputlist),max(inputlist)):
        fuel = sum([int((abs(x-ii)*abs(x-ii)+abs(x-ii))/2) for x in inputlist])
        if fuel < minfuel:
            minfuel = fuel
            optpos = ii
    return minfuel