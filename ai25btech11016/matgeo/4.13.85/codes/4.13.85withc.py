import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./liblines.so")

# Define function signature
lib.generate_lines.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_double,
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
]
lib.generate_lines.restype = None

# Parameters
n_points = 200
t_min, t_max = -10, 10
k = 2.0  # change this as needed

# Allocate numpy arrays
x1 = np.zeros(n_points, dtype=np.float64)
y1 = np.zeros(n_points, dtype=np.float64)
z1 = np.zeros(n_points, dtype=np.float64)
x2 = np.zeros(n_points, dtype=np.float64)
y2 = np.zeros(n_points, dtype=np.float64)
z2 = np.zeros(n_points, dtype=np.float64)

# Call C function
lib.generate_lines(t_min, t_max, n_points, k, x1, y1, z1, x2, y2, z2)

# Plot 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

ax.plot(x1, y1, z1, label="Line 1", color="blue")
ax.plot(x2, y2, z2, label=f"Line 2 (k={k})", color="orange")

ax.scatter(x1[0], y1[0], z1[0], color="red", s=50, label="Start Line 1")
ax.scatter(x2[0], y2[0], z2[0], color="green", s=50, label="Start Line 2")

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Plot of Two Lines (from C library)")
ax.legend()
plt.show()
