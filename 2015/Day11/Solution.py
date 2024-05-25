
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
#%%
#file = open("inputfile.txt","r")
#start = file.read()
#startlist = start.split("\n")

#file = open("inputtest.txt","r")
#startb = file.read()
#testlist = startb.split("\n")

#%%
testinput = "abcdefgh"
startinput = "vzbxkghb"
allowed = 'abcdefghjkmnpqrstuvwxyz'

#%%
def increment(password):
    count = 0
    for ii in range (len(password)-1,-1,-1):
        #print(ii,password[ii])
        if password[ii] != "z":
            pos = allowed.find(password[ii])+1
            #print(pos,allowed[pos])
            password[ii] = allowed[pos]
            for jj in range (len(password)-1,len(password)-1-count,-1):
                password[jj] = "a"
            return password
        else:
          count += 1  
    for jj in range (len(password)-1,len(password)-1-count,-1):
        password[jj] = "a"
    return password

def testrun(inputlist):
    for ii in range(0,len(inputlist)-2):
        aa = [alphabet.find(x) for x in inputlist[ii:ii+3]]
        if aa[0]+1 == aa[1] and aa[0]+2 == aa[2]:
            return True
    return False

def testrpt(inputlist):
    for ii in range(0,len(inputlist)-1):
        aa = [alphabet.find(x) for x in inputlist[ii:ii+2]]
        if aa[0] == aa[1]:
            newlist = inputlist[ii+2:]
            for jj in range(0,len(newlist)-1):
                bb = [alphabet.find(x) for x in newlist[jj:jj+2]]
                if bb[0] == bb[1]:
                    return True
    return False

def bantest(inputlist):
    banlist = ['i','o','l']
    if sum([x in banlist for x in inputlist]) > 0:
        return False
    return True
#%%

def part1(inputlist):
    pwlist = list(inputlist)
    stop = 0
    while stop < 1:
        pwlist = increment(pwlist)
        #print(pwlist)
        if bantest(pwlist) and testrpt(pwlist) and testrun(pwlist):
            newpw = ''
            for ii in range(0,len(pwlist)):
                newpw += pwlist[ii]
            stop = 1
    return newpw

   
# %%

def part2(inputlist):
    
    return 
# %%
