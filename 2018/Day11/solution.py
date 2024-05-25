#%%
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque
import itertools as it
import copy

#%%
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()
numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
numlist = [str(x) for x in range(0,10)]
#%%
file = open("inputfile.txt","r")
start = file.read()
startlist = start.split("\n")

file = open("inputtest.txt","r")
startb = file.read()
testlist = startb.split("\n")
#%%

def power_level(serial,x,y):
    rack_id = x+10
    # print(rack_id)
    power = rack_id*y
    # print(power)
    power = power+serial
    # print(power)
    power = power*rack_id
    # print(power)
    powmod1k = power % 1000
    hundreds = int((powmod1k - (powmod1k % 100))/100)
    # print(hundreds)
    return hundreds-5

def create_power_grid(serial):
    grid = []
    for ii in range(0,300):
        row = []
        for jj in range(0,300):
            power = power_level(serial,jj+1,ii+1)
            row.append(power)
        grid.append(row)
    return np.array(grid)

def create_fuel_scores(serial):
    power_grid = create_power_grid(serial)
    fuel_grid = np.zeros((297,297))
    for ii in range (0,3):
        for jj in range(0,3):
            fuel_grid = np.add(fuel_grid,power_grid[jj:297+jj,ii:297+ii])
    return fuel_grid

def p2_create_fuel_scores(serial):
    power_grid = create_power_grid(serial)
    fuel_grid_list = []
    max_fuel = -9999
    for size in range(1,300):
        fuel_grid = np.zeros((300-size,300-size))
        for ii in range (0,size):
            for jj in range(0,size):
                fuel_grid = np.add(fuel_grid,power_grid[jj:(300-size)+jj,ii:(300-size)+ii])
        print(size,fuel_grid.max())
        if fuel_grid.max() < 0:
            return fuel_grid_list
        max_fuel = fuel_grid.max()
        fuel_grid_list.append(fuel_grid)
        # print(size,fuel_grid.max())
    return fuel_grid_list

#%%
def part1(serial):
    fuel_grid = create_fuel_scores(serial)
    max_fuel = fuel_grid.max()
    indices = np.where(fuel_grid == max_fuel)
    return [int(indices[1]+1),int(indices[0]+1),max_fuel]

def part2(serial):
    fuel_grid_list = p2_create_fuel_scores(serial)
    max_fuel_list = [x.max() for x in fuel_grid_list]
    size = max_fuel_list.index(max(max_fuel_list))+1
    max_fuel_grid = fuel_grid_list[size-1]
    max_fuel = max_fuel_grid.max()
    indices = np.where(max_fuel_grid == max_fuel)
    x = int(indices[1]+1)
    y = int(indices[0]+1)
    return x,y,size
