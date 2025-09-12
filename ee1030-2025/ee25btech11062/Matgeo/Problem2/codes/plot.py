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

my_lib.write_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
my_lib.write_points.restype = None
my_lib.write_points(2, 2, -1, 20000)

points = np.loadtxt('plot.dat', delimiter=',', usecols = (0,1, 2))
points2 = np.loadtxt('plot2.dat', delimiter=',', usecols = (0,1, 2))

x = points[:, 0]
y = points[:, 1]
z = points[:, 2]

x2 = points2[:, 0]
y2 = points2[:, 1]
z2 = points2[:, 2]

print(f"The directions cosines of OR are \n {np.array([x2[-1], y2[-1], z2[-1]]).reshape(-1, 1)}")

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot(x, y, z, label = 'Line through OR')
ax.plot(x2, y2, z2, label = 'Direction cosines of OR')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.legend(loc='best')
ax.grid() 
ax.axis('equal')

line_coords = np.array([[x[0], y[0], z[0]], [x[-1], y[-1], z[-1]], [x2[-1], y2[-1], z2[-1]]])

ax.scatter(line_coords[:, 0], line_coords[:, 1], line_coords[:, 2])
vert_labels = ['O','R','X']
for i, txt in enumerate(vert_labels):
    ax.text(line_coords[i][0], line_coords[i][1], line_coords[i][2], txt, color='red')

fig.savefig('../figs/fig2.png')
print('Saved figure to ../figs/fig2.png')

if(termux == 'y'):
    subprocess.run(shlex.split('termux-open ../figs/fig2.png'))
else:
    subprocess.run(["open",  "../figs/fig2.png"])
