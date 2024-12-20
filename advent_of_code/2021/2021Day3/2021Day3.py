# -*- coding: utf-8 -*-
"""


@author: Andy
"""

import pandas as pd
import numpy as np

filetest = open("2021day3test.txt","r")
starttest = filetest.read()
startlisttest = starttest.split("\n")

file = open("2021day3input.txt","r")
start = file.read()
startlist = start.split("\n")

def splitnumbers(inputlist):
    numberslist = []
    for row in inputlist:
        newrow = []
        for char in row:
            newrow.append(int(char))
        numberslist.append(newrow)
    return numberslist

def preplist(inputlist):
    numbers = splitnumbers(inputlist)
    return numbers

def mostcommon(numbers):
    numrows = len(numbers)
    numcols = len(numbers[0])
    gamma = ''
    epsilon = ''
    for ii in range(0,numcols):
        zeros = 0
        ones = 0
        for jj in range(0,numrows):
#            print(ii)
#            print(jj)
#            print(numbers[jj][ii])
            if numbers[jj][ii] == 0:
                zeros = zeros + 1
            else:
                ones += 1
        if zeros > ones:
            gamma +='0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return gamma,epsilon

def power(inputlist):
    numbers = preplist(inputlist)
    gamma,epsilon = mostcommon(numbers)
    power = int(gamma,2)*int(epsilon,2)
    return power
    
        
def oxygen(inputlist):
    numbers = preplist(inputlist)
#    print(len(numbers))
#    print(len(numbers[0]))
    numcols = len(numbers[0])
    oxygen = numbers
    carbon = numbers
#    print(oxygen)
#    print(carbon)
    for ii in range(0,numcols):
        gamma = mostcommon(oxygen)[0]
#        print(gamma)
        epsilon = mostcommon(carbon)[1]
#        print(epsilon)
#        print(len(oxygen))
        if len(oxygen) > 1:
            newoxygen = [ x for x in oxygen if int(x[ii]) == int(gamma[ii]) ]
        else:
            newoxygen = oxygen
        if len(carbon) > 1:
            newcarbon = [ x for x in carbon if int(x[ii]) == int(epsilon[ii]) ]
        else:
            newcarbon = carbon
        oxygen = newoxygen
        carbon = newcarbon
#        print('Step '+str(ii))
#        print(len(oxygen))
#        print(len(carbon))
    return oxygen,carbon
        
def part2(inputlist):
    oxy,carb = oxygen(inputlist)
    oxyword = ''
    carbword = ''
#    print(oxy)
#    print(carb)
    for char in oxy[0]:
        oxyword += str(char)
#        print(oxyword)
    for char in carb[0]:
        carbword += str(char)
#    print(oxyword)
    power = int(oxyword,2)*int(carbword,2)
    return power