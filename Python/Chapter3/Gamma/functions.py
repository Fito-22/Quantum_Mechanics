# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Functions needed for solutions

def alpha_gamma(gamma,beta):
    return np.sqrt(gamma**2-beta**2)

def alpha_tan(beta):
    return beta * np.tan(beta)

def alpha_cotan(beta):
    return - beta * 1/(np.tan(beta))



def bisection(a : float,b : float,f,tol: float, gamma: float):

    x_0 = (a+b)/2
    while(abs(a-b)>tol):

        if(f(a,gamma)*f(x_0,gamma)>0):
            a=x_0
        else:
            b=x_0

        x_0 = (a+b)/2
    return x_0

def f_tan(beta, gamma):
    return alpha_gamma(gamma,beta)-alpha_tan(beta)

def f_cotan(beta, gamma):
    return alpha_gamma(gamma,beta)-alpha_cotan(beta)


def solutions_gamma(gamma, mode):

    N = int(np.ceil(gamma/(np.pi/2)))                    # Number of beta arrays needed, for every N we get 2 solutions for alpha

    tol = 1e-8
    d_beta = 0.01

    beta_solutions = []
    alpha_solutions = []
    print(f"The number of solutions is going to be {N}")

    for n in range(N):

        beta = 1e-5 + np.pi/2 * n
        if ( n == 0) or (n % 2 == 0) :
            # B=0
            while(f_tan(beta,gamma)>0):
                a = beta
                beta += d_beta
            b = beta

            beta_sol = bisection(a,b,f_tan,tol,gamma)
            alpha_sol = alpha_tan(beta_sol)

            beta_solutions.append(beta_sol)
            alpha_solutions.append(alpha_sol)
        else:
            # C=0
            while(f_cotan(beta,gamma)>0):
                a = beta
                beta += d_beta
            b = beta

            beta_sol = bisection(a,b,f_cotan,tol,gamma)
            alpha_sol = alpha_cotan(beta_sol)

            beta_solutions.append(beta_sol)
            alpha_solutions.append(alpha_sol)

        if mode == "Single":
            print(f"\u03B2{n+1}={beta_sol}, α{n+1}={alpha_sol}, \u03B3{n+1}={beta_sol**2+alpha_sol**2}, E{n+1}={alpha_sol**2}")

    return beta_solutions, alpha_solutions
