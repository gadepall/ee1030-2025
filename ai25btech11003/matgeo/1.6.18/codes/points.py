# Code by GVV Sharma
# September 12, 2023
# Revised July 21, 2024
# released under GNU GPL

# Point Vectors
import sys                                          # for path to external scripts
sys.path.insert(0, '/home/bhavesh-g/Documents/matgeo/1.6.18/codes/line')  # path to my scripts

import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# --- Using given points directly ---
A = np.array(([2, 1])).reshape(-1, 1)     # A(2,1)
B = np.array(([0, 5])).reshape(-1, 1)     # B(0,5)
C = np.array(([-1, 2])).reshape(-1, 1)    # C(-1,2)

# Generating all lines
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

# Plotting all lines
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')
plt.plot(x_BC[0, :], x_BC[1, :], label='$BC$')
plt.plot(x_CA[0, :], x_CA[1, :], label='$CA$')

# Labeling the coordinates
colors = np.arange(1, 4)
tri_coords = np.block([[A, B, C]])
plt.scatter(tri_coords[0, :], tri_coords[1, :], c=colors)
vert_labels = ['A', 'B', 'C']
for i, txt in enumerate(vert_labels):
    plt.annotate(
        f'{txt}\n({tri_coords[0,i]:.2f}, {tri_coords[1,i]:.2f})',
        (tri_coords[0, i], tri_coords[1, i]),
        textcoords="offset points",
        xytext=(25, 5),
        ha='center'
    )

# Axes crossing at origin
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

plt.grid()
plt.axis('equal')

# if using termux
plt.savefig('fig1.png')
# subprocess.run(shlex.split("termux-open fig1.pdf"))  # uncomment on Termux
# else
# plt.show()

