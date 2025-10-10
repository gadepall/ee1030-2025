import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Hardcoded coordinates
A = [4, 8, 10]
B = [6, 10, -8]
P = [0, 4, 46]

# Hardcoded division ratio
k = -2 / 3



# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points A, B, P
ax.scatter(*A, color='blue', label='Point A (4, 8, 10)', s=50)
ax.scatter(*B, color='green', label='Point B (6, 10, -8)', s=50)
ax.scatter(*P, color='red', label='Point P (0, 4, 46)', s=50)

# Plot line AB
line_points = np.linspace(0, 1, 100)
AB_line = np.array([A[i] + t * (B[i] - A[i]) for t in line_points for i in range(3)]).reshape(100,3)
ax.plot(AB_line[:, 0], AB_line[:, 1], AB_line[:, 2], label='Line AB', color='black')

# Plot YZ-plane (x=0)
yz_y, yz_z = np.meshgrid(np.linspace(-5, 15, 20), np.linspace(-10, 50, 20))
yz_x = np.zeros_like(yz_y)
ax.plot_surface(yz_x, yz_y, yz_z, alpha=0.3, color='cyan')

# Connect P to A and B
ax.plot([P[0], A[0]], [P[1], A[1]], [P[2], A[2]], color='purple', linestyle='--', label='P-A')
ax.plot([P[0], B[0]], [P[1], B[1]], [P[2], B[2]], color='orange', linestyle='--', label='P-B')

# Labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot (Hardcoded Coordinates and Ratio)')
ax.legend()

# Save the figure as 1.png
plt.savefig('2.png')

plt.show()

