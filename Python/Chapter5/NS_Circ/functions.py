# Import functions

import numpy as np
import matplotlib.pyplot as plt

def RHS(d,alpha):
    return np.cosh(alpha*d) - 1/alpha * np.sinh(alpha*d)

def LHS(N: int, k: int):
    return np.cos(2*np.pi*k/N)

def func_alp(N,k,d,alpha):
    return LHS(N,k) - RHS(d,alpha)


def bisection(a : float, b : float, tol: float, d: float, N: int, k: int):
    """
    This definition of the bisection process is not general. Is special for this case in particular
    """

    while(abs(func_alp(N,k,d,a) - func_alp(N,k,d,b))>tol):
        x0 = (a+b)/2
        if(func_alp(N,k,d,a)*func_alp(N,k,d,x0)>0):
            a=x0
        else:
            b=x0
    return x0, func_alp(N,k,d,x0)
