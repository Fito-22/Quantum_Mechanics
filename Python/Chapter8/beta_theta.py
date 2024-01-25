"""

Code by Alexander Lohr

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# Define the functions
def my_function1(x, a):
    return np.sqrt((1 + np.sqrt(1-1/a**2) * np.sin(2*np.arctan((1/a)*np.tan(x))))*a)*np.cos(x)

def my_function2(x, a):
    return np.sqrt((1 + np.sqrt(1-1/a**2) * np.sin(2*np.arctan((1/a)*np.tan(x))))*a)*np.sin(x)

# Set up the figure and axis
fig, ax = plt.subplots()
x_values = np.linspace(0, 2*np.pi, 1000)  # Larger x-axis limit

# Initialize the plot with a=1
l_values = my_function1(x_values, 1)
y_values = my_function2(x_values, 1)
line, = ax.plot(l_values, y_values, label=f'Function: a=1')

# Add labels, title, legend, and grid
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Animated Graph of the Function')
ax.legend()
ax.grid(True)

plt.figure()
for i in [1,10,100]:
    plt.plot(my_function1(x_values,i),my_function2(x_values,i),label=f'a={i}')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title("Motion of the particle")
plt.savefig("GRAPHS/beta_theta.png")





# # Animation function
# def update(frame):
#     a_value = (frame+1)
#     line.set_data(my_function1(x_values, a_value), my_function2(x_values, a_value))
#     line.set_label(f'Function: a={a_value}')
#     ax.legend()

# # Create the animation
# animation = anim.FuncAnimation(fig, update, frames=100, interval=100)

# # Set larger x-axis and y-axis limits
# ax.set_xlim([-50, 50])  # Adjust as needed
# ax.set_ylim([-50, 50])  # Adjust as needed

# # Show the plot
# anim.Animation.save(animation,'beta_theta.gif', writer='ffmpeg')

# Plot the graph
