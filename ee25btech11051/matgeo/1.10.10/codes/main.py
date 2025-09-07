import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os
import sys

norm = ctypes.CDLL('./norm.so')
norm.norm.argtypes = [
        ctypes.POINTER(ctypes.c_double),
        ctypes.c_int
]

norm.norm.restype = ctypes.c_double


given_vector = np.array([1, -2, 2], dtype=np.float64)
m = len(given_vector)


norm = norm.norm(
        given_vector.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        m
)

final_vector = (given_vector/norm)*9




fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.quiver(0, 0, 0, given_vector[0], given_vector[1], given_vector[2], color='b', arrow_length_ratio=0.1)

ax.quiver(0, 0, 0, final_vector[0], final_vector[1], final_vector[2], color='r', arrow_length_ratio=0.1)

ax.scatter(given_vector[0], given_vector[1], given_vector[2], color='b', s=50)
ax.scatter(final_vector[0], final_vector[1], final_vector[2], color='r', s=50)

label = f'({given_vector[0]}, {given_vector[1]}, {given_vector[2]})'
ax.text(given_vector[0], given_vector[1], given_vector[2], s=label, color='g', fontsize=10)

label = f'({final_vector[0]}, {final_vector[1]}, {final_vector[2]})'
ax.text(final_vector[0], final_vector[1], final_vector[2], s=label, color='g', fontsize=10)

ax.set_xlim([0, 6])
ax.set_ylim([-6, 0])
ax.set_zlim([0, 6])


ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')


plt.title('1.10.10')

plt.savefig('/home/shreyas/GVV_Assignments/matgeo/1.10.10/figs/fig1.png')


plt.show()







