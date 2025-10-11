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

my_lib.write_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
my_lib.write_points.restype = None
A = np.array([8, 2]).reshape(-1, 1)
m = np.array([1, -1/2]).reshape(-1, 1)
npts = 20000

my_lib.write_points(A[0][0], A[1][0], m[0][0], m[1][0], npts)

labels = ['Line with min OP+OQ']
point_labels = ['P(0, 6)', 'Q(12, 0)', 'A(8,2)']
pts = np.block([A-8*m, A+4*m, A])

for i,label in enumerate(labels):
    points = np.loadtxt('plot.dat', delimiter = ',', usecols=(0,1))[i*(npts+1):(i+1)*(npts+1)]
    plt.plot(points[:, 0], points[:, 1], label = label)

for i,label in enumerate(point_labels):
    plt.annotate(label, (pts[0,i],pts[1,i]), textcoords="offset points", xytext=(20,5),ha='center')

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.savefig('../figs/fig2.png')
print('Saved figure to ../figs/fig2.png')

if(termux == 'y'):
    subprocess.run(shlex.split('termux-open ../figs/fig2.png'))
else:
    subprocess.run(["open",  "../figs/fig2.png"])
