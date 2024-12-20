
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
startlist = start.split("\n\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n\n")


#%%

def parselist(inputlist):
    inst = [[x for x in y.split("|")] for y in inputlist[0].split("\n")]
    updates = inputlist[1].split("\n")
    return inst,updates
#%%

def checks(inst,update):
    mid = len(update)//2
    midpage = int(update[mid-1:mid+1])
    for check in inst:
        p1 = update.find(check[0])
        p2 = update.find(check[1])
        if p1 != -1 and p2 != -1 and p1>p2:
            return 0
    return midpage
        


def part1(inputlist):
    inst,updates = parselist(inputlist)
    score = 0
    for update in updates:
        # print(score)
        score = score+checks(inst,update)
    return score
        

#%%

def part2(inputlist):
    inst,old_updates = parselist(inputlist)
    updates = []
    for upd in old_updates:
        # print(upd,checks(inst,upd))
        if checks(inst,upd) == 0:
            updates.append(upd)
    # print("endcheck")
    # print(updates)
    # print("clean")
    new_updates=[]
    score = 0
    for jj in range(0,len(updates)):
        update = updates[jj]
        ii = 0
        toclear = len(inst)
        # print('start',jj,update)
        while toclear > 0:
            # print(ii,toclear)
            check = inst[ii]
            p1 = update.find(check[0])
            p2 = update.find(check[1])
            # print(p1,p2)
            # if p1 != -1 and p2 != -1:

            #     print(check,p1,p2,update,toclear)
            if p1 != -1 and p2 != -1 and p1>p2:
                if p1+3 < len(update):
                    update = update[:p2]+update[p1:p1+3]+update[p2:p1]+update[p1+3:]
                    toclear = len(inst)
                else:
                    update = update[:p2]+update[p1:]+','+update[p2:p1-1]
                    toclear = len(inst)
            else:
                toclear = toclear - 1
            if ii == len(inst)-1:
                ii = -1
            ii = ii+1
            # print(ii)
        new_updates.append(update)
        mid = len(update)//2
        midpage = int(update[mid-1:mid+1])
        # print('score',jj,score,mid,midpage)
        score = score+midpage
    # print(new_updates)
    return score
    

        
#%%