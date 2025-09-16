import numpy as np

import matplotlib.pyplot as plt

import sys

import ctypes

c_lib=ctypes.CDLL('./3c.so')


c_lib.anglefinder.argtypes = [ctypes.c_float, ctypes.c_float,ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]

c_lib.anglefinder.restype = ctypes.c_float


v1 = np.array([1,2,-2])
v2 = np.array([3,-6,2])

angle = c_lib.anglefinder(
    ctypes.c_float(v1[0]),
    ctypes.c_float(v1[1]), 
    ctypes.c_float(v1[2]),
    ctypes.c_float(v2[0]), 
    ctypes.c_float(v2[1]),
    ctypes.c_float(v2[2])
)

print(angle*180/3.1415)

import numpy as np
import matplotlib.pyplot as plt



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)


X, Y = np.meshgrid(x, y)

Z = (X-2*Y- 1)/2
z1 = (6*Y - 3*X)/2

ax.plot_surface(X, Y, Z, alpha=1, cmap='Blues')
ax.plot_surface(X, Y, z1, alpha=1, cmap='Oranges')


ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Plot of the planes')

plt.show()
