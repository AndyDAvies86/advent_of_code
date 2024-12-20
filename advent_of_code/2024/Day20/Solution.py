
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque,Counter
import itertools as it
import copy
import networkx as nx
import matplotlib.pyplot as plt
from functools import cache

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
    paths = []
    for jj in range(0,len(inputlist)):
        for ii in range(0, len(inputlist[0])):
            if inputlist[jj][ii] == '#':
                walls.append((ii,jj))
            elif inputlist[jj][ii] == '.':
                paths.append((ii,jj))
            elif inputlist[jj][ii] == 'S':
                s = (ii,jj)
                paths.append((ii,jj))
            elif inputlist[jj][ii] == 'E':
                e = (ii,jj)
                paths.append((ii,jj))
    return paths,walls,s,e
#%%
def drawgraph(G):
    pos = {(x,y):(x,-y) for x,y in G.nodes()}
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                        node_size = 200)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, arrows=False)
    plt.show()  

#%%

def walls_list(W,sp):
    remove_singles = []
    for wall in W:
        if len(list(W.neighbors(wall))) <= 2:
            remove_singles.append(wall)
    return remove_singles

def part1(inputlist):
    sdict = {}
    paths,walls,s,e = parselist(inputlist)
    h = len(inputlist)
    w = len(inputlist[0])
    W = nx.grid_2d_graph(w,h)
    W.remove_nodes_from(paths+[s,e])
    G = nx.grid_2d_graph(w,h)
    G.remove_nodes_from(walls)
    sp = nx.shortest_path(G,s,e)
    t = len(sp)-1
    rem_walls = walls_list(W,sp)
    for wall in rem_walls:
        neigh = [(wall[0]+1,wall[1]),(wall[0]-1,wall[1]),(wall[0],wall[1]+1),(wall[0],wall[1]-1)]
        nind = [sp.index(x) for x in neigh if x in sp]
        for x in nind:
            for y in nind:
                if y > x:
                    sdict[(sp[x],sp[y])] = y-x-2
    return sum(v >= 100 for v in sdict.values())


#%%

def part2(inputlist,maxdist,mcheat):
    paths,walls,s,e = parselist(inputlist)
    h = len(inputlist)
    w = len(inputlist[0])
    G = nx.grid_2d_graph(w,h)
    G.remove_nodes_from(walls)
    sp = nx.shortest_path(G,s,e)
    print(len(sp)-1)
    score = 0
    if mcheat > len(sp):
        return 0
    for ii in range(0,len(sp)-mcheat):
        for jj in range(ii+mcheat,len(sp)):
            md = abs(sp[ii][0]-sp[jj][0])+abs(sp[ii][1]-sp[jj][1])
            # print(sp[ii],sp[jj],md)
            if md <= maxdist and jj-ii>mcheat-2+md:
                # print(sp[ii],sp[jj],md,ii,jj)
                score = score + 1
    return score
#%%