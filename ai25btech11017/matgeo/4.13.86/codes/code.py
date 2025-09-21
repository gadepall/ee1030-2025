import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Plane: x + y + 1 = 0  => normal = (1,1,0)
a, b, c, d = 1, 1, 0, 1  # ax + by + cz + d = 0

# Point
P = np.array([1, 2, 2])

# Distance formula
dist = abs(a*P[0] + b*P[1] + c*P[2] + d) / np.sqrt(a*a + b*b + c*c)
print("Distance =", dist)

# Foot of perpendicular
t = -(a*P[0] + b*P[1] + c*P[2] + d) / (a*a + b*b + c*c)
foot = P + t * np.array([a, b, c])

# Grid for plane
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)  # since c=0, plane is vertical (no z-dependence)

# Plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Highlighted Plane (solid color + edge lines)
ax.plot_surface(X, Y, Z, color='lightblue', alpha=0.8, edgecolor='k', linewidth=0.5)

# Point
ax.scatter(P[0], P[1], P[2], color='red', s=60, label=f"Point {tuple(P)}")

# Foot of perpendicular
ax.scatter(foot[0], foot[1], foot[2], color='green', s=60, label="Foot of perpendicular")

# Distance line
ax.plot([P[0], foot[0]], [P[1], foot[1]], [P[2], foot[2]], 'k--', lw=2, label=f"Distance = {dist:.2f}")

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Highlighted Plane with Point-to-Plane Distance")

ax.legend()

# Save
plt.savefig("highlighted_plane_distance.png", dpi=300)
plt.show()
