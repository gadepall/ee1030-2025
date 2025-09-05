import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os

# Load the shared library
lib = ctypes.CDLL(os.path.abspath("./libequidist.so"))
lib.equidist_check.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.equidist_check.restype  = ctypes.c_int

def is_on_bisector(x, y, tol=1e-9):
    """Check if point (x,y) satisfies 3x = 2y using C library"""
    return bool(lib.equidist_check(x, y, tol))

# Points A, B, midpoint
A = np.array([5, 1])
B = np.array([-1, 5])
midpoint = (A + B) / 2

# Equation: 3x=2y -> y=(3/2)x
x_vals = np.linspace(-2, 6, 200)
y_vals = (3/2) * x_vals

# Example points to check
points_to_check = [A, B, midpoint]

# Print verification results using C library
for p in points_to_check:
    result = is_on_bisector(p[0], p[1])
    print(f"Point {p} on bisector? {result}")

# Plotting
plt.figure(figsize=(6, 6))
plt.scatter(A[0], A[1], color='red', label='A(5,1)')
plt.scatter(B[0], B[1], color='blue', label='B(-1,5)')
plt.scatter(midpoint[0], midpoint[1], color='black', label='Midpoint')

# Perpendicular bisector line
plt.plot(x_vals, y_vals, 'g--', label='3x = 2y (Perp. bisector)')

# Mark example points
for p in points_to_check:
    plt.scatter(p[0], p[1], label=f"Point {p}")

# Decorations
plt.title("Perpendicular Bisector of A and B: 3x=2y")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

