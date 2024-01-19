import numpy as np
import matplotlib.pyplot as plt

# Define the function P_i(u,v)
def P_0(u, v):
    return 1/np.pi * np.exp(-u**2 - v**2)
def P_1_0(u,v):
    return 2/np.pi * u**2 * np.exp(-u**2 - v**2)
def P_0_1(u,v):
    return 2/np.pi * v**2 * np.exp(-u**2 - v**2)

# Generate u and v values
u = np.linspace(-2, 2, 100)
v = np.linspace(-2, 2, 100)
u, v = np.meshgrid(u, v)

# Calculate P_i(u,v) values
P0 = P_0(u, v)
P10 = P_1_0(u,v)
P01 = P_0_1(u,v)

# Create a 3D plot for P_0(u,v)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(u, v, P0)

# Set labels and title
ax.set_xlabel('u')
ax.set_ylabel('v')
ax.set_zlabel(r'$P_{0,0}(u,v)$')
ax.set_title(r'Plot of $P_{0,0}(u,v)$')

# Show the plot
plt.savefig('GRAPHS/P_0,0.png')

# Create a 3D plot for P_1_0(u,v)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(u, v, P10)

# Set labels and title
ax.set_xlabel('u')
ax.set_ylabel('v')
ax.set_zlabel(r'$P_{1,0}(u,v)$')
ax.set_title(r'Plot of $P_{1,0}(u,v)$')

# Show the plot
plt.savefig('GRAPHS/P_1,0.png')

# Create a 3D plot for P_0_1(u,v)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(u, v, P01)

# Set labels and title
ax.set_xlabel('u')
ax.set_ylabel('v')
ax.set_zlabel(r'$P_{0,1}(u,v)$')
ax.set_title(r'Plot of $P_{0,1}(u,v)$')

# Show the plot
plt.savefig('GRAPHS/P_0,1.png')


# In polar coordinates:

# Define the function P_i(r,theta)

def P_1_0_r(r,theta):
    return 1/np.pi * np.sin(theta)**2 * r**2 *np.exp(-r**2)
def P_0_1_r(r,theta):
    return 1/np.pi * np.cos(theta)**2 * r**2 *np.exp(-r**2)


r = np.linspace(0, 5, 100)
theta = np.linspace(0, 2*np.pi, 100)
r, theta = np.meshgrid(r, theta)

# Calculate P_i(r,theta) values
P10 = P_1_0_r(r,theta)
P01 = P_0_1_r(r,theta)

# Create a 3D plot for P_1_0(r,theta)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(r, theta, P10)

# Set labels and title
ax.set_xlabel('r')
ax.set_ylabel('theta')
ax.set_zlabel(r'$P_{1,0}(r,\theta)$')
ax.set_title(r'Plot of $P_{1,0}(r,\theta)$')

# Show the plot
plt.savefig('GRAPHS/P_1,0(r).png')

# Create a 3D plot for P_0_1(r,theta)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(r, theta, P01)

# Set labels and title
ax.set_xlabel('r')
ax.set_ylabel('theta')
ax.set_zlabel(r'$P_{0,1}(r,\theta)$')
ax.set_title(r'Plot of $P_{0,1}(r,\theta)$')

# Show the plot
plt.savefig('GRAPHS/P_0,1(r).png')
