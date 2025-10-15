import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared C library
lib = ctypes.CDLL("./trianglearea.so")
lib.triangle_area.argtypes = [ctypes.c_float, ctypes.c_float,
                              ctypes.c_float, ctypes.c_float,
                              ctypes.c_float, ctypes.c_float]
lib.triangle_area.restype = ctypes.c_float

# Fixed Vertices
B = (2, 0)
C = (0, -2)

# Vertices for the two possible values of k
A1 = (0, 0)  # k = 0
A2 = (4, 0)  # k = 4


# --- Call C function to calculate and verify areas ---
area1 = lib.triangle_area(A1[0], A1[1], B[0], B[1], C[0], C[1])
print(f"Area for k=0 (from C): {area1}")

area2 = lib.triangle_area(A2[0], A2[1], B[0], B[1], C[0], C[1])
print(f"Area for k=4 (from C): {area2}")


# --- Plotting ---
# Coordinates for triangle 1 (k=0)
x1 = [A1[0], B[0], C[0], A1[0]]
y1 = [A1[1], B[1], C[1], A1[1]]

# Coordinates for triangle 2 (k=4)
x2 = [A2[0], B[0], C[0], A2[0]]
y2 = [A2[1], B[1], C[1], A2[1]]


plt.plot(x1, y1, 'bo-', label='Triangle (k=0)')
plt.plot(x2, y2, 'mo-', label='Triangle (k=4)')


# Labeling points
plt.text(A1[0], A1[1] + 0.2, "A(0,0)", fontsize=10, ha="center")
plt.text(A2[0], A2[1] + 0.2, "A(4,0)", fontsize=10, ha="center")
plt.text(B[0], B[1] - 0.4, "B(2,0)", fontsize=10, ha="center")
plt.text(C[0], C[1] - 0.4, "C(0,-2)", fontsize=10, ha="center")

plt.title("Triangles with Area = 2 sq. units (plotted with C library)")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()
