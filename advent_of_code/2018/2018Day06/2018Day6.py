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
    
    for pos in coordlist:
        closest[(pos[0],pos[1])] = 0
    
    for i in range(listxmin-1,listxmax+2):
        for j in range(listymin-1,listymax+2):
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
        closest[(pos[0],pos[1])] = sum(value == (pos[0],pos[1]) for value in field.values())
#        postuple = (pos[0],pos[1])
#        closest[pos] = sum(value == postuple for value in field)
 #   for point in field:
#        pointpos = (point[0],point[1])        
#        closept = field[(point[0],point[1])]
#        closest[closept] += 1
    return closest

def removeedge(coordlist):
    listxmin,listxmax,listymin,listymax = findminmax(coordlist)
    remove = {}
    for x in range(listxmin-1,listxmax+2):
        for y in range(listymin-1,listymax+2):
            remove[(x,y)] = 0
    for x in range(listxmin-1,listxmax+2):
        remove[(x,listymin-1)]=1
        remove[(x,listymax+1)]=1
    for y in range(listymin-1,listymax+2):
        remove[(listxmin-1),y]=1
        remove[(listxmax+1),y]=1
    return remove
    
def maxsize(coordlist):
    listxmin,listxmax,listymin,listymax = findminmax(coordlist)
    closestfound = findclosest(coordlist)
    closest = countclosest(closestfound,coordlist)
    closearea = {}
    remove=removeedge(coordlist)
    removelist = {}
    for pos in coordlist:
        removelist[(pos[0],pos[1])] = 1
    for pos in closestfound:
        if remove[pos] == 1:
            removelist[closestfound[pos]] = 0
#    print(removelist)
    for pos in coordlist:
        closearea[(pos[0],pos[1])] = closest[(pos[0],pos[1])]*removelist[(pos[0],pos[1])]
    maxsize = max(closearea.values())
    return maxsize
    
print("Part 1: " + str(maxsize(testint)))


def saferegion(coordlist,maxdist):
    listxmin,listxmax,listymin,listymax = findminmax(coordlist)
    
    distance = {}
    for x in range(listxmin-1,listxmax+2):
        for y in range(listymin-1,listymax+2):
            distance[(x,y)] = 0
            for pos in coordlist:
                distance[(x,y)] = distance[(x,y)] + manhattan(pos,[x,y])
        
    safespace = sum(value < maxdist for value in distance.values())
    return safespace

print("Part 2: " +str(saferegion(startint,10000)))

