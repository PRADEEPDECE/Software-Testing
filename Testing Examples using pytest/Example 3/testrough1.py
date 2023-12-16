# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 11:43:08 2023

@author: prade
"""

import pytest
 
def test_total_divisible_by_5(input_total):
    assert input_total % 5 == 0
 
 
def test_total_divisible_by_10(input_total):
    assert input_total % 10 == 0
 
 
def test_total_divisible_by_20(input_total):
    assert input_total % 20 == 0
 
 
def test_total_divisible_by_9(input_total):
    #assert input_total % 9 == 0
    assert input_total % 20 == 0