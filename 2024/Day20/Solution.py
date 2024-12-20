
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
            # if (wall[0]+1,wall[1]) in sp or (wall[0]-1,wall[1]) in sp or (wall[0],wall[1]+1) in sp or (wall[0],wall[1]-1) in sp:
            if True:
                remove_singles.append(wall)
    return remove_singles

def new_short(walls,wall,h,w,s,e,t):
    P = nx.grid_2d_graph(w,h)
    walls = [wl for wl in walls if wl != wall]
    P.remove_nodes_from(walls)
    nshort = nx.shortest_path(P,s,e)
    return len(nshort)-1

# def try_short(wall,G,s,e,t):
    # G.add

def part1(inputlist):
    saves = []
    sdict = {}
    paths,walls,s,e = parselist(inputlist)
    h = len(inputlist)
    w = len(inputlist[0])
    W = nx.grid_2d_graph(w,h)
    W.remove_nodes_from(paths+[s,e])
    # drawgraph(W)
    G = nx.grid_2d_graph(w,h)
    G.remove_nodes_from(walls)
    # drawgraph(G)
    sp = nx.shortest_path(G,s,e)
    # print(sp)
    t = len(sp)-1
    print('t',t)
    rem_walls = walls_list(W,sp)
    print('w',len(rem_walls))
    for wall in rem_walls:
        neigh = [(wall[0]+1,wall[1]),(wall[0]-1,wall[1]),(wall[0],wall[1]+1),(wall[0],wall[1]-1)]
        nind = [sp.index(x) for x in neigh if x in sp]
        for x in nind:
            for y in nind:
                if y > x:
                    sdict[(sp[x],sp[y])] = y-x-2
    # return sorted(Counter(sdict.values()).items())
    return sum(v >= 100 for v in sdict.values())
        # if len(nind) > 1:
        #     saves.append(max(nind)-min(nind))
        # if t-new_short(W,wlist,h,w,s,e,t) == 64:
            # print(wlist)
        # saves.append(t-new_short(W,wall,h,w,s,e,t))
        # if len(saves) % 100 == 0:
            # print(len(saves))
    # return sorted(Counter(saves).items())
    # return sum([x>=100 for x in saves])


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
    for ii in range(0,len(sp)-2):
        for jj in range(ii+2,len(sp)):
            md = abs(sp[ii][0]-sp[jj][0])+abs(sp[ii][1]-sp[jj][1])
            # print(sp[ii],sp[jj],md)
            if md <= maxdist and jj-ii>mcheat-2+md:
                # print(sp[ii],sp[jj],md,ii,jj)
                score = score + 1
    return score
#%%