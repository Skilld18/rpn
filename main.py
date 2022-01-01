#!/usr/bin/python3

import re

f = open('sample.rpn', 'r')


string = "\".*\""
number = "[0-9]+"
func = "[a-z]+"

stack = []
vars = {}

def plus(a,b):
    return a + b

def minus(a,b):
    return a - b

def p(a):
    print(a)


def assign(a, b):
    global vars
    global stack
    vars[b] = a


def apply(func):
    global stack
    stack = [func.func(*func.args)]
    if stack == [None]:
        stack = []

def decide_func(a):
    if a == "plus":
        return plus
    if a == "minus":
        return minus
    if a == "assign":
        return assign
    if a == "print":
        return p


def act(i):
    global string
    global number
    global func
    global vars

    global stack
    if i in vars.keys():
        stack.append(vars[i])
        return
    if re.match(string, i):
        stack.append(i)
    if re.match(number, i):
        stack.append(int(i))
    if re.match(func, i):
        i = decide_func(i)
        class f:
            def __init__(self, func, args):
                self.func = func
                self.args = args
        apply(f(i, stack))

opstack = []
prog = f.read()
for symbol in prog.split():
    act(symbol)


