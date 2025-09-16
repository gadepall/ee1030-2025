import ctypes
import matplotlib.pyplot as plt

# Load the shared library (in the same folder)
lib = ctypes.CDLL("./function.so")
lib.distance2d.argtypes = (ctypes.c_double, ctypes.c_double,
                           ctypes.c_double, ctypes.c_double)
lib.distance2d.restype = ctypes.c_double

# Points
A = (0.0, 5.0)
B = (-5.0, 0.0)

# Call the C function
d = lib.distance2d(A[0], A[1], B[0], B[1])
print("Distance ||B - A|| =", d)

# Plot
plt.scatter([A[0], B[0]], [A[1], B[1]], s=60)
plt.plot([A[0], B[0]], [A[1], B[1]], linewidth=2)

plt.title(f"Distance ||B - A|| = {d:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)

import os

# Build the path: one folder out (..), then into figures/
save_path = os.path.join("..", "figures", "distancenew.png")

plt.savefig(save_path, dpi=150)

plt.show()
