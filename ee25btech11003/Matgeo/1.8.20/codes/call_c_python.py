import ctypes
import sys
import matplotlib.pyplot as plt
import numpy as np

# Load the compiled shared library
lib = ctypes.CDLL("./libslope.so")

# Define the argument and return types for the C function
lib.perpendicularSlope.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]
lib.perpendicularSlope.restype = ctypes.c_float


# Input points

# Input points
x1, y1 = 3.0, 6.0
x2, y2 = -3.0, 4.0

# Call the C function
perpslope = lib.perpendicularSlope(x1, y1, x2, y2)


A = (x1,y1)
B = (x2,y2)
M = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)

# Plot line segment AB
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', label='Line segment AB')

# Plot points A, B, and M
plt.scatter(*A, color='red', label='A(3,6)')
plt.scatter(*B, color='green', label='B(-3,4)')
plt.scatter(*M, color='purple', marker='x', s=100, label='Midpoint M(0,5)')

# Annotate points
plt.text(A[0]+0.2, A[1], 'A(3,6)', fontsize=10)
plt.text(B[0]-1, B[1]-0.3, 'B(-3,4)', fontsize=10)
plt.text(M[0]+0.2, M[1], 'M(0,5)', fontsize=10, color='purple')

# Perpendicular bisector: y = 5 - 3x
x_vals = np.linspace(-5, 5, 400)
y_vals = 5 + perpslope*x_vals
plt.plot(x_vals, y_vals, 'r--', label='Perpendicular bisector (y+3x=5)')

# Axes, grid, legend
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.title("Line Segment AB with Midpoint M and Perpendicular Bisector")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.axis('equal')

plt.show()
plt.savefig("fig1.png")
