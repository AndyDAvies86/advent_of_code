# -*- coding: utf-8 -*-
"""


@author: Andy
"""

import pandas as pd
import numpy as np

filetest = open("2021day8test.txt","r")
starttest = filetest.read()
test = starttest.split("\n")

filetest2 = open("2021day8test2.txt","r")
starttest2 = filetest2.read()
test2 = starttest2.split("\n")

file = open("2021day8input.txt","r")
start = file.read()
startlist = start.split("\n")

def puzzle(inputlist):
    allnums = []
    code = []
    for row in inputlist:
        newrow = row.split(" | ")
        allnums += [[''.join(sorted(x)) for x in newrow[0].split(" ")]]
        code += [[''.join(sorted(x)) for x in newrow[1].split(" ")]]
    return allnums,code

def count1478(inputlist):
    allnums,code=puzzle(inputlist)
    lengths = [len(x) for x in code]
    counter = sum([x in (2,3,4,7) for x in lengths])
    return counter

def deducenumbers(row):
#    allnums,code=puzzle(inputlist)
    keydict = {}
    revkey = {}
#    print(row)
    for digit in row:
#        print(digit)
        if len(digit) == 7:
            keydict[digit] = 8
            revkey[8] = digit
        elif len(digit) == 2:
            keydict[digit] = 1
            revkey[1] = digit
        elif len(digit) == 3:
            keydict[digit] = 7
            revkey[7] = digit
        elif len(digit) == 4:
            keydict[digit] = 4
            revkey[4] = digit
#                print(4,digit)
#    print(("Pre",keydict))
    for digit in row:
        count4 = sum([x in digit for x in revkey[4]])
        count7 = sum([x in digit for x in revkey[7]])            
#        print(digit,count4,count7)
        if len(digit) == 6:
            if count4 == 4:
                keydict[digit] = 9
                revkey[9] = digit
            elif count7 == 3:
                keydict[digit] = 0
                revkey[0] = digit
            else:
                keydict[digit] = 6
                revkey[6] = digit
        elif len(digit) == 5:
            if count7 == 3:
                keydict[digit] = 3
                revkey[3] = digit
            elif count4 == 3:
                keydict[digit] = 5
                revkey[5] = digit
            else:
                keydict[digit] = 2
                revkey[2] = digit
#        print(digit,keydict[digit])
    return keydict
    
def decode(inputlist):
    allnums,code = puzzle(inputlist)
    decoded =[]
    for jj in range(0,len(allnums)):
        num = code[jj]
        keydict = deducenumbers(allnums[jj])
#        print(num)
#        print(keydict)
#        for ii in num:
#            print(keydict[ii])
        decodedlist = [keydict[x] for x in num]
        outnum = 1000*decodedlist[0] + 100*decodedlist[1] + 10*decodedlist[2] + decodedlist[3]
        print(outnum)
        decoded.append(outnum)
    return sum(decoded)
    
            
                
                
        
    