# Code by /sdcard/github/matgeo/codes/CoordGeoVV Sharma
# September 12, 2023
# Revised July 21, 2024
# Released under GNU GPL
# Section Formula

import sys
import subprocess
import shlex
sys.path.insert(0, '/sdcard/Matrix/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import matplotlib.pyplot as plt

print('Using termux? (y/n)')
termux = input()

# Local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

from call import get_point_from_c
xc, yc = get_point_from_c()

A = np.array([-4, 0]).reshape(-1, 1)
B = np.array([0, 6]).reshape(-1, 1)
R = np.array([xc, yc]).reshape(-1, 1)

# Generating line AB
x_AB = line_gen(A, B)

# Plotting
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')

# Labeling the coordinates
tri_coords = np.block([[A, B, R]])
plt.scatter(tri_coords[0, :], tri_coords[1, :])

vert_labels = ['A', 'B', 'R']

# Helper function: format number with decimal only if needed
def fmt(val):
    return f"{val:.1f}" if abs(val - round(val)) > 1e-6 else f"{int(val)}"

for i, txt in enumerate(vert_labels):
    x = tri_coords[0, i]
    y = tri_coords[1, i]
    plt.annotate(f'{txt}\n({fmt(x)}, {fmt(y)})',
                 (x, y),
                 textcoords="offset points",
                 xytext=(20, -10),
                 ha='center')

# Styling
ax = plt.gca()
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.savefig('../figs/fig1.png')
plt.show()

if(termux == 'y'):
    subprocess.run(shlex.split('termux-open ../figs/fig1.png'))
