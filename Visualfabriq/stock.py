# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 18:46:42 2023

@author: BHARGAV REDDY
"""

def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))

prices = [7, 6, 4, 3, 1]
print(max_profit(prices)) 