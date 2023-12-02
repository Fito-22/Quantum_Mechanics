# Import libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from function import *


# Define our parameters
N=60
d=2
alpha_array = np.arange(0.01,2,0.001)
tol = 1e-6

################ Some tests with the Matrix class #################

# mat = Matrix(2,0,0,2)
# T = mat.power(N)
# T.print_mat()

################ Solving the real problem for a fix d,N #################

alpha_old = 0.001
count = 0
for alpha in alpha_array:
    if count == N : break
    mat_old = T(alpha_old,d,N)
    mat = T(alpha,d,N)

    if (mat_old * mat) < 0:
        count += 1
        a = alpha_old
        b = alpha
        sol = bisection_eff(a,b,N,d,tol)
        # print(count, sol)
    else: continue

    alpha_old = alpha

################ Solving the real problem for multiple N #################

E_sol=[]
alpha_sol=[]
N_sol=[]

for N in range(1,60,1):
    alpha_old = 0.001
    for alpha in alpha_array:
        if count == N : break
        mat_old = T(alpha_old,d,N)
        mat = T(alpha,d,N)
        if (mat_old * mat) < 0:
            a = alpha_old
            b = alpha
            sol = bisection_eff(a,b,N,d,tol)
            alpha_sol.append(sol[0])
            E_sol.append(-sol[0]**2)
            N_sol.append(N)
        else: continue
        alpha_old = alpha
    print(N)

plt.figure("alpha")
plt.scatter(N_sol,alpha_sol,color="black")
plt.title(f"d={d}")
plt.xlabel("N")
plt.ylabel("alpha")
plt.savefig(f"GRAPHS/N_alpha_d_eff={d}.png")

plt.figure("E")
plt.scatter(N_sol,E_sol,color="black")
plt.title(f"d={d}")
plt.xlabel("N")
plt.ylabel("E")
plt.savefig(f"GRAPHS/N_E_d_eff={d}.png")
