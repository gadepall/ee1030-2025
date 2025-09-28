#Code by GVV Sharma (modified for circle through line intersection)
#Sep 27, 2025
#Released under GNU GPL

import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

# Local imports from CoordGeo
sys.path.insert(0, '/sdcard/github/matgeo/codes/CoordGeo')
from line.funcs import line_isect, line_norm
from conics.funcs import circ_gen

# Line equations: 3x + y = 14,  2x + 5y = 18
n1 = np.array([3,1]).reshape(-1,1)
c1 = 14
n2 = np.array([2,5]).reshape(-1,1)
c2 = 18

# Intersection of lines
P = line_isect(n1,c1,n2,c2)

# Circle centre
O = np.array([1,-2]).reshape(-1,1)

# Radius = distance between centre and intersection point
r = LA.norm(O-P)

# Generate circle
x_circ = circ_gen(O,r)

# Generate lines
x_line1 = line_norm(n1,c1,-5,5)
x_line2 = line_norm(n2,c2,-5,5)

# Plotting
plt.plot(x_circ[0,:], x_circ[1,:], label="Circle")
plt.plot(x_line1[0,:], x_line1[1,:], label="$3x+y=14$")
plt.plot(x_line2[0,:], x_line2[1,:], label="$2x+5y=18$")

# Points
plt.scatter(P[0],P[1],color='red')
plt.scatter(O[0],O[1],color='blue')
plt.annotate("Intersection P",(P[0],P[1]),textcoords="offset points",xytext=(10,10))
plt.annotate("Centre O",(O[0],O[1]),textcoords="offset points",xytext=(10,-10))

# Axes formatting
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

plt.legend()
plt.grid()
plt.axis("equal")

# Save and show
plt.savefig("circle_question.png", dpi=300)
plt.show()
