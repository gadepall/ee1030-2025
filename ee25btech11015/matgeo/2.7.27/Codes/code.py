import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os

# --- Load the C library ---
try:
    c_lib = ctypes.CDLL('./code.so')
except OSError:
    print("Error: 'code.so' not found. Compile using: gcc -shared -o code.so -fPIC triangle.c")
    exit()

# Define argument and return types
c_lib.triangle_area.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float,
                                ctypes.c_float, ctypes.c_float, ctypes.c_float,
                                ctypes.c_float, ctypes.c_float, ctypes.c_float]
c_lib.triangle_area.restype = ctypes.c_float

# --- Given points (2D extended to 3D with z=0) ---
A = np.array([2, 5, 0], dtype=np.float32)
B = np.array([4, 7, 0], dtype=np.float32)
C = np.array([6, 2, 0], dtype=np.float32)

# --- Call C function ---
area = c_lib.triangle_area(A[0], A[1], A[2],
                           B[0], B[1], B[2],
                           C[0], C[1], C[2])
print(f"✅ Area of triangle = {area:.2f}")

# --- Plotting in 2D ---
fig, ax = plt.subplots(figsize=(6,6))

# Plot triangle edges
ax.plot([A[0], B[0]], [A[1], B[1]], color="black")
ax.plot([B[0], C[0]], [B[1], C[1]], color="black")
ax.plot([C[0], A[0]], [C[1], A[1]], color="black")

# Fill triangle
ax.fill([A[0], B[0], C[0]], [A[1], B[1], C[1]], color="cyan", alpha=0.3)

# Points
ax.scatter(A[0], A[1], color="red", s=60)
ax.scatter(B[0], B[1], color="blue", s=60)
ax.scatter(C[0], C[1], color="green", s=60)

# Labels
ax.text(A[0]+0.1, A[1], "A(2,5)", color="red")
ax.text(B[0]+0.1, B[1], "B(4,7)", color="blue")
ax.text(C[0]+0.1, C[1], "C(6,2)", color="green")

# Area annotation
ax.text(3.5, 4.5, f"Area = {area:.2f}", color="purple", fontsize=12)

# Formatting
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Triangle ABC in 2D plane")
ax.grid(True)
ax.set_aspect("equal")

plt.show()
