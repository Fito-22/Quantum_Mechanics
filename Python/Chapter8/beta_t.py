# Import libraries
import numpy as np
import matplotlib.pyplot as plt


# Define the constants
alpha=np.array([1.1,2,5])
beta_0 = 0.05

# Define tau and beta


tau = np.linspace(0.1,10,100)
plt.figure()

for a in alpha:
    B = np.sqrt(1-1/a**2)
    beta = B * np.sin(2*tau+np.arcsin(beta_0/B))
    plt.plot(tau,beta,label=fr"$\alpha$ = {a}")
plt.legend()
plt.xlabel(r"$\tau$")
plt.ylabel(r"$\beta (\tau)$")
plt.savefig("GRAPHS/beta_tau.png")
