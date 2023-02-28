#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

df = pd.read_csv('sp500.csv')

plt.figure()

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

df.plot(figsize=(14.1, 6), x='month', y=['SP500-cum', 'Quant-cum'], color=['b', 'r'])

# Define a custom formatter function for the y-axis ticks
def percent_fmt(x, pos):
    return '{:.1%}'.format(x)

# Create a FuncFormatter object with the custom formatter function
percent_formatter = FuncFormatter(percent_fmt)

# Set the y-axis tick formatter to the FuncFormatter object
plt.gca().yaxis.set_major_formatter(percent_formatter)

plt.title('SP500 回测收益曲线')
plt.xlabel(r'月份')
plt.legend(labels=['SP500指数', '夹头机'])

plt.grid(True)
plt.axis('tight')

plt.savefig('sp500.png')

