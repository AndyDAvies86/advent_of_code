# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:49:48 2020

@author: Andy
"""

import pandas as pd
import numpy as np

inputfile = pd.read_csv("2020day1.txt")

start=np.array(inputfile)

for i in range(1,199):
    for j in range(i,199):
        if start[i] + start[j] == 2020:
            print("Lines ",i," and ",j,". ")
            print(start[i])
            print(start[j])
            print(start[i]*start[j])

    