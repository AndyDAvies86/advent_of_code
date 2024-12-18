
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import networkx as nx
import matplotlib.pyplot as plt

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
    walls = []
    for jj in range(0,len(inputlist)):
        for ii in range(0, len(inputlist[0])):
            if inputlist[jj][ii] == '#':
                walls.append((ii,jj))
            elif inputlist[jj][ii] == '.':
                pass
            elif inputlist[jj][ii] == 'S':
                s = (ii,jj)
            elif inputlist[jj][ii] == 'E':
                e = (ii,jj)
    return walls,s,e
#%%

def part1(inputlist):
    h = len(inputlist)
    w = len(inputlist)
    walls,s,e = parselist(inputlist)
    G = nx.grid_2d_graph(w,h)
    G.remove_nodes_from(walls)
    paths = nx.all_simple_paths(G,s,e)
    print(len(list(paths)))
    return paths
#%%

def part2(inputlist):
    pass
#%%