
import pandas as pd
import numpy as np
import re
import datetime as dt
from collections import deque,defaultdict
import itertools as it
import copy


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()
numbers = '1234567890'

#file = open("2020day22.txt","r")
#start = file.read()
#startlist = start.split("\n\n")
#
#file = open("2020day22test.txt","r")
#startb = file.read()
#testlist = startb.split("\n\n")

start = '952438716'
test = '32415'
testb = '389125467'

def turn(board,current):
    maxval = max(board)
    origin = board[current]
    board.rotate(-current-1)
    pickup = [board[x] for x in range(0,3)]
    board.popleft()
    board.popleft()
    board.popleft()
    dest = origin - 1
    if dest == 0:
         dest = maxval
#    print(pickup)
    if dest in pickup:
         while dest in pickup:
             dest -= 1
             if dest == 0:
                 dest = maxval
#    print(dest)
    loc = board.index(dest)
    board.rotate(-1-loc)
    for num in pickup:
        board.append(num)
    board.rotate(current+5+loc)
    return board


def part1(inputlist,moves):
    board = deque([int(x) for x in inputlist])
    maxval = max(board)
    current = 0
    i = 0
    while i < moves:
#        print(board)
        board = turn(board,current)
#        print(board)
        current += 1
#        print(current)
        if current >= maxval:
            current = 0
        i+=1
    board.rotate(-board.index(1))
    boardlist = [str(x) for x in board]
    return ''.join(boardlist[1:])


def part2(inputlist,moves):
    board = deque([int(x) for x in inputlist]+[x for x in range(10,1000001)])
    print(list(board)[0:20])
    maxval = max(board)
    current = 0
    i = 0
    while i < moves:
#        print(list(board)[0:20])
        board = turn(board,current)
#        print(board)
        current += 1
#        print(current)
        if current >= maxval:
            current = 0
        i+=1
#        print(board[(board.index(1)+1)%1000000],board[(board.index(1)+2)%1000000])
#        if i % 10000 == 0:
#        print(i)
    board.rotate(-board.index(1))
    return board[1]*board[2]
