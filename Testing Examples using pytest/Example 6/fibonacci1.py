# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 11:59:45 2023

@author: prade
"""

def fib(n):
    old, new = 0, 1
    for i in range(n):
        old, new = new, old + new
    return old
def rfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rfib(n-1) + rfib(n-2)