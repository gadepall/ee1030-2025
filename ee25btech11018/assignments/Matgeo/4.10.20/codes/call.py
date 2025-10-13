import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load the shared library
lib = ctypes.CDLL("./perpendicular.so")

# Argument and return types
lib.perpendicularBisector.argtypes = [ctypes.c_float, ctypes.c_float,
                                      ctypes.c_float, ctypes.c_float,
                                      ctypes.POINTER(ctypes.c_float)]
lib.perpendicularBisector.restype = ctypes.c_float

lib.intersectionY.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_float]
lib.intersectionY.restype = ctypes.c_float

# Input points
Ax, Ay = -1.0, 1.0
Bx, By = 3.0, 3.0

# Prepare coeff array (a,b)
coeff = (ctypes.c_float * 2)()
c = lib.perpendicularBisector(Ax, Ay, Bx, By, coeff)

a, b = coeff[0], coeff[1]
print(f"Equation: {a:.1f}x + {b:.1f}y = {c:.1f}")

# Intersection with y-axis
y_inter = lib.intersectionY(coeff, c)
print(f"Intersection with y-axis: (0, {y_inter:.1f})")

# Plotting
# Original line AB
x_vals = np.array([Ax, Bx])
y_vals = np.array([Ay, By])

# Perpendicular bisector line: ax + by = c  -> y = (c - a*x)/b
x_line = np.linspace(-2, 5, 100)
y_line = (c - a * x_line) / b

plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, 'r--', label="Line AB")
plt.scatter([Ax, Bx], [Ay, By], color='red', label="Points A & B")

plt.plot(x_line, y_line, 'b-', label="Perpendicular Bisector")
plt.scatter([0], [y_inter], color='green', s=80, label="Intersection with y-axis")

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.legend()
plt.grid(True)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Perpendicular Bisector of AB and Intersection with Y-axis")
plt.show()

