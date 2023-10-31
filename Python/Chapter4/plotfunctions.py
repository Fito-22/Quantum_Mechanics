"""
Code to plot a potential that is a delta function.

Created on Fall 2023

@author on: Adolfo Menendez
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


################################ DELTA ###################################################################
plt.figure()
# Axis
plt.plot(np.arange(-2,3),np.zeros(5), color="black")
plt.plot(np.zeros(5),np.arange(-2,3), color="black")

# Function
plt.plot(np.arange(-2,3),np.zeros(5), color="blue")
plt.plot(np.zeros(3),-np.arange(0,3), color="blue")
plt.scatter(0,-1.9,marker=11, color="blue")

plt.savefig("GRAPHS/delta.png")

################################ PHI(X) != 0 ###################################################################

plt.figure()
# Axis
plt.plot(np.arange(-2,3),np.zeros(5), color="black")
plt.plot(np.zeros(5),np.arange(-2,3), color="black")

# Function
A=1.5
alpha=2.5
x_1 = np.linspace(-2,0,50)     # x < 0
x_2 = np.linspace(0,2,50)      # x > 0
phi_1 = A*np.exp(alpha*x_1)    # x < 0
phi_2 = A*np.exp(-alpha*x_2)     # x > 0

plt.plot(x_1,phi_1,color="orange")
plt.plot(x_2,phi_2,color="orange")
plt.xlabel("x")
plt.ylabel(r"$\phi(x)$")
plt.yticks([])
plt.text(0.1,A,"A")
plt.scatter(0,A,color="black",marker="_")


plt.savefig("GRAPHS/phi(x).png")
