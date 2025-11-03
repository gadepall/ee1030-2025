import numpy as np
import ctypes
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./c8.so")
lib.plane_point.argtypes = [
    ctypes.c_double,
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double)
]

plane_n = np.array([20.0, 23.0, 26.0], dtype=np.float64)
constant = 69.0

grid_size = 50
x_vals = np.linspace(-10, 10, grid_size)
y_vals = np.linspace(-10, 10, grid_size)

points = np.zeros((grid_size*grid_size, 3), dtype=np.float64)

idx = 0
for x in x_vals:
    for y in y_vals:
        lib.plane_point(
            ctypes.c_double(x),
            ctypes.c_double(y),
            plane_n.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            ctypes.c_double(constant),
            points[idx].ctypes.data_as(ctypes.POINTER(ctypes.c_double))
        )
        idx += 1

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

X = points[:,0].reshape(grid_size, grid_size)
Y = points[:,1].reshape(grid_size, grid_size)
Z = points[:,2].reshape(grid_size, grid_size)

ax.plot_surface(X, Y, Z, alpha=0.5, color='cyan')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Plane (20,23,26)·x=69 using c8.so')

plt.show()

