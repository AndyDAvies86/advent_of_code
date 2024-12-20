
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

file = open("2020day21.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("2020day21test.txt","r")
startb = file.read()
testlist = startb.split("\n")

def cleanlist(inputlist):
    outlist = []
    for row in inputlist:
        temprow = row.replace(",","").replace(")","")
        splitrow = temprow.split(" (contains ")
        newrow = [x.split(" ") for x in splitrow]
        outlist.append(newrow)
    return outlist

def allergens(inputlist):
    allergy = set()
    for row in inputlist:
        allergy = allergy.union(set(row[1]))
    return allergy

def inglist(inputlist):
    ingredients = set()
    for row in inputlist:
        ingredients = ingredients.union(set(row[0]))
    return ingredients

def part1(inputlist):
    clean = cleanlist(inputlist)
    allergy = allergens(clean)
    ingredients = inglist(clean)
    solution = {}
    allbad = set()
    for allerg in allergy:
        solution[allerg] = ingredients
        for row in clean:
            if allerg in row[1]:
                solution[allerg] = solution[allerg].intersection(set(row[0]))
        allbad = allbad.union(solution[allerg])
    ingredients.difference_update(allbad)
    count = 0 
    for row in clean:
        count += len(ingredients.intersection(set(row[0]))        )
    return count

def remallergy(solset,allergen,ingredient):
    for row in solset.keys():
        if row != allergen:
            solset[row].discard(ingredient)
    return solset

def part2(inputlist):
    clean = cleanlist(inputlist)
    allergy = allergens(clean)
    ingredients = inglist(clean)
    solution = {}
    allbad = set()
    for allerg in allergy:
        solution[allerg] = ingredients
        for row in clean:
            if allerg in row[1]:
                solution[allerg] = solution[allerg].intersection(set(row[0]))
        allbad = allbad.union(solution[allerg])
    finalsol = {}
    i = 0
    while len(finalsol) < len(allergy):
        for row in allergy:
            if len(solution[row]) == 1:
                finalsol[row] = list(solution[row])[0]
                solution = remallergy(solution,row,list(solution[row])[0])
        print(i)
        i += 1
    badlist = ''
    allerlist = list(allergy)
    allerlist.sort()
    for aller in allerlist:
        badlist += finalsol[aller]+','
    return badlist[:-1]