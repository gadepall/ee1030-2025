import numpy as np
import matplotlib.pyplot as plt

# --- Geometry ---
P = np.array([2, -1, 2])        # Point P
d = np.array([1, 1, 1])         # Direction vector
n = np.array([2, 1, 1])         # Normal of plane
plane_rhs = 9

# Intersection Q
t = (plane_rhs - n.dot(P)) / n.dot(d)
Q = P + t * d

# Line points
t_vals = np.linspace(-10, 10, 200)
line_pts = P.reshape(3,1) + np.outer(d, t_vals)

# Plane mesh
xx = np.linspace(-10, 10, 10)
yy = np.linspace(-10, 10, 10)
XX, YY = np.meshgrid(xx, yy)
ZZ = plane_rhs - 2*XX - YY

# --- Plotting ---
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

# Plane (smooth yellow surface)
ax.plot_surface(XX, YY, ZZ, color='khaki', alpha=0.5, edgecolor='none')

# Line (blue)
ax.plot(line_pts[0], line_pts[1], line_pts[2], color='blue', linewidth=2, label="Line")

# PQ segment (red)
ax.plot([P[0], Q[0]], [P[1], Q[1]], [P[2], Q[2]], color='red', linewidth=2, label="PQ")

# Mark points P and Q clearly with larger markers
ax.scatter([P[0]], [P[1]], [P[2]], color='blue', s=80, marker='o')
ax.text(P[0]+0.5, P[1]-0.5, P[2], r"$P(2,-1,2)$", fontsize=12, color='blue')

ax.scatter([Q[0]], [Q[1]], [Q[2]], color='black', s=80, marker='o')
ax.text(Q[0]+0.5, Q[1], Q[2], r"$Q(3,0,3)$", fontsize=12, color='black')

# Plane equation label
ax.text(5, 5, -5, r"$2x+y+z=9$", fontsize=14, color='brown')

# Axes labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

# Grid and viewing angle
ax.grid(True)
ax.view_init(elev=20, azim=-60)

plt.title("Line-Plane Intersection")
plt.legend()
plt.show()
