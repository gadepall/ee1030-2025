import matplotlib.pyplot as plt
import numpy as np

# Solve for a and b
# Given midpoint = (1, 2a + 1)
# From equations: a = 2, b = 2
a, b = 2, 2

# Points
A = (2*a, 4)     # (4, 4)
B = (-2, 3*b)    # (-2, 6)
M = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)  # (1, 5)

# Plot line AB
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', label="Line AB")

# Plot points
plt.scatter(A[0], A[1], color='red', s=100, label=f"A{A}")
plt.scatter(B[0], B[1], color='green', s=100, label=f"B{B}")
plt.scatter(M[0], M[1], color='purple', s=150, marker='*', label=f"M{M}")

# Annotate points
plt.text(A[0]+0.2, A[1], f"A{A}")
plt.text(B[0]-1.5, B[1], f"B{B}")
plt.text(M[0]+0.2, M[1], f"M{M}")

# Axis labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Midpoint using Pure Python")

# Add grid + legend
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Show plot
plt.show()# give an absolute path
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/1.5.15/figs/figure2.png")
import matplotlib.pyplot as plt

# Solve for a and b
# Given midpoint = (1, 2a + 1)
# From equations: a = 2, b = 2
a, b = 2, 2

# Points
A = (2*a, 4)     # (4, 4)
B = (-2, 3*b)    # (-2, 6)
M = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)  # (1, 5)

# Plot line AB
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', label="Line AB")

# Plot points
plt.scatter(A[0], A[1], color='red', s=100, label=f"A{A}")
plt.scatter(B[0], B[1], color='green', s=100, label=f"B{B}")
plt.scatter(M[0], M[1], color='purple', s=150, marker='*', label=f"M{M}")

# Annotate points
plt.text(A[0]+0.2, A[1], f"A{A}")
plt.text(B[0]-1.5, B[1], f"B{B}")
plt.text(M[0]+0.2, M[1], f"M{M}")

# Axis labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Midpoint using Pure Python")

# Add grid + legend
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

import ctypes
import matplotlib.pyplot as plt
import numpy as np
# Load the shared library
lib = ctypes.CDLL("./midpoint.so")   # use "midpoint.dll" on Windows

# Define function signature
lib.midpoint.argtypes = [
    ctypes.c_float, ctypes.c_float,  # x1, y1
    ctypes.c_float, ctypes.c_float,  # x2, y2
    ctypes.POINTER(ctypes.c_float),  # mx
    ctypes.POINTER(ctypes.c_float)   # my
]

# Given values from problem
a, b = 2, 2
A = (2*a, 4)   # (4,4)
B = (-2, 3*b)  # (-2,6)

# Prepare variables to hold midpoint
mx, my = ctypes.c_float(), ctypes.c_float()

# Call the C function
lib.midpoint(A[0], A[1], B[0], B[1], ctypes.byref(mx), ctypes.byref(my))
M = (mx.value, my.value)

print(f"Midpoint from C: {M}")

# --- Plot ---
plt.figure(figsize=(6,6))
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', linewidth=2, label='Line AB')

# Scatter points
plt.scatter(*A, color='red', s=100, label=f"A{A}")
plt.scatter(*B, color='green', s=100, label=f"B{B}")
plt.scatter(*M, color='purple', s=120, marker='*', label=f"M{M}")

# Annotate
plt.text(A[0]+0.2, A[1]+0.2, f"A{A}", fontsize=10)
plt.text(B[0]+0.2, B[1]+0.2, f"B{B}", fontsize=10)
plt.text(M[0]+0.2, M[1]+0.2, f"M{M}", fontsize=10, color="purple")

# Axes formatting
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.title("Midpoint using C + Python")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# give an absolute path
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/1.5.15/figs/figure2.png")
# Show plot
plt.show()
