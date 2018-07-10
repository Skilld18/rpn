#!/usr/bin/python

import re

f = open('sample.rpn', 'r')

current_symbol = ""

types = [
   ["[+-]?[0-9]+", "int"],
   ["[+-]?[0-9]+\.[0-9]+", "real"],
   ["\+", "plus"]
]
#These need to be properly greedy

opstack = []
prog = f.read()
for symbol in prog.split():
    print(symbol)
    if re.match(types[0][0], symbol):
        print(types[0][1])
        opstack.append(int(symbol))
    elif re.match(types[1][0], symbol):
        print(types[1][1])
        opstack.append(float(symbol))
    elif re.match(types[2][0], symbol):
        print(types[2][1])
        print(opstack.pop() + opstack.pop())



