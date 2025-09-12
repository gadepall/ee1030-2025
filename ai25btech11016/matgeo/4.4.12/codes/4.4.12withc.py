import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the C shared library (compile first: gcc -shared -o geometry.so -fPIC geometry.c)
lib = ctypes.CDLL("./geometry.so")

# Define Vec3 struct (same as in C)
class Vec3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

# Configure function
lib.find_intersection.argtypes = [Vec3, Vec3, Vec3, Vec3, Vec3]
lib.find_intersection.restype = Vec3

# Define points
A = Vec3(2, 5, -3)
B = Vec3(-2, -3, 5)
C = Vec3(5, 3, -3)
P = Vec3(3, 1, 5)
Q = Vec3(-1, -3, -1)

# Call C function to get intersection
inter = lib.find_intersection(A, B, C, P, Q)

# Convert to numpy arrays for plotting
A_np = np.array([A.x, A.y, A.z])
B_np = np.array([B.x, B.y, B.z])
C_np = np.array([C.x, C.y, C.z])
P_np = np.array([P.x, P.y, P.z])
Q_np = np.array([Q.x, Q.y, Q.z])
inter_np = np.array([inter.x, inter.y, inter.z])

# --- Compute plane for plotting ---
AB = B_np - A_np
AC = C_np - A_np
n = np.cross(AB, AC)   # normal
d = -np.dot(n, A_np)   # plane constant

xx, yy = np.meshgrid(range(-5, 8), range(-5, 8))
zz = (-n[0]*xx - n[1]*yy - d) / n[2]

# --- Compute line for plotting ---
d_line = Q_np - P_np
t = np.linspace(-5, 5, 100)
line_points = P_np[:, None] + d_line[:, None] * t

# --- Plot ---
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Line
ax.plot(line_points[0], line_points[1], line_points[2], color='red', label="Line")

# Intersection
ax.scatter(*inter_np, color='black', s=60, label="Intersection")

# Points
ax.scatter(*A_np, color='blue', s=50, label='A')
ax.scatter(*B_np, color='green', s=50, label='B')
ax.scatter(*C_np, color='purple', s=50, label='C')
ax.scatter(*P_np, color='orange', s=50, label='P')
ax.scatter(*Q_np, color='brown', s=50, label='Q')

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()

plt.savefig("\sdcard\4.4.12.png")
plt.show()
