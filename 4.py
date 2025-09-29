import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Points
P = np.array([-1.5, 3, 0])
Q = np.array([6, -2, 0])
R = np.array([-3, 4, 0])

# Function to compute area of triangle
def triangle_area(A, B, C):
    return 0.5 * np.linalg.norm(np.cross(B - A, C - A))

# Calculate area
area = triangle_area(P, Q, R)

# Plot the triangle in 3D
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*P, color='r', s=50)
ax.scatter(*Q, color='g', s=50)
ax.scatter(*R, color='b', s=50)

# Plot triangle edges
ax.plot([P[0], Q[0]], [P[1], Q[1]], [P[2], Q[2]], 'k-')
ax.plot([Q[0], R[0]], [Q[1], R[1]], [Q[2], R[2]], 'k-')
ax.plot([R[0], P[0]], [R[1], P[1]], [R[2], P[2]], 'k-')

# Labels for points
ax.text(*P, "P(-1.5,3)", color='r')
ax.text(*Q, "Q(6,-2)", color='g')
ax.text(*R, "R(-3,4)", color='b')

# Axis labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title(f"Area of Triangle PQR = {area:.2f}")

# Save and show
plt.savefig("fig4.png")
plt.show()

