"""
Code to plot the probabilty function among space of the measure of a static object.

Created on Fall 2023

@author on: Adolfo Menendez
"""

# Import libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
"""

1º Figure: Create a Gaussian function that simulate meassuring a particle in x = 0 by different people

"""

# Parameters for the Gaussian distribution
mu = 0  # Mean
sigma = 1  # Standard Deviation

# Generate x-values from -5 to 5
x = np.linspace(-5, 5, 100)

# Calculate the PDF (probability density function) values for the given x-values
pdf = norm.pdf(x, mu, sigma)

# Plot the Gaussian PDF
plt.plot(x, pdf, 'r-', lw=2)

# Customize the plot
plt.title('P(x)')
plt.xlabel('Value (x)')
plt.ylabel('PDF')
plt.savefig("GRAPHS/PDF_function.png")
