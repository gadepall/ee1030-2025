import ctypes
import numpy as np
import matplotlib.pyplot as plt


lib = ctypes.CDLL("./libquad.so")


lib.triangle_area.argtypes = [ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double]
lib.triangle_area.restype = ctypes.c_double
lib.quad_area.argtypes = [ctypes.c_double, ctypes.c_double,
                          ctypes.c_double, ctypes.c_double,
                          ctypes.c_double, ctypes.c_double,
                          ctypes.c_double, ctypes.c_double]
lib.quad_area.restype = ctypes.c_double

# Vertices of quadrilateral
A = (-3.0, -1.0)
B = (-2.0, -4.0)
C = (4.0, -1.0)
D = (3.0, 4.0)


area = lib.quad_area(A[0], A[1], B[0], B[1], C[0], C[1], D[0], D[1])
print("Area of Quadrilateral ABCD =", area)
points = np.array([A, B, C, D, A])  
plt.plot(points[:,0], points[:,1], 'b-o')
plt.fill(points[:,0], points[:,1], color='skyblue', alpha=0.5)
plt.text(A[0], A[1], "A")
plt.text(B[0], B[1], "B")
plt.text(C[0], C[1], "C")
plt.text(D[0], D[1], "D")

plt.title(f"Quadrilateral ABCD (Area = {area:.2f})")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.savefigs("/Users/bhargavkrish/Documents/ee1030-2025/ee25btech11013/matgeo/2.7.25/figs/Figure_1.png")
plt.show()