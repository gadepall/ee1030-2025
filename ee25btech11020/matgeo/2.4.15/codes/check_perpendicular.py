import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./libcheck.so")  

lib.check_perpendicular.argtypes = [ctypes.c_double, ctypes.c_double,
                                    ctypes.c_double, ctypes.c_double,
                                    ctypes.c_double, ctypes.c_double,
                                    ctypes.c_double, ctypes.c_double]
lib.check_perpendicular.restype = ctypes.c_int

A = np.array([3, -4])
B = np.array([-2, 6])
C = np.array([-3, 6])
D = np.array([9, -18])

result = lib.check_perpendicular(A[0], A[1], B[0], B[1], C[0], C[1], D[0], D[1])

if result == 1:
    print("The lines are perpendicular.")
else:
    print("The lines are NOT perpendicular.")

plt.figure(figsize=(6,6))

plt.plot([A[0], B[0]], [A[1], B[1]], 'r-', label="Line AB")
plt.scatter([A[0], B[0]], [A[1], B[1]], c='r')

plt.plot([C[0], D[0]], [C[1], D[1]], 'b-', label="Line CD")
plt.scatter([C[0], D[0]], [C[1], D[1]], c='b')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.title("Line AB vs Line CD")
plt.grid(True)

plt.savefig("../figs/cplot.png", dpi=300)
