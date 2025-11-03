import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./liblines.so")

# Define argument and return types
lib.are_perpendicular.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.are_perpendicular.restype = ctypes.c_int

# Coefficients [a, b, c]
line1 = np.array([2.0, 3.0, 1.0], dtype=np.double)
line2 = np.array([3.0, -2.0, 3.0], dtype=np.double)

# Call C function
result = lib.are_perpendicular(line1.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                               line2.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
print("Perpendicular?" , "Yes" if result == 1 else "No")

# Create x values
x = np.linspace(-30, 30, 800)

# Line equations: ax + by + c = 0 => y = -(a*x + c)/b
y1 = -(line1[0]*x + line1[2]) / line1[1]
y2 = -(line2[0]*x + line2[2]) / line2[1]

plt.figure(figsize=(8,8))
plt.plot(x, y1, color="blue")
plt.plot(x, y2, color="green")

# Add text labels near the middle of each line
mid = len(x) // 2
plt.text(x[mid], y1[mid], f"{line1[0]}x + {line1[1]}y + {line1[2]} = 0",
         color="blue", fontsize=10, backgroundcolor="white")
plt.text(x[mid], y2[mid], f"{line2[0]}x + {line2[1]}y + {line2[2]} = 0",
         color="green", fontsize=10, backgroundcolor="white")

# Axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Adjust to 30x30 view
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Solve intersection point
A = np.array([[line1[0], line1[1]], [line2[0], line2[1]]], dtype=float)
b = -np.array([line1[2], line2[2]], dtype=float)
intersection = np.linalg.solve(A, b)

# Mark intersection
plt.scatter(*intersection, color="red", zorder=5)
plt.text(intersection[0], intersection[1], f"({intersection[0]:.1f}, {intersection[1]:.1f})", color="red")

plt.grid(True)
plt.title("Given Lines (30x30 View)")
plt.savefig("../figs/img")

