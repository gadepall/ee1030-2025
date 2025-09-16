import sys
sys.path.insert(0, '/home/ganachari-vishwmabhar/Downloads/codes/CoordGeo')
import numpy as np
import matplotlib.pyplot as plt

from line.funcs import *
from triangle.funcs import *

# Load λ from previous result
lambda_val = -2.5
a = np.array([2, lambda_val, 1])   # vector a
b = np.array([1, 2, 3])            # vector b

# Prepare 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors from origin
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='r', label='Vector a')
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='b', label='Vector b')

# Mark points
ax.text(a[0], a[1], a[2], 'a', fontsize=12)
ax.text(b[0], b[1], b[2], 'b', fontsize=12)

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Orthogonal Vectors a and b")
ax.legend()
plt.savefig("../figs/plot.png")
plt.show()

