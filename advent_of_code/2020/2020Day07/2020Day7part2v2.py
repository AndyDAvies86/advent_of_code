# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:46:13 2020

@author: Andy
"""



import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import anytree
import networkx

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2020day7.txt","r")
start = file.read()
startlist = start.split("\n")


file = open("2020day7test.txt","r")
startb = file.read()
testlist = startb.split("\n")


file = open("2020day7test2.txt","r")
startc = file.read()
test2list = startc.split("\n")


def splitinput(inputlist):
    splitlist = []
    for row in inputlist:
        row = row.replace(" bags"," bag").replace(" bag.","").replace(" contain","").replace(" other","").replace(",","").replace(" no","")
#        print(row)
        splitrow = row.split(" bag ")
        if len(splitrow) == 1:
            splitrow[0]=splitrow[0].replace(" bag","")
        splitlist.append(splitrow)
    return splitlist


def fullbaglist(inputlist):
    allbagsposs = []
    for row in inputlist:
        allbagsposs.append(row[0])
    return allbagsposs

def createdependency(inputlist):
    dependency = {}
    for row in inputlist:
        if len(row) > 1:
            i = 1
            while i < len(row):
                splitrow = row[i].split(" ")
#                print(splitrow) 
                name = [str(row[0]),str(splitrow[1]) + " " + str(splitrow[2])]
                dependency[str(name)] = splitrow[0]
                i += 1

    return dependency

def graphbuild(inputlist):
    graph = {}
    for row in inputlist:
        if len(row) > 1:
            deps = []
            for i in range(1,len(row)):
                splitrow = row[i].split(" ")
                deps.append(str(splitrow[1] + " " + splitrow[2]))
            graph[row[0]] = deps
        else:
            graph[row[0]] = []
    return graph

def graphbuild2(inputlist):
    graph = {}
    for row in inputlist:
        pass

def reversegraph(inputgraph):
    graph = {}
    for row in inputgraph:
        graph[row] = []
        for dep in inputgraph[row]:
            graph[dep] = []
    for row in inputgraph:
        newlist = inputgraph[row]
        for dep in newlist:
            templist = graph[dep]
#            print(templist)
            templist.append(row)
            graph[dep]=templist
    return graph


def findpath(inputgraph,startbag):
    currentbag = startbag
    path = [startbag]
    while len(inputgraph[currentbag]) > 0:
        nextstep = inputgraph[currentbag][0]
        path.append(nextstep)
        currentbag = nextstep
#        print(path)
    return path

def removepath(inputgraph,path):
    tempdep = inputgraph[path[-2]]
    tempdep.remove(path[-1])
    inputgraph[path[-2]] = tempdep
    return inputgraph
    
        
def findallpaths(inputgraph,startbag):
    nowgraph = inputgraph
    allpaths = []
    allbags = set([])
    
    path = findpath(nowgraph,startbag)
    allpaths.append(path)
    while len(path) > 1:
        for bag in path:
            allbags.add(bag)
        nowgraph = removepath(nowgraph,path)
        path = findpath(nowgraph,startbag)       
        allpaths.append(path)
    allbags.remove(startbag)   
    countbags = len(allbags)
    return countbags,allpaths

    
def solvepart1(unsplit,startbag):
    inputlistb = splitinput(unsplit)
    ingraph = graphbuild(inputlistb)
    revgraph = reversegraph(ingraph)
    bagtypes,allpaths = findallpaths(revgraph,startbag)
    return bagtypes,allpaths

def addbags(allbags,nowbags)  :
    for bag in nowbags:
        allbags[bag] += nowbags[bag]
    return allbags

def openbags(nowbags,inputgraph,deplist):
    nextbags =  dict.fromkeys(nowbags,0)
    for bag in nowbags:
        for bag2 in inputgraph[bag]:
            nextbags[bag2] += int(deplist[str([bag,bag2])])*nowbags[bag]
    return nextbags
        
def solvepart2(unsplit,startbag):
    inputlistc = splitinput(unsplit)
    ingraph = graphbuild(inputlistc)
    deplist = createdependency(inputlistc)
    allbagslist = fullbaglist(inputlistc)
    allbags = dict.fromkeys(allbagslist,0)
    nowbags = dict.fromkeys(allbagslist,0)
#    nextbags =  dict.fromkeys(allbagslist,0)
    
    nowbags[startbag] = 1
    for i in range(0,10):
        nowbags=openbags(nowbags,ingraph,deplist)
        allbags = addbags(allbags,nowbags)
        
#        print(sum(nowbags.values()))
#    print (ingraph['shiny gold'])
#    deplist = createdependency(inputlistc)
#    bagtypes,allpaths = findallpaths(ingraph,startbag)
#    countall = 0
#    allbags = {}
#    nowbags = {}
#    nowbags[startbag] = 1
#    nextbags = {}
#    i = 0
#    while sum(nowbags.values()) > 0:
##        print(i)
##        print(nowbags)
#        nextbags = dict.fromkeys(nextbags,0) 
#        for bag in nowbags:
#            if bag not in allbags:
#                allbags[bag] = int(nowbags[bag])
#            else:
#                allbags[bag] += int(nowbags[bag])
##            print(allbags)
##            print(bag)
##            print(graphbuild(inputlistc)[str(bag)])
#            for nexbag in graphbuild(inputlistc)[bag]:
#                print(nexbag)
#                if nexbag not in nextbags:
#                    nextbags[nexbag] = int(deplist[str([bag,nexbag])])*nowbags[bag]
#                else:
#                    nextbags[nexbag] += int(deplist[str([bag,nexbag])])*nowbags[bag]
##        print(nextbags)
#        nowbags = dict.fromkeys(nowbags,0)
#        for bag in nextbags:
#            if bag not in nowbags:
#                nowbags[bag] = nextbags[bag]
#            else:
#                nowbags[bag] += nextbags[bag]
#        i += 1
##        print(nowbags)

    allbagstotal = sum(allbags.values())
    return allbagstotal
            
            
            
            
    newbag = []
    for bag in baglist:
        newbag = newbag + ingraph[bag]
    pathdedupe = []
    for path in pathdedupe:        
        countthis = 1
        for i in range(0,len(path)-1):            
            name = str([path[i],path[i+1]])
            countthis = countthis * int(deplist[name])
            countall = countall + countthis

    return pathdedupe,countall    


#split_test = splitinput(testlist)
#testdep = createdependency(split_test)
#test_graph = graphbuild(split_test)
#test_rev = reversegraph(test_graph)
#test_path = findpath(test_rev,'shiny gold')
#count,allpaths1 = findallpaths(test_rev,'shiny gold')
#print(count)
#
split_start = splitinput(startlist)
startdep = createdependency(split_start)
start_graph = graphbuild(splitinput(startlist))
#splitpathcount,splitpath = findallpaths(start_graphb,'shiny gold')


#
#allpaths2,countall = solvepart2(testlist,'shiny gold')
#allpaths3,countall2 = solvepart2(test2list,'shiny gold')

part1,notpart1 = solvepart1(startlist,'shiny gold')
part2 = solvepart2(startlist,'shiny gold')

#tpart1,tnotpart1 = solvepart1(testlist,'shiny gold')
#tpart2 = solvepart2(testlist,'shiny gold')

print("Part 1 :" + str(part1))
print("Part 2 :" + str(part2))


    