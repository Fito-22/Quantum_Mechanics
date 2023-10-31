"""
Code with the package vpython to try to simulate the motion of two bodies feeling a centrial force.

Created on Fall 2023

@author on: Adolfo Menendez

"""

# Import packages
from vpython import *
from time import *
import numpy as np
import math as m


# Physical magnitudes
r_s =           # Sun radious
r_e =           # Earth radious
r_aph =         # Aphelion
r_peri =        # Perihelion

# Make axes

def make_axes(length):
    x_axis = arrow(pos=vector(0,0,0), axis=length*vector(1,0,0), color=color.red)
    y_axis = arrow(pos=vector(0,0,0), axis=length*vector(0,1,0), color=color.blue)
    z_axis = arrow(pos=vector(0,0,0), axis=length*vector(0,0,1), color=color.green)
    return

make_axes(5)




# Create the sun:

sol = sphere(color = color.yellow, radio = r_s)

# Create the earth (Initial Conditions)

theta = np.linspace(0,2*m.pi,100)
rad_orbit = (r_aph + r_peri)/2
earth = sphere(radio = r_e, color = color.blue, pos=vector(rad_orbit*np.cos(theta[0]),rad_orbit*np.sin(theta[0]), 0))
i=0

while True:

    rate(10)
    i+=1
    if i == len(theta):
        i = 1
    # Create the movement of the ball
    earth.pos = vector(rad_orbit*cos(theta[i]), rad_orbit*sin(theta[i]), 0)
