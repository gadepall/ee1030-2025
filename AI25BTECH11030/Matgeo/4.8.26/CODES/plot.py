import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Points
P = np.array([2, -3, 4])  # Given point
Q = np.array([0, -3, 0])  # Foot of the perpendicular on Y axis

# Y-axis vector for reference
y_axis = np.array([[0, 0], [min(P[1], Q[1]) - 1, max(P[1], Q[1]) + 1], [0, 0]])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot point P
ax.scatter(P[0], P[1], P[2], color='r', s=100, label='Point P (2, -3, 4)')

# Plot foot of perpendicular Q
ax.scatter(Q[0], Q[1], Q[2], color='g', s=100, label='Foot of perpendicular Q')

# Plot the perpendicular line from P to Q
ax.plot([P[0], Q[0]], [P[1], Q[1]], [P[2], Q[2]], color='b', label='Perpendicular')

# Plot Y axis
ax.plot(y_axis[0], y_axis[1], y_axis[2], color='k', linestyle='--', label='Y axis')

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Foot of Perpendicular from P to Y axis')

ax.legend()

# Adjust view angle
ax.view_init(elev=20, azim=45)

# Save the figure as .png
plt.savefig('foot_of_perpendicular.png')
plt.show()
