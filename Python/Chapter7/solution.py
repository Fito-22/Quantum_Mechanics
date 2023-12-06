# Import libraries

import numpy as np
import matplotlib.pyplot as plt

# Plotting the function

y = np.linspace(-3.5,3.5,100)
k=1

plt.figure()
plt.plot(y,1/2 * k * y**2, color="blue")
plt.plot(np.zeros(9),[-3,-2,-1,0,1,2,3,4,5],color="black")
plt.plot([-5,-4,-3,-2,-1,0,1,2,3,4,5],np.zeros(11),color="black")
plt.xlabel("x=by")
plt.ylabel("V(x)")
plt.plot(y,np.ones(100),color="red")
plt.plot(y,np.ones(100)+1,color="red")
plt.plot(y,np.ones(100)+2,color="red")
plt.xticks([])
plt.yticks([])
plt.savefig("GRAPHS/sol.png")
