"""
Code to plot the probabilty function and the fourier analysis fucntion.

Created on Fall 2023

@author on: Adolfo Menendez
"""

# Import libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


"""

1º Figure: Plot P(x) and P(k)

"""

# Parameters for P(x) and P(k)

k = 1
sigma = 0.1  # Standard Deviation

# Generate x-values and k-values from -5 to 5
x = np.linspace(-10, 10, 100)
k = np.linspace(-10, 10, 100)

# Define my functions
def P_x(x):
    A = 1/np.sqrt(2*np.pi*sigma**2)
    exp = - (x**2 / (2*sigma**2))
    return A * np.exp(exp)

def P_k(k):
    return 2**(3/2) * np.pi**(1/2) * sigma * np.exp(-2*sigma**2*k**2)


print(P_x(x))

# Plot both functions with subplot
plt.figure()
plt.subplot(1,2,1)
plt.plot(x, P_x(x))
plt.title('P(x)')
plt.xlabel('x')

plt.subplot(1,2,2)
plt.plot(k, P_k(k))
plt.title('P(k)')
plt.xlabel('k')

plt.suptitle(fr"$\sigma$ = {sigma}")

# Customize the plot
plt.savefig(f"GRAPHS/P_x&P_k_sigma={sigma}.png")
