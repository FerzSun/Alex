# -*- coding: utf-8 -*-
"""Копия блокнота "Добро пожаловать в Colaboratory!"

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FtPqfObZsvjEyYy772DmJWL3TCwiqfTc
"""

seconds_in_a_day = 24 * 60 * 60
seconds_in_a_day

seconds_in_a_week = 7 * seconds_in_a_day
seconds_in_a_week

import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()