import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load the compiled C shared library
lib = ctypes.CDLL("./point.so")

# Set argument and return types
lib.computeX1.argtypes = [ctypes.c_double, ctypes.c_double]
lib.computeX1.restype = ctypes.c_double

lib.computeX2.argtypes = [ctypes.c_double, ctypes.c_double]
lib.computeX2.restype = ctypes.c_double

lib.computeY.argtypes = [ctypes.c_double]
lib.computeY.restype = ctypes.c_double

lib.checkRelation.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.checkRelation.restype = ctypes.c_int

# Example values (you can change these)
a, b, c, d = 1.0, 1.0, -2.0, -3.0

# Call C functions
x1 = lib.computeX1(a, c)
x2 = lib.computeX2(b, d)

if abs(x1 - x2) > 1e-6:
    print("Inconsistent intersection: x1 != x2")
    exit()

x = x1
y = lib.computeY(x)

print(f"Intersection Point: ({x:.3f}, {y:.3f})")

# Check relation
if lib.checkRelation(a, b, c, d):
    print("Relation satisfied: 3bc - 2ad = 0 ")
else:
    print("Relation NOT satisfied ")

# ---------- Plotting ----------
X = np.linspace(-10, 10, 400)

# Line1: 4ax + 2ay + c = 0 -> y = -(4aX + c)/(2a)
Y1 = -(4*a*X + c) / (2*a)

# Line2: 5bx + 2by + d = 0 -> y = -(5*bX + d)/(2*b)
Y2 = -(5*b*X + d) / (2*b)

plt.figure(figsize=(6,6))
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.plot(X, Y1, label="Line 1")
plt.plot(X, Y2, label="Line 2")
plt.scatter([x], [y], color="red", s=80, label="Intersection Point")

plt.title("Intersection of Two Lines")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True)
plt.show()

