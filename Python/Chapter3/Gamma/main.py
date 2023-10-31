# Import libraries and functions
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from functions import *                              # import the functions from funtions.py


# Define gamma, N, a empty list for solutions and functions.

mode = input("Select Mode: Single or Multiple \n")

if (mode == "Single"):

    """
    This mode return all the solutions of beta and alpha for the gamma given.
    Also it allows you to select one alpha and plot phi(x) and P(x) for that alpha
    """

    print("Single \u03B3 mode selected \n")

    gamma = float(input("Give the value for gamma: "))     # Gamma given by the user

    beta_l,alpha_l = solutions_gamma(gamma=gamma,mode=mode)

    index = int(input("\n For wich alpha do you want to plot ? \n")) - 1

    ################### PLOT P(X) #################################################3
    """Now we will plot for phi(x) and P(x) for this alpha"""

    alpha = alpha_l[index]
    beta = beta_l[index]
    n = index

    # Define the intervals

    a = 1 # Is the same as saying y=x/a and plot everything for P(y)
    x_1 = np.linspace(-5,-a,1000)    # x < -a
    x_2 = np.linspace(-a,a,1000)     # -a < x < a
    x_3 = np.linspace(a,5,1000)      # x > a

    if ( n == 0) or (n % 2 == 0) :
        # B=0
        # Define A,B,C and D
        B = 0
        C = np.sqrt((alpha*np.exp(2*alpha))/(a*(1+alpha)))
        A = C*np.cos(beta)
        D = A

        # Define the functions in different intervals
        phi_1_C = D * np.exp(alpha*x_1/a)                     # x < a
        phi_2_C = C * np.exp(-alpha) * np.cos(beta*x_2/a)     # -a < x < a
        phi_3_C = A * np.exp(-alpha*x_3/a)                    # x > a

        # Create the figure
        plt.figure(figsize=(15,10))
        plt.subplot(1,2,1)
        plt.plot(x_1,phi_1_C)
        plt.plot(x_2,phi_2_C)
        plt.plot(x_3,phi_3_C)
        plt.xlabel("x")
        plt.ylabel(r"$\phi(x)$")
        plt.xlim(-2,2)

        plt.subplot(1,2,2)
        plt.plot(x_1,phi_1_C*phi_1_C)
        plt.plot(x_2,phi_2_C*phi_2_C)
        plt.plot(x_3,phi_3_C*phi_3_C)
        plt.xlabel("x")
        plt.ylabel(r"$P(x)$")
        plt.xlim(-2,2)

        plt.suptitle(fr"B=0, $\gamma={round(gamma,2)}$, $\alpha=${round(alpha,2)}")
        plt.savefig(f"Gamma/Graphs/phi_gamma={round(gamma,2)}_alpha={round(alpha,2)}.png")

    else:
        # C=0
        # Define A,B,C and D
        B = np.sqrt((alpha*np.exp(2*alpha))/(a*(1+alpha)))
        C = 0
        A = B*np.sin(beta)
        D = -A

        # Define the functions in different intervals
        phi_1_B = D * np.exp(alpha*x_1/a)                     # x < a
        phi_2_B = B * np.exp(-alpha) * np.sin(beta*x_2/a)     # -a < x < a
        phi_3_B = A * np.exp(-alpha*x_3/a)                    # x > a

        # Create the figure
        plt.figure(figsize=(15,10))
        plt.subplot(1,2,1)
        plt.plot(x_1,phi_1_B)
        plt.plot(x_2,phi_2_B)
        plt.plot(x_3,phi_3_B)
        plt.xlabel("x")
        plt.ylabel(r"$\phi(x)$")
        plt.xlim(-2,2)

        plt.subplot(1,2,2)
        plt.plot(x_1,phi_1_B*phi_1_B)
        plt.plot(x_2,phi_2_B*phi_2_B)
        plt.plot(x_3,phi_3_B*phi_3_B)
        plt.xlabel("x")
        plt.ylabel(r"$P(x)$")
        plt.xlim(-2,2)

        plt.suptitle(fr"C=0, $\gamma={round(gamma,2)}$, $\alpha=${round(alpha,2)}")
        plt.savefig(f"Gamma/Graphs/phi_gamma={round(gamma,2)}_alpha={round(alpha,2)}.png")


    print("Plot printed")

elif(mode=="Multiple"):
    """
    This mode allow you to get all the solutions for different gammas and create a plot alpha as a function of gamma
    """
    print("Multiple \u03B3 mode selected \n")
    gamma_start = float(input("Please introduce the starting value for gamma: "))
    gamma_last = float(input("Please introduce the last value for gamma: "))
    gamma_num = int(input("Please introduce the number of gammas for the calculation: "))

    gamma_array = np.linspace(gamma_start,gamma_last,gamma_num)

    plt.figure()
    for gamma in gamma_array:
        beta, alpha = solutions_gamma(gamma=gamma,mode=mode)
        plt.scatter(np.ones(len(alpha))*gamma,alpha, color="black", marker="o")
    plt.xlabel("\u03B3")
    plt.ylabel("α")
    plt.savefig("Gamma/alpha_gamma.png")
    plt.ylim(0,100)

else: print(f"Error. MODE:{mode} not found")
