# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 11:43:55 2023

@author: prade
"""

import pytest
 
def test_total_divisible_by_6(input_total):
    assert input_total % 6 == 0
 
 
def test_total_divisible_by_15(input_total):
    assert input_total % 15 == 0
 
 
def test_total_divisible_by_9(input_total):
    assert input_total % 9  == 0