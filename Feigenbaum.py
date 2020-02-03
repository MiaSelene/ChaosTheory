#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:28:59 2020

@author: thausmann
"""
import matplotlib.pyplot as plt

def find_stable_set(r):
    stable_set = []
    x = 0.5
    try:
        while not type(proximity_bound(x, stable_set))==int:
            stable_set.append(x)
            x = r * x * (1 - x)
        return stable_set[proximity_bound(x, stable_set):]
    except OverflowError:
        return [r]

def proximity_bound(x, seq):
    for i, xi in enumerate(seq):
        if (xi-x)**2 < 0.0000000001:
            return i
    return False

arr = [find_stable_set(3.0 + r/100000) for r in range(100000)]
new = []
newx = []
for i,el in enumerate(arr):
    for eli in el:
        new.append(eli)
        newx.append(3.0 + i/100000)

plt.plot(newx,new, 'or', markersize=0.1, alpha=0.01)
