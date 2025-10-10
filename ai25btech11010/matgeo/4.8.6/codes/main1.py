import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D

# Function to compute foot of perpendicular, distance, and reflection
def solve_point_plane(P, n, d):
    P = np.array(P, dtype=float)
    n = np.array(n, dtype=float)

    # λ = (n^T P - d) / (n^T n)
    lam = (np.dot(n, P) - d) / np.dot(n, n)

    # Foot of perpendicular
    Q = P - lam * n

    # Distance
    dist = abs(lam) * np.linalg.norm(n)

    # Reflection
    R = 2 * Q - P

    return lam, Q, dist, R


# ---------------- MAIN CODE ----------------
P = np.array([3, 2, 1])
n = np.array([2, -1, 1])
d = -1   # Plane equation: n^T x = -1

# Solve
lam, Q, dist, R = solve_point_plane(P, n, d)

print("λ =", lam)
print("Foot of perpendicular Q =", Q)
print("Distance =", dist)
print("Reflection R =", R)

# ---------- Plotting ----------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a grid for the plane
xx, yy = np.meshgrid(range(-2, 5), range(-2, 5))
zz = (-d - n[0]*xx - n[1]*yy) / n[2]

# Plot the plane surface
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Plot points P, Q, R
ax.scatter(*P, color='red', s=60, label='P (given point)')
ax.scatter(*Q, color='green', s=60, label='Q (foot of perpendicular)')
ax.scatter(*R, color='blue', s=60, label='R (reflection)')

# Draw perpendicular line P-Q
ax.plot([P[0], Q[0]], [P[1], Q[1]], [P[2], Q[2]], 'k--', label='Perpendicular')

# Draw line Q-R
ax.plot([Q[0], R[0]], [Q[1], R[1]], [Q[2], R[2]], 'm--', label='Reflection line')

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()

# ---------- Save figure ----------
os.makedirs("figs", exist_ok=True)   # create folder if not exists
save_path = os.path.join("../figs", "point_plane.png")
plt.savefig(save_path, dpi=300, bbox_inches='tight')


plt.close(fig)  # Close figure instead of showing
