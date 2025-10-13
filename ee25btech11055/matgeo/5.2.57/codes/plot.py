import ctypes
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

e1 = np.array([2, 1, 1, 1])
e2 = np.array([1, -2, -1, 3 / 2])
e3 = np.array([0, 3, -5, 9])


cols = ["red", "blue", "green"]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

x_steps, y_steps = 100, 100
total_points = x_steps * y_steps
x_plane = np.zeros(total_points, dtype=np.double)
y_plane = np.zeros(total_points, dtype=np.double)
z_plane = np.zeros(total_points, dtype=np.double)

for i in range(1, 4):
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
        eval(f"e{i}")[0],
        eval(f"e{i}")[1],
        eval(f"e{i}")[2],
        eval(f"e{i}")[3],
    )
    ax.scatter(x_plane, y_plane, z_plane, alpha=0.03, color=cols[i - 1])

ax.scatter(1, 1 / 2, -3 / 2, color="yellow", label="Point")
ax.text(1, 1 / 2, -3 / 2, " Point")

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
