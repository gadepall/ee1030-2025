import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./libdistance.so")

# Define argument and return types
lib.distance_point_line.argtypes = [ctypes.POINTER(ctypes.c_double),
                                    ctypes.POINTER(ctypes.c_double),
                                    ctypes.POINTER(ctypes.c_double)]
lib.distance_point_line.restype = ctypes.c_double

# Define arrays
p = np.array([2.0, 4.0, -1.0], dtype=np.double)
a = np.array([-5.0, -3.0, 6.0], dtype=np.double)
m = np.array([1.0, 4.0, -9.0], dtype=np.double)

# Call C function
d = lib.distance_point_line(p.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                            a.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                            m.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

print(f"Distance from point to line (via C lib) = {d:.2f}")

# --- Plot (same as before) ---
w = p - a
proj = (np.dot(m, w)/np.dot(m, m))*m
foot = a + proj

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Line points
t_vals = np.linspace(-2, 2, 100)
line_points = np.array([a + t*m for t in t_vals])

ax.plot(line_points[:,0], line_points[:,1], line_points[:,2], 'b', label="Line")
ax.scatter(p[0], p[1], p[2], color='r', s=50, label="Point P")
ax.plot([p[0], foot[0]], [p[1], foot[1]], [p[2], foot[2]], 'r--', label="Perpendicular")
ax.scatter(foot[0], foot[1], foot[2], color='k', s=60, marker='x', label="Foot")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
plt.show()
