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

my_lib.write_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
my_lib.write_points.restype = ctypes.c_float
p1 = np.array([2, 3, -4])
p2 = np.array([3, -4 , -5])
p3 = np.array([3, 2, -3])
npts = 20000
k = my_lib.write_points(p1[0], p1[1], p1[2], p2[0], p2[1], p2[2], p3[0], p3[1], p3[2], npts)

print(f'The norm of A+B+C = {k}')

points = np.loadtxt('plot.dat', delimiter=',', usecols = (0,1, 2))[0:npts+1]
points2 = np.loadtxt('plot.dat', delimiter=',', usecols = (0,1, 2))[npts+1:2*(npts+1)]
points3 = np.loadtxt('plot.dat', delimiter =',', usecols = (0,1,2))[2*(npts+1):3*(npts+1)]
points4 = np.loadtxt('plot.dat', delimiter =',', usecols = (0,1,2))[3*(npts+1):4*(npts+1)]

x = points[:, 0]
y = points[:, 1]
z = points[:, 2]

x2 = points2[:, 0]
y2 = points2[:, 1]
z2 = points2[:, 2]

x3 = points3[:, 0]
y3 = points3[:, 1]
z3 = points3[:, 2]

x4 = points4[:, 0]
y4 = points4[:, 1]
z4 = points4[:, 2]

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot(x, y, z, label = 'Vector A')
ax.plot(x2, y2, z2, label = 'Vector B')
ax.plot(x3, y3, z3, label = 'Vector C')
ax.plot(x4, y4, z4, label = 'Vector A+B+C')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.legend(loc='best')
ax.grid() 
ax.axis('equal')
ax.set_xlim([-15, 10])
ax.set_ylim([-15, 10])
ax.set_zlim([-15, 10])

fig.savefig('../figs/fig2.png')
print('Saved figure to ../figs/fig2.png')

if(termux == 'y'):
    subprocess.run(shlex.split('termux-open ../figs/fig2.png'))
else:
    subprocess.run(["open",  "../figs/fig2.png"])
