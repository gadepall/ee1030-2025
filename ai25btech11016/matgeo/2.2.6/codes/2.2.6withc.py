import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load .so
lib = ctypes.CDLL("2.2.6fuction.so")
lib.angle_between.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.angle_between.restype = ctypes.c_double

# Original 3D vectors
a = np.array([2, -1, 1])
b = np.array([3, 4, -1])

# Call C function
theta = lib.angle_between(*a, *b)
print("Angle (radians):", theta)
print("Angle (degrees):", np.degrees(theta))

# ---- Project to 2D plane ----
# Orthonormal basis from vector a
u = a / np.linalg.norm(a)             # first basis vector
v = b - np.dot(b, u) * u              # make b orthogonal to u
v = v / np.linalg.norm(v)             # second basis vector

# Coordinates of a and b in this 2D plane
a2d = np.array([np.dot(a, u), np.dot(a, v)])
b2d = np.array([np.dot(b, u), np.dot(b, v)])

# ---- Plot in 2D ----
plt.figure(figsize=(6,6))
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)

plt.quiver(0, 0, a2d[0], a2d[1], angles='xy', scale_units='xy', scale=1, color="r", label="a = (2,-1,1)")
plt.quiver(0, 0, b2d[0], b2d[1], angles='xy', scale_units='xy', scale=1, color="b", label="b = (3,4,-1)")

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.gca().set_aspect("equal")

plt.legend()
plt.savefig("/sdcard/Matrix/ee1030-2025/ai25btech11016/Matgeo/2.2.6/figs/2.2.6.png")
plt.show()
