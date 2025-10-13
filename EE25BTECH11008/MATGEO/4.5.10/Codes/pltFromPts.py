import numpy as np
import ctypes
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./pts.so")

lib.line_point.argtypes = [ctypes.c_double,
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double)]

h = np.array([1.0, 2.0, 3.0], dtype=np.float64)
m = np.array([3.0, 2.0, -2.0], dtype=np.float64)

kappa_values = np.linspace(-2, 2, 100)

points = np.zeros((len(kappa_values), 3), dtype=np.float64)

for i, k in enumerate(kappa_values):
    lib.line_point(ctypes.c_double(k),
                   h.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                   m.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                   points[i].ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(points[:,0], points[:,1], points[:,2], color='blue')
ax.scatter(h[0], h[1], h[2], color='red', s=50)
ax.text(h[0], h[1], h[2], '(1,2,3)', color='red')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Line through (1,2,3) parallel to [3,2,-2]')

plt.show()
