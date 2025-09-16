import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the shared library
lib = ctypes.CDLL("./libdot.so")

# Define function signature
lib.dot_product.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.double),
    np.ctypeslib.ndpointer(dtype=np.double),
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_double)
]

# Vectors
l, m = 0.6, 0.8
dl, dm = 0.1, -0.05

v1 = np.array([l, m], dtype=np.double)
v2 = np.array([l+dl, m+dm], dtype=np.double)

# Call C function for dot product
res = ctypes.c_double()
lib.dot_product(v1, v2, 2, ctypes.byref(res))
dot = res.value

# Normalize
v1u = v1 / np.linalg.norm(v1)
v2u = v2 / np.linalg.norm(v2)

# Angle between vectors
theta = np.arccos(np.clip(dot / (np.linalg.norm(v1) * np.linalg.norm(v2)), -1.0, 1.0))

# Angles relative to x-axis
a1 = np.arctan2(v1u[1], v1u[0])
a2 = np.arctan2(v2u[1], v2u[0])
start, end = sorted([a1, a2])

# Plot
fig, ax = plt.subplots(figsize=(6,6))

ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='b', label='(l,m)')
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='r', label='(l+dl,m+dm)')

# Arc for angle
r = 0.3
arc_angles = np.linspace(start, end, 100)
arc_x = r * np.cos(arc_angles)
arc_y = r * np.sin(arc_angles)
ax.plot(arc_x, arc_y, 'k-')

# Label theta
mid = (start + end) / 2
ax.text(0.35*np.cos(mid), 0.35*np.sin(mid), r'$\theta$', fontsize=14)

# Formatting
ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1.2)
ax.set_aspect('equal')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Angle between two vectors (C + Python)")
ax.legend()
ax.grid(True)

plt.savefig("vectors.png", dpi=300)
plt.show()
