# Import libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from function import *


# Define our parameters
N=40
d=2
alpha_array = np.linspace(1e-6,2,10000)
tol = 1e-8

################ Some tests with the Matrix class #################

# mat = Matrix(2,0,0,2)
# T = mat.power(N)
# T.print_mat()

################ Solving the real problem for a fix d,N #################

alpha_old = 1e-6
count = 0
for alpha in alpha_array:
    if count == N : break
    mat_old = Matrix(T_11_init(d,alpha_old),T_12_init(alpha_old),T_21_init(alpha_old),T_22_init(d,alpha_old))
    mat_old_N = mat_old.power(N)

    mat = Matrix(T_11_init(d,alpha),T_12_init(alpha),T_21_init(alpha),T_22_init(d,alpha))
    mat_N = mat.power(N)

    if (mat_old_N.bb * mat_N.bb) < 0:
        count += 1
        a = alpha_old
        b = alpha
        sol = bisection(a,b,tol,d,N)
        print(count, sol)
    else: continue

    alpha_old = alpha

################ Solving the real problem for multiple N #################

plt.figure()
for N in range(2,41,2):
    alpha_old = 1e-6
    count = 0
    for alpha in alpha_array:
        if count == N : break
        mat_old = Matrix(T_11_init(d,alpha_old),T_12_init(alpha_old),T_21_init(alpha_old),T_22_init(d,alpha_old))
        mat_old_N = mat_old.power(N)

        mat = Matrix(T_11_init(d,alpha),T_12_init(alpha),T_21_init(alpha),T_22_init(d,alpha))
        mat_N = mat.power(N)

        if (mat_old_N.bb * mat_N.bb) < 0:
            count += 1
            a = alpha_old
            b = alpha
            sol = bisection(a,b,tol,d,N)
            # print(N, count)
            plt.scatter(N,sol[0], color="black")
        else: continue

        alpha_old = alpha
plt.title(f"d={d}")
plt.xlabel("N")
plt.ylabel("alpha")
plt.savefig(f"GRAPHS/N_alpha_d={d}.png")
