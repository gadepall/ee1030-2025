import ctypes
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

lib = ctypes.CDLL("./line.so")

get_point = lib.point_gen
get_point.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # P1
    ctypes.POINTER(ctypes.c_double),  # P2
    ctypes.c_double,  # t
    ctypes.POINTER(ctypes.c_double),  # result_point
]
get_point.restype = None

DoubleArray3 = ctypes.c_double * 3
P1_arr = DoubleArray3(0, 0, 0)
P2_arr = DoubleArray3(1, 1, -1)

t_values = np.linspace(0, 1, 100)
line_points_x, line_points_y, line_points_z = [], [], []

for t in t_values:
    result_arr = DoubleArray3()

    get_point(P1_arr, P2_arr, t, result_arr)

    line_points_x.append(result_arr[0])
    line_points_y.append(result_arr[1])
    line_points_z.append(result_arr[2])

point = np.array([1, 1, -1])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

x, y, z = point
ax.scatter(
    x,
    y,
    z,
    color="red",
    s=50,
    label="Given Point",
)

ax.plot(
    line_points_x,
    line_points_y,
    line_points_z,
    color="blue",
    label="Given Vector",
)

unit_vec = point / LA.norm(point)
unit = list(unit_vec)
x, y, z = unit
P3_arr = DoubleArray3(x, y, z)
t_values = np.linspace(0, 1, 100)
line_points_x, line_points_y, line_points_z = [], [], []

for t in t_values:
    result_arr = DoubleArray3()

    get_point(P1_arr, P3_arr, t, result_arr)

    line_points_x.append(result_arr[0])
    line_points_y.append(result_arr[1])
    line_points_z.append(result_arr[2])

ax.plot(
    line_points_x,
    line_points_y,
    line_points_z,
    color="green",
    label="Unit Vector",
)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("1.10.18")
ax.legend()
ax.grid(True)

plt.savefig("../figs/plot.png")
plt.show()
