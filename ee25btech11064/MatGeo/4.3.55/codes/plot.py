import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the points
R = np.array([2, 5, -3])
S = np.array([-2, -3, 5])
T = np.array([5, 3, -3])
normal = np.array([2, 3, 4])
# Create a grid to plot the plane
x = np.linspace(-5, 7, 10)
y = np.linspace(-5, 7, 10)
X, Y = np.meshgrid(x, y)

# Equation of the plane: Ax + By + Cz = D
A, B, C = normal
D = np.dot(normal, R)

# Solve for Z
Z = (D - A * X - B * Y) / C

# Plotting the plane and the points R, S, T
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(*R, color='r', label='R (2, 5, -3)', s=10)
ax.scatter(*S, color='g', label='S (-2, -3, 5)', s=10)
ax.scatter(*T, color='b', label='T (5, 3, -3)', s=10)

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5, rstride=100, cstride=100, color='c')

# Plot the normal vector starting from point R
ax.quiver(0, 0, 0, normal[0], normal[1], normal[2], color='k', length=1, linewidth=1, label='Normal Vector')

# Labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Display plot
plt.show()
