
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
    blocks = [int(x) for x in inputlist[0]]
    f_bl = [blocks[ii] for ii in range(0,len(blocks),2)]
    s_bl = [blocks[ii] for ii in range(1,len(blocks),2)]
    return blocks,f_bl,s_bl
#%%

def part1(inputlist):
    blocks,f_bl,s_bl = parselist(inputlist)
    score = 0
    end_pos = (len(blocks)-1)//2
    st_pos = 0
    mult = 0
    while sum(f_bl) > 0:
        if f_bl[0] > 0:
            for ii in range(0,f_bl[0]):
                score = score + st_pos*mult
                mult = mult+1
            f_bl[0] = 0
        elif f_bl[0] == 0 and s_bl[0] > 0:
            if s_bl[0] <= f_bl[-1]:
                for ii in range(0,s_bl[0]):
                    score = score+end_pos*mult
                    mult = mult+1
                f_bl[-1] = f_bl[-1]-s_bl[0]
                s_bl[0] = 0
            else:
                for ii in range(0,f_bl[-1]):
                    score = score + mult*end_pos
                    mult = mult+1
                s_bl[0] = s_bl[0] - f_bl[-1]
                f_bl = f_bl[:-1]
                end_pos = end_pos-1
        else:
            f_bl = f_bl[1:]
            s_bl = s_bl[1:]
            st_pos = st_pos+1
        # print(score)
    return score



#%%

def shuffle(f_bl,s_bl,jj):
    for kk in range(0,len(s_bl)):
        # print(kk,f_bl[-1-jj][1],s_bl[kk][1])
        if f_bl[-1-jj][1] <= s_bl[kk][0] and f_bl[-1-jj][2] > s_bl[kk][1]: 
            s_bl[kk][0] = s_bl[kk][0] - f_bl[-1-jj][1]
            f_bl[-1-jj][2] = s_bl[kk][1]
            s_bl[kk][1] = s_bl[kk][1] + f_bl[-1-jj][1]
            return f_bl,s_bl
    return f_bl,s_bl
        


def part2(inputlist):
    blocks,f_bl_pre,s_bl_pre = parselist(inputlist)
    s_bl_pre = s_bl_pre +[0]
    f_bl =[]
    s_bl = []
    pos = 0
    for ii in range(0,len(f_bl_pre)):
        f_bl.append([ii,f_bl_pre[ii],pos])
        s_bl.append([s_bl_pre[ii],pos+f_bl_pre[ii]])
        pos = pos + f_bl_pre[ii]+s_bl_pre[ii]

    for jj in range(0,len(f_bl)):  
        f_bl,s_bl = shuffle(f_bl,s_bl,jj)

    return sum([x[0]*sum(range(x[2],x[1]+x[2])) for x in f_bl])
   
#%%