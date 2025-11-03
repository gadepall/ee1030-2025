import ctypes
import numpy as np
import matplotlib.pyplot as plt

libline = ctypes.CDLL("./line.so")

get_point = libline.point_gen
get_point.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # P1
    ctypes.POINTER(ctypes.c_double),  # P2
    ctypes.c_double,  # t
    ctypes.POINTER(ctypes.c_double),  # result_point
]
get_point.restype = None

DoubleArray2 = ctypes.c_double * 2
a = DoubleArray2(-7, 5)
b = DoubleArray2(1 / 3, 1 / 9)
c = DoubleArray2(5 / 4, 7 / 8)

t_values = np.linspace(0, 1, 100)
line_points_x, line_points_y = [], []

for t in t_values:
    result_arr = DoubleArray2()

    get_point(a, b, t, result_arr)

    line_points_x.append(result_arr[0])
    line_points_y.append(result_arr[1])

plt.plot(line_points_x, line_points_y, color="blue")

for t in t_values:
    result_arr = DoubleArray2()

    get_point(c, b, t, result_arr)

    line_points_x.append(result_arr[0])
    line_points_y.append(result_arr[1])

plt.plot(line_points_x, line_points_y, color="green")

for t in t_values:
    result_arr = DoubleArray2()

    get_point(a, c, t, result_arr)

    line_points_x.append(result_arr[0])
    line_points_y.append(result_arr[1])

plt.plot(line_points_x, line_points_y, color="orange")

a_values = np.linspace(-1.5, -1, 100) 
a_points_x, a_points_y = [],[]

for val in a_values:
    a_points_x.append(val)
    a_points_y.append(val**2)

plt.plot(a_points_x, a_points_y,color='blue')
a_values = np.linspace(1 / 2, 1, 100)
a_points_x, a_points_y = [],[]

for val in a_values:
    a_points_x.append(val)
    a_points_y.append(val**2)

plt.plot(a_points_x, a_points_y,color='blue')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("4.13.59")
plt.legend()
plt.grid(True)

plt.savefig("../figs/plot.png")
plt.show()
