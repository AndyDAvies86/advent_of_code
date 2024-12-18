
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
    return [tuple([int(y) for y in x.split(',')]) for x in inputlist]

#%%

def drawgraph(G):
    pos = {(x,y):(x,-y) for x,y in G.nodes()}
    # labels = nx.get_node_attributes(parselist(testlist),'value')
    # colour = ['#EEEE00' if labels[node]==1 else '#999999' for node in G]
    # print(labels)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                        # node_color=colour,
                        node_size = 500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, arrows=False)
    plt.show()

#%%

def part1(inputlist,m,r):
    G = nx.grid_2d_graph(m,m)
    rems = parselist(inputlist)
    for n in rems[0:r]:
        if n in G:
            G.remove_node(n)
    # drawgraph(G)
    # G.remove_node((1,0))
    # G.remove_node((0,1))
    return len(nx.shortest_path(G,(0,0),(m-1,m-1)))-1

#%%

def part2(inputlist,m):
    G = nx.grid_2d_graph(m,m)
    rems = parselist(inputlist)
    for n in rems:
        if n in G:
            G.remove_node(n)
            try:
                x = len(nx.shortest_path(G,(0,0),(m-1,m-1)))-1
            except:
                return n
#%%