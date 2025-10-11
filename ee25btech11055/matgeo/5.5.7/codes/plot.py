import ctypes
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import sys

libline = ctypes.CDLL("./line.so")
get_point = libline.point_gen
get_point.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # P1
    ctypes.POINTER(ctypes.c_double),  # P2
    ctypes.c_double,  # t
    ctypes.POINTER(ctypes.c_double),  # result_point
]
get_point.restype = None

libmatrix = ctypes.CDLL("./matrix.so")
libmatrix.find_inverse.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    ctypes.c_int,
]
libmatrix.find_inverse.restype = ctypes.c_int
find_inv = libmatrix.find_inverse

libmatrix.mul.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
]
libmatrix.mul.restype = None
matmul = libmatrix.mul

DoubleArray3 = ctypes.c_double * 3
a = DoubleArray3(0,0,0)
x = np.array([1,1,1],dtype=np.float64)

A = np.array([[3, 0, -1], [2, 3, 0], [0, 4, 1]],dtype=np.float64)
A_flat = A.flatten()
# flatten() passes a COPY! matrix isn't stored
inv = np.empty_like(A_flat)
if not find_inv(A_flat,inv,3):
    print("Matrix is singular")
    sys.exit()

inv = inv.reshape(A.shape)
b = np.empty_like(x)
c = np.empty_like(x)
matmul(A.flatten(),x,b,3,3,1)
matmul(inv.flatten(),b,c,3,3,1)

#print(x,A,inv,b,c,sep='\n')

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(121, projection="3d")

t_values = np.linspace(0, 1, 100)
line_points_x, line_points_y, line_points_z = [], [], []

for t in t_values:
    result_arr = DoubleArray3()

    get_point(a, DoubleArray3(x[0], x[1], x[2]), t, result_arr)

    line_points_x.append(result_arr[0])
    line_points_y.append(result_arr[1])
    line_points_z.append(result_arr[2])

ax.plot(
    line_points_x,
    line_points_y,
    line_points_z,
    color="red",
    label="Original Vector"
)
ax.text(x[0], x[1], x[2], " V1")

t_values = np.linspace(0, 1, 100)
line_points_x, line_points_y, line_points_z = [], [], []

for t in t_values:
    result_arr = DoubleArray3()

    get_point(a, DoubleArray3(b[0], b[1], b[2]), t, result_arr)

    line_points_x.append(result_arr[0])
    line_points_y.append(result_arr[1])
    line_points_z.append(result_arr[2])

ax.plot(
    line_points_x,
    line_points_y,
    line_points_z,
    color="blue",
    label="Modified Vector"
)
ax.text(b[0], b[1], b[2], " V2")

ax2 = fig.add_subplot(122, projection="3d")

t_values = np.linspace(0, 1, 100)
line_points_x, line_points_y, line_points_z = [], [], []

for t in t_values:
    result_arr = DoubleArray3()

    get_point(a, DoubleArray3(b[0], b[1], b[2]), t, result_arr)

    line_points_x.append(result_arr[0])
    line_points_y.append(result_arr[1])
    line_points_z.append(result_arr[2])

ax2.plot(
    line_points_x,
    line_points_y,
    line_points_z,
    color="blue",
    label="Modified Vector"
)
ax2.text(b[0], b[1], b[2], " V2")

t_values = np.linspace(0, 1, 100)
line_points_x, line_points_y, line_points_z = [], [], []

for t in t_values:
    result_arr = DoubleArray3()

    get_point(a, DoubleArray3(c[0], c[1], c[2]), t, result_arr)

    line_points_x.append(result_arr[0])
    line_points_y.append(result_arr[1])
    line_points_z.append(result_arr[2])

ax2.plot(
    line_points_x,
    line_points_y,
    line_points_z,
    color="green",
    label="Reverted Vector"
)
ax2.text(c[0], c[1], c[2], " V3")

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("5.5.7")
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])
ax.legend()
ax.grid(True)

ax2.set_xlabel("X-axis")
ax2.set_ylabel("Y-axis")
ax2.set_zlabel("Z-axis")
ax2.set_title("5.5.7")
ax2.set_xlim([-10, 10])
ax2.set_ylim([-10, 10])
ax2.set_zlim([-10, 10])
ax2.legend()
ax2.grid(True)

plt.savefig("../figs/plot.png")
plt.show()
