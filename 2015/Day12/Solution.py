
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
startlist = start.split("\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n")

startc = '[1,{"c":"red","b":2},3]'
startd = '{"d":"red","e":[1,2,3,4],"f":5}'
starte = '[1,"red",5]'
startf = '[[[3]]]'
startg = '{"a":{"b":4},"c":-1}'
starth = '{"a":{"b":4},"c":-1}'
starti = '[-1,{"a":1}]'
#%%
def remove_non_num(inputstring):
    # outstring = re.sub("[^1-9,-]","",inputstring)
    midstring = re.sub("[\{\}\[\]\"a-z]","",inputstring)
    outstring = re.sub(":",",",midstring)
    return outstring

def string_to_int_list(inputstring):
    outlist = [int(x) for x in inputstring.split(",") if len(x) > 0]
    return outlist
#%%
def create_objarr(inputstring):
    # outstring = re.sub("({(.*)red(.*)?})","",inputstring)
    outstring = ''
    ii = 0
    objarray = ''
    next_oa = ''
    depth_list = []
    start_list = []
    depth=0
    start = 0
    for char in inputstring:
        if char == '[':
            next_oa += 'a'
            depth += 1
            start = ii
        if char == '{':
            next_oa += 'o'
            depth += 1
            start = ii
        objarray += next_oa[-1]
        depth_list.append(depth)
        start_list.append(start)
        if char in (']','}'):
            next_oa = next_oa[:-1]
            depth -= 1
    end_list = []
    end = len(inputstring)-1
    for jj in range(0,len(inputstring)):
        if depth_list[jj] > 1:
            end = depth_list.index(depth_list[jj]-1,jj)
        else:
            end = len(inputstring)-1
        end_list.append(end)
        
        
    return objarray,depth_list,start_list,end_list

def remove_red_object(inputstring):
    objarray,depth_list,start_list,endlist = create_objarr(inputstring)
    for ii in range(0,len(inputstring)-3):
        # print(inputstring[ii:ii+3],objarray[ii])
        if inputstring[ii:ii+3] == 'red' and objarray[ii] == 'a':
            inputstring = inputstring[:ii]+'blu'+inputstring[ii+3:]
            # print(inputstring)
    return inputstring

def remove_red(inputstring):
    # outstring = re.sub("({(.*)\:\"red\"(.*)})","",inputstring)
    objarray,depth_list,start_list,endlist = create_objarr(inputstring)
    ii = 0
    while ii < len(inputstring):
        pass

    return outstring
#%%

def part1(inputlist):
    num_string = remove_non_num(inputlist)
    intlist = string_to_int_list(num_string)    
    return sum(intlist)


   
# %%

def part2(inputlist):
    midstring = remove_red_object(inputlist)
    nextstring = remove_red(midstring)
    total = part1(nextstring)
    return total
# %%


def hook(obj):
  if "red" in obj.values(): return {}
  else: return obj
stuff = str(json.loads(start, object_hook=hook))
print("Sum of all numbers 2:", sum(map(int, re.findall("-?[0-9]+", stuff))))

#%%