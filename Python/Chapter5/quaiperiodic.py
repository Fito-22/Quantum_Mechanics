# Import libraries

import numpy as np
import matplotlib.pyplot as plt


################# -d/2 ----- d/2 ######################################

plt.figure()

# Axis

plt.scatter(-1.8,0,marker="|", color="black")
plt.scatter(1.8,0,marker="|", color="black")

# Potential
plt.plot(np.arange(-2,3),np.zeros(5)  , color="blue")
plt.plot(np.zeros(3),-np.arange(0,3)  , color="blue")

plt.scatter(0,-1.9,marker=11, color="blue")
plt.plot(np.arange(-2,3),np.zeros(5), color="black")
plt.plot(np.zeros(5),np.arange(-2,3), color="black")

# Text
plt.text(-2,-0.2,"-d/2", color="black")
plt.text(1.8,-0.2,"d/2", color="black")
plt.text(0.1,-2,"V(x)", color="black")

plt.savefig("GRAPHS/quasiperf.png")
