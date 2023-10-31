"""
Code to plot the probabilty function among space and time of the measure of a static object.

Created on Fall 2023

@author on: Adolfo Menendez
"""

# Import the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#  Define the functions

def sigma_func(t):
    return sigma*np.sqrt(1 + ((hb**2 * t**2) / (4*m**2*sigma**4)) )

def P_func(x,t):
    A = 1/np.sqrt(2*np.pi*sigma_func(t)**2)
    exp = - (x**2 / (2*sigma_func(t)**2))
    return A * np.exp(exp)

def tau():
    return (m*sigma**2)/hb

# Define x (near 0)

x = np.linspace(-5,5,100)

#################### Earth problem #####################

# Variables

m = 5.97 * 10**(24)     # Earth mass in kilograms (kg)
sigma = 0.1             # Initial experimental deviation of 10%
hb = 1.05 * 10**(-34)   # Planck constant, hbar (J/s)

# Define the time

"""
For this part we will use the characteristic time as the step.
"""

t = np.arange(0,10 * tau(), tau())

# Plot sigma(t)
plt.figure("earth_sigma")
plt.plot(t/tau(),sigma_func(t))
plt.xlabel("time/tau")
plt.ylabel(r"$\sigma$")
plt.title(r"Earth $\sigma(t)$")
plt.savefig("GRAPHS/EARTH/sigma.png")

# Plot P(x,t) for different times

t = np.arange(0,20 * tau(), tau())
count=0
for t_i in t:
    plt.figure()
    plt.plot(x,P_func(x,t_i))
    plt.xlabel("x")
    plt.ylim(-0.1,4)
    plt.ylabel("P(x,t)")
    plt.title(fr"Earth P(x,t={count} $\tau$ )")
    plt.savefig(f"GRAPHS/EARTH/P-{count}.png")
    count+=1

plt.close()

#################### Electron problem #####################

# Variables

m = 9.11 * 10**(-31)     # Electron mass in kilograms (kg)
sigma = 0.1             # Initial experimental deviation of 10%
hb = 1.05 * 10**(-34)   # Planck constant, hbar (J/s)

# Define the time

"""
For this part we will use the characteristic time as the step.
"""

t = np.arange(0,10 * tau(), tau())

# Plot sigma(t)
plt.figure("electron_sigma")
plt.plot(t/tau(),sigma_func(t))
plt.xlabel("time/tau")
plt.ylabel(r"$\sigma$")
plt.title(r"Electron $\sigma(t)$")
plt.savefig("GRAPHS/ELECTRON/sigma.png")

# Plot P(x,t) for different times

t = np.arange(0,20 * tau(), tau())
count=0
for t_i in t:
    plt.figure()
    plt.plot(x,P_func(x,t_i))
    plt.xlabel("x")
    plt.ylim(-0.1,4)
    plt.ylabel("P(x,t)")
    plt.title(fr"Electron P(x,t={count} $\tau$ )")
    plt.savefig(f"GRAPHS/ELECTRON/P-{count}.png")
    count+=1

plt.close()

#################### NEUTRON problem #####################

# Variables

m = 1.67 * 10**(-27)     # Electron mass in kilograms (kg)
sigma = 0.1             # Initial experimental deviation of 10%
hb = 1.05 * 10**(-34)   # Planck constant, hbar (J/s)

# Define the time

t = np.linspace(0,879,20)

# Plot sigma(t)
plt.figure()
plt.plot(t, sigma_func(t) )
plt.xlabel("time (s)")
plt.ylabel(r"$\sigma$")
plt.title(r"Neutron $\sigma(t)$")
plt.savefig("GRAPHS/NEUTRON/sigma.png")

# Plot P(x,t) for different times

count=0
for t_i in t:
    plt.figure()
    plt.plot(x,P_func(x,t_i))
    plt.xlabel("x")
    plt.ylim(-0.1,4)
    plt.ylabel("P(x,t)")
    plt.title(fr"Neutron P(x,t={round(t_i,2)})")
    plt.savefig(f"GRAPHS/NEUTRON/P-{count}.png")
    count+=1
    plt.close()

plt.close()

################ HUMAN problem #####################################################


# Variables

m = 70                  # Human mass in kilograms (kg)
sigma = 0.1             # Initial experimental deviation of 10%
hb = 1.05 * 10**(-34)   # Planck constant, hbar (J/s)

# Define the time

"""
For this part we will use the characteristic time as the step.
"""

t = np.arange(0,10 * tau(), tau())

# Plot sigma(t)
plt.figure("human_sigma")
plt.plot(t/tau(),sigma_func(t))
plt.xlabel("time/tau")
plt.ylabel(r"$\sigma$")
plt.title(r"Human $\sigma(t)$")
plt.savefig("GRAPHS/HUMAN/sigma.png")

# Plot P(x,t) for different times

t = np.arange(0,20 * tau(), tau())
count=0
for t_i in t:
    plt.figure()
    plt.plot(x,P_func(x,t_i))
    plt.xlabel("x")
    plt.ylim(-0.1,4)
    plt.ylabel("P(x,t)")
    plt.title(fr"Human P(x,t={count} $\tau$ )")
    plt.savefig(f"GRAPHS/HUMAN/P-{count}.png")
    count+=1

plt.close()
