
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
startlist = start.split("\n\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n\n")

file = open("inputtestsm.txt","r")
startc = file.read()
testsmlist = startc.split("\n\n")


#%%

def parselist(inputlist):
    inst = inputlist[1].replace('\n','')
    b_def = inputlist[0].split('\n')
    # board = [[y for y in x] for x in inputlist[0].split('\n')]
    # pieces = {'#':9,'@':5,'O':1,'.':0}
    # board = np.array([[pieces[x] for x in y] for y in inputlist[0].split('\n')])
    walls = [(jj,ii) for ii in range(0,len(b_def)) for jj in range(0,len(b_def[0])) if b_def[ii][jj]=='#']
    boxes = [(jj,ii) for ii in range(0,len(b_def)) for jj in range(0,len(b_def[0])) if b_def[ii][jj]=='O']
    robot = [(jj,ii) for ii in range(0,len(b_def)) for jj in range(0,len(b_def[0])) if b_def[ii][jj]=='@'][0]
    return inst,walls,boxes,robot,b_def
#%%

def drawgraph(G):
    pos = {(x,y):(x,-y) for x,y in G.nodes()}
    # colour = ['#EEEE00' if labels[node]==1 else '#999999' for node in G]
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                        # node_color=colour,
                        node_size = 500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, arrows=False)
    plt.show()

def move(board,robot,d):
    points = {'<':[0,-1],'>':[0,1],'^':[-1,0],'V':[1,0]}
    shove = points[d]
    l = 0
    # while  



def part1(inputlist):
    inst,walls,boxes,robot,board = parselist(inputlist)
    h = len(board)
    w = len(board)
    G = nx.grid_2d_graph(w,h)
    G.remove_nodes_from(walls)
    drawgraph(G)

    
#%%

def part2(inputlist):
    pass
#%%