import ctypes
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

libline = ctypes.CDLL("./line.so")

get_point = libline.point_gen
get_point.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # P1
    ctypes.POINTER(ctypes.c_double),  # P2
    ctypes.c_double,  # t
    ctypes.POINTER(ctypes.c_double),  # result_point
]
get_point.restype = None

lib = ctypes.CDLL("./plane.so")

lib.generate_plane_points.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_int,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_int,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
]
lib.generate_plane_points.restype = None

DoubleArray3 = ctypes.c_double * 3

a = DoubleArray3(2, -1, 2)
b = DoubleArray3(5, 3, 4)
p = DoubleArray3(2, 0, 3)
q = DoubleArray3(1, 1, 5)
r = DoubleArray3(3, 2, 4)

l1 = DoubleArray3(-28, -41, -18)
l2 = DoubleArray3(32, 39, 22)
n = DoubleArray3(0.2, -0.2, 0.2)
c = 1

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

t_values = np.linspace(0, 1, 100)
line_points_x, line_points_y, line_points_z = [], [], []

for t in t_values:
    result_arr = DoubleArray3()

    get_point(l1, l2, t, result_arr)

    line_points_x.append(result_arr[0])
    line_points_y.append(result_arr[1])
    line_points_z.append(result_arr[2])

ax.plot(
    line_points_x,
    line_points_y,
    line_points_z,
    color="green",
)

x_steps, y_steps = 70, 70
total_points = x_steps * y_steps
x_plane = np.zeros(total_points, dtype=np.double)
y_plane = np.zeros(total_points, dtype=np.double)
z_plane = np.zeros(total_points, dtype=np.double)

lib.generate_plane_points(
    x_plane.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    y_plane.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    z_plane.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    -5.0,
    5.0,
    x_steps,
    -5.0,
    5.0,
    y_steps,
    n[0],
    n[1],
    n[2],
    c,
)

ax.scatter(x_plane, y_plane, z_plane, alpha=0.1)

ax.scatter(b[0], b[1], b[2], color="blue", label="B")
ax.scatter(a[0], a[1], a[2], color="red", label="A")
ax.scatter(13 / 5, -1 / 5, 12 / 5, color="yellow", label="Point")

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("4.11.32")
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])
ax.legend()
ax.grid(True)

plt.savefig("../figs/plot.png")
plt.show()
