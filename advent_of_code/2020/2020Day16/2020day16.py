
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2020day16.txt","r")
start = file.read()
#startlist = start.split("\n")

file = open("2020day16test.txt","r")
startb = file.read()
#testlist = startb.split("\n")

file = open("2020day16test2.txt","r")
startc = file.read()
#testlist = startb.split("\n")

def separatelists(inputlist):
    lists = inputlist.split("\n\n")
#    print(lists)
    yourticketlist = lists[1].split("\n")[1]
    yourticketstr = yourticketlist.split(",") 
    yourticket = [int(x) for x in yourticketstr]
#    print(yourticket)
    nearticketlist = lists[2].split("\n")[1:]
    nearticketstr = [x.split(",") for x in nearticketlist]
    neartickets = []
    for row in nearticketstr:
        neartickets.append([int(x) for x in row])
#    print(neartickets)
    ranges = []
    rangelist = lists[0].split("\n")
    for row in rangelist:
        colon = row.index(":")
        newrow = [row[0:colon]]+row[colon+2:].split(" ")
#        print(newrow)
        temprow = [int(x) for x in newrow[1].split("-")+newrow[3].split("-")]
#        print(temprow)
        finalrow = [newrow[0]]+temprow
        ranges.append(finalrow)
    return yourticket, neartickets, ranges

def fieldranges(ranges):
    fullset = set()
    separateranges = []
    for row in ranges:
        rowrange = set(range(row[1],row[2]+1)).union(set(range(row[3],row[4]+1)))
        separateranges.append(rowrange)
        fullset = fullset.union(rowrange)
    return fullset, separateranges

def part1(inputlist):
    yourticket, neartickets, ranges = separatelists(inputlist)
    fullset, separateranges = fieldranges(ranges)
    count = 0
    for ticket in neartickets:
        for field in ticket:
            if field not in fullset:
                count += field
    return count

def potentialmaps(yourticket,valid,separateranges):
    potentials = [set(range(0,len(yourticket))) for x in yourticket]
    print(potentials)
    for ticket in valid:
        for i in range(0,len(ticket)):
            check = set()
            for j in  range(0,len(ticket)):
                if ticket[i] in separateranges[j]:
                    check.add(j)
            potentials[i] = potentials[i].intersection(check)
    return potentials
    

def part2(inputlist):
    yourticket, neartickets, ranges = separatelists(inputlist)
    fullset, separateranges = fieldranges(ranges)
    valid = []
    for ticket in neartickets:
        out = True
        for field in ticket:
            if field not in fullset:
                out = False
        if out == True:
            valid.append(ticket)
#    print(valid)
#    fields = [[x] for x in yourticket]
#    print(fields)
#    print(separateranges)
    potentials = potentialmaps(yourticket,valid,separateranges)
    fieldlist = {}
#    return potentials
    for jj in range(0,len(yourticket)):
#        print("jj"+str(jj))
        potlen = [len(x) for x in potentials]
        nextfield = potlen.index(1)
        ticketfield = list(potentials[nextfield])[0]
        fieldlist[ticketfield] = nextfield
        for pot in potentials:
            pot.discard(ticketfield)
    # feldlist is row on ticket to row in ranges
    departurerows = []
    for i in range(0,len(ranges)):
        if ranges[i][0][0:9] == 'departure':
            departurerows.append(i)
    mult = 1
    for row in departurerows:
        field = fieldlist[row]
        print(field)
        print(yourticket[field])
        mult = mult*yourticket[field]
    return mult
    
    
    
    