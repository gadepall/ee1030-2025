import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os
import sys
import subprocess

print('Using termux? (y/n)')
termux = input()

lib_path = os.path.join(os.path.dirname(__file__), 'plot.so')
my_lib = ctypes.CDLL(lib_path)

my_lib.write_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
my_lib.write_points.restype = ctypes.c_int
r1 = np.array([5, 0, 0])
r2 = np.array([2, 0, 0])
m1 = np.array([0, 2/3, -2])
m2 = np.array([0, -1, -1/3])
p1 = r1 - 8*m1
p2 = r1 + 8*m1
p3 = r2 - 8*m2
p4 = r2 + 8*m2
k = my_lib.write_points(p1[0], p1[1], p1[2], p2[0], p2[1], p2[2], p3[0], p3[1], p3[2], p4[0], p4[1], p4[2], 20000)

if k == 0:
    print('The given lines are perpendicular')
else:
    print('The given lines are not perpendicular')

points = np.loadtxt('plot.dat', delimiter=',', usecols = (0,1, 2))
points2 = np.loadtxt('plot2.dat', delimiter=',', usecols = (0,1, 2))

x = points[:, 0]
y = points[:, 1]
z = points[:, 2]

x2 = points2[:, 0]
y2 = points2[:, 1]
z2 = points2[:, 2]

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot(x, y, z, label = 'Line L1')
ax.plot(x2, y2, z2, label = 'Line L2')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.legend(loc='best')
ax.grid() 
ax.axis('equal')

fig.savefig('../figs/fig2.png')
print('Saved figure to ../figs/fig2.png')

if(termux == 'y'):
    subprocess.run(shlex.split('termux-open ../figs/fig2.png'))
else:
    subprocess.run(["open",  "../figs/fig2.png"])
