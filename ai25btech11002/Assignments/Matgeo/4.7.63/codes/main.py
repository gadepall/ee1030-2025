import math
#import sys   
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpim
from mpl_toolkits.mplot3d import Axes3D
from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen
#if using termux
#import subprocess
#import shlex
#end if

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Generating mesh grid
x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)
# Plane 1: z = 2y - x
Z1 = 2*Y - X
ax.plot_surface(X, Y, Z1, alpha=0.3, color='cyan')

# Plane 2: z = x + y
Z2 = X + Y
ax.plot_surface(X, Y, Z2, alpha=0.3, color='orange')

# Plane 3: z = 5   (horizontal plane)
Z3 = 5*np.ones_like(X)
ax.plot_surface(X, Y, Z3, alpha=0.3, color='green')

# --- Scatter a point ---
P = np.array([1, -1, 2])  # Example point
ax.scatter(P[0], P[1], P[2], color='red', s=60, marker='o', label='Point (1,-1,2)')

# Axes labels and settings
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Three Planes and a Point')
ax.legend()
ax.grid(True)

# Save to figs folder
plt.savefig("../Figs/plot.png")
plt.show()
