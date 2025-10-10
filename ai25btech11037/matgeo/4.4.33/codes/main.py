import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given vectors (with x unknown)
# A = 3i + 2j + k
A = np.array([3, 2, 1])

# Solve for x such that points are coplanar

# Let x be the unknown coordinate in B's j component and k component
# B = 4i + xj + 5k
# C = 4i + 2j - 2k
# D = 6i + 5j - k

# Set up vectors AB, AC, AD
def scalar_triple_product(x):
    B = np.array([4, x, 5])
    C = np.array([4, 2, -2])
    D = np.array([6, 5, -1])

    AB = B - A
    AC = C - A
    AD = D - A

    return np.dot(AB, np.cross(AC, AD))

# Solve for x using the derived formula or by root finding
from scipy.optimize import fsolve

x_solution = fsolve(scalar_triple_product, 0)[0]

# Recalculate B with the found x
B = np.array([4, x_solution, 5])
C = np.array([4, 2, -2])
D = np.array([6, 5, -1])

# 3D plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*A, color='r', label='A')
ax.scatter(*B, color='g', label=f'B (x={x_solution:.2f})')
ax.scatter(*C, color='b', label='C')
ax.scatter(*D, color='purple', label='D')

# Draw vectors from origin for clarity
for vec, name, color in zip([A, B, C, D], ['A', 'B', 'C', 'D'], ['r', 'g', 'b', 'purple']):
    ax.text(vec[0], vec[1], vec[2], f'{name}', size=12, color=color)

# Plot the plane defined by A, C, D (since points are coplanar)
# Plane normal vector
normal = np.cross(C - A, D - A)

# Create a grid of points on the plane
d = -np.dot(normal, A)
xx, yy = np.meshgrid(np.linspace(2, 7, 10), np.linspace(0, 6, 10))
zz = (-normal[0] * xx - normal[1] * yy - d) / normal[2]

ax.plot_surface(xx, yy, zz, alpha=0.3, color='cyan')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Coplanar Points A, B, C, D')

ax.legend()
plt.savefig('coplanar_points.png')
plt.show()
