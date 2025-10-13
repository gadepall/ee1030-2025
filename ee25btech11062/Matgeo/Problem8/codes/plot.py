import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os
import sys
import subprocess
import math

print('Using termux? (y/n)')
termux = input()

lib_path = os.path.join(os.path.dirname(__file__), 'plot.so')
my_lib = ctypes.CDLL(lib_path)

my_lib.write_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
my_lib.write_points.restype = None
A = np.array([3, 5]).reshape(-1, 1)
B = np.array([6, 3]).reshape(-1, 1)
C = np.array([1, 2]).reshape(-1, 1)
npts = 20000

my_lib.write_points(A[0][0], A[1][0], B[0][0], B[1][0], C[0][0], C[1][0], npts)

fig = plt.figure()
ax = fig.add_subplot(111)
labels = ['3x-2y+1=0', '2x+3y-21=0', 'x-5y+9=0']
point_labels = ['A(3, 5)', 'B(6, 3)', 'C(1,2)']
pts = np.block([A, B, C])

for i,label in enumerate(labels):
    points = np.loadtxt('plot.dat', delimiter = ',', usecols=(0,1))[i*(npts+1):(i+1)*(npts+1)]
    ax.plot(points[:, 0], points[:, 1], label = label)
    ax.text(pts[0, i], pts[1, i], s=point_labels[i])

ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.legend(loc='best')
ax.grid() 
ax.axis('equal')

fig.savefig('../figs/fig2.png')
print('Saved figure to ../figs/fig2.png')

if(termux == 'y'):
    subprocess.run(shlex.split('termux-open ../figs/fig2.png'))
else:
    subprocess.run(["open",  "../figs/fig2.png"])
