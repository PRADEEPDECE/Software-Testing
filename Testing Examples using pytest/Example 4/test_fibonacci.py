# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 11:56:20 2023

@author: prade
"""

from fibonacci import fib
def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55