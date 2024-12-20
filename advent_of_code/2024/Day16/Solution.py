
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

def drawgraph(G):
    d = {'N':(0,0.25),'E':(0.25,0),'S':(0,-0.25),'W':(-0.25,0),'':(0,0)}
    pos = {(x[0],x[1],x[2]):(x[0]+d[x[2]][0],-x[1]-d[x[2]][1]) for x in G.nodes()}
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                        node_size = 200)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, arrows=False)
    plt.show()  

#%%
def part1(inputlist):
    h = len(inputlist)
    w = len(inputlist[0])
    d = 'NESWN'
    walls,s,e = parselist(inputlist)
    G = nx.DiGraph()
    node_list = [(x,y,z) for x in range(0,w) for y in range(0,h) for z in ('N','E','S','W')]
    G.add_nodes_from([(x,y,z) for x in range(0,w) for y in range(0,h) for z in ('N','E','S','W')])
    cturn_list = [((x[0],x[1],d[z]),(x[0],x[1],d[z+1])) for x in node_list for z in range(0,4)]
    aturn_list = [((x[0],x[1],d[z+1]),(x[0],x[1],d[z])) for x in node_list for z in range(0,4)]
    nedge_list = [((x,y,'N'),(x,y+1,'N')) for x in range(0,w) for y in range(0,h-1)]
    eedge_list = [((x,y,'E'),(x+1,y,'E')) for x in range(0,w-1) for y in range(0,h)]
    sedge_list = [((x,y+1,'S'),(x,y,'S')) for x in range(0,w) for y in range(0,h-1)]
    wedge_list = [((x+1,y,'W'),(x,y,'W')) for x in range(0,w-1) for y in range(0,h)]
    G.add_edges_from(nedge_list,weight = 1)
    G.add_edges_from(eedge_list,weight = 1)
    G.add_edges_from(sedge_list,weight = 1)
    G.add_edges_from(wedge_list,weight = 1)
    G.add_edges_from(cturn_list,weight=1000)
    G.add_edges_from(aturn_list,weight=1000)
    enew = (e[0],e[1],'')
    G.add_node(enew)
    end_edges = [((e[0],e[1],x),enew) for x in ('N','E','S','W')]
    G.add_edges_from(end_edges,weight=0)
    dwalls = [(x[0],x[1],y) for x in walls for y in d[:4]]
    G.remove_nodes_from(dwalls)
    # drawgraph(G)
    sp = nx.shortest_path(G,(s[0],s[1],'E'),enew,'weight')
    # print(len(sp))
    # for step in sp:
        # print(step)
    return sum([G[sp[x]][sp[x+1]]['weight'] for x in range(0,len(sp)-1)])
    # return sum([G[(sp[ii],sp[ii+1])]['weight'] for ii in range(0,len(sp-1))])
    # print(len(list(paths)))
    # return paths
#%%

def part2(inputlist):
    h = len(inputlist)
    w = len(inputlist[0])
    d = 'NESWN'
    walls,s,e = parselist(inputlist)
    G = nx.DiGraph()
    node_list = [(x,y,z) for x in range(0,w) for y in range(0,h) for z in ('N','E','S','W')]
    G.add_nodes_from([(x,y,z) for x in range(0,w) for y in range(0,h) for z in ('N','E','S','W')])
    cturn_list = [((x[0],x[1],d[z]),(x[0],x[1],d[z+1])) for x in node_list for z in range(0,4)]
    aturn_list = [((x[0],x[1],d[z+1]),(x[0],x[1],d[z])) for x in node_list for z in range(0,4)]
    nedge_list = [((x,y,'N'),(x,y+1,'N')) for x in range(0,w) for y in range(0,h-1)]
    eedge_list = [((x,y,'E'),(x+1,y,'E')) for x in range(0,w-1) for y in range(0,h)]
    sedge_list = [((x,y+1,'S'),(x,y,'S')) for x in range(0,w) for y in range(0,h-1)]
    wedge_list = [((x+1,y,'W'),(x,y,'W')) for x in range(0,w-1) for y in range(0,h)]
    G.add_edges_from(nedge_list,weight = 1)
    G.add_edges_from(eedge_list,weight = 1)
    G.add_edges_from(sedge_list,weight = 1)
    G.add_edges_from(wedge_list,weight = 1)
    G.add_edges_from(cturn_list,weight=1000)
    G.add_edges_from(aturn_list,weight=1000)
    enew = (e[0],e[1],'')
    G.add_node(enew)
    end_edges = [((e[0],e[1],x),enew) for x in ('N','E','S','W')]
    G.add_edges_from(end_edges,weight=0)
    dwalls = [(x[0],x[1],y) for x in walls for y in d[:4]]
    G.remove_nodes_from(dwalls)
    paths = nx.all_shortest_paths(G,(s[0],s[1],'E'),enew,'weight')
    # print(paths)
    spots = set()
    for path in paths:
        spots = spots.union(set([(x[0],x[1]) for x in path]))
        # print(spots)
    return len(spots)
#%%