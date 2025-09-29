import numpy as np
import matplotlib.pyplot as plt

# Input points
A = np.array([2.0, 3.0, 4.0], dtype=np.double)
B = np.array([4.0, 5.0, 8.0], dtype=np.double)
M = (A + B) / 2.0   # Midpoint

# Normal vector (AB) and plane constant
N = B - A
d = -(N[0]*M[0] + N[1]*M[1] + N[2]*M[2])

# Plane equation function
def plane_z(x, y):
    return (-N[0] * x - N[1] * y - d) / N[2]

# Create a small plane patch around M
span = 1.5
xx, yy = np.meshgrid(
    np.linspace(M[0] - span, M[0] + span, 10),
    np.linspace(M[1] - span, M[1] + span, 10)
)
zz = plane_z(xx, yy)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot and label points
ax.scatter(*A, color='red', s=100)
ax.text(A[0], A[1], A[2], "A(2,3,4)", color='red')

ax.scatter(*B, color='green', s=100)
ax.text(B[0], B[1], B[2], "B(4,5,8)", color='green')

ax.scatter(*M, color='purple', s=200, marker='*')
ax.text(M[0], M[1], M[2], "M(3,4,6)", color='purple')

# Line AB
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]],
        color='blue', label="Line AB")

# Plane patch
ax.plot_surface(xx, yy, zz, alpha=0.4, color='cyan')

# Axes labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Required Plane")
ax.legend()
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/2.4.22/figs/figure1.png")

plt.show()
