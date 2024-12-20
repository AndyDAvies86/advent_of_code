# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:46:13 2020

@author: Andy
"""



import pandas as pd
import numpy as np
import re

file = open("2017day18test2.txt","r")
start = file.read()
startlist = start.split("\n")

fullinst =[]
for item in startlist    :
    fullinst.append(item.split(" "))

letters = 'abcdefghijklmnopqrstuvwxyz'
for char in letters:
    exec (char + " = 0")
sound = 0
rcv = 0

machaout = []
machbout = []

machapos = 0
machbpos = 0

machareg = {}
machbreg = {}
for char in letters:
    machareg[char]=0
    machbreg[char]=0
machbreg['p']=1

machregout = {}
sounda = []
soundb = []


def machine(ii,machlet,register):
    for char in letters:
        temp = register[char]
        exec(char + " = temp")
    while ii < len(fullinst):
        print(ii)
        if fullinst[ii][0] == 'snd':
            print("Sound: " + str(eval(fullinst[ii][1])))
            exec('sound' + machlet + '.append(eval(fullinst[ii][1]))')
        if fullinst[ii][0] == 'set':
            exec(fullinst[ii][1] + " = " + str(eval(fullinst[ii][2])))
        if fullinst[ii][0] == 'add':
            exec(fullinst[ii][1] + " = " + str(eval(fullinst[ii][1])) + " + " + str(eval(fullinst[ii][2])))
        if fullinst[ii][0] == 'mul':
            exec(fullinst[ii][1] + " = " + str(eval(fullinst[ii][1])) + " * " + str(eval(fullinst[ii][2])))
        if fullinst[ii][0] == 'mod':
            exec(fullinst[ii][1] + " = " + str(eval(fullinst[ii][1])) + " % " + str(eval(fullinst[ii][2])))
        if fullinst[ii][0] == 'rcv':
            #if eval(fullinst[ii][1]) != 0 :
                rcv = sound
                print("Recover: " + str(rcv))
                for char in letters:
                    print(char + " = " + str(eval(char)))
                    machregout[char] = eval(char)
                return ii
                break
        if fullinst[ii][0] == 'jgz':
            if eval(fullinst[ii][1]) != 0 :
                ii = ii + eval(fullinst[ii][2])
                continue
        ii += 1
    

# machine A

machaposout=machine(0,'a',machareg)
machbposout=machine(0,'b',machbreg)

#for char in letters:
 #   machareg[char] = machregout[char]

#for char in letters:
 #   exec(char + " = " + str(machbreg[char]))