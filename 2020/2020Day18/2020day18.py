
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()
numbers = '1234567890'

file = open("2020day18.txt","r")
start = file.read()
startlist = start.split("\n")

#file = open("2020day17test.txt","r")
#startb = file.read()
#testlist = startb.split("\n")

#file = open("2020day16test2.txt","r")
#startc = file.read()
#testlist = startb.split("\n")
#

def sumcalc(inputlist):
    count = [0]
    newsum = ''
    for i in range(len(inputlist)-1,0,-1):
        if inputlist[i] == " " and inputlist[i-1] not in ('+','*'):
            newsum += ')'
            count[0] += 1
        elif inputlist[i] == ")":
            newsum += inputlist[i]
            count = [0]+count
        elif inputlist[i] == "(":
            newsum += inputlist[i]
            newsum += "("*count[0]
            count = count[1:]
        else:
            newsum += inputlist[i]
    newsum += inputlist[0]
    while len(count) > 0:
        newsum += "("*count[0]
        count = count[1:]
    return eval(newsum[::-1])


def part1(inputlist):
    out = 0
    for row in inputlist:
        out += sumcalc(row)
    return out

def calcplus(sumlist):
    i = 0
    while i < len(sumlist):
#        print(sumlist)
        if sumlist[i] == "+":
            if sumlist[i-1].isnumeric() and sumlist[i+1].isnumeric():
                sumlist = sumlist[:i-1]+[str(int(sumlist[i-1])+int(sumlist[i+1]))]+sumlist[i+2:]
            else:
                i += 1
        else:
            i += 1
#        print(i)
    return sumlist

def calcbracket(inputlist):
    depth = [1]
    for i in range(1,len(inputlist)):
        if inputlist[i] == "(":
            depth.append(depth[-1]+1)
        elif inputlist[i] == ")":
            depth.append(depth[-1]-1)
        else:
            depth.append(depth[-1])
#    print(inputlist)
#    print(depth)
    start = depth.index(max(depth))
    end = depth.index(max(depth)-1,start)
#    print(inputlist[start+1:end])
    newsumlist = calcplus(inputlist[start+1:end])
#    print(newsumlist)
    out = eval(''.join(newsumlist))
    return inputlist[:start]+[str(out)]+inputlist[end+1:]

def tolist(inputlist):
    sumlist = ["("]+list(inputlist.replace(" ",""))+[")"]
    return sumlist

def part2(inputlist):
    sums = []
    outsum = 0
    for row in inputlist:
        sumlist = tolist(row)
        i = 0
#        while i < 4:
        while sumlist.count("(") > 0:
            sumlist = calcplus(sumlist)
            sumlist = calcbracket(sumlist)
            sumlist = calcplus(sumlist)
#            print(i,sumlist)
            i+=1
        
        outsum += eval(''.join(sumlist))
        
    return outsum
        

#def sumcalc2(inputlist):
#    inputlist = ' '*3+inputlist+' '*3
#    depth = [0]
#    for i in range(1,len(inputlist)):
#        if inputlist[i] == "(":
#            depth.append(depth[-1]+1)
#        if inputlist[i] == ")":
#            depth.append(depth[-1]-1)
#        else:
#            depth.append(depth[-1])
#    count = [0]
#    newsum = copy.deepcopy(inputlist)
#    for i in range(0,len(inputlist)):
#        if inputlist[i] == "+":
#            if inputlist[i-2] in numbers:
#                newsum = newsum[:i-3]+"("+newsum[i-2:]
#            else:
#                start = i-3 - depth[i-3::-1].index(depth[i])
#                newsum = newsum[:start]+"("+newsum[start+1:]
#            print(newsum)
#            if inputlist[i+2] in numbers:
#                newsum = newsum[:i+3]+")"+newsum[i+4:]
#            else:
#                start = i+3 + depth[i+3:].index(depth[i])
#                newsum = newsum[:start]+")"+newsum[start+1:]
#            print(newsum)
#    return newsum