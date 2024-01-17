# Import libraries
import numpy as np
import matplotlib.pyplot as plt


# Define the cosntants
L = 1
m = 1
omega = 1

# Define rho and the potential


rho = np.linspace(0.1,10,100)


U = L**2/(2*m*rho**2) + 1/2 * m*omega**2 * rho**2

plt.plot(rho,U)
plt.savefig("GRAPHS/U_eff.png")
