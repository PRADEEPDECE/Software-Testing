# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 12:00:26 2023

@author: prade
"""

import pytest
from fibonacci1 import fib, rfib
def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(34) == 5702887
@pytest.mark.crazy
@pytest.mark.slow
def test_rfib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert rfib(34) == 5702887