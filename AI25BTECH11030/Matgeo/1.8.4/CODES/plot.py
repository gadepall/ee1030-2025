import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Points
P = np.array([3, -2, 5])
Q1 = np.array([0, 2, 0])
Q2 = np.array([0, -6, 0])

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*P, color='red', label='P(3,-2,5)', s=50)
ax.scatter(*Q1, color='green', label='Q1(0,2,0)', s=50)
ax.scatter(*Q2, color='blue', label='Q2(0,-6,0)', s=50)

# Plot Y-axis line for reference
y_axis = np.array([[0, y, 0] for y in np.linspace(-8, 4, 100)])
ax.plot(y_axis[:,0], y_axis[:,1], y_axis[:,2], color='orange', linestyle='--', label='Y-axis')

# Lines from P to Q1 and Q2
ax.plot([P[0], Q1[0]], [P[1], Q1[1]], [P[2], Q1[2]], color='purple', linestyle='-', label='Distance PQ1')
ax.plot([P[0], Q2[0]], [P[1], Q2[1]], [P[2], Q2[2]], color='cyan', linestyle='-', label='Distance PQ2')

# Labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Set aspect ratio equal for better visualization
ax.set_box_aspect([1,2,1])

plt.title('3D Visualization of Point P and Points on Y-axis Q1, Q2')
plt.savefig('3d_points_plot.png', dpi=300)

plt.show()
