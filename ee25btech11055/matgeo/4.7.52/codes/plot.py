import ctypes
import numpy as np
import matplotlib.pyplot as plt

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

A1 = np.array([1, 1, 1]).T
A2 = np.array([1, 1, 7 / 3]).T
B = np.array([-3, 0, 1]).T
n = np.array([3, 4, -12]).T
c = -13


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

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection="3d")

ax.scatter(x_plane, y_plane, z_plane, alpha=0.3, s=5, label="Given Plane")

ax.scatter(A1[0], A1[1], A1[2], color="red", s=120, label=f"A1 (1, 1, 1)")
ax.scatter(
    A2[0],
    A2[1],
    A2[2],
    color="magenta",
    s=120,
    label=f"A2 (1, 1, 7/3)",
)
ax.scatter(B[0], B[1], B[2], color="blue", s=120, label="B (-3, 0, 1)")
ax.text(B[0], B[1], B[2], "B (-3, 0, 1)")
ax.text(A1[0], A1[1], A1[2], "A1 (1,1,1)")
ax.text(A2[0], A2[1], A2[2], "A2 (1,1,7/3)")

ax.set_xlabel("X-axis", fontweight="bold")
ax.set_ylabel("Y-axis", fontweight="bold")
ax.set_zlabel("Z-axis", fontweight="bold")
ax.set_title("4.7.52", fontsize=16)
ax.view_init(elev=20, azim=135)
ax.legend()
plt.tight_layout()
plt.savefig("../figs/plot.png")
plt.show()
