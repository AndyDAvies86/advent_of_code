# -*- coding: utf-8 -*-
"""


@author: Andy
"""

import pandas as pd
import numpy as np

filetest = open("2021day10test.txt","r")
starttest = filetest.read()
test = starttest.split("\n")


file = open("2021day10input.txt","r")
start = file.read()
startlist = start.split("\n")

def illegal(row):
#    count = np.array([0,0,0,0])
    openbrack = ['(','[','{','<']
    closebrack = [')',']','}','>']
    brackcheck = {'(':')','[':']','{':'}','<':'>'}
    score = {')':3,']':57,'}':1197,'>':25137}
    bracklist = []
    for char in row:
#        print(char,bracklist)
        if char in openbrack:
            bracklist.append(char)
        if char in closebrack:
#            print(brackcheck[bracklist[-1]])
            if char != brackcheck[bracklist[-1]]:
                return score[char]
            else:
                bracklist = bracklist[:-1]
    return 0
            
def part1(inputlist):
    score = 0
    for row in inputlist:
#        print(row,score,illegal(row))
        score += illegal(row)
#        print(row,score,illegal(row))
    return score

def discard(inputlist):
    cleaned = []
    for row in inputlist:
#        print(illegal(row),row)
        if illegal(row) == 0:
            cleaned.append(row)
    return cleaned

def rump(row):
    openbrack = ['(','[','{','<']
    closebrack = [')',']','}','>']
    bracklist = []
    for char in row:
        if char in openbrack:
            bracklist.append(char)
        if char in closebrack:
            bracklist = bracklist[:-1]
    return ''.join(bracklist)

def ending(row):
    finish = ''
    brackcheck = {'(':')','[':']','{':'}','<':'>'} 
    for ii in range (0,len(row)):
        finish += brackcheck[row[-1-ii]]
    return finish
        

def part2(inputlist):
    cleaned = discard(inputlist)
    brackscore = {')':1,']':2,'}':3,'>':4}
    scores = []  
    for row in cleaned:
        leftover = rump(row)
        finish = ending(leftover)
        score = 0
        for char in finish:
            score = 5*score + brackscore[char]
        scores.append(score)
    sortscores = sorted(scores)
    return sortscores[int((len(scores)-1)/2)]
        
        
        
        
        
        
        
        