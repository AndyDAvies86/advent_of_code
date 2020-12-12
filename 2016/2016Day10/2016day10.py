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
import itertools as it
import copy


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()

file = open("2016day10.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("2016day10test.txt","r")
startb = file.read()
testlist = startb.split("\n")

def cleanlist(inputlist):
    bot = {}
    for row in inputlist:
        newrow = row.split(" ")
        if newrow[0] == 'bot':
            bot[int(newrow[1])] = [[newrow[5],int(newrow[6])],[newrow[-2],int(newrow[-1])]]
    return bot

def process(inputlist):
    botgo = cleanlist(inputlist)
    bots = len(botgo)
    botvals = [[] for x in range(0,bots)]
    botout = {}
    for row in inputlist:
        newrow = row.split(" ")
        if newrow[0] == 'value':
            print
            botvals[int(newrow[-1])].append(int(newrow[1]))
    while len(botout) < bots - 1:
        botlen = [len(x) for x in botvals]
        if max(botlen)<2:
            return botout
#        print(botlens)
#        print(botvals)
        thisbot = botlen.index(2)
#        print(botgo[thisbot],thisbot)
        send = [min(botvals[thisbot]),max(botvals[thisbot])]
#        if send == [17,61]:
#            return thisbot
        for i in range(0,2):
            if botgo[thisbot][i][0] == 'output':
                botout[botgo[thisbot][i][1]] = send[i]
            else:
                botvals[botgo[thisbot][i][1]].append(send[i])
        botvals[thisbot] =[]
#        print(botout)
        
    return botout
                
                
                
        
    
    
    

