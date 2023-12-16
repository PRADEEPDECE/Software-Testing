# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 11:35:51 2023

@author: prade
"""

import alg
def test_area():
    output=alg.area_of_rectangle(2, 5)
    assert output==10
def test_perimeter():
    output=alg.perimeter_of_rectangle(2, 5)
    assert output==14