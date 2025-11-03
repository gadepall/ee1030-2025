import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./plane_distance.so")  

lib.plane_from_points.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

lib.parallel_plane_through_point.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

lib.plane_distance.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_double,
    ctypes.c_double
]
lib.plane_distance.restype = ctypes.c_double

A = [1, 1, -2]  # Given vector A
B = [2, -1, 1]  # Given vector B
C = [1, 2, 1]   # Given vector C
P = [2, 3, 7]   # Point P for the parallel plane

A_c = (ctypes.c_double * 3)(*A)
B_c = (ctypes.c_double * 3)(*B)
C_c = (ctypes.c_double * 3)(*C)
P_c = (ctypes.c_double * 3)(*P)

coeff1 = (ctypes.c_double * 4)()
lib.plane_from_points(A_c, B_c, C_c, coeff1)
plane1 = np.array(coeff1[:])

coeff2 = (ctypes.c_double * 4)()
lib.parallel_plane_through_point(coeff1, P_c, coeff2)
plane2 = np.array(coeff2[:])

a, b, c, d1 = plane1
a2, b2, c2, d2 = plane2

n = np.array([a, b, c], dtype=np.double)
dist = lib.plane_distance(n.ctypes.data_as(ctypes.POINTER(ctypes.c_double)), d1, d2)
print(f"Distance between planes: {dist:.4f}")

xx, yy = np.meshgrid(np.linspace(-2, 3, 30), np.linspace(-2, 4, 30))
zz1 = (-d1 - a * xx - b * yy) / c
zz2 = (-d2 - a2 * xx - b2 * yy) / c2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=25, azim=45)

ax.plot_surface(xx, yy, zz1, alpha=0.5, color='blue')
ax.plot_surface(xx, yy, zz2, alpha=0.5, color='green')

points = np.array([A, B, C, P])
labels = ["A", "B", "C", "P"]
for (x, y, z), label in zip(points, labels):
    ax.scatter(x, y, z, color='red', s=50)
    ax.text(x, y, z, label, color='black')

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"Two Planes and Distance = {dist:.4f}")

plt.show()

