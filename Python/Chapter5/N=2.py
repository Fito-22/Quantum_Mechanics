"""
Program to find the solution for alpha when N=2 by ploting left and right side.
"""

# Import libraries

import numpy as np
import matplotlib.pyplot as plt

# Fixed values

N=2

d = 1

alpha= np.linspace(0,2,100)

func_1 = 1+np.exp(-alpha*d)
func_2 = 1-np.exp(-alpha*d)

# If d = 2
# alpha_sol1 = 0.7968121299
# alpha_sol2 = 1.1088575527

# If d=0.5
alpha_sol1 = 1.4776700633

# Making the figure

plt.figure()
plt.plot(np.arange(-2,3),np.zeros(5), color="black")
plt.plot(np.zeros(5),np.arange(-2,3), color="black")

plt.title(f"N=2, d={d}")
plt.plot(alpha,alpha,color="blue")
plt.plot(alpha,func_1,color="blue")
plt.plot(alpha,func_2,color="blue")

plt.scatter(alpha_sol1,alpha_sol1, color="red")
    # plt.scatter(alpha_sol2,alpha_sol2, color="red")

plt.xlabel(r"$\alpha$")
plt.xlim(-0.1,2.1)
plt.ylim(-0.1,2.1)

plt.savefig("GRAPHS/N=2,d=1.png")
# plt.savefig("GRAPHS/N=2,d=0.5.png")
