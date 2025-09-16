import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given data
norm_a = 12
norm_b = 4 * np.sqrt(3)
b_dot_c = 24

# Assume coordinates for visualization
# Let’s place vectors in 3D space for clarity
# a = QR, b = RP, c = PQ

# Pick simple coordinates consistent with magnitudes
Q = np.array([0, 0, 0])
R = np.array([12, 0, 0])  # so that a = (12,0,0), ||a|| = 12
P = np.array([0, 4*np.sqrt(3), 0])  # so that b = P - R = (-12, 4√3, 0)

# Vectors
a = R - Q
b = P - R
c = Q - P

# Calculations
val1 = np.linalg.norm(c)**2 / 2 - np.linalg.norm(a)
val2 = np.linalg.norm(c)**2 / 2 + np.linalg.norm(a)
val3 = np.linalg.norm(np.cross(a, b) + np.cross(c, a))
val4 = np.dot(a, b)

print("||c||^2/2 - ||a|| =", val1)
print("||c||^2/2 + ||a|| =", val2)
print("||a×b + c×a|| =", val3)
print("a·b =", val4)

# Plot triangle in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Draw triangle edges
X = [P[0], Q[0], R[0], P[0]]
Y = [P[1], Q[1], R[1], P[1]]
Z = [P[2], Q[2], R[2], P[2]]
ax.plot(X, Y, Z, 'b-', linewidth=2)

# Mark points
ax.scatter(P[0], P[1], P[2], c='r', label='P')
ax.scatter(Q[0], Q[1], Q[2], c='g', label='Q')
ax.scatter(R[0], R[1], R[2], c='m', label='R')

# Add labels
ax.text(P[0], P[1], P[2], 'P', fontsize=12)
ax.text(Q[0], Q[1], Q[2], 'Q', fontsize=12)
ax.text(R[0], R[1], R[2], 'R', fontsize=12)

# Styling
ax.set_title("Triangle PQR in 3D")
ax.legend()

# Save as image
plt.savefig("triangle_vectors.png")
plt.show()
