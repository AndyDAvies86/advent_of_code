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

from advent_of_code.utils.helper_functions import *

#%%
start = lineparse('inputfile.txt')
test = lineparse('inputtest.txt')

#%%

def parselist(inputlist):
    pass

def drawmaze(stringlist):
    h = len(stringlist)
    w = len(stringlist[0])
    G = nx.DiGraph()
    for ii in range(0,h):
        for jj in range(0,w):
            if stringlist[ii][jj] =='S':
                s = (jj,ii)
            if stringlist[ii][jj] =='E':
                e = (jj,ii)
    node_list = [(x,y) for x in range(0,w) for y in range(0,h)]
    G.add_nodes_from(node_list)
    heights={x:alphabet.index(x) for x in alphabet}
    heights['S'] = 1
    heights['E'] = 26
    for n1 in node_list:
        for n2 in node_list:
            if abs(n1[0]-n2[0])+abs(n1[1]-n2[1]) == 1:
                if heights[stringlist[n2[1]][n2[0]]] <= heights[stringlist[n1[1]][n1[0]]]+2:
                    G.add_edge(n1,n2)
    return G,s,e

def bfs(edges,min_dist,h,w):
    for ii in range(0,h):
        for jj in range(0,w):
            for pp in edges[(jj,ii)]:
                min_dist[pp] = min(min_dist[pp],min_dist[(jj,ii)]+1)
    return min_dist

#%%

def nxpart1(inputlist):
    G,s,e = drawmaze(inputlist)
    drawgraph(G)
    sp=nx.shortest_path(G,s,e)
    print(sp)
    return len(sp)-1

def part1(inputlist):
    edges= {}
    heights={x:alphabet.index(x) for x in alphabet}
    heights['S'] = 1
    heights['E'] = 26
    h = len(inputlist)
    w = len(inputlist[0])
    min_dist = {}
    for ii in range(0,h):
        for jj in range(0,w):
            if inputlist[ii][jj] =='S':
                start = (jj,ii)
                print('s',start)
            if inputlist[ii][jj] =='E':
                end = (jj,ii)
                print('e',end)
            conn = []
            for d in [(jj+1,ii),(jj-1,ii),(jj,ii+1),(jj,ii-1)]:
                if d[0] in range(0,w) and d[1] in range(0,h):
                    if heights[inputlist[ii][jj]] + 1 >= heights[inputlist[d[1]][d[0]]]:
                        conn.append(d)
            edges[(jj,ii)] = conn
            min_dist[(jj,ii)] = h*w*10
    min_dist[start] = 0
    for tt in range(0,h*w):
        min_dist = bfs(edges,min_dist,h,w)
        # print(tt,min_dist[end])
    return min_dist[end]

def checks(inputlist):
    edges= {}
    heights={x:alphabet.index(x) for x in alphabet}
    heights['S'] = 1
    heights['E'] = 26
    h = len(inputlist)
    w = len(inputlist[0])
    min_dist = {}
    for ii in range(0,h):
        for jj in range(0,w):
            if inputlist[ii][jj] =='S':
                start = (jj,ii)
                print('s',start)
            if inputlist[ii][jj] =='E':
                end = (jj,ii)
                print('e',end)
            conn = []
            for d in [(jj+1,ii),(jj-1,ii),(jj,ii+1),(jj,ii-1)]:
                if d[0] in range(0,w) and d[1] in range(0,h):
                    if heights[inputlist[ii][jj]] + 1 >= heights[inputlist[d[1]][d[0]]]:
                        conn.append(d)
            edges[(jj,ii)] = conn
            min_dist[(jj,ii)] = h*w*10
    min_dist[start] = 0
    for tt in range(0,h*w):
        min_dist = bfs(edges,min_dist,h,w)
        # print(tt,min_dist[end])
    return min_dist


#%%

def part2(inputlist):
    edges= {}
    heights={x:alphabet.index(x) for x in alphabet}
    heights['S'] = 1
    heights['E'] = 26
    h = len(inputlist)
    w = len(inputlist[0])
    min_dist = {}
    start_list = []
    for ii in range(0,h):
        for jj in range(0,w):
            if inputlist[ii][jj] =='S':
                start = (jj,ii)
                print('s',start)
                start_list.append(start)
            if inputlist[ii][jj] =='a':
                start_list.append((jj,ii))            
            if inputlist[ii][jj] =='E':
                end = (jj,ii)
                print('e',end)
            conn = []
            for d in [(jj+1,ii),(jj-1,ii),(jj,ii+1),(jj,ii-1)]:
                if d[0] in range(0,w) and d[1] in range(0,h):
                    # print((jj,ii),heights[inputlist[ii][jj]],d,heights[inputlist[d[1]][d[0]]])
                    if heights[inputlist[ii][jj]] <= heights[inputlist[d[1]][d[0]]] +1:
                        conn.append(d)
            edges[(jj,ii)] = conn
            min_dist[(jj,ii)] = h*w*10
    # print(edges)
    # print(end,edges[end])
    min_dist[end] = 0
    mins = []
    for tt in range(0,550):
        min_dist = bfs(edges,min_dist,h,w)
        # print(tt,min_dist[start])
        if tt%100 == 0:
            print(tt)
        # print('\n'.join([','.join([str(min_dist[(x,y)]) for x in range(w)]) for y in range(h)]))
    return min([min_dist[x] for x in start_list])
#%%