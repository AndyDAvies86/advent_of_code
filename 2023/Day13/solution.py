
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import json

#%%
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()
#%%
file = open("inputfile.txt","r")
start = file.read()
startlist = start.split("\n\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n\n")

#%%

def parse(inputlist):
    grids = []
    for grid in inputlist:
       rc = []
       n_grid = grid.split("\n")
       rc.append(n_grid)
       rc.append([''.join([n_grid[x][y] for x in range(0,len(n_grid))]) for y in range(0,len(n_grid[0]))])
       grids.append(rc)
    return grids

def findsplits(inputgrid):
    mirrors = []
    for ii in range(1,len(inputgrid)):
        start = max(0,2*ii-len(inputgrid))
        end = min(2*ii,len(inputgrid))
        # print(ii,start,end,inputgrid[start:ii],inputgrid[end-1:ii-1:-1])
        if inputgrid[start:ii] == inputgrid[end-1:ii-1:-1]:
            mirrors.append(ii)
    return mirrors

def smudge(old_grid,rows,cols):
    # print(len(old_grid),len(old_grid[0]),len(old_grid[0][0]))
    # print(len(old_grid),len(old_grid[1]),len(old_grid[1][0]))
    # print(old_grid[0])
    for ii in range(0,len(old_grid[0])):
            for jj in range(0,len(old_grid[0][0])):
                grid=copy.deepcopy(old_grid)
                if grid[0][ii][jj]=='.':
                    grid[0][ii] = grid[0][ii][:jj]+'#'+grid[0][ii][jj+1:]
                    grid[1][jj] = grid[1][jj][:ii]+'#'+grid[1][jj][ii+1:]
                    # grid[0][ii][jj]='#'
                    # grid[1][jj][ii]='#'
                else:
                    grid[0][ii] = grid[0][ii][:jj]+'.'+grid[0][ii][jj+1:]
                    grid[1][jj] = grid[1][jj][:ii]+'.'+grid[1][jj][ii+1:]
                    # grid[0][ii][jj]='.'
                    # grid[1][jj][ii]='.'
                # if ii==0 and jj == 5:
                #     print(grid[1])
                new_rows = findsplits(grid[0])
                new_cols = findsplits(grid[1])
                # print(ii,jj,new_rows,new_cols,rows,cols,grid[0][ii][jj])
                row_check = set(new_rows).difference(set(rows))
                col_check = set(new_cols).difference(set(cols))
                if len(row_check)==1:
                    return [list(row_check)[0],0]
                if len(col_check)==1:
                    return [0,list(col_check)[0]]
                


#%%        

def part1(inputlist):
    row_scores=[]
    col_scores=[]
    for grid in parse(inputlist):
        row_scores = row_scores+findsplits(grid[0])
        col_scores = col_scores+findsplits(grid[1])
    return sum(col_scores)+100*sum(row_scores)



def part2(inputlist):
    row_scores=[]
    col_scores=[]
    for grid in parse(inputlist):
        rows=findsplits(grid[0])
        cols=findsplits(grid[1])
        diffs=smudge(grid,rows,cols)
        # print(diffs)
        row_scores.append(diffs[0])
        col_scores.append(diffs[1])
    return sum(row_scores)*100+sum(col_scores)
        



#%%