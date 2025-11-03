import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given points
A = np.array([3, 2, 1])
B = np.array([4, 5, 5])   # x = 5 from solution
C = np.array([4, 2, -2])
D = np.array([6, 5, -1])

# Compute normal vector using (C-A) x (D-A)
n = np.cross(C - A, D - A)

# Equation of plane: n1*x + n2*y + n3*z = d
d = np.dot(n, A)

# Create meshgrid for the plane
xx, yy = np.meshgrid(np.linspace(2, 7, 10), np.linspace(1, 6, 10))
zz = (d - n[0]*xx - n[1]*yy) / n[2]

# Plotting
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Plot the points
ax.scatter(*A, color='red', s=60, label='A(3,2,1)')
ax.scatter(*B, color='blue', s=60, label='B(4,5,5)')
ax.scatter(*C, color='green', s=60, label='C(4,2,-2)')
ax.scatter(*D, color='orange', s=60, label='D(6,5,-1)')

# Labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title("Plane through A, C, D (also contains B)")

# Save figure
plt.savefig("plot7.png")
plt.show()

