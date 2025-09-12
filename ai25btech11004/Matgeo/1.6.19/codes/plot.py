import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# ----- Correct value -----
lam = -2  # correct λ

# Vectors
A = np.array([lam, lam, 2], dtype=float)
B = np.array([1, lam, -1], dtype=float)
C = np.array([2, -1, lam], dtype=float)

# Verify coplanarity via scalar triple product: A · (B × C) = 0
triple = float(np.dot(A, np.cross(B, C)))
print(f"Scalar triple product at λ={lam}: {triple:.6g} (0 => coplanar)")

# ----- Plot -----
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

origin = np.zeros(3)

# Plot vectors from origin
ax.quiver(*origin, *A, length=1, normalize=False, label=f"A = {A}", color='r')
ax.quiver(*origin, *B, length=1, normalize=False, label=f"B = {B}", color='g')
ax.quiver(*origin, *C, length=1, normalize=False, label=f"C = {C}", color='b')

# Plot the plane spanned by B and C (shows A lies in this plane)
s = np.linspace(-1.2, 1.2, 20)
t = np.linspace(-1.2, 1.2, 20)
S, T = np.meshgrid(s, t)
plane = np.outer(S.ravel(), B) + np.outer(T.ravel(), C)
X = plane[:, 0].reshape(S.shape)
Y = plane[:, 1].reshape(S.shape)
Z = plane[:, 2].reshape(S.shape)
ax.plot_surface(X, Y, Z, alpha=0.2, edgecolor='none')

# Aesthetic: equal aspect & limits
all_pts = np.vstack([origin, A, B, C, plane])
mins = all_pts.min(axis=0)
maxs = all_pts.max(axis=0)
ranges = maxs - mins
center = (maxs + mins) / 2
max_range = ranges.max() * 0.55 + 1e-9
ax.set_xlim(center[0]-max_range, center[0]+max_range)
ax.set_ylim(center[1]-max_range, center[1]+max_range)
ax.set_zlim(center[2]-max_range, center[2]+max_range)
ax.set_box_aspect([1,1,1])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f"Vectors A, B, C for λ = {lam} (coplanar)")

ax.legend(loc='upper left')

# ----- Save the figure -----
plt.savefig("vectors.png", dpi=300, bbox_inches='tight')

# Show on screen too (optional)
plt.show()


