# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:46:13 2020

@author: Andy
"""



import pandas as pd
import numpy as np
import re

file = open("2018day2.txt","r")
start = file.read()
startlist = start.split("\n")

twos = 0
threes = 0
for word in startlist:
    twoshere = 0
    threeshere = 0
    for char in word:
        if word.count(char) == 2:
            twoshere = 1
        if word.count(char) == 3 :
            threeshere = 1
    twos = twos + twoshere
    threes = threes + threeshere
    
checksum = twos * threes

print('Part 1: ' + str(checksum))
  
solutiona = ''
solutionb = ''
solution = ''
      
for word in startlist:
    for wordb in startlist:
        checkword = 0
        for i in range(0,len(word)):
            if word[i] == wordb[i]:
                checkword += 1
        if checkword == len(word)-1:
            solutiona = word
            solutionb = wordb


for i in range(0,len(solutiona)):
    if solutiona[i] == solutionb[i]:
        solution = solution + solutiona[i]
                    
print("Part 2: " + solution)


        
        
        