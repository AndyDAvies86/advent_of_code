# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:46:13 2020

@author: Andy
"""



import pandas as pd
import numpy as np
import re

file = open("2018day1.txt","r")
start = file.read()
startlist = start.split("\n")

pos = 0
for move in startlist:
    exec('pos = pos ' + move)
    
print (pos)