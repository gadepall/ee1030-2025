import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given points
A = np.array([2, 5, -3])
B = np.array([-2, -3, 5])
C = np.array([5, 3, -3])

# Create vectors AB and AC
AB = B - A
AC = C - A

# Normal vector to the plane
normal = np.cross(AB, AC)
a, b, c = normal

# Equation of the plane: ax + by + cz = d
d = np.dot(normal, A)

# Create a grid of x, y values
xx, yy = np.meshgrid(range(-5, 6), range(-5, 6))
zz = (d - a * xx - b * yy) / c  # solving for z

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Plot points A, B, C
ax.scatter(*A, color='r', s=50, label='A(2,5,-3)')
ax.scatter(*B, color='g', s=50, label='B(-2,-3,5)')
ax.scatter(*C, color='b', s=50, label='C(5,3,-3)')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Plane passing through points A, B, C')
ax.legend()

plt.show()




