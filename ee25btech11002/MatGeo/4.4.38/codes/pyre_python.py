import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Define the points and vectors from the problem ---

# The required line passes through the midpoint h(3, 4, 6)
h = np.array([3, 4, 6])

# --- Information for the two given lines ---

# Line 1: Passes through P1(8, -19, 10) with direction vector m1(3, -16, 7)
p1 = np.array([8, -19, 10])
m1 = np.array([3, -16, 7])

# Line 2: Passes through P2(15, 29, 5) with direction vector m2(3, 8, -5)
p2 = np.array([15, 29, 5])
m2 = np.array([3, 8, -5])

# --- Information for the required line (the solution) ---

# The direction vector of the required line is m(2, 3, 6)
m_solution = np.array([2, 3, 6])

# --- 2. Setup the 3D plot ---
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# --- 3. Generate and plot the lines and points ---

# Plot the midpoint h
ax.scatter(h[0], h[1], h[2], color='green', s=150, label='Midpoint h (3, 4, 6)', zorder=5)

# Generate points for and plot the two given lines
t = np.linspace(-1.5, 1.5, 100)
line1_points = np.array([p1 + val * m1 for val in t])
line2_points = np.array([p2 + val * m2 for val in t])
ax.plot(line1_points[:, 0], line1_points[:, 1], line1_points[:, 2], color='orange', label='Given Line 1')
ax.plot(line2_points[:, 0], line2_points[:, 1], line2_points[:, 2], color='purple', label='Given Line 2')

# Generate points for and plot the required line (the solution)
# Use a larger range for 't' to make this line longer and more prominent
t_solution = np.linspace(-7, 7, 100)
solution_line_points = np.array([h + val * m_solution for val in t_solution])
ax.plot(solution_line_points[:, 0], solution_line_points[:, 1], solution_line_points[:, 2], color='red', linewidth=3, label='Required Line (Solution)')

# --- 4. Formatting the plot ---
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
ax.set_zlabel('Z-axis', fontsize=12)
ax.set_title('Visualization of Line Bisecting a Segment and Perpendicular to Two Lines', fontsize=16)

# Add a legend to identify the different elements
ax.legend()

# Add a grid for better visualization
ax.grid(True)

# Set aspect ratio to be equal
ax.set_box_aspect([1,1,1])

# Display the plot
plt.show()