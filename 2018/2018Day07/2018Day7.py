# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:46:13 2020

@author: Andy
"""



import pandas as pd
import numpy as np
import re
import datetime as dt

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2018day7.txt","r")
start = file.read()
startlist = start.split("\n")


file = open("2018day7test.txt","r")
startb = file.read()
testlist = startb.split("\n")


def dependencies(inlist):
    deplist = []
    for row in inlist:
        splitlist = row.split(" ")
        deplist.append([splitlist[1],splitlist[7]])
    return deplist

testdep = dependencies(testlist)

def allsteps(inlist):
    steps = ''
    for row in inlist:
        if row[0] not in steps:
            steps = steps + row[0]
        if row[1] not in steps:
            steps = steps + row[1]
    sortedsteps = ''.join(sorted(steps))
    return sortedsteps

def stepthrough(inlist):
    steps = allsteps(inlist)
    for char in steps:
        stop = 0
        for dep in inlist:
            if dep[1] == char:
                stop = 1
                break
        if stop == 0:
            nextstep = char
            return nextstep

def removedeps(inlist,done):
    outlist = []
    for row in inlist:
        if row[0] != done:
            outlist.append(row)
    return outlist

def iterthrough(inlist):
    steporder = ''
    deplistin = dependencies(inlist)
    deplist = deplistin
    while len(deplist) > 1:
        chardone = stepthrough(deplist)
        steporder = steporder + chardone
        deplist = removedeps(deplist,chardone)
    steporder = steporder + deplist[0][0] + deplist[0][1]
    return steporder

#print(iterthrough(testlist))
#print(iterthrough(startlist))

def workertimes(inlist,penalty):
    allthesteps = allsteps(inlist)
    times = {}
    for letter in allthesteps:
        times[letter] = ord(letter.lower())-96+penalty
    return times
    
def canido(inlist,char):
    allthesteps = allsteps(inlist)
    for row in inlist:
        if row[1] == char:
            if row[0] in allthesteps:
                return 0;
    return 1;

def workersfree(workerstatus):
    free = []
    for i in range (0,len(workerstatus)):
        if workerstatus[i][1] == 0:
            free.append(i)
    return free

def stepthroughb(inlist,steps):
    
    for char in steps:
        stop = 0
        for dep in inlist:
            if dep[1] == char:
                stop = 1
                break
        if stop == 0:
            nextstep = char
            return nextstep 
 
def doall(inlist,workers,penalty):
    print("a")
    deplistin = dependencies(inlist)
    times = workertimes(deplistin,penalty)
    allstepsin = allsteps(deplistin)
    workerstatus = []
    for i in range(0,workers):
        workerstatus.append(['',0])
    print("a")
    stepsremaining = allstepsin
    completed = ''
    deplistrem = deplistin
    time = 0
    while len(completed) < len(allstepsin):
        freeworkers = workersfree(workerstatus) 
        for i in freeworkers:
            workerstatus[i][0] = ''
            nextstep = stepthroughb(deplistrem,stepsremaining)
            if nextstep != None:
                workerstatus[i][0] = nextstep
                workerstatus[i][1] = times[nextstep]
                stepsremaining = stepsremaining.replace(nextstep,"")
       
        tasks = []
        for worker in workerstatus:
            if worker[1] == 1:
                worker[1] = 0
                completed = completed + worker[0]
                deplistrem = removedeps(deplistrem,worker[0])
                                
            else:
                worker[1] = max(0,worker[1]-1)
            tasks.append(worker[0])
        print(str(time) + " " + str(tasks))
        time += 1   
    return time





    
    

        
