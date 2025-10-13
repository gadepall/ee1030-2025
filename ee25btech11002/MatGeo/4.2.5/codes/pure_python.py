import numpy as np
import matplotlib.pyplot as plt

# The equation of the line is 2x = -5y, which can be rewritten as 2x + 5y = 0.

# --- 1. Define the Normal and Direction Vectors ---
# For a line Ax + By + C = 0, the normal vector is (A, B).
normal_vector = np.array([2, 5])
normal = np.array([0.4 , 1])
# The direction vector is perpendicular to the normal vector.
# If n = (A, B), the direction vector d can be (-B, A).
direction_vector = np.array([-5, 2])
direction = np.array([1 , -0.4])
# --- 2. Generate points to plot the line ---
# From the equation 2x + 5y = 0, we can express y as y = (-2/5)x.
# We will generate a set of x-values to find the corresponding y-values.
x_vals = np.linspace(-10, 10, 100)
y_vals = (-2/5) * x_vals

# --- 3. Create the plot ---
plt.figure(figsize=(9, 9))
ax = plt.gca()

# Plot the line itself
plt.plot(x_vals, y_vals, label='Line: 2x + 5y = 0', color='blue', zorder=1)

# Plot the normal and direction vectors starting from the origin (0,0)
# We use plt.quiver to draw arrows.
origin = [0], [0]
plt.quiver(*origin, normal_vector[0], normal_vector[1], 
           angles='xy', scale_units='xy', scale=1, 
           color='red', label=f'Normal Vector: [0.4 , 1]')

plt.quiver(*origin, direction_vector[0], direction_vector[1], 
           angles='xy', scale_units='xy', scale=1, 
           color='green', label=f'Direction Vector: [1 , -0.4]')


# --- 4. Format the plot for clarity ---
# Set the limits for the x and y axes
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Ensure the aspect ratio is equal, so perpendicular lines look correct
plt.axis('equal')

# Move the x and y axes to the center to mimic a Cartesian plane
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Add labels, a title, a legend, and a grid
plt.xlabel('x-axis', fontsize=12)
plt.ylabel('y-axis', fontsize=12, rotation=0)
ax.xaxis.set_label_coords(1.05, 0.51)
ax.yaxis.set_label_coords(0.51, -0.05)
plt.title('Direction and Normal Vector for the Line 2x = -5y', fontsize=14)
plt.legend(loc='best')
plt.grid(True)

# Display the plot
plt.show()