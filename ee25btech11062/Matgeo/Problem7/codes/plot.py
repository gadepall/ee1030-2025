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
x = np.array([1, -2]).reshape(-1, 1)
m1 = np.array([-2, 1]).reshape(-1, 1)
m2 = np.array([1/2, 1]).reshape(-1, 1)
npts = 20000

my_lib.write_points(x[0][0], x[1][0], m1[0][0], m1[1][0], m2[0][0], m2[1][0], npts)

fig = plt.figure()
ax = fig.add_subplot(111)
labels = ['Given Line', 'Required Line']
pts = np.block([x])

for i,label in enumerate(labels):
    points = np.loadtxt('plot.dat', delimiter = ',', usecols=(0,1))[i*(npts+1):(i+1)*(npts+1)]
    ax.plot(points[:, 0], points[:, 1], label = label)

ax.text(pts[:, 0][0], pts[:, 0][1], s=f'(1, -2)')

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
