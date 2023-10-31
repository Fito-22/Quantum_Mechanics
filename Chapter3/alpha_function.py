"""
Functions needed to plot alpha and beta in the square root potential problem

Created on Fall 2023

@author on: Adolfo Menendez
"""

# Import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define beta gamma and alpha

gamma = 5
N = int(np.ceil(gamma/np.pi))

def beta_tan(n):
    return np.linspace(-np.pi/2 + n*np.pi + 0.01,np.pi/2+n*np.pi -0.01, 100)
def beta_cot(n):
    return np.linspace(0+n*np.pi+0.01,np.pi+n*np.pi-0.01,100)
def alpha_tan(beta):
    return beta * np.tan(beta)
def alpha_cot(beta):
    return - beta * 1/(np.tan(beta))
def alpha_gamma(beta):
    return np.sqrt(gamma**2 - beta**2)

beta_gamma = np.linspace(0,gamma,100)

plt.figure()
for n in range(N):
    plt.plot(beta_tan(n),alpha_tan(beta_tan(n)), color="black")
    plt.plot(beta_cot(n),alpha_cot(beta_cot(n)), color="blue")
    for beta in beta_tan(n):
        if (beta<0) or (beta>gamma): continue
        if ( abs(alpha_tan(beta) - alpha_gamma(beta) ) < 0.15):
            plt.scatter(beta,alpha_gamma(beta), color="red")
            print(beta)
        else:continue
    for beta in beta_cot(n):
        if (beta<0) or (beta>gamma): continue
        if (abs(alpha_cot(beta) - alpha_gamma(beta))< 0.15):
            plt.scatter(beta,alpha_gamma(beta), color="red")
            print(beta)
        else:continue

plt.plot(beta_gamma,alpha_gamma(beta_gamma), color="orange")
plt.xlabel(r"$\beta$")
plt.ylabel(r"$\alpha$")
plt.ylim(0,2*np.pi)
plt.xlim(0,2*np.pi)
plt.legend(["B=0","C=0"])
plt.title(r"$\alpha(\beta)$ function for $\gamma=5$")
plt.savefig("GRAPHS/alpha_beta.png")
