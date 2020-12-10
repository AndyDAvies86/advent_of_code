# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:46:13 2020

@author: Andy
"""



import pandas as pd
import numpy as np
import re
import datetime as dt

file = open("2018day5.txt","r")
start = file.read()
startlist = start.split("\n")

i=0

teststring = start
while i < len(teststring)-1:
    #print(str(i) + " " + teststring)
    if teststring[i] == teststring[i+1].swapcase():
        teststring = teststring[:i]+teststring[i+2:]
        if i > 0 :
            i = i-1
    else:
        i += 1

print(len(teststring))
    
        
    
