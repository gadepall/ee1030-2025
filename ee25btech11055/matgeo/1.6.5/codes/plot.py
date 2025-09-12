import ctypes
import numpy as np
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
P1_arr = DoubleArray3(-1, -2, 1)
P2_arr = DoubleArray3(5, 8, 7)

t_values = np.linspace(0, 1, 100)
line_points_x, line_points_y, line_points_z = [], [], []

for t in t_values:
    result_arr = DoubleArray3()

    get_point(P1_arr, P2_arr, t, result_arr)

    line_points_x.append(result_arr[0])
    line_points_y.append(result_arr[1])
    line_points_z.append(result_arr[2])

original_points = np.array([[-1, -2, 1], [2, 3, 4], [5, 8, 7]])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

ax.scatter(
    original_points[:, 0],
    original_points[:, 1],
    original_points[:, 2],
    color="red",
    s=50,
    label="Given Points",
)

ax.plot(
    line_points_x,
    line_points_y,
    line_points_z,
    color="blue",
    label="Line Segment",
)

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("1.6.5")
ax.legend()
ax.grid(True)

plt.savefig("../figs/plot.png")
plt.show()
