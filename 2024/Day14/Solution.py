
#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy
from PIL import Image
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
    robots = []
    for row in inputlist:
        sp = [x[2:] for x in row.split(' ')]
        robot = [[int(x) for x in y.split(',')] for y in sp]
        robots.append(robot)
    return robots
#%%

def part1(inputlist,t,x,y):
    ends = []
    robots = parselist(inputlist)
    x_check = x//2
    y_check = y//2
    for robot in robots:
        p = robot[0]
        v = robot[1]
        end = [(p[0]+t*v[0]) % x, (p[1]+t*v[1]) % y]
        ends.append(end)
    # print([r[0] for r in robots])
    # print([r[1] for r in robots])
    # print (x_check,y_check)
    # print(ends)
    a=sum([e[0] < x_check and e[1] < y_check for e in ends])
    b=sum([e[0] > x_check and e[1] < y_check for e in ends])
    c=sum([e[0] < x_check and e[1] > y_check for e in ends])
    d=sum([e[0] > x_check and e[1] > y_check for e in ends])
    # print(a,b,c,d)
    return a*b*c*d
#%%

def part2(inputlist,t0,t1):
    x=101
    y = 103
    ends = []
    robots = parselist(inputlist)
    t=t0
    pos = [r[0] for r in robots]
    vel = [r[1] for r in robots]
    while t < t1:
        if True:
            # print(t)
            new_pos = [[(pos[kk][0]+t*vel[kk][0])%x,(pos[kk][1]+t*vel[kk][1])%y] for kk in range(0,len(pos))]
            a = ''
            img = Image.new('RGB', (x,y), "black")
            pix = img.load()
            for p in new_pos:
                pix[p[0],p[1]] = (255,255,255)
            # plt.imshow(img)
            # plt.show()
            filename = str(t).zfill(5)+'.png'
            img.save(filename)
            # for ii in range(0,x):
            #     for jj in range(0,y):
            #         if [ii,jj] in new_pos:
            #             a = a+'#'
            #         else:
            #             a= a+' '
            #     a = a + '\n'
            # print(a)
        t = t+1


def p2search(inputlist):
    x=101
    y = 103
    robots = parselist(inputlist)
    t = 0
    xy_range = []
    pos = [r[0] for r in robots]
    vel = [r[1] for r in robots]   
    xrangemin = 9999999999
    yrangemin = 9999999999
    txmin = 9999999999
    tymin = 9999999999
    for t in range(0,10403):
        new_pos = set(([tuple([(pos[kk][0]+t*vel[kk][1])%x,(pos[kk][1]+t*vel[kk][0])%y]) for kk in range(0,len(pos))]))
        x_var = np.var([p[0] for p in new_pos])
        y_var = np.var([p[1] for p in new_pos])
        # xmin=min([p[0] for p in new_pos])
        # xmax=max([p[0] for p in new_pos])
        # ymin=min([p[1] for p in new_pos])
        # ymax=max([p[1] for p in new_pos])
        # spread = (ymax-ymin)*(xmax-xmin)
        spread = x_var*y_var
        if t%1000 == 0:
            print(t)
        if x_var < xrangemin:
            print('x',t,txmin,yrangemin,x_var,y_var,spread)
            xrangemin = x_var
            txmin = t
        if y_var < yrangemin:
            print('y',t,tymin,yrangemin,x_var,y_var,spread)
            yrangemin = y_var
            tymin = t
    return txmin,tymin


#%%