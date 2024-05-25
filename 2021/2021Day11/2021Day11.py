# -*- coding: utf-8 -*-
"""


@author: Andy
"""

import pandas as pd
import numpy as np

filetest = open("2021day11test.txt","r")
starttest = filetest.read()
test = starttest.split("\n")

filetest0 = open("2021day11test0.txt","r")
starttest0 = filetest0.read()
test0 = starttest0.split("\n")


file = open("2021day11input.txt","r")
start = file.read()
startlist = start.split("\n")

def startstate(inputlist):
    return np.array([[int(x) for x in y] for y in inputlist])

def flash(state,flashstate):
    newstate = state
    newflash = flashstate
    for ii in range(0,len(state)):
        for jj in range(0,len(state[0])):
#            print(ii,jj,newstate[6][9])
            if state[ii][jj] > 9 and newflash[ii][jj] == 0:
                newflash[ii][jj] = 1
                for kk in range(-1,2):
                    for ll in range(-1,2):
                        if ii+kk >= 0 and jj+ll >= 0 and ii+kk < len(state) and jj+ll < len(state[0]) and (kk != 0 or ll!= 0):
                            newstate[ii+kk][jj+ll] += 1
#                return newstate,newflash
    return newstate,newflash
                            
def stepthrough(oldstate):
    flashstate = 0*oldstate
    newstate = oldstate+1
    checksum = np.sum(flashstate)
    a=0
    while a == 0:
#        print(checksum)
#        print(newstate)
#        print(flashstate)
        newstate,flashstate = flash(newstate,flashstate)
        if checksum == np.sum(flashstate):
            a = 1
            for ii in range(0,len(newstate)):
                for jj in range(0,len(newstate[0])):
                    if newstate[ii][jj]>9:
                        newstate[ii][jj] = 0
            return newstate,checksum
        else:
            checksum = np.sum(flashstate)

def allsteps(inputlist,steps):
    state = startstate(inputlist)
    counter = 0
    for ii in range(0,steps):
        state,addcount = stepthrough(state)
#        print(state)
#        print(addcount)
        counter += addcount
    return counter

def allflash(inputlist):
    state = startstate(inputlist)
    a = 0
    step = 1
    total = len(state)*len(state[0])
    print(total)
    while a == 0:
        state,addcount = stepthrough(state)
#        print(state)
#        print(addcount)
        if addcount == total:
            return step
        step += 1
    