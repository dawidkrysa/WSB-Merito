# Author: Dawid Krysa
# Repository: https://github.com/dawidkrysa/WSB-Merito

import numpy as np

# Advertising Spending. Which companies spend the most money on advertising?
# Business Insider maintains a list of the top-spending companies. In 2014,
# Procter & Gamble spent more than any other company, a whopping $5 billion.
# In second place was Comcast, which spent $3.08 billion (Business Insider
# website). The top 12 companies and the amount each spent on advertising
# in billions of dollars are as follows.
#
# a. What is the mean amount spent on advertising?
# b. What is the median amount spent on advertising?
# c. What are the first and third quartiles?

company = np.array(
    [
        "Procter & Gamble",
        "Comcast",
        "AT&T",
        "Ford",
        "Verizon",
        "L'Oreal",
        "American Express",
        "General Motors",
        "Toyota",
        "Fiat Chrysler",
        "Walt Disney Company",
        "J.P. Morgan",
    ]
)

# Wydatki na reklamę w miliardach dolarów
advertising_b = np.array(
    [
        5.00,
        3.08,
        2.91,
        2.56,
        2.44,
        2.34,
        2.19,
        2.15,
        2.09,
        1.97,
        1.96,
        1.88,
    ]
)


print("""---------------------------------------------------------------
a. What is the mean amount spent on advertising?
---------------------------------------------------------------""")
print(f"Mean: {np.mean(advertising_b):.4f}")


print("""
---------------------------------------------------------------
b. What is the median amount spent on advertising?
---------------------------------------------------------------""")
print(f"Median: {np.median(advertising_b):.4f}")


print("""
---------------------------------------------------------------
c. What are the first and third quartiles?
---------------------------------------------------------------""")
q1 = np.quantile(advertising_b, 0.25, method="midpoint")
q3 = np.quantile(advertising_b, 0.75, method="midpoint")
print(f"First quartile: {q1:.4f}\nThird quartile: {q3:.4f}")
