import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./libtriangle.so")  
lib.triangle_area.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
lib.triangle_area.restype = ctypes.c_double

A = np.array([2, 3], dtype=float)
B = np.array([3, 5], dtype=float)
C = np.array([4, 4], dtype=float)

p1 = (ctypes.c_double * 2)(*A)
p2 = (ctypes.c_double * 2)(*B)
p3 = (ctypes.c_double * 2)(*C)

area = lib.triangle_area(p1, p2, p3)
print(f"Area of triangle = {area:.2f}")

plt.figure(figsize=(6,6))

x_vals = [A[0], B[0], C[0], A[0]]
y_vals = [A[1], B[1], C[1], A[1]]
plt.plot(x_vals, y_vals, 'g-', linewidth=2)
plt.fill(x_vals, y_vals, color='lightgreen', alpha=0.4)

plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], c='red')
plt.text(A[0], A[1], "A(2,3)", fontsize=12, ha='right')
plt.text(B[0], B[1], "B(3,5)", fontsize=12, ha='left')
plt.text(C[0], C[1], "C(4,4)", fontsize=12, ha='left')

cx = (A[0] + B[0] + C[0]) / 3
cy = (A[1] + B[1] + C[1]) / 3

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Triangle Area")
plt.grid(True)

plt.savefig("../figs/img.png", dpi=300)
