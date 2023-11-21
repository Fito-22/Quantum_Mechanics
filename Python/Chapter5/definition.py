# Import libraries

import numpy as np
import matplotlib.pyplot as plt


################# Potentials ######################################

plt.figure()

# Axis
plt.plot(np.arange(-2,3),np.zeros(5), color="black")
plt.plot(np.zeros(5),np.arange(-2,3), color="black")

# Potentials

plt.plot(np.arange(-2,3),np.zeros(5)  , color="blue")
plt.plot(np.zeros(3),-np.arange(0,3)  , color="blue")
plt.plot(np.zeros(3)+1,-np.arange(0,3), color="blue")
plt.plot(np.zeros(3)-1,-np.arange(0,3), color="blue")

plt.scatter(0,-1.9,marker=11, color="blue")
plt.scatter(-1,-1.9,marker=11, color="blue")
plt.scatter(1,-1.9,marker=11, color="blue")

# Definition of d
plt.scatter(-1,0.1,marker=8, color="black")
plt.scatter(-0.1,0.1,marker=9, color="black")
plt.plot(np.linspace(-1,-0.1,5),np.zeros(5)+0.1, color="black")
plt.text(-0.5,0.2,"d", color="black")


plt.xticks([])
plt.yticks([])

plt.savefig("GRAPHS/def.png")

############################ Position nd ###############################################333


plt.figure()

# Axis
plt.plot(np.arange(-2,3),np.zeros(5), color="black")
plt.plot(np.zeros(5),np.arange(-2,3), color="black")

# Potentials

plt.plot(np.arange(-2,3),np.zeros(5)  , color="blue")
plt.plot(np.zeros(3),-np.arange(0,3)  , color="blue")
plt.plot(np.zeros(3)+1,-np.arange(0,3), color="blue")
plt.plot(np.zeros(3)-1,-np.arange(0,3), color="blue")

plt.scatter(0,-1.9,marker=11, color="blue")
plt.scatter(-1,-1.9,marker=11, color="blue")
plt.scatter(1,-1.9,marker=11, color="blue")

# Definition of d

plt.text(-1,0.2,"(n-1)d", color="black")
plt.text(0.05,0.2,"nd", color="black")
plt.text(1,0.2,"(n+1)d", color="black")

# Definition of A and B
plt.text(-0.5,-0.5,r"$A_{n-1}$")
plt.text(-0.5,-0.7,r"$B_{n-1}$")

plt.text(0.5,-0.5,r"$A_{n}$")
plt.text(0.5,-0.7,r"$B_{n}$")


plt.xticks([])
plt.yticks([])

plt.savefig("GRAPHS/def_n.png")


