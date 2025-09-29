import ctypes
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

libline = ctypes.CDLL("./line.so")
libvec = ctypes.CDLL("./vector.so")

get_point = libline.point_gen
get_point.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # P1
    ctypes.POINTER(ctypes.c_double),  # P2
    ctypes.c_double,  # t
    ctypes.POINTER(ctypes.c_double),  # result_point
]
get_point.restype = None

add = libvec.vec_sum
add.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # vec1
    ctypes.POINTER(ctypes.c_double),  # vec2
    ctypes.POINTER(ctypes.c_double),  # sum
]
add.restype = None

diff = libvec.vec_diff
diff.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
]
diff.restype = None

DoubleArray3 = ctypes.c_double * 3
o = DoubleArray3(0, 0, 0)
a = DoubleArray3(1, 2, -3)
b = DoubleArray3(3, -1, 2)
c = DoubleArray3()
d = DoubleArray3()

add(a, b, c)
diff(a, b, d)


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

t_values = np.linspace(0, 1, 100)
line_points_x, line_points_y, line_points_z = [], [], []

for t in t_values:
    result_arr = DoubleArray3()

    get_point(o, c, t, result_arr)

    line_points_x.append(result_arr[0])
    line_points_y.append(result_arr[1])
    line_points_z.append(result_arr[2])

ax.plot(
    line_points_x,
    line_points_y,
    line_points_z,
    color="blue",
    label="a+b",
)

t_values = np.linspace(0, 1, 100)
line_points_x, line_points_y, line_points_z = [], [], []

for t in t_values:
    result_arr = DoubleArray3()

    get_point(o, d, t, result_arr)

    line_points_x.append(result_arr[0])
    line_points_y.append(result_arr[1])
    line_points_z.append(result_arr[2])

ax.plot(
    line_points_x,
    line_points_y,
    line_points_z,
    color="green",
    label="a-b",
)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("2.5.18")
ax.legend()
ax.grid(True)

plt.savefig("../figs/plot.png")
plt.show()
