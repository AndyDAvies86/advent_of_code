
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

file = open("inputsi.txt","r")
si = file.read()
silist = si.split("\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n")

file = open("inputtest2.txt","r")
startc = file.read()
testlist2 = startc.split("\n")


#%%

def parselist(inputlist):
    pass

class comp:
    def __init__(self,inputlist):
        self.reg={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7}
        self.reg['a'] = int(inputlist[0].split(' ')[-1])
        self.reg['b'] = int(inputlist[1].split(' ')[-1])
        self.reg['c'] = int(inputlist[2].split(' ')[-1])
        self.ops = [int(x) for x in inputlist[-1].split(' ')[-1].split(',')]
        self.pos = 0
        self.combo = {0:0,1:1,2:2,3:3,4:'a',5:'b',6:'c'}
        self.outs = []
    def move(self):
        inst = self.ops[self.pos]
        lit = self.reg[self.ops[self.pos+1]]
        combo = self.reg[self.combo[self.ops[self.pos+1]]]
        if inst == 0:
            self.reg['a']=self.reg['a']//(2**combo)
        elif inst == 1:
            self.reg['b'] = self.reg['b']^lit
        elif inst == 2:
            self.reg['b'] = combo % 8
        elif inst == 3:
            if self.reg['a'] != 0:
                self.pos = self.reg[lit] - 2
        elif inst == 4:
            self.reg['b'] = self.reg['b']^self.reg['c']
        elif inst == 5:
            self.outs.append(combo % 8)
        elif inst == 6:
            self.reg['b']=self.reg['a']//(2**combo)
        elif inst == 7:
            self.reg['c']=self.reg['a']//(2**combo)
        self.pos = self.pos+2


    
#%%

#Me 2,4,1,1,7,5,1,5,4,3,0,3,5,5,3,0
#Si 2,4,1,2,7,5,1,3,4,3,5,5,0,3,3,0
#SI pct 4532306073267275

def part1(inputlist):
    box = comp(inputlist)
    t = 0
    while True:
        # print(t,box.pos,box.reg['a'],box.ops[box.pos:box.pos+2],box.outs)
        t = t+1
        if box.pos >= len(box.ops):
            return ','.join([str(x) for x in box.outs])
        else:
            box.move()
        # print(bo)
#%%

#2,4,1,1,7,5,1,5,4,3,0,3,5,5,3,0
def p2test(inputlist,a_start,a_max):
    a_test = a_start
    while a_test < a_start+a_max:
        # if a_test % 10000 == 0:
        #     print(a_test)
        box = comp(inputlist)
        box.reg['a'] = a_test
        t = 0
        go = True
        while go:
            # print(t,box.pos,box.reg['a'],box.ops[box.pos:box.pos+2],box.outs)
            t = t+1
            if box.pos >= len(box.ops):
                box_outs = ','.join([str(x) for x in box.outs])
                if box.outs == box.ops:
                    return a_test
                print(a_test,box_outs)
                go = False
            else:
                box.move()
        a_test = a_test+1

def checkbox(inputlist,a_test):
    box = comp(inputlist)
    box.reg['a'] = a_test
    while True:
        if box.pos >= len(box.ops):
            return box.outs
        else:
            box.move()


def checkboxes(inputlist,a_start,t_out,ii):
    for a_test in range(a_start,a_start+8**(ii+1)):
        checklist = checkbox(inputlist,a_test)
        # print('ts',a_test,checklist,t_out,t_out[-ii-1:])
        if t_out[-ii-1:] == checklist[:ii+1]:
            return[int(x) for x in oct(a_test)[2:]]
    short = [int(x) for x in oct(a_start)[2:]]
    k = ii+1-len(short)
    return [0]*k + short

#test is 345300
def part2(inputlist):
    m_box = comp(inputlist)
    t_out = m_box.ops
    eights = [0]
    # outlist = []
    for ii in range(0,len(t_out)):
        a_start = sum([(8**(jj+1))*eights[-jj-1] for jj in range(0,len(eights))])
        # print('st',a_start,ii)
        eights=checkboxes(inputlist,a_start,t_out,ii)
        # print('eights',a_start,eights)
    return sum([(8**(jj))*eights[-jj-1] for jj in range(0,len(eights))])


    
    
#%%