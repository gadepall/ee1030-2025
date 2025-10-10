import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def unit_vector(P, Q):
    """Compute unit vector from P to Q in 3D."""
    dx, dy, dz = Q[0]-P[0], Q[1]-P[1], Q[2]-P[2]
    norm = math.sqrt(dx*dx + dy*dy + dz*dz)
    if norm == 0:
        raise ValueError("P and Q are the same point, unit vector undefined.")
    return (dx/norm, dy/norm, dz/norm)

# Example points
P = (5, 0, 8)
Q = (3, 3, 2)

# Compute vector PQ and unit vector
PQ = (Q[0]-P[0], Q[1]-P[1], Q[2]-P[2])
u = unit_vector(P, Q)

print("Vector PQ =", PQ)
print("Unit vector =", u)

# --- Plot ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*P, color="red", s=60, label="P")
ax.scatter(*Q, color="blue", s=60, label="Q")

# Vector PQ (green arrow)
ax.quiver(P[0], P[1], P[2], PQ[0], PQ[1], PQ[2],
          color="green", label="PQ", arrow_length_ratio=0.1)

# Unit vector (orange arrow, length 1)
ax.quiver(P[0], P[1], P[2], u[0], u[1], u[2],
          color="orange", label="Unit vector", arrow_length_ratio=0.2)

# Labels and aesthetics
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
ax.set_title("Vector PQ and Unit Vector from P")
ax.grid(True)

plt.show()

