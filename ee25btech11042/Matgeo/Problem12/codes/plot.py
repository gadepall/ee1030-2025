import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os

# --- Part 1: Call the C Shared Library to Find k ---

# Load the shared library
solver_lib = ctypes.CDLL('./5.13.67.so')

# Specify the function's return type to ensure it's read as a float
solver_lib.find_k.restype = ctypes.c_double

# Call the C function to get the exact value of k
k = solver_lib.find_k()




# --- Part 2: Plotting the Three Planes Using the Result from C ---

# Create a figure and a 3D axes object
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Create a grid of points for the surfaces
x_grid = np.linspace(-10, 10, 50)
y_grid = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x_grid, y_grid)

# Equations of the three planes, using the value of k from the C library
Z1 = (-X - k*Y) / 3
Z2 = (3*X + k*Y) / 2
Z3 = (2*X + 3*Y) / 4

# Plot the surfaces of the three planes
ax.plot_surface(X, Y, Z1, alpha=0.5, color='royalblue')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='crimson')
ax.plot_surface(X, Y, Z3, alpha=0.5, color='forestgreen')

# Plot the line of intersection (its direction vector is constant)
t = np.linspace(-2, 2, 100)
ax.plot(15 * t, -2 * t, 6 * t, color='black', linewidth=4)

# --- Formatting the plot ---
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
ax.set_zlabel('Z-axis', fontsize=12)
ax.set_title(f'Intersection of Three Planes at k = {k:.1f} (from C library)', fontsize=16, fontweight='bold')
ax.view_init(elev=20, azim=-65)

# Create a custom legend for the plot
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
p1 = mpatches.Patch(color='royalblue', label=f'x + {k:.1f}y + 3z = 0')
p2 = mpatches.Patch(color='crimson', label=f'3x + {k:.1f}y - 2z = 0')
p3 = mpatches.Patch(color='forestgreen', label='2x + 3y - 4z = 0')
line = Line2D([0], [0], color='black', linewidth=3, label='Line of Intersection')
ax.legend(handles=[p1, p2, p3, line], fontsize=10)

plt.show()
