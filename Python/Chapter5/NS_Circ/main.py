# Import functions

import numpy as np
import matplotlib.pyplot as plt
from functions import *

################## AUXILIAR ####################################

beta=np.linspace(0.001,10,1000)
plt.figure()
plt.plot(beta,URHS(1,beta))
plt.plot(beta,np.ones(1000),color="red")
plt.plot(beta,-np.ones(1000),color="red")
plt.xlabel("beta")
plt.savefig("AUX/UnboundRHS")

######### Solutions for alpha (Bound States) ###############

### Continuous for infinite N ###

# d = 2
# alpha_array = np.linspace(0.1,5,100)
# E_l=[]
# N_l=[]
# tol = 1E-6
# for N in range(1,21):
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

# plt.figure("0")
# plt.scatter(N_l,E_l, color="black")
# plt.xlabel("N")
# plt.ylabel("E")
# plt.title("d=2")
# plt.savefig("GRAPHS/E_d=2_N.png")


### Behaviour for d ###

N = 100
alpha_array = np.linspace(0.1,7,100)
tol = 1E-6


E_lbound=[]
d_lbound=[]
for d in np.arange(1,4,0.1):
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
        # print(f"For k = {k}, d= {d}, alpha={sol[0]}")
        E_lbound.append(-sol[0]*sol[0])
        d_lbound.append(d)

# plt.savefig("GRAPHS/E_d_N=40.png")

######### Solutions for beta (Unbound States) ###############


### Continuous for infinite N ###

# d = 2
# alpha_array = np.linspace(0.1,5,100)
# E_l=[]
# N_l=[]
# tol = 1E-6
# nband=2

# for N in range(1,21):
#     count = 0
#     for k in range(N):
#             for i in range(len(alpha_array)):
#                 try:
#                     if func_bet(N,k,d,alpha_array[i+1]) * func_bet(N,k,d,alpha_array[i]) < 0:
#                         a = alpha_array[i]
#                         b = alpha_array[i+1]
#                         sol = bisection_bet(a,b,tol,d,N,k)
#                         E_l.append(sol[0]*sol[0])
#                         N_l.append(N)
#                         count+=1
#                         if count == nband: break
#                 except:
#                     sol = (0, 0)
#                     E_l.append(sol[0]*sol[0])
#                     N_l.append(N)
#             # print(f"For k = {k}, d= {d}, alpha={sol[0]}")

# E_sol = []
# N_sol = []

# for i in range(len(E_l)):
#     if E_l[i]!=0:
#         E_sol.append(E_l[i])
#         N_sol.append(N_l[i])


# plt.figure("0")
# plt.scatter(N_sol,E_sol, color="black")
# plt.xlabel("N")
# plt.ylabel("E")
# plt.title("d=2")
# plt.savefig("GRAPHS/Etotal_d=2_N.png")

### Behaviour for d ###

E_l=[]
d_l=[]
for d in np.arange(1,4,0.1):
    count = 0
    for k in range(N):
        for i in range(len(alpha_array)):
            try:
                if func_bet(N,k,d,alpha_array[i+1]) * func_bet(N,k,d,alpha_array[i]) < 0:
                    a = alpha_array[i]
                    b = alpha_array[i+1]
                    sol = bisection_bet(a,b,tol,d,N,k)
                    E_l.append(sol[0]*sol[0])
                    d_l.append(d)
                    count += 1
                    if count == 2: break
            except: break


plt.figure("1",figsize=(15,10))
plt.suptitle(f"N={N}")
plt.subplot(1,2,1)
plt.scatter(d_l,E_l,color="black")
plt.scatter(d_lbound,E_lbound,color="black")

plt.xlabel("d")
plt.ylabel("E")

plt.subplot(1,2,2)
plt.scatter(d_l,E_l,color="black")
plt.scatter(d_lbound,E_lbound,color="black")
plt.xlabel("d")
plt.ylim(-4,10)
plt.savefig(f"GRAPHS/Etotal_d_N={N}.png")
