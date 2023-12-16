# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 12:02:17 2023

@author: prade
"""

import pytest
from foobar import foo, bar

@pytest.mark.crazy
def test_foo():
    assert foo() == "foo"

@pytest.mark.crazy
def test_bar():
    assert bar() == "bar"