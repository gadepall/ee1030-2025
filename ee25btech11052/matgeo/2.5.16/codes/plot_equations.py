import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("/home/shriyasnh/Desktop/matgeonew/2.5.16/codes/libequations.so")

lib.solve_equations.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.dot_product.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.dot_product.restype = ctypes.c_double

# Solve using C
p = ctypes.c_double()
lib.solve_equations(ctypes.byref(p))
print(f"Solution from C: p = {p.value}")

# Build direction vectors
m1 = np.array([-3.0, p.value, 2.0], dtype=np.double)
m2 = np.array([-3.0*p.value, 1.0, -5.0], dtype=np.double)

# Compute dot product with C
dot_val = lib.dot_product(m1.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                          m2.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
print(f"Dot product (should be 0): {dot_val}")

# Plot
fig = plt.figure(figsize=(7,6))
ax = fig.add_subplot(111, projection="3d")

origin = np.array([0, 0, 0])

# Draw vectors
ax.quiver(*origin, *m1, color="blue", linewidth=2, arrow_length_ratio=0.1, label="m1")
ax.quiver(*origin, *m2, color="red", linewidth=2, arrow_length_ratio=0.1, label="m2")

# Draw coordinate axes
axis_len = 6
ax.quiver(0,0,0, axis_len,0,0, color="black", arrow_length_ratio=0.05)
ax.quiver(0,0,0, 0,axis_len,0, color="black", arrow_length_ratio=0.05)
ax.quiver(0,0,0, 0,0,axis_len, color="black", arrow_length_ratio=0.05)

# Labels
ax.text(axis_len, 0, 0, "X", color="black")
ax.text(0, axis_len, 0, "Y", color="black")
ax.text(0, 0, axis_len, "Z", color="black")

ax.set_xlim([-6,6])
ax.set_ylim([-6,6])
ax.set_zlim([-6,6])
ax.set_box_aspect([1,1,1])  # Equal aspect ratio

ax.set_title("Direction Vectors (Lines Perpendicular at p=1)")
ax.legend()

plt.savefig("/home/shriyasnh/Desktop/matgeonew/2.5.16/figs/equations_solution.png", dpi=300, bbox_inches="tight")
plt.show()
