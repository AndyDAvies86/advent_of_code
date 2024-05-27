
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

def creat_dict(inputlist):
    midlist = inputlist.split("\n")[1:]
    newlist = [[int(x) for x in y.split(" ")] for y in midlist]
    # dict = {}
    # for row in newlist:
    #     # print(row)
    #     for ii in range(0,row[2]):
    #         dict[row[1]+ii] = row[0]+ii
    # return dict
    return newlist

def parse(inputlist):
    seeds = [int(x) for x in inputlist[0][7:].split(" ")]
    mappings = []
    for ii in range (1,8):
        mappings.append(creat_dict(inputlist[ii]))
    # mappings = [[int(x) for x in y.split(" ")] for y[1:] in inputlist[1:].split("\n")]
    return seeds,mappings

def map_dict(inputint,inputdict):
    for mapping in inputdict:
        if inputint in range(mapping[1],mapping[1]+mapping[2]):
            return inputint+mapping[0]-mapping[1]
    return inputint
    # if inputint in inputdict:
    #     return inputdict[inputint]
    # else:
    #     return inputint
    
def map_locations(seedlist,dictlist):
    loc_list=[]
    for seed in seedlist:
        # print(seed)
        loc = seed
        for dict in dictlist:
            loc = map_dict(loc,dict)
            # print(loc)
        loc_list.append(loc)
        # print(loc_list)
    return loc_list
            
def map_seed(seed,mappings):
    loc = seed
    # print(mappings)
    # print(loc)
    for mapping in mappings:
        # print(mapping)
        # print(loc)
        loc = map_dict(loc,mapping)
    return loc
#%%        
def find_inverse(target,mappings):
    for mapping in mappings:
        if target in range(mapping[0],mapping[0]+mapping[2]+1):
            additional = target-mapping[0]
            inverse = mapping[1]+additional
            return inverse
        
def find_inverse_range(target,max_target,mappings):
    for mapping in mappings:
        if target in range(mapping[0],mapping[0]+mapping[2]+1):
            additional = target-mapping[0]
            inverse = mapping[1]+additional
            new_max = mapping[1]+mapping[2]
            return inverse,new_max
    for mapping in mappings:
        if max_target in range(mapping[0],mapping[0]+mapping[2]+1):
            additional = mapping[0]+mapping[2]-max_target
            inverse = mapping[1]+additional
            new_max = mapping[1]+mapping[2]
            return inverse,new_max
#%%

def test_inverse(inputlist):
    seeds,map_list=parse(inputlist)
    target = 0
    max_target = 9999999999999999
    map_length = len(map_list)-1
    print(map_length)
    for ii in range(map_length,-1,-1):
        mappings = map_list[ii]
        print(mappings)
        print(find_inverse_range(target,max_target,mappings))
        # target,max_target=find_inverse_range(target,max_target,mappings)
        # print(target,max_target)

def top_bottom(min_seed,max_seed,mappings,top_min):
    mid_seed = int((min_seed+max_seed)/2)
    seeds = [min_seed,mid_seed,max_seed]
    locs = map_locations(seeds,mappings)
    min_index = locs.index(min(locs))
    # print(seeds,locs)
    if min_index == 0:
        return min_seed,mid_seed,0
    if min_index == 2:
        return mid_seed,max_seed,1
    if top_min == 1 and min_index == 1:
        return min_seed,mid_seed,1
    return mid_seed,max_seed,0


#%%

def part1(inputlist):
   seeds,mappings=parse(inputlist)
#    seed_num=len(seeds)
   loc_list = map_locations(seeds,mappings)
#    loc_list = map(map_seed,tuple(seeds),tuple([mappings]*seed_num))
#    print(list(loc_list))
   return min(loc_list)



def part2(inputlist):
    oldseeds,mappings=parse(inputlist)
    seeds = []
    for ii in range(0,len(oldseeds),2):
        # seeds=seeds+[x for x in range(oldseeds[ii],oldseeds[ii]+oldseeds[ii+1])]
        seeds.append(oldseeds[ii])
        seeds.append(oldseeds[ii]+oldseeds[ii+1]-1)
    # seed_num=len(seeds)
    # loc_list = map(map_seed,tuple(seeds),tuple([mappings]*seed_num))
    loc_list = map_locations(seeds,mappings)
    min_index = loc_list.index(min(loc_list))
    if min_index % 2 == 1:
        # seeds = [seeds[min_index-1],int((seeds[min_index-1]+seeds[min_index])/2),seeds[min_index]]
        # print(seeds[min_index-1:min_index+1],loc_list[min_index-1:min_index+1])
        min_seed = seeds[min_index-1]
        max_seed = seeds[min_index]
        top_min = 1
    else:
        # seeds = [seeds[min_index],int((seeds[min_index]+seeds[min_index+1])/2),seeds[min_index+1]]
        # print(seeds[min_index:min_index+2],loc_list[min_index:min_index+2])
        min_seed = seeds[min_index]
        max_seed = seeds[min_index+1]
        top_min=0
    while max_seed>min_seed+1:
        # print(min_seed,max_seed,top_min)
        min_seed,max_seed,top_min=top_bottom(min_seed,max_seed,mappings,top_min)
    # print(min_seed,max_seed,top_min)
    if top_min == 0:
        return map_locations([min_seed],mappings)[0]
    return map_locations([max_seed],mappings)[0]
    
    # return min(loc_list),loc_list.index(min(loc_list)),loc_list


#%%