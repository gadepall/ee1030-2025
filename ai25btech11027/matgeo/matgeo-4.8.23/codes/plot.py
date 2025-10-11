import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the plane 3x + 5y + 4z = 11
# Solve for z: z = (11 - 3x - 5y)/4
def plane_z(x, y):
    return (11 - 3*x - 5*y) / 4

# Create grid for the plane
x = np.linspace(-2, 4, 20)
y = np.linspace(-2, 4, 20)
X, Y = np.meshgrid(x, y)
Z = plane_z(X, Y)

# Points (2, 1, 5) and (2, 1, -5)
P1 = np.array([2, 1, 5])
P2 = np.array([2, 1, -5])

# Normal vector of plane
n = np.array([3, 5, 4])

# Calculate foot of perpendicular for each point on the plane:
def foot_of_perpendicular(P, n, d):
    # d = 11 (plane constant)
    # foot F = P - ((n.P - d)/||n||^2)*n
    n_norm_sq = np.dot(n, n)
    t = (np.dot(n, P) - d) / n_norm_sq
    F = P - t*n
    return F

F1 = foot_of_perpendicular(P1, n, 11)
F2 = foot_of_perpendicular(P2, n, 11)

# Plotting
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5, color='cyan', rstride=1, cstride=1, edgecolor='none')

# Plot points
ax.scatter(*P1, color='red', s=100, label='Point (2,1,5)')
ax.scatter(*P2, color='blue', s=100, label='Point (2,1,-5)')

# Plot foot of perpendicular points on plane
ax.scatter(*F1, color='black', s=50, label='Foot of perpendicular from (2,1,5)')
ax.scatter(*F2, color='black', s=50, label='Foot of perpendicular from (2,1,-5)')

# Draw lines from points to foot of perpendicular (showing distance)
ax.plot([P1[0], F1[0]], [P1[1], F1[1]], [P1[2], F1[2]], 'r--')
ax.plot([P2[0], F2[0]], [P2[1], F2[1]], [P2[2], F2[2]], 'b--')

# Labels and limits
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Distance from point to plane visualization')
ax.legend()

# Set axis limits for better view
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.set_zlim(-6, 6)

plt.show()

