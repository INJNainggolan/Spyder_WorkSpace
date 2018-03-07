#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:50:05 2017

@author: nainggolan
"""
'''
import matplotlib.pyplot as plt
plt.subplot(321)
plt.subplot(3, 2, 4)
plt.plot([3, 1, 4, 5, 2])
plt.ylabel("grade")
plt.show()
'''
import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


a = np.arange(0.0, 5.0, 0.02)

plt.subplot(211)
plt.plot(a, f(a))

plt.subplot(2, 1, 2)
plt.plot(a, np.cos(2 * np.pi * a), 'r--')
plt.show()