import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL('./libplane.so')

# Define argument and return types
lib.find_plane.argtypes = [
    ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,
    ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,
    ctypes.POINTER(ctypes.c_float)
]

# Input from user
print("Enter coefficients of Plane 1 (a1 b1 c1 d1): ")
a1, b1, c1, d1 = map(float, input().split())
print("Enter coefficients of Plane 2 (a2 b2 c2 d2): ")
a2, b2, c2, d2 = map(float, input().split())

# Output array
res = (ctypes.c_float * 5)()
lib.find_plane(a1, b1, c1, d1, a2, b2, c2, d2, res)

lam, a, b, c, d = [res[i] for i in range(5)]
print(f"\nλ = {lam:.2f}")
print(f"Required plane: {a:.2f}x + {b:.2f}y + {c:.2f}z = {d:.2f}")

# ---- Plotting Section ----
rng = np.linspace(-6, 6, 60)
X, Y = np.meshgrid(rng, rng)

Z1 = (a1 * X + b1 * Y - d1) / (-c1)
Z2 = (a2 * X + b2 * Y - d2) / (-c2)
Z3 = (a * X + b * Y - d) / (-c)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z1, color='skyblue', alpha=0.5)
ax.plot_surface(X, Y, Z2, color='lightgreen', alpha=0.5)
ax.plot_surface(X, Y, Z3, color='salmon', alpha=0.6)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Plane through Intersection (Equal X and Z Intercepts)')
ax.view_init(elev=28, azim=45)
plt.tight_layout()
plt.show()
