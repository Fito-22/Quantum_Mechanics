"""

ALL THIS CODE WAS GIVE IT TO ME BY ALEX LOHR, CLASSMATE IN QUANTUM MECHANICS II IN FIU

Alex email: alohr001@fiu.edu

"""
#%%
import numpy as np
import matplotlib.pyplot as plt

n = 1
Z = 1
m = 9.1093837015e-31
e = 1.602176634e-19
ep = 8.8541878128e-12
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

#%%
print(E(1))
print(E(2)-E(1))
c = 299792458
h = 6.62607015 * 10**(-34)

print((4/3)* (E(2)-E(1))/(c*h))
