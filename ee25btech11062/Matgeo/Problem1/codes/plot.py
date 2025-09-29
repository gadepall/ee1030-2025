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

my_lib.write_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
my_lib.write_points.restype = None
my_lib.write_points(-4, 6, -4, -6, 20000)

my_lib.check_collinearity.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
my_lib.check_collinearity.restype = ctypes.c_int
collinearity = my_lib.check_collinearity(-4, 6, -4, -6, -4, 2)

if (collinearity == 1):
    print('The given points are collinear and the rank of the collinearity matrix is 1')
else:
    print('The given points are not collinear and the rank of the collinearity matrix is not 1')

points = np.loadtxt('plot.dat', delimiter=',', usecols = (0,1))

x = points[:, 0]
y = points[:, 1]

plt.plot(x, y, label = 'Line through AB')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')

plt.savefig('../figs/fig2.png')
print('Saved figure to ../figs/fig2.png')

if(termux == 'y'):
    subprocess.run(shlex.split('termux-open ../figs/fig2.png'))
else:
    subprocess.run(["open",  "../figs/fig2.png"])
