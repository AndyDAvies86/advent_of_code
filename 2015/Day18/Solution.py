
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
    lights = {}
    for ii in range(0,len(inputlist[0])):
        for jj in range (0,len(inputlist)):
            lights[(ii,jj)] = 0
            if inputlist[jj][ii] == '#':
                lights[(ii,jj)] = 1
    return lights
#%%
def drawgraph(G,lights):
    pos = {(x,y):(x,-y) for x,y in G.nodes()}
    # labels = nx.get_node_attributes(parselist(testlist),'value')
    colour = ['#EEEE00' if lights[node]==1 else '#999999' for node in G]
    # print(labels)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                        node_color=colour,node_size = 500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, arrows=False)
    plt.show()

#%%

def nextstep(lights,G):
    newlights = {}
    for n in G:
        n_l = sum([lights[x] for x in G.neighbors(n)])
        newlights[n] = 0
        if n_l == 3 or (n_l == 2 and lights[n] == 1):
            newlights[n] = 1
    return newlights
    

def part1(inputlist):
    lights = parselist(inputlist)
    # print(lights)
    h = len(inputlist)
    w = len(inputlist[0])
    G = nx.grid_2d_graph(w,h)
    G.add_edges_from([ ((x,y), (x+1, y+1)) for x in range(0,w-1) for y in range(0,h-1)]) 
    G.add_edges_from([ ((x+1,y), (x, y+1)) for x in range(0,w-1) for y in range(0,h-1)]) 
    t=0
    # print(t)
    # drawgraph(G,lights)
    for tt in range (0,100):
        lights = nextstep(lights,G)
        # print(tt+1)
        # drawgraph(G,lights)
    return sum([lights[x] for x in G])


#%%

def part2(inputlist):
    h = len(inputlist)
    w = len(inputlist[0])
    lights = parselist(inputlist)
    for x in [(0,0),(0,h-1),(w-1,0),(w-1,h-1)]:
            lights[x] = 1
    # print(lights)

    G = nx.grid_2d_graph(w,h)
    G.add_edges_from([ ((x,y), (x+1, y+1)) for x in range(0,w-1) for y in range(0,h-1)]) 
    G.add_edges_from([ ((x+1,y), (x, y+1)) for x in range(0,w-1) for y in range(0,h-1)]) 
    t=0
    # print(t)
    # drawgraph(G,lights)
    for tt in range (0,100):
        lights = nextstep(lights,G)
        # print(tt+1)
        # drawgraph(G,lights)
        for x in [(0,0),(0,h-1),(w-1,0),(w-1,h-1)]:
            lights[x] = 1
    return sum([lights[x] for x in G])
#%%