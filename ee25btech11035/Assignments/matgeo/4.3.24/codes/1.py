import ctypes
import math
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./1.so")

# Function signatures
lib.findRatio.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int,
                          ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.findRatio.restype = ctypes.c_double

lib.findDivisionPoint.argtypes = [ctypes.c_double,
                                  ctypes.c_int, ctypes.c_int,
                                  ctypes.c_int, ctypes.c_int,
                                  ctypes.POINTER(ctypes.c_double),
                                  ctypes.POINTER(ctypes.c_double)]
lib.findDivisionPoint.restype = None

# Example: line 2x+3y-5=0 and points A(8,-9), B(2,1)
a, b, c = 2, 3, -5
x1, y1 = 8, -9
x2, y2 = 2, 1

# Call C function to get ratio
k = lib.findRatio(a, b, c, x1, y1, x2, y2)
print(f"Ratio: {k:.6f} : 1")

# Call C function to get division point
px = ctypes.c_double()
py = ctypes.c_double()
lib.findDivisionPoint(k, x1, y1, x2, y2, ctypes.byref(px), ctypes.byref(py))
print(f"Point of division: ({px.value:.6f}, {py.value:.6f})")

# ---------- Plotting ----------
# Line segment AB
plt.plot([x1, x2], [y1, y2], 'b--', label="Segment AB")

# Division point
plt.scatter([px.value], [py.value], color='red', zorder=5, label="Division Point")

# Endpoints
plt.scatter([x1, x2], [y1, y2], color='green', label="Endpoints A,B")

# Line 2x + 3y - 5 = 0
import numpy as np
xx = np.linspace(min(x1,x2)-2, max(x1,x2)+2, 100)
yy = (-(a*xx + c))/b  # from ax+by+c=0 → y=-(ax+c)/b
plt.plot(xx, yy, 'k-', label="Line 2x+3y-5=0")

# Decorations
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Line, Segment, and Division Point")
plt.savefig('1.png')
plt.show()
