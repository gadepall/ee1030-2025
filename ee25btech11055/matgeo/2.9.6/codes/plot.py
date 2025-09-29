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

DoubleArray3 = ctypes.c_double * 3
o = DoubleArray3(0, 0, 0)
a = DoubleArray3(8, 0, 0)
b = DoubleArray3((27**0.5) / 2, 1.5, 0)

vec1 = np.array([8, 0, 0]).T
vec2 = np.array([(27**0.5) / 2, 1.5, 0]).T
cross = np.cross(vec1,vec2)

c = DoubleArray3(cross[0],cross[1],cross[2])



fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

t_values = np.linspace(0, 1, 100)
line_points_x, line_points_y, line_points_z = [], [], []

for t in t_values:
    result_arr = DoubleArray3()

    get_point(o, a, t, result_arr)

    line_points_x.append(result_arr[0])
    line_points_y.append(result_arr[1])
    line_points_z.append(result_arr[2])

ax.plot(
    line_points_x,
    line_points_y,
    line_points_z,
    color="red",
    label="a",
)

t_values = np.linspace(0, 1, 100)
line_points_x, line_points_y, line_points_z = [], [], []

for t in t_values:
    result_arr = DoubleArray3()

    get_point(o, b, t, result_arr)

    line_points_x.append(result_arr[0])
    line_points_y.append(result_arr[1])
    line_points_z.append(result_arr[2])

ax.plot(
    line_points_x,
    line_points_y,
    line_points_z,
    color="blue",
    label="b",
)

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
    color="green",
    label="axb",
)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("2.9.6")
ax.legend()
ax.grid(True)

plt.savefig("../figs/plot.png")
plt.show()
