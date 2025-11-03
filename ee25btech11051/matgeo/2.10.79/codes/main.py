import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os
import sys



a = np.array([3, 0, 0], dtype=np.float64)

y = 2
z = np.sqrt(12 - y**2)
b = np.array([-2, y, z], dtype=np.float64)  

axb = np.array([0, 0, 0], dtype=np.float64)


cross_lib = ctypes.CDLL('./cross.so')
cross_lib.cross.argtypes = [
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double)
    ]

cross_lib.cross.restype = ctypes.c_double

cross=cross_lib.cross(
        a.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        b.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        axb.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    )

fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, a[0], a[1], a[2], color='b', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='g', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, axb[0], axb[1], axb[2], color='r', arrow_length_ratio=0.1)


label = f'({a[0]}, {a[1]}, {a[2]})'
ax.text(a[0], a[1], a[2], s=label, color='b', fontsize=10)

label = f'({b[0]}, {b[1]}, {b[2]})'
ax.text(b[0], b[1], b[2], s=label, color='g', fontsize=10)

label = f'({axb[0]}, {axb[1]}, {axb[2]})'
ax.text(axb[0], axb[1], axb[2], s=label, color='r', fontsize=10)



ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])
plt.title('3D Projection of Vectors a, b, and a x b')
plt.savefig('/home/shreyas/GVV_Assignments/matgeo/2.10.79/figs/fig1.png')

plt.grid(True)
plt.show()

