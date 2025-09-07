import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared object
so = ctypes.CDLL("./find_point.so")

# Prepare arguments
px = ctypes.c_double()
py = ctypes.c_double()

so.find_point(ctypes.byref(px), ctypes.byref(py))

A = np.array([-6, 10])
B = np.array([3, -8])
P = np.array([px.value, py.value])

# Plot
plt.figure(figsize=(6,6))
plt.plot([A[0], B[0]], [A[1], B[1]], 'g--', label="Line AB")
plt.scatter(*A, color="red")
plt.scatter(*B, color="blue")
plt.scatter(*P, color="black")

plt.text(A[0], A[1]+0.5, "A(-6,10)", fontsize=10)
plt.text(B[0], B[1]-0.8, "B(3,-8)", fontsize=10)
plt.text(P[0], P[1]+0.5, f"P({px.value:.1f},{py.value:.1f})", fontsize=10)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Point P from C code")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()
