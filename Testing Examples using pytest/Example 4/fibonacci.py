# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 11:54:41 2023

@author: prade
"""

def fib(n):
    old, new = 0, 1
    for _ in range(n):
        old, new = new, old + new
    return old