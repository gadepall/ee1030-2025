import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
a = np.array([2, 1, 1])
b = np.array([1, 2, -1])
c = np.array([0, -1, 1]) / np.sqrt(2)  # unit vector

# Compute normal to plane (a x b)
n = np.cross(a, b)
A, B, C = n  # plane coefficients
# Plane equation: A*x + B*y + C*z = 0 (through origin)

# Create a grid for x and y
x_vals = np.linspace(-2.5, 2.5, 10)
y_vals = np.linspace(-2.5, 2.5, 10)
X, Y = np.meshgrid(x_vals, y_vals)

# Solve for Z from plane equation (avoid divide by zero)
Z = (-A * X - B * Y) / C

# Create 3D figure
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, projection='3d')

origin = np.zeros(3)

# Plot the plane as a translucent surface
ax.plot_surface(X, Y, Z, alpha=0.3, color='gray')

# Plot vectors
ax.quiver(*origin, *a, color='r', arrow_length_ratio=0.1)
ax.quiver(*origin, *b, color='g', arrow_length_ratio=0.1)
ax.quiver(*origin, *c, color='b', arrow_length_ratio=0.1)

# Add text labels near arrowheads
ax.text(*(a * 1.05), r'$\vec{a}$', color='r', fontsize=12)
ax.text(*(b * 1.05), r'$\vec{b}$', color='g', fontsize=12)
ax.text(*(c * 1.2),  r'$\vec{c}$', color='b', fontsize=12)

# Set axes limits and labels
ax.set_xlim([-2.5, 2.5])
ax.set_ylim([-2.5, 2.5])
ax.set_zlim([-2.5, 2.5])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.grid(True)
plt.title("Vectors a, b, and c")
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/2.10.39/figs/q5.png")
plt.show()
