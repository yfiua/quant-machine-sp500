#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import pandas as pd

df = pd.read_csv('sp500.csv')

N = len(df)

# Calculate monthly returns
returns = df['Quant'].values - 1

# Annualized return
annualized_return = np.prod(returns + 1) ** (12 / N) - 1

print("Annualized Return:", annualized_return)

# Calculate average monthly return (geometric mean)
avg_return = np.prod(returns + 1) ** (1 / N) - 1

print("Average Monthly Return (geometric mean):", avg_return)

# Risk-free rate
risk_free_rate = 0.00

# Set the Minimum Acceptable Return (MAR)
mar = 0.0

# Calculate downside deviation (annualized)
downside_returns = [r for r in returns if r < mar]
downside_deviation = np.std(downside_returns) * np.sqrt(12)

# Calculate Sortino Ratio
sortino_ratio = (annualized_return - (risk_free_rate + 1) ** 12 + 1) / downside_deviation

print("Downside Deviation:", downside_deviation)
print("Sortino Ratio:", sortino_ratio)

# Calculate standard deviation (annualized)
std_dev = np.std(returns) * np.sqrt(12)

# Calculate Sharpe Ratio
sharpe_ratio = (annualized_return -  (risk_free_rate + 1) ** 12 + 1) / std_dev

print("Average Monthly Return (geometric mean):", avg_return)
print("Standard Deviation:", std_dev)
print("Sharpe Ratio:", sharpe_ratio)

# Calculate maximum drawdown
cumulative_returns = np.cumprod(1 + returns)
peak = np.maximum.accumulate(cumulative_returns)
drawdown = (cumulative_returns - peak) / peak
max_drawdown = np.min(drawdown)

# Calculate Calmar Ratio
calmar_ratio = - annualized_return / max_drawdown

print("Maximum Drawdown:", max_drawdown)
print("Calmar Ratio:", calmar_ratio)
