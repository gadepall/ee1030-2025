import ctypes
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np


lib = ctypes.CDLL('./libcollinearity.so')
lib.check_collinearity.argtypes = [ctypes.c_double, ctypes.c_double,
                                   ctypes.c_double, ctypes.c_double,
                                   ctypes.c_double, ctypes.c_double,
                                   ctypes.c_double]
lib.check_collinearity.restype = ctypes.c_int

def check_collinearity(A, B, C, tol=1e-9):
    return lib.check_collinearity(A[0], A[1], B[0], B[1], C[0], C[1], tol)


A = (1,5)
B = (2,3)
C = (-2,-11)

is_collinear = check_collinearity(A, B, C)
print("Collinear" if is_collinear else "Not collinear")


plt.figure(figsize=(8, 8))


x_line = np.linspace(min(A[0], C[0]) - 1, max(A[0], C[0]) + 1, 100)
slope = (C[1] - A[1]) / (C[0] - A[0])
y_line = A[1] + slope * (x_line - A[0])
plt.plot(x_line, y_line, 'k--', label="Line through A & C")


plt.plot(A[0], A[1], 'ro', label='A')
plt.plot(B[0], B[1], 'go', label='B')
plt.plot(C[0], C[1], 'bo', label='C')

plt.text(A[0]+0.2, A[1], f"A{A}", fontsize=12)
plt.text(B[0]+0.2, B[1], f"B{B}", fontsize=12)
plt.text(C[0]+0.2, C[1], f"C{C}", fontsize=12)

mp.use("TkAgg")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Collinearity Check')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

plt.savefig("/home/shriyasnh/Desktop/matgeo/1.6.3/codes", dpi=300, bbox_inches='tight')
plt.show()
