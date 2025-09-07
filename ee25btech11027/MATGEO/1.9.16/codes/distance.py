import numpy as np
import ctypes
import matplotlib.pyplot as plt

# Load shared C library
lib = ctypes.CDLL("./distance.so")
lib.distance.argtypes = [ctypes.c_float, ctypes.c_float]
lib.distance.restype = ctypes.c_float

# Example values
a, b = 4, 4  # change as needed

# Call C function
dist = lib.distance(a, b)
print(f"Distance between ({a},{b}) and (-{a},-{b}) = {dist}")

# Coordinates
x1, y1 = a, b
x2, y2 = -a, -b

# Plot
plt.figure(figsize=(6,6))

# Line between points
plt.plot([x1, x2], [y1, y2], "b-", label=f"Distance = {dist:.2f}")

# Point  
plt.scatter(x1, y1, color="red", s=100, label=f"A({x1}, {y1})")
plt.scatter(x2, y2, color="green", s=100, label=f"B({x2}, {y2})")

# Labels near points
plt.text(x1+0.2, y1, f"A({x1}, {y1})", fontsize=10, color="red")
plt.text(x2-1.5, y2, f"B({x2}, {y2})", fontsize=10, color="green")

# Axes + Grid
plt.axhline(0, color="black", linewidth=0.7)
plt.axvline(0, color="black", linewidth=0.7)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Distance using C + Python")
plt.grid(True)
plt.legend()
plt.savefig("/media/indhiresh-s/New Volume/matgeo/figs/figure1.png")
plt.show()

