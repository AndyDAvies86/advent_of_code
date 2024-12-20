# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:49:48 2020

@author: Andy
"""

import pandas as pd
import numpy as np

inputfile = pd.read_csv("2020day2.csv",header=None)

start=np.array(inputfile)

countpass = 0
for i in range(0,1000):
    countletters = 0
    for j in range(0,len(start[i,3])):
        if start[i,3][j] == start [i,2]:
            countletters = countletters + 1
    if start[i,0]  <= countletters <= start[i,1]:
        countpass = countpass+1

print(countpass)