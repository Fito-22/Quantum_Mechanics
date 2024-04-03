"""

ALL THIS CODE WAS GIVE IT TO ME BY ALEX LOHR, CLASSMATE IN QUANTUM MECHANICS II IN FIU

"""

import numpy as np
import matplotlib.pyplot as plt

n = 1
Z = 1
m = 9.1093837e-31
e = 1.60217662e-19
ep = 8.854187817e-12
hbar = 1.054571817e-34

E = (-Z**2*e**4*m)/(32*np.pi**2*ep**2*hbar**2*n**2)
print(E)



def E(n):
    return (-Z**2 * e**4 * m) / (32 * np.pi**2 * ep**2 * hbar**2 * n**2)

n_values = np.arange(1, 11)

energy_values = [E(n) for n in n_values]

plt.plot(n_values, energy_values, marker='o')
plt.xlabel('n')
plt.ylabel('Energy (J)')
plt.title('Energy vs. Principal Quantum Number (n)')
plt.grid(True)
plt.savefig('images/energy_vs_n.png')
