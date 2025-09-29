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
A = np.array([273, 32]).reshape(-1, 1)
B = np.array([373, 212]).reshape(-1, 1)
C = np.array([0, -459.4]).reshape(-1, 1)
npts = 20000

my_lib.write_points(A[0][0], A[1][0], B[0][0], B[1][0], C[0][0], C[1][0], npts)

fig = plt.figure()
ax = fig.add_subplot(111)
labels = ['CB', 'CA', 'AB']
pts = np.block([A, B, C])
vertices = ['A', 'B', 'C']
for i,label in enumerate(labels):
    points = np.loadtxt('plot.dat', delimiter = ',', usecols=(0,1))[i*(npts+1):(i+1)*(npts+1)]
    if(i > 0):
        ax.plot(points[:, 0], points[:, 1], label = (f'Line {label}'))
    else:
        ax.plot(points[:, 0], points[:, 1])
    ax.text(pts[:, i][0], pts[:, i][1], s=f'{vertices[i]}({round(pts[:, i][0],3)}, {round(pts[:, i][1],3)})')

ax.set_xlabel('$K(Kelvin)$')
ax.set_ylabel('$F(Fahrenheit)$')
ax.legend(loc='best')
ax.grid() 
ax.axis('equal')
ax.set_xlim([-200, 800])
ax.set_ylim([-500, 300])

fig.savefig('../figs/fig2.png')
print('Saved figure to ../figs/fig2.png')

if(termux == 'y'):
    subprocess.run(shlex.split('termux-open ../figs/fig2.png'))
else:
    subprocess.run(["open",  "../figs/fig2.png"])
