import sys
sys.path.insert(0, '/sdcard/github/matgeo/codes/CoordGeo')  # path to CoordGeo
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex
import os  # << add this

# Local imports
from line.funcs import line_gen

# Define points as column vectors
O = np.array([[0], [0]])
A = np.array([[1], [0]])
B = np.array([[0], [1]])
C = A + B
D = (O + A) / 2

# Compute intersection P on BD such that P = B + (2/3)(D - B)
lam = 2/3
P = B + lam * (D - B)

# Generate required lines
x_OC = line_gen(O, C)
x_BD = line_gen(B, D)

# Parallelogram edges
x_OA = line_gen(O, A)
x_AB = line_gen(A, C)
x_CB = line_gen(C, B)
x_BO = line_gen(B, O)

# Plot lines
plt.plot(x_OC[0,:], x_OC[1,:], 'r--', label='$OC$')
plt.plot(x_BD[0,:], x_BD[1,:], 'g--', label='$BD$')

for line in [x_OA, x_AB, x_CB, x_BO]:
    plt.plot(line[0,:], line[1,:], 'k-')

# Points to plot
coords = np.block([[O, A, B, C, D, P]])
labels = ['O', 'A', 'B', 'C', 'D', 'P']
plt.scatter(coords[0,:], coords[1,:])

for i, txt in enumerate(labels):
    plt.annotate(f'{txt}\n({coords[0,i]:.2f}, {coords[1,i]:.2f})',
                 (coords[0,i], coords[1,i]),
                 textcoords="offset points",
                 xytext=(10,-10),
                 ha='center')

# Styling
ax = plt.gca()
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.axis('equal')
plt.grid()
plt.legend(loc='best')
plt.title("Intersection of BD and OC (Pure Python)")

# Create directory if needed and save figure
save_path = 'chapters/10/7/2/2/figs/fig.pdf'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

try:
    subprocess.run(shlex.split(f"termux-open {save_path}"))
except:
    plt.show()

