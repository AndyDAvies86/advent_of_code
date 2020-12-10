# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:46:13 2020

@author: Andy
"""



import pandas as pd
import numpy as np
import re
import datetime as dt

file = open("2018day6.txt","r")
start = file.read()
startlist = start.split("\n")


file = open("2018day6test.txt","r")
startb = file.read()
testlist = startb.split("\n")

def coords(list):
    outint = [[int(x) for x in y.split(",")] for y in list]
    return outint

startint = coords(startlist)
testint = coords(testlist)


def findminmax(list):
    listxmin = list[0][0]
    listxmax = list[0][0]
    listymin = list[0][1]
    listymax = list[0][1]
    for pos in list:
        listxmin = min(listxmin, pos[0])
        listxmax = max(listxmax, pos[0])
        listymin = min(listymin, pos[1])
        listymax = max(listymax, pos[1])
    return listxmin, listxmax, listymin, listymax

testlistxmin, testlistxmax, testlistymin, testlistymax = findminmax(testint)

def manhattan(posa,posb):
    dist = abs(posa[0]-posb[0]) + abs(posa[1]-posb[1])
    return dist

def findclosest(coordlist):
    
    field = {}    
    closest ={}
    
    listxmin,listxmax,listymin,listymax = findminmax(coordlist)
    fullfield = np.zeros(listxmax-listxmin)
    
    for pos in coordlist:
        closest[(pos[0],pos[1])] = 0
    
    for i in range(listxmin-1,listxmax+1):
        for j in range(listymin-1,listymax+1):
            checkpos = {}
            for pos in coordlist:
                dist = manhattan([i,j],pos)
                checkpos[(pos[0],pos[1])] = dist
            closestpos = min(checkpos, key = checkpos.get)
            mindist  = checkpos[closestpos]
            if sum(value == mindist for value in checkpos.values()) == 1:
                field[(i,j)] = closestpos
                closest[(closestpos[0],closestpos[1])] += 1
    return field
 


def countclosest(field,coordlist):
    closest = {} 
    for pos in coordlist:
        postuple = (pos[0],pos[1])
        closest[pos] = sum(value == postuple for value in field)
#    for point in field:
#        pointpos = (point[0],point[1])        
#        closept = field[(point[0],point[1])]
#        closest[closept] += 1
    return closest
    
def maxsize(coordlist):
    listxmin,listxmax,listymin,listymax = findminmax(coordlist)
    closestfound = findclosest(coordlist)
    closest = countclosest(closestfound,coordlist)
    closestb = {}
    for pos in coordlist:
        if pos[0] in range(listxmin+1,listxmax) and pos[1] in range(listymin+1,listymax):
            closestb[(pos[0],pos[1])] = closest[(pos[0],pos[1])]
    maxsize = max(closestb.values())
    return maxsize
    
print(maxsize(testint))



        

