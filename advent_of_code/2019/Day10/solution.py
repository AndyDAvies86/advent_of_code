#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
import json
from math import lcm,gcd

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

def parse(inputlist):
    asteroids = []
    for ii in range(0,len(inputlist)):
        for jj in range(0,len(inputlist[0])):
            # print(inputlist[ii][jj])
            if inputlist[ii][jj]=='#':
                # print(1)
                asteroids.append(np.array([ii,jj]))
    return asteroids

def checkast(rel,cansee):
    if np.dot(rel,rel) == 0:
        # print('zero')
        return cansee
    if len(cansee)==0:
        # print('first')
        return [list(rel)]
    for astb in cansee:
        ast = np.array(astb)
        if np.dot(rel,ast)**2==np.dot(rel,rel)*np.dot(ast,ast):
            if rel[0]*ast[0]<0:
                pass
            elif abs(rel[0])<abs(ast[0]):
                # print('swap',rel,ast,cansee)
                cansee.remove(list(ast))
                cansee.append(list(rel))
                return cansee
            else:
                # print('block')
                return cansee
    # print('add')
    cansee.append(list(rel))
    return cansee

#%%        

def part1(inputlist):
    asteroids = parse(inputlist)
    sight = 0
    best = asteroids[0]
    for asteroid in asteroids:
        cansee = []
        rel_list = [x-asteroid for x in asteroids if not np.array_equal(x,asteroid)]
        rel_dict = {}
        for rel in rel_list:
            r_gcd = gcd(rel[0],rel[1])
            a_unit = rel//r_gcd
            unit = tuple(a_unit)
            if unit in rel_dict.keys():
                rel_dict[unit] = min(rel_dict[unit],r_gcd)
            else:
                rel_dict[unit] =  r_gcd
        if len(rel_dict)>sight:
            sight = len(rel_dict)
            best = asteroid          
        # for check in asteroids:
        #     rel = check-asteroid
        #     cansee = checkast(rel,cansee)
            # print('ch',check,'a',asteroid,'r',rel,'c',cansee)
        # print('ast',asteroid,'s',len(cansee),'see',cansee)
        # if len(cansee) > sight:
        #     sight = len(cansee)
        #     best = asteroid
    # print(best)
    return sight,best
        

            



def part2(inputlist):
    station = part1(inputlist)[1]
    print(station)
    asteroids = parse(inputlist)
    rel_list = [x-station for x in asteroids if not np.array_equal(x,station)]
    rel_dict = {}
    for rel in rel_list:
        r_gcd = gcd(rel[0],rel[1])
        # a_unit = rel//r_gcd
        angle = np.arctan2(rel[1],rel[0])
        if angle in rel_dict.keys():
            rel_dict[angle].append(r_gcd)
        else:
            rel_dict[angle] =  [r_gcd]
    angles = list(rel_dict.keys())
    angles.sort(reverse=True)
    targets = [[x,sorted(rel_dict[x])] for x in angles]
    ord_tar = []
    ii = 0
    jj = 0
    a = 0
    while a == 0:
        # print(ii,jj,len(targets))
        if len(targets[ii][1])>jj:
            ord_tar.append([targets[ii][0],targets[ii][1][jj]])
        ii =(ii+1) % (len(targets)-1)
        if ii == 0:
            jj = jj+1
        if jj == max([len(x[1]) for x in targets]):
            a = 1
    ang = ord_tar[199]
    n_vec = np.array([np.sin(ang[0]),np.cos(ang[0])])
    return n_vec*(1/max(n_vec[0],n_vec[1])),ang[1]



#%%