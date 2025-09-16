import sys
import numpy as np
import matplotlib.pyplot as plt

# Add local path for custom geometry functions
sys.path.insert(0, '/home/ganachari-vishwmabhar/Downloads/codes/CoordGeo')

# Import the given helper functions
from line.funcs import *
from triangle.funcs import *

# Define the vectors a, b, c (unit vectors with a+b+c=0)
a = np.array([1, 0])                         # Along x-axis
b = np.array([-0.5, np.sqrt(3)/2])           # 120° rotated
c = np.array([-0.5, -np.sqrt(3)/2])          # 240° rotated

# Plot the triangle formed by a, b, c
plt.figure()
xs = [a[0], b[0], c[0], a[0]]
ys = [a[1], b[1], c[1], a[1]]
plt.plot(xs, ys, 'k-', label='Triangle (a,b,c)')

# Mark the vectors from origin
O = np.array([0, 0])
plt.plot([O[0], a[0]], [O[1], a[1]], 'r-', label='a')
plt.plot([O[0], b[0]], [O[1], b[1]], 'g-', label='b')
plt.plot([O[0], c[0]], [O[1], c[1]], 'b-', label='c')

# Mark points
plt.scatter([a[0], b[0], c[0]], [a[1], b[1], c[1]], c=['r','g','b'])
plt.text(a[0], a[1], 'a', fontsize=12)
plt.text(b[0], b[1], 'b', fontsize=12)
plt.text(c[0], c[1], 'c', fontsize=12)

plt.axis('equal')
plt.grid(True)
plt.legend()
plt.title("Triangle of unit vectors (a+b+c=0)")
plt.savefig("../figs/plot.png")
plt.show()

