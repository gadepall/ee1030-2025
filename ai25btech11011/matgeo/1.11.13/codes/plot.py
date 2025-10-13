import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL('./libdirection.so')
lib.find_direction_cosines.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]

l = ctypes.c_double()
m = ctypes.c_double()
n = ctypes.c_double()

lib.find_direction_cosines(90, 135, 45, ctypes.byref(l), ctypes.byref(m), ctypes.byref(n))

print(f"Direction cosines:\nl = {l.value}\nm = {m.value}\nn = {n.value}")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

origin = np.array([0, 0, 0])
vector = np.array([l.value, m.value, n.value])

ax.quiver(origin[0], origin[1], origin[2],
          vector[0], vector[1], vector[2],
          length=1, normalize=True, color='red')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Direction Cosines Vector')
plt.savefig("/home/gara-varun-kumar/ee1030-2025/ai25btech11011/matgeo/1.11.13/figs/Fig 1.png")
plt.show()

