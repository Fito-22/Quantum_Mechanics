# Import functions

import numpy as np
import matplotlib.pyplot as plt
from functions import *

######### Solutions for alpha (Bound States) ###############


# ### Continuous for infinite N ###

# d = 2
# alpha_array = np.linspace(0.1,5,100)
# E_l=[]
# N_l=[]
# tol = 1E-6
# for N in range(1,100):
#     for k in range(N):
#             if (LHS(N,k) < 1-d) : continue
#             for i in range(len(alpha_array)):
#                 try:
#                     if func_alp(N,k,d,alpha_array[i+1]) * func_alp(N,k,d,alpha_array[i]) < 0:
#                         a = alpha_array[i]
#                         b = alpha_array[i+1]
#                         sol = bisection(a,b,tol,d,N,k)
#                         break
#                 except: sol = (0, 0)
#             E_l.append(-sol[0]*sol[0])
#             N_l.append(N)
#             # print(f"For k = {k}, d= {d}, alpha={sol[0]}")

# plt.figure()
# plt.scatter(N_l,E_l, color="black")
# plt.xlabel("N")
# plt.ylabel("E")
# plt.title("d=2")
# plt.savefig("GRAPHS/E_d=2_N.png")


# ### Behaviour for d ###

# N = 40
# alpha_array = np.linspace(0.1,5,100)
# tol = 1E-6


# E_l=[]
# d_l=[]
# for d in np.arange(1,4,0.1):
#     for k in range(N):
#         if (LHS(N,k) < 1-d) : continue
#         for i in range(len(alpha_array)):
#             try:
#                 if func_alp(N,k,d,alpha_array[i+1]) * func_alp(N,k,d,alpha_array[i]) < 0:
#                     a = alpha_array[i]
#                     b = alpha_array[i+1]
#                     sol = bisection(a,b,tol,d,N,k)
#                     break
#             except: sol = (0, 0)
#         print(f"For k = {k}, d= {d}, alpha={sol[0]}")
#         E_l.append(-sol[0]*sol[0])
#         d_l.append(N)
# plt.figure()
# plt.scatter(d_l,E_l,color="black")
# plt.xlabel("d")
# plt.ylabel("E")
# plt.title("N=40")
# plt.savefig("GRAPHS/E_d_N=40.png")

######### Solutions for beta (Unbound States) ###############


### Continuous for infinite N ###

d = 2
alpha_array = np.linspace(0.1,100,1000)
E_l=[]
N_l=[]
tol = 1E-6
nband=2
for N in range(1,10):
    count = 0
    for k in range(N):
            for i in range(len(alpha_array)):
                try:
                    if func_bet(N,k,d,alpha_array[i+1]) * func_bet(N,k,d,alpha_array[i]) < 0:
                        a = alpha_array[i]
                        b = alpha_array[i+1]
                        sol = bisection_bet(a,b,tol,d,N,k)
                        E_l.append(sol[0]*sol[0])
                        N_l.append(N)
                        count+=1
                        if count == nband: break
                except:
                    sol = (0, 0)
                    E_l.append(sol[0]*sol[0])
                    N_l.append(N)
    print(N)
            # print(f"For k = {k}, d= {d}, alpha={sol[0]}")

plt.figure()
plt.scatter(N_l,E_l, color="black")
plt.xlabel("N")
plt.ylabel("E")
plt.ylim(0,2000)
plt.title("d=2")
plt.savefig("GRAPHS/Eunbound_d=2_N.png")
