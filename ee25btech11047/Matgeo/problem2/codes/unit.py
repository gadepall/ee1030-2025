#Code adapted to plot only vectors a, b, a+b and unit vector
#Released under GNU GPL
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# local imports (not used here, but kept for consistency with your project)
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Vectors from ctypes example
a = np.array([2.0, -1.0, 1.0])
b = np.array([0.0,  2.0, 1.0])
s = a + b

# Unit vector function
def unit_vector(x):
    return x / LA.norm(x)

u_py = unit_vector(s)

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot vectors (from origin)
ax.quiver(0,0,0,*a,color="r",label="a")
ax.quiver(0,0,0,*b,color="g",label="b")
ax.quiver(0,0,0,*s,color="b",label="a+b")

# Plot unit vector (length = 1)
ax.quiver(0,0,0,*u_py,color="c",label="unit (Python)")

# Plot scaled unit vector (same length as s)
ax.quiver(0,0,0,*(u_py*LA.norm(s)),color="c",linestyle="dashed",label="unit scaled")

ax.set_title("Vectors a, b, a+b and Unit Vector")
ax.legend()
plt.grid()
plt.show()


