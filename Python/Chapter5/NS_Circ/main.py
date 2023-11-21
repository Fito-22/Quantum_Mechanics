# Import functions

import numpy as np
import matplotlib.pyplot as plt
from functions import *

######### Solutions for alpha (Bound States) ###############

N = 40
alpha_array = np.linspace(0.1,5,100)
tol = 1E-6

for d in np.arange(0.1,4,0.1):
    for k in range(N):
        if (LHS(N,k) < 1-d) : continue
        for i in range(len(alpha_array)):
            try:
                if func_alp(N,k,d,alpha_array[i+1]) * func_alp(N,k,d,alpha_array[i]) < 0:
                    a = alpha_array[i]
                    b = alpha_array[i+1]
                    sol = bisection(a,b,tol,d,N,k)
                    break
            except: sol = (0, 0)
        print(f"For k = {k}, d= {d}, alpha={sol[0]}")

