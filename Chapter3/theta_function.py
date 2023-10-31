"""
Code to plot a delta function

Created on Fall 2023

@author on: Adolfo Menendez
"""

# Import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Define the function and the x array

theta_min = np.ones(10)*(-1)
theta_max = np.ones(10)
x_1 = np.linspace(-5,0,10)
x_2 = np.linspace(0,5,10)


plt.figure()
plt.plot(x_1,theta_min,color="blue")
plt.plot(x_2,theta_max,color="blue")
plt.plot(np.zeros(10),np.linspace(-1.5,1.5,10), color="black")
plt.plot(np.linspace(-5,5,10),np.zeros(10), color="black")

plt.xticks([])
plt.yticks([])
plt.text(-0.4,1,r"$\theta_{+}$")
plt.text(0.1,-1,r"$\theta_{-}$")
plt.text(-0.8,1.3,r"$\theta(x)$")
plt.text(4.9,-0.2,r"$x$")



# plt.ylabel(r"$\theta(x)$")
plt.savefig("GRAPHS/theta_func.png")


################## POTENTIAL ####################################################

V_1 = np.zeros(10)
V_2 = np.ones(10)*(-1)
V_3 = np.zeros(10)
x_1 = np.linspace(-5,-2,10)
x_2 = np.linspace(-2,2,10)
x_3 = np.linspace(2,5,10)

plt.figure()
plt.plot(np.zeros(10),np.linspace(-1.5,1.5,10), color="black")  #y-axis
plt.plot(np.linspace(-5,5,10),np.zeros(10), color="black")      #x-axis
plt.plot(x_1,V_1,color="blue")
plt.plot(x_2,V_2,color="blue")
plt.plot(x_3,V_3,color="blue")
plt.plot(np.ones(10)*(-2),np.linspace(-1,0,10),color="blue")
plt.plot(np.ones(10)*(2),np.linspace(-1,0,10),color="blue")



plt.xticks([])
plt.yticks([])
plt.text(-2.1,0.05,"-a")
plt.text(1.9,0.05,"a")
plt.text(2.1,-1,r"$-V_0$")
plt.text(4.9,-0.2,r"$x$")
plt.text(-0.8,1.3,r"$V(x)$")
plt.savefig("GRAPHS/square_potential.png")
