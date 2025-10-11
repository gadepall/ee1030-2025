import numpy as np
import matplotlib.pyplot as plt

# Define the line y = x
x_vals = np.linspace(-5, 5, 100)
y_vals = x_vals

# Normal and direction vectors
normal_vec = np.array([1, -1])
direction_vec = np.array([1, 1])

# Choose a point on the line (origin for simplicity)
point = np.array([0, 0])

# Create the plot
plt.figure(figsize=(6,6))
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis

# Plot the line
plt.plot(x_vals, y_vals, 'b', label='y = x')

# Plot the direction vector (along the line)
plt.quiver(point[0], point[1],
           direction_vec[0], direction_vec[1],
           angles='xy', scale_units='xy', scale=1, color='green')
plt.text(direction_vec[0]/2, direction_vec[1]/2, 'Direction (1,1)', color='green')

# Plot the normal vector (perpendicular to the line)
plt.quiver(point[0], point[1],
           normal_vec[0], normal_vec[1],
           angles='xy', scale_units='xy', scale=1, color='red')
plt.text(normal_vec[0]/2, normal_vec[1]/2, 'Normal (1,-1)', color='red')

# Formatting
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.axis('equal')
plt.grid(True)
plt.title('Line y=x with Direction and Normal Vectors')
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/4.2.13/figs/q6.png")
plt.show()
