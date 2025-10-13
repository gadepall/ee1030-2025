import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given data
P = np.array([4, -3, -4])   # Point 1
Q = np.array([3, -2,  2])   # Point 2

# Plane: 2x + y + z = 6
n = np.array([2, 1, 1])     # Normal vector
c = 6

# Direction vector of the line
d = Q - P

# Parameter t for intersection point
t = (c - np.dot(n, P)) / np.dot(n, d)

# Intersection point
R = P + t * d

print("Intersection point:", R)

# --- Plotting the line, plane, and intersection point ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate the plane surface
xx, yy = np.meshgrid(np.linspace(0, 5, 10), np.linspace(-5, 5, 10))
zz = 6 - 2*xx - yy  # from plane equation 2x + y + z = 6

# Plot the plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Plot the line passing through P and Q
line_points = np.array([P, Q])
ax.plot(line_points[:,0], line_points[:,1], line_points[:,2],
        color='red', label='Line PQ')

# Plot the intersection point
ax.scatter(R[0], R[1], R[2], color='blue', s=50, label='Intersection Point')

# Annotate points
ax.text(P[0], P[1], P[2], 'P(4,-3,-4)', color='black')
ax.text(Q[0], Q[1], Q[2], 'Q(3,-2,2)', color='black')
ax.text(R[0], R[1], R[2], f'R({R[0]:.1f},{R[1]:.1f},{R[2]:.1f})', color='blue')

# Labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Intersection of Line and Plane')

ax.legend()
plt.show()

