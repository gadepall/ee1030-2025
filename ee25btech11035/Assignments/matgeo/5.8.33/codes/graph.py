import numpy as np
import matplotlib.pyplot as plt

# --- 1. Define the equations and vertices ---

# Create a range of x-values for the plot
x = np.linspace(-1, 6, 400)

# Define the two lines by solving for y
# y = 5x - 5
y1 = 5*x - 5
# y = 3x - 3
y2 = 3*x - 3

# Define the coordinates of the triangle's vertices
vertices = np.array([
    [1, 0],   # Intersection of the two lines
    [0, -5],  # Intersection of y=5x-5 and y-axis
    [0, -3]   # Intersection of y=3x-3 and y-axis
])
x_coords = vertices[:, 0]
y_coords = vertices[:, 1]

# --- 2. Create the plot ---
plt.figure(figsize=(8, 8))

# Plot the two lines
plt.plot(x, y1, label='$5x - y = 5$')
plt.plot(x, y2, label='$3x - y = 3$')

# Plot the y-axis
plt.axvline(0, color='black', linestyle='--', label='y-axis (x=0)')

# Plot and label the vertices
plt.plot(x_coords, y_coords, 'ro', markersize=8)
for i, (vx, vy) in enumerate(vertices):
    plt.text(vx + 0.1, vy, f'({int(vx)}, {int(vy)})', fontsize=12, va='center')

# Fill the triangle area
plt.fill(x_coords, y_coords, 'yellow', alpha=0.3, label='Triangle Area')

# --- 3. Formatting ---
plt.title('Triangle Formed by Lines and y-axis', fontsize=16)
plt.xlabel('x-axis', fontsize=12)
plt.ylabel('y-axis', fontsize=12)
plt.axhline(0, color='grey', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.xlim(-1, 5)
plt.ylim(-6, 4)
plt.gca().set_aspect('equal', adjustable='box')

# Save and show the plot
plt.savefig('2.png')
plt.show()