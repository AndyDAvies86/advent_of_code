# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:46:13 2020

@author: Andy
"""



import pandas as pd
import numpy as np
import re

file = open("2018day3.txt","r")
start = file.read()
startlist = start.split("\n")

cleanlist = []
for word in startlist:
    firstsplit=word.split(" ")
    firstsplit[0] = firstsplit[0].replace("#", "")
    firstsplit[2] = firstsplit[2].replace(":","").split(",")
    firstsplit[3] = firstsplit[3].split("x")
    cleanlist.append(firstsplit)
    
claimscount = {}
for word in cleanlist:
    for i in range(0,int(word[3][0])):
        for j in range (0,int(word[3][1])):
            if (int(word[2][0])+i,int(word[2][1])+j) in claimscount:
                claimscount[(int(word[2][0])+i,int(word[2][1])+j)] += 1
            else:
                claimscount[(int(word[2][0])+i,int(word[2][1])+j)] = 1
                    
multiclaims = [x for x in claimscount if claimscount[x] > 1]

print('Part 1: ' + str(len(multiclaims)))

cleanclaim = 0
for word in cleanlist:
    error = 0
    for i in range(0,int(word[3][0])):
        for j in range (0,int(word[3][1])):
#            print(str(word[0])+" "+str((int(word[2][0])+i))+" "+str(int(word[2][1])+j)) 
            if claimscount[(int(word[2][0])+i,int(word[2][1])+j)] > 1:
                error = 1
    if error == 0:
        cleanclaim = word[0]
        break

print("Part 2: " + str(cleanclaim))