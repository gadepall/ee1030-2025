import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Points A and B
A = np.array([-2, -1, -3])
B = np.array([1, -3, 3])

# Compute normal vector AB = B - A
normal_vector = B - A
a, b, c = normal_vector

# Compute d using point B
d = -(a * B[0] + b * B[1] + c * B[2])

# Define plane function
def plane_z(x, y):
    if c != 0:
        return (-a * x - b * y - d) / c
    else:
        return np.zeros_like(x)

# Create grid for plotting plane
x_vals = np.linspace(-5, 5, 20)
y_vals = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x_vals, y_vals)
Z = plane_z(X, Y)

# Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5, rstride=1, cstride=1, color='cyan', edgecolor='k')

# Plot points A and B
ax.scatter(A[0], A[1], A[2], color='red', s=100, label='A (-2, -1, -3)')
ax.scatter(B[0], B[1], B[2], color='green', s=100, label='B (1, -3, 3)')

# Plot the line AB
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='blue', linewidth=2, label='Line AB')

# Labels and legend
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Plane and Points A, B')
ax.legend()

# Automatically set a good view angle
ax.view_init(elev=30, azim=45)

# Save figure as 1.png
plt.savefig('2.png')
plt.show()

