
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


def get_to_output(intcode):
    while len(intcode.mem)<2:
        if intcode.program[intcode.pos] == 99:
            return
        intcode.oprun()
    return

#%%        

def part1(inputlist):
    whites = []
    painted = set([])
    rob_pos = [0,0]
    nesw = deque([[0,1],[1,0],[0,-1],[-1,0]])
    program = parse(inputlist)
    int_m=intcode(program,[0])
    a = 0
    while int_m.program[int_m.pos] != 99:
        get_to_output(int_m)
        if int_m.program[int_m.pos] == 99:
            return len(painted)
        # print(a,nesw,int_m.mem)
        if int_m.mem[0] == 0 and rob_pos in whites:
            whites.remove(rob_pos)
        if int_m.mem[0] == 1 and rob_pos not in whites:
            whites.append(rob_pos)
        if int_m.mem[0] == 1:
            painted.add(tuple(rob_pos))
        if int_m.mem[1] == 1:
            nesw.rotate(1)
        if int_m.mem[1] == 0:
            nesw.rotate(-1)
        rob_pos = [rob_pos[0]+nesw[0][0],rob_pos[1]+nesw[0][1]]
        if rob_pos in whites:
            int_m.inputdata=[1]
        else:
            int_m.inputdata=[0]
        int_m.paramters()
        # print(a,nesw,int_m.oc,int_m.pos)
        # print(int_m.program[int_m.pos:int_m.pos+4],int_m.mem,int_m.inputdata)
        # print(a,rob_pos,nesw[0],int_m.mem,whites)
        int_m.mem = []
        a = a+1
        
    return len(painted)



def part2(inputlist):    
    whites = [[0,0]]
    painted = set([])
    rob_pos = [0,0]
    nesw = deque([[0,1],[1,0],[0,-1],[-1,0]])
    program = parse(inputlist)
    int_m=intcode(program,[1])
    a = 0
    while int_m.program[int_m.pos] != 99:
        get_to_output(int_m)
        if int_m.program[int_m.pos] == 99:
            break
        # print(a,nesw,int_m.mem)
        if int_m.mem[0] == 0 and rob_pos in whites:
            whites.remove(rob_pos)
        if int_m.mem[0] == 1 and rob_pos not in whites:
            whites.append(rob_pos)
        if int_m.mem[0] == 1:
            painted.add(tuple(rob_pos))
        if int_m.mem[1] == 1:
            nesw.rotate(1)
        if int_m.mem[1] == 0:
            nesw.rotate(-1)
        rob_pos = [rob_pos[0]+nesw[0][0],rob_pos[1]+nesw[0][1]]
        if rob_pos in whites:
            int_m.inputdata=[1]
        else:
            int_m.inputdata=[0]
        int_m.paramters()
        # print(a,nesw,int_m.oc,int_m.pos)
        # print(int_m.program[int_m.pos:int_m.pos+4],int_m.mem,int_m.inputdata)
        # print(a,rob_pos,nesw[0],int_m.mem,whites)
        int_m.mem = []
        a = a+1
    # print(whites)
    x_min=99999
    x_max=-99999
    y_min=99999
    y_max=-99999
    for pos in whites:
        x_min = min(x_min,pos[0])
        x_max = max(x_max,pos[0])
        y_min = min(y_min,pos[1])
        y_max = max(y_max,pos[1])
    print(x_min,x_max,y_min,y_max)
    board=[' '*(x_max-x_min)]*(y_max-y_min+1)
    for pos in whites:
        x=pos[0]-x_min
        y=pos[1]-y_min
        print(x,y)
        if pos[0] == x_max:
            board[y] = board[y][:-1]+'#'
        elif pos[0] == x_min:
            board[y] = '#'+board[y][1:]
        else:
            board[y] = board[y][:x]+'#'+board[y][x+1:]

    print(board)
    return board

#%%