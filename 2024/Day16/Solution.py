
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
    d = 'NESWN'
    walls,s,e = parselist(inputlist)
    G = nx.Graph()
    node_list = [(x,y,z) for x in range(0,w) for y in range(0,h) for z in ('N','E','S','W')]
    G.add_nodes_from([(x,y,z) for x in range(0,w) for y in range(0,h) for z in ('N','E','S','W')])
    turn_list = [((x[0],x[1],d[z]),(x[0],x[1],d[z+1])) for x in node_list for z in range(0,4)]
    edge_list = [(x,y) for x in node_list for y in node_list if (x[2] == y[2] and (abs(x[0]-y[0])+abs(x[1]-y[1])==1))]
    G.add_edges_from(edge_list,wt = 1000)
    G.add_edges_from(turn_list,weight=1)
    G.add_node(e)
    end_edges = [((e[0],e[1],x),e) for x in ('N','E','S','W')]
    G.add_edges_from(end_edges,weight=0)
    G.remove_nodes_from(walls)
    return nx.shortest_path(G,(s[0],s[1],'N'),e,'weight')
    # paths = nx.all_simple_paths(G,s,e)
    # print(len(list(paths)))
    # return paths
#%%

def part2(inputlist):
    pass
#%%