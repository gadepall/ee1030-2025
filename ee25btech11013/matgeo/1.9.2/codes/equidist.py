import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the C shared library
lib = ctypes.CDLL("./libequidistant.so")

# Define function prototype: double f(double, double, double, double)
lib.equidistant_point.argtypes = [ctypes.c_double, ctypes.c_double,
                                  ctypes.c_double, ctypes.c_double]
lib.equidistant_point.restype = ctypes.c_double

# Define A and B
A = np.array([-4.0, 0.0])
B = np.array([10.0, 0.0])

# Call C function
x = lib.equidistant_point(A[0], A[1], B[0], B[1])

# Equidistant point
O = np.array([x, 0.0])

print("Equidistant point O =", O)

# ---- Plotting ----
plt.figure(figsize=(6,6))
plt.axhline(0, color='gray', linewidth=0.8)
plt.axvline(0, color='gray', linewidth=0.8)

# Plot points
plt.scatter(A[0], A[1], color='red', label='A (-4,0)')
plt.scatter(B[0], B[1], color='blue', label='B (10,0)')
plt.scatter(O[0], O[1], color='green', marker='*', s=150, label=f'O ({int(O[0])},0)')

# Connect O to A and B
plt.plot([A[0], O[0]], [A[1], O[1]], 'r--')
plt.plot([B[0], O[0]], [B[1], O[1]], 'b--')

plt.legend(loc="upper right")
plt.grid(True, linestyle='--', alpha=0.6)
plt.title("Equidistant Point on X-axis (C + Python)")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.savefig("/Users/bhargavkrish/Documents/ee1030-2025/ee25btech11013/matgeo/1.9.2/figs/Figure_1.png")
plt.show()

