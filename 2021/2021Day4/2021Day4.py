# -*- coding: utf-8 -*-
"""


@author: Andy
"""

import pandas as pd
import numpy as np

filetest = open("2021day4test.txt","r")
starttest = filetest.read()
test = starttest.split("\n\n")

file = open("2021day4input.txt","r")
start = file.read()
startlist = start.split("\n\n")

def cards(inputlist):
    callsheet = [int(x) for x in inputlist[0].split(",")]
    cardslist = []
    for card in inputlist[1:]:
#        print(card)
#        print(type(card))
        cardsheet = card.split("\n")
        newcard =[]
        for row in cardsheet:
#            print(row)
            newrow = []
            for ii in range(0,5):
                newrow.append(int(row[3*ii:3*ii+2]))
            newcard.append(newrow)
        cardslist.append(newcard)
    return callsheet,cardslist


def playcall(thiscall,cardslist,dobber):
    for ii in range(0,5):
        for jj in range(0,5):
            for kk in range(0,len(cardslist)):
#                print(ii,jj,kk)
                if cardslist[kk][ii][jj] == thiscall:
                    dobber[kk][ii][jj] = 1
#    print(len(dobber))
#    print(len(dobber[0]))
#    print(len(dobber[0][0]))
#    print(dobber)
    return dobber

def playbingo(inputlist):
    callsheet,cardslist = cards(inputlist)
    dobber = [[[0 for x in range(0,5)] for y in range(0,5)] for z in range (0,len(cardslist))]
#    print(dobber)
#    while len(callsheet) > 0:
    aa = 0
    while len(callsheet) > 0:
        aa += 1
        thiscall = callsheet[0]
        print('step '+str(aa)+' '+str(thiscall))
        dobber = playcall(thiscall,cardslist,dobber)
        callsheet = callsheet[1:]
        for ii in range(0,len(cardslist)):
            for jj in range(0,5):
                rowsum = sum([dobber[ii][jj][x] for x in range(0,5)])
                colsum = sum([dobber[ii][x][jj] for x in range(0,5)])
                if max(rowsum,colsum) == 5:
                    unmarked = sum([cardslist[ii][x][y]*(1-dobber[ii][x][y]) for x in range(0,5) for y in range(0,5)])
                    return unmarked*thiscall
                    
def playbingo2(inputlist):
    callsheet,cardslist = cards(inputlist)
    dobber = [[[0 for x in range(0,5)] for y in range(0,5)] for z in range (0,len(cardslist))]
#    print(dobber)
#    while len(callsheet) > 0:
    aa = 0
    woncards = []
    while len(callsheet) > 0:
        aa += 1
        thiscall = callsheet[0]
        print('step '+str(aa)+' '+str(thiscall))
        dobber = playcall(thiscall,cardslist,dobber)
        callsheet = callsheet[1:]

        for ii in range(0,len(cardslist)):
            for jj in range(0,5):
                rowsum = sum([dobber[ii][jj][x] for x in range(0,5)])
                colsum = sum([dobber[ii][x][jj] for x in range(0,5)])
                if max(rowsum,colsum) == 5:
                    if ii not in woncards:
                        print(ii)
                        woncards.append(ii)
                        if len(cardslist) == len(woncards):
                            unmarked = sum([cardslist[ii][x][y]*(1-dobber[ii][x][y]) for x in range(0,5) for y in range(0,5)])
                            unmarkedcard = [[[cardslist[ii][x][y]*(1-dobber[ii][x][y]) for x in range(0,5)] for y in range(0,5)]]
                            return unmarked*thiscall,unmarkedcard,woncards
                    
    
    
    
    