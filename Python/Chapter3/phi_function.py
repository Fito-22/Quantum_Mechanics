"""
Code to plot the phi(x) function for a given gamma.

Created on Fall 2023

@author on: Adolfo Menendez
"""

# Import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

################### EARLY DEFINITIONS ##########################

# Values of beta and alpha for gamma = 5 (From the alpha_beta function)
gamma = 5
beta_1 = 1.309
beta_2 = 2.596
alpha_1 = np.sqrt(gamma**2 - beta_1**2)
alpha_2 = np.sqrt(gamma**2 - beta_2**2)

# Define the parameters

a = 2
x_1 = np.linspace(-5,-a,100)    # x < -a
x_2 = np.linspace(-a,a,100)     # -a < x < a
x_3 = np.linspace(a,5,100)      # x > a


################# For the first alpha B=0 ###########################

alpha = alpha_1
beta = beta_1
B = 0
C = np.sqrt((alpha*np.exp(2*alpha))/(a*(1+alpha)))
A = C*np.cos(beta)
D = A

phi_1_C = D * np.exp(alpha*x_1/a)                     # x < a
phi_2_C = C * np.exp(-alpha) * np.cos(beta*x_2/a)     # -a < x < a
phi_3_C = A * np.exp(-alpha*x_3/a)                    # x > a

plt.figure()
plt.plot(x_1,phi_1_C)
plt.plot(x_2,phi_2_C)
plt.plot(x_3,phi_3_C)
plt.xlabel("x")
plt.ylabel(r"$\phi(x)$")
plt.title(fr"B=0, $\gamma=5$, $\alpha=${round(alpha,2)}")
plt.savefig("GRAPHS/B0.png")

################### For the second alpha C=0 ###########################

alpha = alpha_2
beta = beta_2
B = np.sqrt((alpha*np.exp(2*alpha))/(a*(1+alpha)))
C = 0
A = B*np.sin(beta)
D = -A

phi_1_B = D * np.exp(alpha*x_1/a)                     # x < a
phi_2_B = B * np.exp(-alpha) * np.sin(beta*x_2/a)     # -a < x < a
phi_3_B = A * np.exp(-alpha*x_3/a)                    # x > a


plt.figure()
plt.plot(x_1,phi_1_B)
plt.plot(x_2,phi_2_B)
plt.plot(x_3,phi_3_B)
plt.xlabel("x")
plt.ylabel(r"$\phi(x)$")
plt.title(fr"C=0, $\gamma=5$, $\alpha=${round(alpha,2)}")
plt.savefig("GRAPHS/C0.png")

########### COMBINING BOTH #########################################################3

plt.figure()
plt.subplot(1,2,1)
plt.plot(x_1,phi_1_C)
plt.plot(x_2,phi_2_C)
plt.plot(x_3,phi_3_C)
plt.xlabel("x")
plt.title(fr"B=0, $\gamma=5$, $\alpha=${round(alpha,2)}")

plt.subplot(1,2,2)
plt.plot(x_1,phi_1_B)
plt.plot(x_2,phi_2_B)
plt.plot(x_3,phi_3_B)
plt.xlabel("x")
plt.title(fr"C=0, $\gamma=5$, $\alpha=${round(alpha,2)}")

plt.suptitle(r"$\phi(x)$")
plt.savefig("GRAPHS/gamma=5.png")
