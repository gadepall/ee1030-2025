import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Plane coefficients: 2x - 3y + 6z - 11 = 0
a, b, c, d = 2, -3, 6, -11
normal = np.array([a, b, c])

# Grid for plane
y = np.linspace(-6, 6, 41)
z = np.linspace(-6, 6, 41)
Y, Z = np.meshgrid(y, z)
X = (-d - b*Y - c*Z) / a  # from ax+by+cz+d=0

# X-axis vector
x_axis = np.array([1, 0, 0])

# Pick a direction vector lying in the plane (example: (-3,0,1))
v_plane = np.array([-3, 0, 1])
v_plane = v_plane / np.linalg.norm(v_plane)

# Plot
fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(111, projection='3d')

# Plot plane surface
ax.plot_surface(X, Y, Z, alpha=0.45, color="orange")

# Plot x-axis
t = np.linspace(-8, 8, 2)
ax.plot(t, np.zeros_like(t), np.zeros_like(t), color="black")

# Plot vectors from origin
ax.quiver(0,0,0, 4,0,0, color="red", arrow_length_ratio=0.15, label="x-axis")
ax.quiver(0,0,0, v_plane[0]*4, v_plane[1]*4, v_plane[2]*4,
          color="blue", arrow_length_ratio=0.15, label="vector in plane")

# Plot normal vector at a point on plane (choose y=0,z=0 -> x=11/2)
P = np.array([11/2, 0, 0])
ax.quiver(P[0], P[1], P[2], normal[0], normal[1], normal[2],
          color="green", arrow_length_ratio=0.15, label="normal")

# Arc showing angle between x-axis and plane (in xz-plane)
angle_x = np.arctan2(0, 1)          # angle of x-axis
angle_v = np.arctan2(v_plane[2], v_plane[0])  # angle of v_plane
theta = np.linspace(angle_x, angle_v, 50)
r = 2.0
arc_x = r * np.cos(theta)
arc_y = np.zeros_like(theta)
arc_z = r * np.sin(theta)
ax.plot(arc_x, arc_y, arc_z, color="purple", linewidth=2)

# Labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xlim(-8, 8)
ax.set_ylim(-6, 6)
ax.set_zlim(-6, 6)
ax.set_title("Plane 2x - 3y + 6z - 11 = 0\nAngle with x-axis")

plt.legend()
plt.show()
