import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.lines import Line2D

# Define z functions for each plane
def plane1_z(x, y):
    return (5 - x - 2*y) / 3

def plane2_z(x, y):
    return -3*x - 3*y

def required_z(x, y):
    return (-7*x + 8*y - 25) / 3

# Meshgrid
x = np.linspace(-5, 5, 40)
y = np.linspace(-5, 5, 40)
X, Y = np.meshgrid(x, y)

Z1 = plane1_z(X, Y)
Z2 = plane2_z(X, Y)
Zr = required_z(X, Y)

# Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the planes
ax.plot_surface(X, Y, Z1, alpha=0.5, color='cyan')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='yellow')
ax.plot_surface(X, Y, Zr, alpha=0.5, color='red')

# Mark the given point
ax.scatter(-1, 3, 2, color='black', s=50)

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Legend
legend_elements = [
    Line2D([0], [0], color='cyan', lw=4, label='Plane 1: x+2y+3z=5'),
    Line2D([0], [0], color='yellow', lw=4, label='Plane 2: 3x+3y+z=0'),
    Line2D([0], [0], color='red', lw=4, label='Required Plane'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='black', markersize=10, label='Point (-1,3,2)')
]
ax.legend(handles=legend_elements)

# Equal aspect ratio
ax.set_box_aspect([1,1,1])

plt.title("Intersection of Planes and Required Perpendicular Plane")
plt.savefig("plot8.png", dpi=300)
plt.show()

