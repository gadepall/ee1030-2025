import numpy as np
import matplotlib.pyplot as plt

# --- 1. Setup the 3D plot ---
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Visualization of Intersecting Planes", fontsize=16)

# --- 2. Define the grid for the planes ---
# Create a grid of x and y values
x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)

# --- 3. Define and Plot the Three Planes ---

# Plane 1: r . (i + j + k) = 1  =>  x + y + z = 1
Z1 = 1 - X - Y
ax.plot_surface(X, Y, Z1, alpha=0.6, cmap='viridis', label='Plane 1: x+y+z=1')

# Plane 2: r . (2i + 3j - k) + 4 = 0  =>  2x + 3y - z = -4
Z2 = 2*X + 3*Y + 4
ax.plot_surface(X, Y, Z2, alpha=0.6, cmap='plasma', label='Plane 2: 2x+3y-z=-4')

# Resulting Plane: y - 3z + 6 = 0
# NOTE: This plane is parallel to the x-axis, so X is not in its equation.
# We define the grid differently for visualization purposes.
y_res = np.linspace(-10, 10, 50)
z_res = np.linspace(-10, 10, 50)
Y_res, Z_res = np.meshgrid(y_res, z_res)
# Equation: y - 3z + 6 = 0 => y = 3z - 6. We don't need X here.
# To plot it, we create a constant X grid.
X_res = (3*Z_res - Y_res) * 0 # This is a trick to get a 0-filled grid of the right shape
# However, a better way to show a plane parallel to an axis is to use that axis
# in the meshgrid. Let's create a grid of x and z values instead.
x_res, z_res = np.meshgrid(np.linspace(-10,10,50), np.linspace(-5,5,50))
Y_res = 3*z_res - 6 # y - 3z + 6 = 0  =>  y = 3z - 6
ax.plot_surface(x_res, Y_res, z_res, alpha=0.7, color='cyan', label='Result: y-3z+6=0')

# --- 4. Calculate and Plot the Line of Intersection ---
# Parametric equation for the line of intersection of Plane 1 and 2
t = np.linspace(-10, 10, 100)
x_line = t
y_line = (-3 - 3*t) / 4
z_line = (7 - t) / 4
ax.plot(x_line, y_line, z_line, color='red', lw=4, label='Line of Intersection')

# --- 5. Plot the X-axis to show parallelism ---
ax.plot([-15, 15], [0, 0], [0, 0], color='black', lw=3, linestyle='--', label='X-axis')

# --- 6. Formatting the Plot ---
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Set viewing angle for better perspective
ax.view_init(elev=20, azim=-50)

# Create proxy artists for the legend since plot_surface doesn't directly support labels
import matplotlib.patches as mpatches
p1 = mpatches.Patch(color='green', label='Plane 1: x+y+z=1', alpha=0.6)
p2 = mpatches.Patch(color='orange', label='Plane 2: 2x+3y-z=-4', alpha=0.6)
p3 = mpatches.Patch(color='cyan', label='Result: y-3z+6=0', alpha=0.7)
from matplotlib.lines import Line2D
l1 = Line2D([0], [0], color='red', lw=4, label='Line of Intersection')
l2 = Line2D([0], [0], color='black', lw=3, linestyle='--', label='X-axis')

ax.legend(handles=[p1, p2, p3, l1, l2], loc='upper left', bbox_to_anchor=(1.05, 1))

plt.tight_layout()
plt.show()