# Import libraries

import numpy as np
import matplotlib.pyplot as plt

# Plotting the function

beta = np.linspace(0.1,10,100)
func = (beta*(1+np.exp(-beta))) / (2*(1-np.exp(-beta)))

plt.figure()
plt.plot(beta, func, color="blue")
plt.xlabel(r"$\beta$")
plt.ylabel(r"$\frac{E}{K_B T}$")
plt.savefig("GRAPHS/E_beta.png")
