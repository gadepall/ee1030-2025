import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C library
lib = ctypes.CDLL("./libdist.so")
lib.projection.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS")
]
lib.projection.restype = ctypes.c_double

# Define vectors and point
u1 = np.array([1.0, 1.0, 0.0])
u2 = np.array([0.0, 1.0, 1.0])
P  = np.array([1.0, 1.0, 1.0])
P_proj = np.zeros(3, dtype=np.double)

# Compute projection and distance
distance = lib.projection(u1, u2, P, P_proj)
print(f"Distance from P to plane: {distance:.6f}")
print(f"Projection point: {P_proj}")

# Create plane grid
s = np.linspace(-0.5, 2, 10)
t = np.linspace(-0.5, 2, 10)
S, T = np.meshgrid(s, t)
X = S*u1[0] + T*u2[0]
Y = S*u1[1] + T*u2[1]
Z = S*u1[2] + T*u2[2]

# Plot
fig = plt.figure(figsize=(7,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, color='lightblue', alpha=0.5)
ax.scatter(*P, color='red', s=80, label='P = (1,1,1)')
ax.scatter(*P_proj, color='green', s=80)
ax.text(P_proj[0], P_proj[1], P_proj[2],
        f'({P_proj[0]:.2f}, {P_proj[1]:.2f}, {P_proj[2]:.2f})',
        color='green', fontsize=10, ha='left', va='bottom')
ax.plot([P[0], P_proj[0]], [P[1], P_proj[1]], [P[2], P_proj[2]], 'k--', label='Distance')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Distance from Point to Plane')
ax.legend()
plt.savefig("/mnt/c/Users/bharg/Documents/backupmatrix/ee25btech11013/matgeo/12.547/figs/Figure_1.png")
plt.show()




