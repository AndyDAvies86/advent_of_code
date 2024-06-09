
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
class intcode:
    def __init__(self,program,inputdata):
        self.program=program + [0 for x in range(0,10000)]
        self.inputdata=inputdata
        self.pos = 0
        self.mem=[]
        self.relbase=0
        self.outputdata=[]
        self.oc = 0
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.opdict = {
            1:self.op1,
            2:self.op2,
            3:self.op3,
            4:self.op4,
            5:self.op5,
            6:self.op6,
            7:self.op7,
            8:self.op8,
            9:self.op9,
            99:self.op99
        }
    
    def paramters(self):
        self.oc = self.program[self.pos]%100
        par1 = (self.program[self.pos]//100)%10
        par2 = (self.program[self.pos]//1000)%10
        par3 = (self.program[self.pos]//10000)
        if par1 == 1:
            self.p1 = self.pos+1
        elif par1 == 2:
            self.p1 = self.relbase+self.program[self.pos+1]
        else:
            self.p1 = self.program[self.pos+1]
        if par2 == 1:
            self.p2 = self.pos+2
        elif par2 == 2:
            self.p2 = self.relbase+self.program[self.pos+2]
        else:
            self.p2 = self.program[self.pos+2]
        if par3 == 1:
            self.p3 = self.pos+3
        elif par3 == 2:
            self.p3 = self.relbase+self.program[self.pos+3]
        else:
            self.p3 = self.program[self.pos+3]

    def op1(self):
        self.program[self.p3] = self.program[self.p1]+self.program[self.p2]
        self.pos = self.pos+4
    def op2(self):
        self.program[self.p3] = self.program[self.p1]*self.program[self.p2]
        self.pos = self.pos+4
    def op3(self):
        if len(self.inputdata) == 0:
            print("Awaiting data")
        else:
            self.program[self.p1] = self.inputdata[0]
            self.inputdata = self.inputdata[1:]
        self.pos = self.pos+2
    def op4(self):
        self.mem.append(self.program[self.p1])
        self.pos = self.pos+2    
    def op5(self):
        if self.program[self.p1] != 0:
            self.pos = self.program[self.p2]
        else:
            self.pos = self.pos+3
    def op6(self):
        if self.program[self.p1] == 0:
            self.pos = self.program[self.p2]
        else:
            self.pos = self.pos+3
    def op7(self):
        if self.program[self.p1]<self.program[self.p2]:
            self.program[self.p3] = 1
        else:
            self.program[self.p3] = 0
        self.pos = self.pos+4
    def op8(self):
        if self.program[self.p1]==self.program[self.p2]:
            self.program[self.p3] = 1
        else:
            self.program[self.p3] = 0
        self.pos = self.pos+4
    def op9(self):
        self.relbase=self.relbase+self.program[self.p1]
        self.pos = self.pos + 2
    def op99(self):
        print("Terminates")
        print(self.mem)
    
    def oprun(self):
        self.paramters()
        # print(a,self.oc,self.pos,self.p1,self.p2,self.p3,self.relbase,self.program[self.pos:self.pos+4],self.mem)
        self.opdict[self.oc]()



#%%

def parse(inputlist):
    return[int(x) for x in inputlist]



#%%        

def part1(inputlist):
    program = parse(inputlist)
    int_machine=intcode(program,[1])
    # a=0
    oc_list=[]
    while int_machine.oc != 99:
        # a=a+1
        int_machine.paramters()
        # print(a,int_machine.pos,int_machine.program[int_machine.pos:int_machine.pos+4],int_machine.program[1015],int_machine.program[236:238],[int_machine.p1,int_machine.p2,int_machine.p3],int_machine.relbase)
        int_machine.oprun()
        oc_list.append(int_machine.oc)
    return int_machine.mem



def part2(inputlist):
    program = parse(inputlist)
    int_machine=intcode(program,[2])
    # a=0
    while int_machine.oc != 99:
        int_machine.paramters()
        int_machine.oprun()
        # a=a+1
        # print(a)
    return int_machine.mem

#%%