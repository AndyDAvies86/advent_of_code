
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy

#%%
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()
numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
numlist = [str(x) for x in range(0,10)]
#%%
file = open("inputfile.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n")


#%%

def parselist(inputlist):
    outlist = []
    for row in inputlist:
        x=row.split(": ")
        outlist.append([int(x[0]),[int(y) for y in x[1].split(" ")]])
    # outlist = [int(x.split(": ")[0]),[int(y) for y in x.split(": ")[1].split(" ")] for x in inputlist]
    return outlist
#%%

def cleancal(cal_list):
    outlist = []
    for row in cal_list:
        check = sum([y > row[0] for y in row[1]])
        if check == 0:
            outlist.append(row)
    return outlist

def checkperm(t,ops,perm_d,c_ops):
    perm = bin(perm_d)
    score = ops[0]
    for jj in range (1,c_ops):
        if perm[jj+2] == '0':
            score = score+ops[jj]
        else:
            score = score*ops[jj]
        if score == t and jj == c_ops-1:
            # print(t,'wins')
            return 1,perm_d
        elif score > t:
            newperm = perm_d+1
            # np_s = perm_d//(2**(c_ops-jj)) + 1
            # newperm = np_s*(2**(c_ops-jj))
            #can ignore next in power of 2 range
            # jj = 1 means add to next 2**(c_ops-2)
            # newperm_start = perm_d//(2**(c_ops-jj-1)) + 1
            # newperm = (2**(c_ops-jj-1))*(newperm_start)
            # print('more',t,ops,jj,perm,perm_d,score,newperm_start,newperm)
            # print('more',t,ops,perm,perm_d,score,c_ops)
            return 0,newperm
    # print(t,ops,perm,perm_d,score,c_ops)
    if score < t:
        # print('less',t,ops,perm,perm_d,score,c_ops)
        return 0,perm_d+1   
        

def checkrow(cal):
    t = cal[0]
    ops = cal[1]
    c_ops = len(ops)
    perm = 2**(c_ops-1)
    check = 0
    while perm < 2**(c_ops) and check == 0:
        check,perm = checkperm(t,ops,perm,c_ops)
        # print(t,check,perm)
    return check
       

def part1(inputlist):
    cal_list = parselist(inputlist)
    cals = cleancal(cal_list)
    score = 0
    for cal in cals:
        check = checkrow(cal)
        # print(check,perm)
        if check == 1:
            # print(cal[0])
            score=score+cal[0]
    return score
#%%

def ternary(n,c_ops):
    out = ''
    for ii in range(0,c_ops):
        base = 3**(c_ops-ii-1)
        mod = 3**(c_ops-ii)
        char = (n % mod) // base
        out = out+str(char)
    return out

# def checkcatrow(cal):
#     gaps = len(cal[1])-1
#     for ii in range(0,2**gaps):
#         num = bin(2**gaps + ii)[3:]
#         string = str(cal[1][0])
#         for jj in range(0,gaps):
#             if num[jj] == '0':
#                 string = string + ','
#             string = string + str(cal[1][jj+1])
#         newcal = [cal[0],[int(x) for x in string.split(",")]]
#         # print(ii,gaps,num,newcal)
#         if len(newcal[1]) == 1:
#             if cal[0] == newcal[1][0]:
#                 return 1
#         elif checkrow(newcal) == 1:
#             return 1
#     return 0
        


def p2checkrow(cal):
    t = cal[0]
    ops = cal[1]
    c_ops = len(ops)
    perm = 0
    check = 0
    while perm < 3**(c_ops-1) and check == 0:
        check,perm = p2checkperm(t,ops,perm,c_ops)
        # print(t,check,perm)
    return check

def p2checkperm(t,ops,perm_d,c_ops):
    perm = ternary(perm_d,c_ops-1)
    score = ops[0]
    for jj in range (1,c_ops):
        if perm[jj-1] == '0':
            score = score+ops[jj]
        elif perm[jj-1] == '1':
            score = score*ops[jj]
        else:
            score = int(str(score)+str(ops[jj]))
        if score == t and jj == c_ops-1:
            # print(jj,t,ops,perm_d,perm,c_ops,score)
            # print(t,'wins')
            return 1,perm_d
        elif score > t:
            newperm = perm_d+1
            # print(jj,t,ops,perm_d,perm,c_ops,score)
            return 0,newperm
    if score < t:
        # print('a',t,ops,perm_d,perm,c_ops,score)
        return 0,perm_d+1  

def part2(inputlist):
    cal_list = parselist(inputlist)
    cals = cleancal(cal_list)
    score = 0
    for cal in cals:
        check = p2checkrow(cal)
        # print(check,perm)
        if check == 1:
            # print(cal[0])
            score=score+cal[0]
    return score
#%%