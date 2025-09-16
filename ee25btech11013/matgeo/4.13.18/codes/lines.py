import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load shared library
lib = ctypes.CDLL("./liblines.so")

# Declare function signatures
lib.distance_between_lines.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double
]
lib.distance_between_lines.restype = ctypes.c_double

lib.projection_on_line.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
]
lib.projection_on_line.restype = None

# Problem setup
px, py = 13.0, 32.0          # given point on line L
nx, ny = 4.0, -1.0           # normal vector of lines
c1, c2 = 20.0, -3.0          # constants for lines L and K

# Distance between lines
dist = lib.distance_between_lines(c1, c2, nx, ny)
print(f"Distance between L and K = {dist:.6f}")

# Projection of P onto line K
qx, qy = ctypes.c_double(), ctypes.c_double()
lib.projection_on_line(px, py, nx, ny, c2, ctypes.byref(qx), ctypes.byref(qy))
Q = (qx.value, qy.value)
print(f"Foot of perpendicular Q on K = {Q}")

# Plotting
x_vals = np.linspace(-20, 20, 400)
y_L = (nx * x_vals - c1) / ny   # line L: 4x - y = 20
y_K = (nx * x_vals - c2) / ny   # line K: 4x - y = -3

plt.figure(figsize=(8, 8))
plt.plot(x_vals, y_L, label="Line L: 4x - y = 20")
plt.plot(x_vals, y_K, "--", label="Line K: 4x - y = -3")

plt.scatter(px, py, color="red", zorder=5, label=f"P=({int(px)},{int(py)}) on L")
plt.scatter(*Q, color="green", zorder=5, label=f"Q=({Q[0]:.2f},{Q[1]:.2f}) on K")

plt.plot([px, Q[0]], [py, Q[1]], "k--", linewidth=1.5,
         label=f"Perpendicular (dist={dist:.3f})")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Parallel Lines L and K with Perpendicular")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.savefig("/Users/bhargavkrish/Desktop/BackupMatrix/ee25btech11013/matgeo/4.13.18/figs/Figure_1.png")
plt.show()
