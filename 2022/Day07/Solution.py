
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy

#%%
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()
#%%
file = open("inputfile.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n")


#%%
def createtree(inputlist):
    filesizes = {}
    hierarchy = {}
    depth = {'/':0}
    current = ['/']
    row = 1
    while row < len(inputlist):
        content = inputlist[row].split(" ")
        if content[0] == '$':
            if content [1] == 'cd':
                if content[2] == '/':
                    current = ['/']
                elif content[2] == '..':
                    current = current[:-1]
                else:
                    current.append(content[2])
        elif content[0] == 'dir':
            hierarchy['/'.join(current+[content[1]])] = '/'.join(current)
            depth['/'.join(current+[content[1]])] = len(current)
        else:
            filesizes['/'.join(current+[content[1]])] = int(content[0])
            hierarchy['/'.join(current+[content[1]])] = '/'.join(current)
            depth['/'.join(current+[content[1]])] = len(current)
        row += 1
    return filesizes,hierarchy,depth

#%%


#%%


#%%
def part1(inputlist):
    filesizes,hierarchy,depth = createtree(inputlist)
    maxdepth = max(depth.values())
    folders = list(set(list(hierarchy.values())))
    #print(folders)
    foldersize = {x:0 for x in folders}
    #print(foldersize['lfm'])
    for filedepth in range(maxdepth,0,-1):
        for file in depth:
            if depth[file] == filedepth:
                #print(file,depth[file])
                if file in folders:
                    foldersize[hierarchy[file]] += foldersize[file]
                else:
                    foldersize[hierarchy[file]] += filesizes[file]
    foldersizes = list(foldersize.values())
    return sum([x for x in foldersizes if x <= 100000])
#%%

def part2(inputlist):
    filesizes,hierarchy,depth = createtree(inputlist)
    maxdepth = max(depth.values())
    folders = list(set(list(hierarchy.values())))
    #print(folders)
    foldersize = {x:0 for x in folders}
    #print(foldersize['lfm'])
    for filedepth in range(maxdepth,0,-1):
        for file in depth:
            if depth[file] == filedepth:
                #print(file,depth[file])
                if file in folders:
                    foldersize[hierarchy[file]] += foldersize[file]
                else:
                    foldersize[hierarchy[file]] += filesizes[file]
    foldersizes = list(foldersize.values())
    maxsize = 70000000 - 30000000
    required = foldersize['/'] - maxsize
    print(required)
    abovemin = [x for x in foldersizes if x > required ]
    return min(abovemin)
#%%