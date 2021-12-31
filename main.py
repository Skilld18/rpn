#!/usr/bin/python

import re

f = open('sample.rpn', 'r')


string = "\".*\""
number = "[0-9]+"
func = "[a-z]+"

stack = [] 

def plus(a,b):
    return a + b

def minus(a,b):
    return a - b

def apply(func):
    global stack
    arglist = []
    for i in range(0, func.args):
        arglist.insert(0, stack.pop())
    stack.append(func.func(*arglist))
    print(stack)


def act(i):
    global string
    global number
    global func

    global stack
    if re.match(string, i):
        stack.append(i)
    if re.match(number, i):
        stack.append(int(i))
    if re.match(func, i):
        class f:
            def __init__(self, func, args):
                self.func = func
                self.args = args
        apply(f(minus, 2))

opstack = []
prog = f.read()
for symbol in prog.split():
    act(symbol)



