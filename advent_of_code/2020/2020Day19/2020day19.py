
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

file = open("2020day19.txt","r")
start = file.read()
startlist = start.split("\n\n")

file = open("2020day19test2.txt","r")
startb = file.read()
testlist = startb.split("\n\n")

file = open("2020day19test.txt","r")
startc = file.read()
testlistb = startc.split("\n\n")

def twolists(inputlist):
    inrules = inputlist[0].split("\n")
    messages = inputlist[1].split("\n")
    rules = {}
    for row in inrules:
        row2 = row.split(":")
        ruleout = "( "+row2[1][1:]+" )"
        ruleout2 = ruleout.replace('"','').replace('(a)','a').replace('(b)','b')
        rules[row2[0]] = ruleout2.split(" ")
    return messages, rules

def resolverules(inrules):
    zerorule = inrules['0']
    while True:
        newzero = []
        for char in zerorule:
#            print(char)
            if char.isnumeric():
                newzero += inrules[char]
            else:
                newzero += char
        if newzero == zerorule:
            return newzero
        zerorule = copy.deepcopy(newzero)
#        print(len(zerorule))

def resolverules2(inrules):
    zerorule = inrules['0']
    while True:
        newzero = []
        for char in zerorule:
#            print(char)
            if char.isnumeric():
                newzero += inrules[char]
            else:
                newzero += char
        if newzero == zerorule:
            return newzero
        zerorule = copy.deepcopy(newzero)
#        print(len(zerorule))


def check(rule,messages):
    r = re.compile('^'+rule+'$', re.VERBOSE)
    checklist = [bool(r.match(m)) for m in messages]
    return checklist

def part1(inputlist):
    messages, rules = twolists(inputlist)
    valid = ''.join(resolverules(rules))
#    print(valid)
    checklist = check(valid,messages)
    return sum(checklist)

def part2(inputlist):
    messages, rules = twolists(inputlist)
    newrule11 = rules['11'][:-1]
    newrule8 = rules['8'][:-1]
    for i in range(2,10):
        newrule8 += ['|']
        newrule8 += ['42']*i
        newrule11 += ['|']
        newrule11 += ['42']*i
        newrule11 += ['31']*i
    newrule11 += [')']
    newrule8 += [')']
    print(newrule11)
    rules['11'] = newrule11
    rules['8'] = newrule8
    valid = ''.join(resolverules(rules))
#    print(valid)
    checklist = check(valid,messages)
    return sum(checklist)