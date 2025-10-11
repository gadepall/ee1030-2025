import ctypes
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./code.so")
lib.findArea.argtypes = [
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double
]
lib.findArea.restype = ctypes.c_double

# Correct order for function: A, B, C, D
A = (-4, -5)
B = (-1, -6)
C = (-5, 7)
D = (4, 5)

area = lib.findArea(A[0], A[1], B[0], B[1], C[0], C[1], D[0], D[1])

# For plotting, reorder to A, B, D, C to avoid bow-tie
plot_points = [A, B, D, C, A]
x = [p[0] for p in plot_points]
y = [p[1] for p in plot_points]

plt.fill(x, y, alpha=0.3, color="skyblue", edgecolor="black")
plt.scatter(x, y, color="red")

labels = ["A(-4,-5)", "B(-1,-6)", "D(4,5)", "C(-5,7)"]
for xi, yi, lbl in zip(x[:-1], y[:-1], labels):
    plt.text(xi, yi, lbl, fontsize=9, ha="right")

plt.title(f"Quadrilateral ABCD, Area={area}")
plt.gca().set_aspect("equal", adjustable="box")
plt.show()

