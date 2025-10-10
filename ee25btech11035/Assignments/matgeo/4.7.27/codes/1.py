import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load shared library
lib = ctypes.CDLL("./1.so")

# Define argument and return types
lib.perpendicularLine.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                  ctypes.c_int, ctypes.c_int,
                                  ctypes.POINTER(ctypes.c_int),
                                  ctypes.POINTER(ctypes.c_int),
                                  ctypes.POINTER(ctypes.c_int)]

# Inputs: line y = x → x - y = 0 → (a=1, b=-1, c=0), point (3,2)
a, b, c = 1, -1, 0
x0, y0 = 3, 2

# Prepare output variables
A = ctypes.c_int()
B = ctypes.c_int()
C = ctypes.c_int()

# Call C function
lib.perpendicularLine(a, b, c, x0, y0,
                      ctypes.byref(A), ctypes.byref(B), ctypes.byref(C))

print("Equation of perpendicular line: {}x + {}y + {} = 0".format(A.value, B.value, C.value))

# ----- PLOT -----
# Original line: y = x
x_vals = np.linspace(0, 6, 100)
y_given = x_vals

# Perpendicular line: A*x + B*y + C = 0 -> y = (-A*x - C)/B
y_perp = (-A.value * x_vals - C.value) / B.value

plt.figure(figsize=(6,6))
plt.plot(x_vals, y_given, 'r--', label="Given line y = x")
plt.plot(x_vals, y_perp, 'b-', label="Perpendicular line")

# Plot point
plt.scatter(x0, y0, color='black')
plt.text(x0+0.1, y0+0.1, f"({x0},{y0})", fontsize=10)

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Given line (dashed), Perpendicular line (solid), Point (3,2)")
plt.grid(True)
plt.axis("equal")
plt.savefig('2.png')
plt.show()
