"""
Code to plot a Potential Well for V(x) = -k/x.

Created on Fall 2023

@author on: Adolfo Menendez
"""

# Import libraries

import numpy as np
import matplotlib.pyplot as plt

# Define the constants. All of them should be >= 0
m = 9.11*10**-31
e = 1.6*10**(-19)    # Reduce mass (kg)
L = 1.45*10**(-32)              # Angular momentum (kg m^2 /s)
k = e**2 * 9*10**(9)          # Constant of the P.E (Potential Energy) (N m^2)

rho = np.linspace(0.0000004, 0.00002,500)

y = np.linspace(-1.8,1.8,500)*10**(-22)

x = rho * 0
rho_0 = np.linspace(0.0, 0.00002,500)


U_eff = L**2/(2*m*rho*rho) - k/rho
print(U_eff)

plt.plot(x,y, color="black")        # y-axis
plt.plot(rho_0,x, color="black")    # x-axis
plt.plot(rho,U_eff)                 # Potential

# plt.scatter(0.1,-50, color="red")
# plt.scatter(0,-50, color="red", marker="_")
# plt.xlim(-0.1,1.1)
# plt.xticks([])
# plt.yticks([])
# plt.text(0.05,40,r"$\frac{L^2}{2m\rho^2}-\frac{k}{\rho}$")
# plt.text(0.95,5,r"$\rho$")
# plt.text(-0.025,50,"E")
# plt.text(0.13,-54,r"$\rho_0$",fontdict={"color":"red"})
# plt.text(-0.08,-50,"E_0",fontdict={"color":"red"})
# plt.title("Potential Well of Earth-Sun")





plt.savefig("GRAPHS/E-P_elec_Potential_Well")
