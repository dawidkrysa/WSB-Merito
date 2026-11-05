# Author: Dawid Krysa
# Repository: https://github.com/dawidkrysa/WSB-Merito

import numpy as np

# Zadanie 5 (Cost Estimation)
#
# Cost Estimation. An important application of regression analysis in
# accounting is in the estimation of cost. By collecting data on volume and
# cost and using the least squares method to develop an estimated regression
# equation relating volume and cost, an accountant can estimate the cost
# associated with a particular manufacturing volume. Consider the following
# sample of production volumes and total cost data for a manufacturing
# operation.
#
# a) Use these data to develop an estimated regression equation that could be
#    used to predict the total cost for a given production volume.
# b) What is the variable cost per unit produced?
# c) Compute the coefficient of determination. What percentage of the
#    variation in total cost can be explained by production volume?
# d) The company's production schedule shows 500 units must be produced next
#    month. Predict the total cost for this operation.

# Production volume [units]
x = np.array(
    [
        400,
        450,
        550,
        600,
        700,
        750,
    ]
)

# Total cost [$]
y = np.array(
    [
        4000,
        5000,
        5400,
        5900,
        6400,
        7000,
    ]
)


print("""---------------------------------------------------------------
a) Use these data to develop an estimated regression equation that could be
   used to predict the total cost for a given production volume.
---------------------------------------------------------------""")
x_mean = x.mean()
y_mean = y.mean()

numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)

b1 = numerator / denominator
b0 = y_mean - b1 * x_mean

print(f"Regression equation: y = {b1:.2f}*x + {b0:.2f}")


print("""
---------------------------------------------------------------
b) What is the variable cost per unit produced?
---------------------------------------------------------------""")
print(f"Variable cost per unit produced: {b1:.2f} $/unit")


print("""
---------------------------------------------------------------
c) Compute the coefficient of determination. What percentage of the
   variation in total cost can be explained by production volume?
---------------------------------------------------------------""")
y_estimated = b0 + b1 * x

ssr = np.sum((y_estimated - y_mean) ** 2)
sst = np.sum((y - y_mean) ** 2)
R2 = ssr / sst

print(f"R^2 = {R2:.4f}")
print(
    f"{R2 * 100:.2f}% of the variation in total cost is explained by production volume"
)

print("""
---------------------------------------------------------------
d) The company's production schedule shows 500 units must be produced next
   month. Predict the total cost for this operation.
---------------------------------------------------------------""")
print(f"Prediction for x = 500: {(b0 + b1 * 500.0):.2f} $")
