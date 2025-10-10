

import sys
sys.path.insert(0, '/home/chanakya/MATGEO/1.9.25/codes/libs/CoordGeo')   # path to local scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# local imports
from line.funcs import *
from conics.funcs import circ_gen

# Given values
a, b = 2, 3
A = np.array(([a+b, b-a])).reshape(-1,1)   # (5,-3)
B = np.array(([a-b, a+b])).reshape(-1,1)   # (-1,7)

# Choose a point P on line bx = ay
xP = 2
yP = (b*xP)/a
P = np.array(([xP, yP])).reshape(-1,1)

# Distances (radius of circles)
r = LA.norm(P - A)

# Generate locus line bx = ay
xx = np.linspace(-15,15,400)
yy = (b*xx)/a

# Plot locus line
plt.plot(xx, yy, 'r', label='$bx=ay$')

# Plot A, B, P
tri_coords = np.block([[A,B,P]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])

# Labels
vert_labels = ['A','B','P']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
                 (tri_coords[0,i], tri_coords[1,i]),
                 textcoords="offset points",
                 xytext=(10,10),
                 ha='center')


# Circles centered at A and B with radius r
circleA = plt.Circle(A.flatten(), r, color='blue', fill=False, linestyle='--', alpha=0.5)
circleB = plt.Circle(B.flatten(), r, color='green', fill=False, linestyle='--', alpha=0.5)

ax = plt.gca()   # <-- no plt.subplots()
ax.add_patch(circleA)
ax.add_patch(circleB)



# Axes through origin
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title("Locus of P such that PA = PB")
plt.legend()
plt.grid(True, alpha=0.3)
plt.axis('equal')

#plt.savefig("locus.pdf")   # if using termux
plt.show()

