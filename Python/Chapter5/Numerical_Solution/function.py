# Import libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Functions of our matrix T

def T_11_init(d,alpha):
    return (np.exp(-alpha*d/2))**2*(1+1/alpha)

def T_12_init(alpha):
    return 1/alpha

def T_21_init(alpha):
    return -1/alpha

def T_22_init(d,alpha):
    return (1/((np.exp(-alpha*d/2))**2)) * (1-1/alpha)


# Definition of our class Matrix
class Matrix():

    def __init__(self,M_11,M_12,M_21,M_22):
        self.aa = M_11
        self.ab = M_12
        self.ba = M_21
        self.bb = M_22

    def power(self,N):
        """ Power N of a matrix """
        new=self
        for i in range(N-1):
            new = mat_prod(new,self)
        return new

    def print_mat(self):
        print(f"{self.aa}  {self.ab}\n{self.ba}  {self.bb}")
        return 1

def mat_prod(mat_1: Matrix ,mat_2: Matrix):

    """ Definition of the Matrix product"""

    M_11 = mat_1.aa * mat_2.aa + mat_1.ab * mat_2.ba
    M_12 = mat_1.aa * mat_2.ab + mat_1.ab * mat_2.bb
    M_21 = mat_1.ba * mat_2.aa + mat_1.bb * mat_2.ba
    M_22 = mat_1.ba * mat_2.ab + mat_1.bb * mat_2.bb
    return Matrix(M_11,M_12,M_21,M_22)

# Defining the method to find the solutions for alpha

def bisection(a : float, b : float, tol: float, d: float, N: int):
    """
    This definition of the bisection process is not general. Is special for this case in particular
    """

    mat_a   = Matrix(T_11_init(d,a), T_12_init(a), T_21_init(a), T_22_init(d,a))
    mat_a_N = mat_a.power(N)
    f_a     = mat_a_N.bb

    x0 = (a+b)/2
    mat_x0   = Matrix(T_11_init(d,x0), T_12_init(x0), T_21_init(x0), T_22_init(d,x0))
    mat_x0_N = mat_x0.power(N)
    f_x0     = mat_x0_N.bb

    while(abs(f_a-f_x0)>tol):
        x0 = (a+b)/2
        mat_x0   = Matrix(T_11_init(d,x0), T_12_init(x0), T_21_init(x0), T_22_init(d,x0))
        mat_x0_N = mat_x0.power(N)
        f_x0     = mat_x0_N.bb

        mat_a   = Matrix(T_11_init(d,a), T_12_init(a), T_21_init(a), T_22_init(d,a))
        mat_a_N = mat_a.power(N)
        f_a     = mat_a_N.bb

        if(f_a*f_x0>0):
            a=x0
        else:
            b=x0


    return x0, mat_x0_N.bb
