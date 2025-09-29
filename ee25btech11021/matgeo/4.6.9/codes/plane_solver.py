import ctypes
import numpy as np

# Load shared library
lib = ctypes.CDLL("./libline_data.so")

# Define Vec3 struct
class Vec3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

# Create instances
P1 = Vec3(); d1 = Vec3()
P2 = Vec3(); d2 = Vec3()
P3 = Vec3(); d3 = Vec3()

# Populate points and directions
lib.get_lines(ctypes.byref(P1), ctypes.byref(d1), ctypes.byref(P2), ctypes.byref(d2), ctypes.byref(P3), ctypes.byref(d3))

# Convert to numpy arrays
P1 = np.array([P1.x, P1.y, P1.z])
d1 = np.array([d1.x, d1.y, d1.z])
P2 = np.array([P2.x, P2.y, P2.z])
d2 = np.array([d2.x, d2.y, d2.z])
P3 = np.array([P3.x, P3.y, P3.z])
d3 = np.array([d3.x, d3.y, d3.z])

# Vector between points on first two lines
v = P2 - P1

# Constraint matrix
A = np.array([d1, v])

# Null space to find plane normal
U, S, Vt = np.linalg.svd(A)
n = Vt.T[:, -1]

# Scale normal for simplicity
n = n / n[-1]

# Plane equation: n . r = n . P1
d_plane = np.dot(n, P1)

print("Plane normal:", n)
print("Plane equation: {}*x + {}*y + {}*z = {}".format(n[0], n[1], n[2], d_plane))

# Check if third line lies on plane
dot_point = np.dot(n, P3) - d_plane
dot_dir = np.dot(n, d3)
if abs(dot_point) < 1e-6 and abs(dot_dir) < 1e-6:
    print("Line 3 lies on the plane")
else:
    print("Line 3 does NOT lie on the plane")

