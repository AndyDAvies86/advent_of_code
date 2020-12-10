# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:46:13 2020

@author: Andy
"""



import pandas as pd
import numpy as np
import re

file = open("2020day5.txt","r")
start = file.read()
startlist = start.split("\n")

seatnumber =[]

for seat in startlist:    
    seat = seat.replace("F","0")
    seat = seat.replace("B","1")
    seat = seat.replace("L","0")
    seat = seat.replace("R","1")
    seatnumber.append(int(seat, 2))
    
print("Part 1: " + str(max(seatnumber)))

for i in range(min(seatnumber),max(seatnumber)+1):
    if i not in seatnumber:
        print("Part 2: " + str(i))