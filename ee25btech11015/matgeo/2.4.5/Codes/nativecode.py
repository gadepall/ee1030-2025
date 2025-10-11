import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define points
A = np.array([2, -1, 1])
B = np.array([1, -3, -5])
C = np.array([3, -4, -4])

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(A[0], A[1], A[2], color='red', label='A')
ax.scatter(B[0], B[1], B[2], color='green', label='B')
ax.scatter(C[0], C[1], C[2], color='blue', label='C')

# Optionally, connect the points with lines to show the triangle
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='black')
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], color='black')
ax.plot([C[0], A[0]], [C[1], A[1]], [C[2], A[2]], color='black')

# Labels
ax.text(A[0], A[1], A[2], 'A', color='red')
ax.text(B[0], B[1], B[2], 'B', color='green')
ax.text(C[0], C[1], C[2], 'C', color='blue')

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show legend
ax.legend()

# Show plot
plt.show()

