"""
Code to plot a Potential Well for V(x) = -k/x.

Created on Fall 2023

@author on: Adolfo Menendez
"""

# Import libraries

import numpy as np
import matplotlib.pyplot as plt

# Define the constants. All of them should be >= 0
m = 1            # Reduce mass (kg)
L = 1            # Angular momentum (kg m^2 /s)
k = 1            # Constant of the P.E (Potential Energy) (N m^2)

rho = np.linspace(0.4,10,100)

y = np.linspace(0.6,-0.7,100)

x = rho * 0
rho_0 = np.linspace(0,10,100)
rho_E = np.linspace(-0.05,10,100)


U_eff = L**2/(2*m*rho*rho) - k/rho
print(U_eff)

plt.plot(x,y, color="black")                # y-axis
plt.plot(rho_0,x, color="black")            # x-axis
plt.plot(rho,U_eff)                         # Potential
plt.plot(rho_E,x-0.495, color="red")        # Lower Energy
plt.plot(rho_E,x-0.2, color="red")          # Energy < 0
plt.plot(rho_E,x+0.3, color="red")          # Energy > 0




plt.scatter(0.98,-0.495, color="red")
# plt.scatter(0,-0.49, color="red", marker="_")
plt.xlim(-1,11)
plt.xticks([])
plt.yticks([])
plt.text(0.7,0.4,r"$\frac{L^2}{2m\rho^2}-\frac{k}{\rho}$")
plt.text(10.2,0.01,r"$\rho$")
plt.text(-0.3,0.5,"E")
plt.text(1,-0.55,r"$\rho_0$",fontdict={"color":"red"})
plt.text(-0.5,-0.5,r"$E_0$", color="red")
plt.text(-0.9,-0.22,r"$E<0$", color="red")
plt.text(-0.9,0.28,r"$E>0$", color="red")



# plt.text(-0.08,-50,"E_0",fontdict={"color":"red"})

# plt.title("Potential Well of Earth-Sun")

plt.savefig("GRAPHS/general")
