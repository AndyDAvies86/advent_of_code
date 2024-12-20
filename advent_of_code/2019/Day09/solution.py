
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import json

#%%
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()
#%%
file = open("inputfile.txt","r")
start = file.read()
startlist = start.split(",")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split(",")

#%%

def parse(inputlist):
    return[int(x) for x in inputlist]

def op1(inputlist,p1,p2,p3,mem,pos,relbase,inputint):
    inputlist[p3] = inputlist[p1]+inputlist[p2]
    pos=pos+4
    return inputlist,mem,pos,relbase

def op2(inputlist,p1,p2,p3,mem,pos,relbase,inputint):
    inputlist[p3] = inputlist[p1]*inputlist[p2]
    pos=pos+4
    return inputlist,mem,pos,relbase

def op3(inputlist,p1,mem,pos,relbase,inputint):
    inputlist[p1] = inputint
    pos=pos+2
    return inputlist,mem,pos,relbase

def op4(inputlist,p1,mem,pos,relbase,inputint):
    mem.append(inputlist[p1])
    pos=pos+2
    # print(pos,p1,mem)
    return inputlist,mem,pos,relbase

def op5(inputlist,p1,p2,mem,pos,relbase,inputint):
    if inputlist[p1] != 0:
        pos = inputlist[p2]
    else: 
        pos = pos+3
    return inputlist,mem,pos,relbase        

def op6(inputlist,p1,p2,mem,pos,relbase,inputint):
    if inputlist[p1] == 0:
        pos = inputlist[p2]
    else: 
        pos = pos+3
    return inputlist,mem,pos,relbase

def op7(inputlist,p1,p2,p3,mem,pos,relbase,inputint):
    if inputlist[p1]<inputlist[p2]:
        inputlist[p3] = 1
    else:
        inputlist[p3] = 0
    pos=pos+4
    return inputlist,mem,pos,relbase

def op8(inputlist,p1,p2,p3,mem,pos,relbase,inputint):
    if inputlist[p1]==inputlist[p2]:
        inputlist[p3] = 1
    else:
        inputlist[p3] = 0
    pos=pos+4
    return inputlist,mem,pos,relbase 

def op9(inputlist,p1,mem,pos,relbase,inputint):
    relbase = relbase+inputlist[p1]
    pos=pos+2
    return inputlist,mem,pos,relbase       

def oprun(inputlist,oc,p1,p2,p3,mem,pos,relbase,inputint):
    if oc == 1:
        return op1(inputlist,p1,p2,p3,mem,pos,relbase,inputint)
    if oc==2:
        return op2(inputlist,p1,p2,p3,mem,pos,relbase,inputint)
    if oc==3:
        return op3(inputlist,p1,mem,pos,relbase,inputint)
    if oc==4:
        return op4(inputlist,p1,mem,pos,relbase,inputint)
    if oc==5:
        return op5(inputlist,p1,p2,mem,pos,relbase,inputint)
    if oc==6:
        return op6(inputlist,p1,p2,mem,pos,relbase,inputint)
    if oc == 7:
        return op7(inputlist,p1,p2,p3,mem,pos,relbase,inputint)
    if oc==8:
        return op8(inputlist,p1,p2,p3,mem,pos,relbase,inputint)
    if oc==9:
        return op9(inputlist,p1,mem,pos,relbase,inputint)
    # else:
    #     return inputlist

def intcode(program,inputint):
    program = program + [0 for x in range(0,10000)]
    pos = 0
    relbase = 0
    mem=[]
    l = len(program)
    a=0
    while True:
        if program[pos] == 99:
            # print(program)
            return mem
        # print(a,pos,program[pos:min(l-1,pos+4)])
        oc = program[pos]%100
        par1 = (program[pos]//100)%10
        par2 = (program[pos]//1000)%10
        par3 = (program[pos]//10000)
        # print("pars",oc,par1,par2,par3)
        if par1==1:
            p1 = pos+1
        elif par1==2:
            p1 = relbase+program[pos+1]
        else:
            p1 = program[pos+1]
        # print("p1: ",p1)
        if par2==1:
            p2 = pos+2
        elif par2==2:
            p2 = relbase+program[pos+2]
        else:
            p2 = program[min(l-1,pos+2)]
        # print("p2: ",p2)
        if par3==1:
            p3 = pos+3
        elif par3==2:
            p3 = relbase+program[pos+3]
        else:
            p3 = program[min(l-1,pos+3)]
        # print("p3: ",p3)
        # print("pars",pos,oc,par1,par2,par3,p1,p2,p3,mem,relbase,inputint)
        a=a+1
        program,mem,pos,relbase = oprun(program,oc,p1,p2,p3,mem,pos,relbase,inputint)




#%%        

def part1(inputlist):
    program = parse(startlist)
    # print(program)
    return intcode(program,1)[0]



def part2(inputlist):
    program = parse(startlist)
    # print(program)
    return intcode(program,2)[0]

#%%