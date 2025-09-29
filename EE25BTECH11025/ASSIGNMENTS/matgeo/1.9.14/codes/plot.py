import sys
import math
sys.path.insert(0, '/home/ganachari-vishwmabhar/Downloads/codes/CoordGeo')
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Local imports as given
from line.funcs import *
from triangle.funcs import *

# Define triangle vertices
P = np.array([2, 2])
Q = np.array([-4, -4])
R = np.array([5, -8])

# Calculate the midpoint M of PQ (for the median through R)
M = (P + Q) / 2

# Prepare plot
plt.figure()
# Plot the triangle
xs = [P[0], Q[0], R[0], P[0]]
ys = [P[1], Q[1], R[1], P[1]]
plt.plot(xs, ys, 'k-', label='Triangle')

# Plot the median from R to M
plt.plot([R[0], M[0]], [R[1], M[1]], 'r--', label='Median from R')

# Mark vertices
plt.scatter([P[0], Q[0], R[0], M[0]], [P[1], Q[1], R[1], M[1]], c=['b','g','r','m'])
plt.text(P[0], P[1], 'P', fontsize=12)
plt.text(Q[0], Q[1], 'Q', fontsize=12)
plt.text(R[0], R[1], 'R', fontsize=12)
plt.text(M[0], M[1], 'M', fontsize=12)

plt.axis('equal')
plt.grid(True)
plt.legend()
plt.title("Triangle ΔPQR and Median through R")
plt.savefig("../figs/plot.png")
plt.show()

