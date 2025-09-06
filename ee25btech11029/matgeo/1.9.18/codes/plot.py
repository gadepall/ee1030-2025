import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared object
lib = ctypes.CDLL("./libline.so")

# Define function signature
lib.distance.argtypes = [ctypes.c_double, ctypes.c_double,
                         ctypes.c_double, ctypes.c_double]
lib.distance.restype = ctypes.c_double

# Fixed point A
A = (0, 0)

# Two B points
B1 = (3, -4)
B2 = (-3, 4)

# Distances from A using C function
d1 = lib.distance(A[0], A[1], B1[0], B1[1])
d2 = lib.distance(A[0], A[1], B2[0], B2[1])
# Plot line segments A->B1 and A->B2
plt.figure(figsize=(6,6))

# Line A->B1
plt.plot([A[0], B1[0]], [A[1], B1[1]], 'b-o', label=f"A→B1 {B1}, d={d1:.2f}")
plt.text(B1[0], B1[1], f"B1{B1}", fontsize=12, ha='left')

# Line A->B2
plt.plot([A[0], B2[0]], [A[1], B2[1]], 'g-o', label=f"A→B2 {B2}, d={d2:.2f}")
plt.text(B2[0], B2[1], f"B2{B2}", fontsize=12, ha='left')

# Mark A
plt.scatter(A[0], A[1], color='red')
plt.text(A[0], A[1], "A(0,0)", fontsize=12, ha='right')

# Labels & styling
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Segments from A(0,0) to B1 and B2")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.savefig('figs/distance.png')
plt.show(block=True)
