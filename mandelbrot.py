#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:28:58 2020

@author: thausmann
"""

import matplotlib.pyplot as plt
import numpy as np


def criterion(x):
    c = 0
    for i in range(50):
        c = c**2 + x
        if abs(c) > 2:
            return i-50
    return 0

x_size = 5000
y_size = 5000
x_range = (-2, 2)
y_range = (-3, 1)
xStar = lambda x: (x_range[0] + (x_range[1] - x_range[0]) * x / x_size)
yStar = lambda y: (y_range[0] + (y_range[1] - y_range[0]) * y / y_size)
result = []
for x in range(x_size):
    if x%1000==0:
        print(x/10000*100)
    result.append([])
    for y in range(y_size):
        result[-1].append(criterion(complex(yStar(y), xStar(x))))
plt.matshow(result, cmap='CMRmap')
