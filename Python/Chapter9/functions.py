"""

ALL THIS CODE WAS GIVE IT TO ME BY ALEX LOHR, CLASSMATE IN QUANTUM MECHANICS II IN FIU

"""

import numpy as np
import scipy.special as spe
import matplotlib.pyplot as plt


n = 2
l = 0
m = 0

s = 50  # Number of steps
render_radius_factor = 100

def R(r, n=n, l=l):
    coeff = np.sqrt((2.0 / n)**3 * spe.factorial(n - l - 1) / (2.0 * n * spe.factorial(n + l)))
    laguerre = spe.assoc_laguerre(2.0 * r / n, n - l - 1, 2 * l + 1)
    return coeff * np.exp(-r / n) * (2.0 * r / n)**l * laguerre

def psi(n, l, m, r, azimuth, zenith):
    return spe.sph_harm(m, l, azimuth, zenith) * R(r)

def prob(res):
    return np.absolute(res)**2

def cartesian_prob(n, l, m, x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    azimuth = np.arctan2(y, x)
    zenith = np.arctan2(np.sqrt(x**2 + y**2), z)
    return prob(psi(n, l, m, r, azimuth, zenith))

def get_render_radius(n, l):
    render_radius = render_radius_factor * n
    current_radius = 0
    check_step = render_radius / 50
    max_R = 0

    while current_radius < render_radius:
        curr_R = R(current_radius, n, l)**2
        for_R = R(current_radius + check_step, n, l)**2
        max_R = max(curr_R, for_R, max_R)
        if for_R - curr_R > 0:
            current_radius += check_step
            render_radius = render_radius_factor * current_radius
        else:
            current_radius += check_step

    while R(render_radius, n, l)**2 < max_R / 100000:
        render_radius -= render_radius * 0.01

    return render_radius

def render_3d_surface(n, l, m):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim(-30, 30)  # Example range for x-axis
    ax.set_ylim(-30, 30)  # Example range for y-axis
    ax.set_zlim(-30, 30)  # Example range for z-axis

    for y in range(-60, 65, 1):
        render_radius = get_render_radius(n, l)
        step = 2 * render_radius / s
        x_vals = np.linspace(-render_radius, render_radius, s+1)
        z_vals = np.linspace(-render_radius, render_radius, s+1)

        X, Z = np.meshgrid(x_vals, z_vals)
        Y = np.ones_like(X) * y

        probabilities = cartesian_prob(n, l, m, X, Y, Z)
        mask = probabilities >= 0.00001  # Create a mask for points with probability >= 0.1
        ax.scatter(X[mask], Y[mask], Z[mask], c=probabilities[mask],  marker='o', alpha=0.5)

    ax.set_title('3D Plot of a (' + str(n) + ', ' + str(l) + ', ' + str(m) + ') Hydrogen Orbital')
    ax.set_xlabel(r'x ($a_{0}$)')
    ax.set_ylabel(r'y ($a_{0}$)')
    ax.set_zlabel(r'z ($a_{0}$)')
    # plt.colorbar(cm.ScalarMappable(), label='Probability')
    plt.savefig(f"images/3d_plot_{n},{l},{m}.png")

render_3d_surface(n, l, m)
