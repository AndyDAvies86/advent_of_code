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


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2017day23.txt","r")
start = file.read()
startlist = start.split("\n")

#file = open("2017day22test.txt","r")
#startb = file.read()
#testlist = startb.split("\n")

#file = open("2017day20test2.txt","r")
#startc = file.read()
#testlist2 = startc.split("\n")

def splitlist(inputlist):
    outlist = []
    for row in inputlist:
        outlist.append(row.split(" "))
    return outlist
        
def runcode(inputlist):
    code = splitlist(inputlist)
    t = 0 
    i = 0
    count = 0
    register = {x:0 for x in alphabet[0:8]}
    while i < len(code):
#        print((t,i,code[i],register))
        if code[i][2] in alphabet:
            value = register[code[i][2]]
        else:
            value = int(code[i][2])
        if code[i][0] == 'set':
           register[code[i][1]] = value
        if code[i][0] == 'sub':
            register[code[i][1]] -= value
        if code[i][0] == 'mul':
            register[code[i][1]] *= value
            count += 1
        if code[i][0] == 'jnz':
            if code[i][1] in alphabet:
                valueb = register[code[i][1]]
            else:
                valueb = int(code[i][1])
            if valueb != 0:
                i += value-1
        i+=1
        t+=1
    return count



def runcode2(inputlist,time):
    code = splitlist(inputlist)
    t = 0 
    i = 0
    count = 0
    register = {x:0 for x in alphabet[0:8]}
    register['a'] = 1
#    print(register)
#    linelist = []
    while t < time:
        j = i
        if code[i][2] in alphabet:
            value = register[code[i][2]]
        else:
            value = int(code[i][2])
        if code[i][0] == 'set':
            register[code[i][1]] = value
        if code[i][0] == 'sub':
            register[code[i][1]] -= value
        if code[i][0] == 'mul':
            register[code[i][1]] *= value
            count += 1
        if code[i][0] == 'jnz':
            if code[i][1] in alphabet:
                valueb = register[code[i][1]]
            else:
                valueb = int(code[i][1])
            if valueb != 0:
                i += value-1
#        linelist.append(i)
        print((t,j,inputlist[j],[register[x] for x in alphabet[0:8]]))
        i+=1
        t+=1
    return register
 
     
        
"""
        Manually overwrite regicter to be 1,109900,126900,2,109900,1,0,0 as loop e-g = b and moves by 1
    A   Line 23 is 1, 109900, 126900, 3, 109900, 1, -109897, 0
        Then next will be 1,109900,126900,3,109900,1,0,0 as loop d-g = b and moves by 1, d is one higher
        Lines 23 is 1, 109900, 126900, 4, 109900, 1, -109896, 0
        so d-g = 109900 with one moving from g to d each time
        Try 1,109900,126900,109900,109900,1,0,0 on line 23
        Then back to A with b = 109917
        h goes up 1 here so h is 1001 before last round so 1001 but onl if n is non-prime
        
        answer is non-primes between 109900 and 126900 divisible by 17
        
    
"""

count = 0
for i in range(109900,126917,17):
    maxcheck = int(i**0.5)+1
    if i % 2 == 0:
        count += 1
    else:
        countadd = 0
        for j in range(3,maxcheck,2):
            if i % j == 0:
                countadd = 1
        count += countadd

   
#    
#
#def runcode2b(inputlist,time,line):
#    code = splitlist(inputlist)
#    t = 0 
#    i = line
#    count = 0
#    register = {'a':1, 'b': 126900, 'c':126900, 'd':126899, 'e':126898, 'f':0, 'g':-2 , 'h':1000}
#    while t < time:
#        j = i
#        if code[i][2] in alphabet:
#            value = register[code[i][2]]
#        else:
#            value = int(code[i][2])
#        if code[i][0] == 'set':
#            register[code[i][1]] = value
#        if code[i][0] == 'sub':
#            register[code[i][1]] -= value
#        if code[i][0] == 'mul':
#            register[code[i][1]] *= value
#            count += 1
#        if code[i][0] == 'jnz':
#            if code[i][1] in alphabet:
#                valueb = register[code[i][1]]
#            else:
#                valueb = int(code[i][1])
#            if valueb != 0:
#                i += value-1
##        linelist.append(i)
#        print((t,j,inputlist[j],[register[x] for x in alphabet[0:8]]))
#        i+=1
#        t+=1
#    return register
#   
#
#def runcode2c(inputlist):
#    code = splitlist(inputlist)
#    t = 0 
#    i = 0
#    count = 0
#    register = {x:0 for x in alphabet[0:8]}
#    register['a'] = 1
#    while t < 18:
#        j = i
#        if code[i][2] in alphabet:
#            value = register[code[i][2]]
#        else:
#            value = int(code[i][2])
#        if code[i][0] == 'set':
#            register[code[i][1]] = value
#        if code[i][0] == 'sub':
#            register[code[i][1]] -= value
#        if code[i][0] == 'mul':
#            register[code[i][1]] *= value
#            count += 1
#        if code[i][0] == 'jnz':
#            if code[i][1] in alphabet:
#                valueb = register[code[i][1]]
#            else:
#                valueb = int(code[i][1])
#            if valueb != 0:
#                i += value-1
#        t += 1
#        i += 1
#    print((i,inputlist[i]))
#    while g != 0:
#        code[e] += 1
#        code[g] += 1
#    while t < 18:
#        j = i
#        if code[i][2] in alphabet:
#            value = register[code[i][2]]
#        else:
#            value = int(code[i][2])
#        if code[i][0] == 'set':
#            register[code[i][1]] = value
#        if code[i][0] == 'sub':
#            register[code[i][1]] -= value
#        if code[i][0] == 'mul':
#            register[code[i][1]] *= value
#            count += 1
#        if code[i][0] == 'jnz':
#            if code[i][1] in alphabet:
#                valueb = register[code[i][1]]
#            else:
#                valueb = int(code[i][1])
#            if valueb != 0:
#                i += value-1
#        t += 1
#        i += 1
#    
#    return register    