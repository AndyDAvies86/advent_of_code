
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import networkx as nx

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
    H = []
    G = nx.DiGraph()

    for row in inputlist:
        conn = row.split(' -> ')
        out = conn[1]
        inp = conn[0].split(' ')
        H.append([inp,out])
        print(inp,out)
        if len(inp) == 1:
            try:   
                inpint = int(inp[0])
                print(inpint)
                G.addnode(out,value=inpint)
            except:
                G.add_edge(inp[0],out)



    return G

#%%

def part1(inputlist):
    pass
#%%

def part2(inputlist):
    pass
#%%