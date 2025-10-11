
#Plane through 4 points

import sys                                          #for path to external scripts
sys.path.insert(0, '/Users/unnathi/Documents/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

data = np.loadtxt("values.dat")  

x = data


# Points
A = np.array([x, 5, -1])
B = np.array([3, 2, 1])
C = np.array([4, 5, 5])
D = np.array([4, 2, -2])

# Vectors in plane
AB = B - A
AC = C - A

# Normal vector (cross product)
n = np.cross(AB, AC)
a, b, c = n

# Plane equation: ax + by + cz + d = 0
d = -np.dot(n, A)



# Create grid for plotting plane
x = np.linspace(-2, 8, 20)
y = np.linspace(-2, 8, 20)
X, Y = np.meshgrid(x, y)

# Solve for Z from plane equation
Z = (-a*X - b*Y - d) / c

# Plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot plane
ax.plot_surface(X, Y, Z, alpha=0.5, color="blue")

# Scatter points
points = np.array([A, B, C, D]).T
ax.scatter(points[0], points[1], points[2], color='red', s=50)

labels = ['A(6,5,-1)', 'B(3,2,1)', 'C(4,5,5)', 'D(4,2,-2)']
for i, txt in enumerate(labels):
    ax.text(points[0, i], points[1, i], points[2, i], txt, fontsize=10)


# Axes settings
ax.set_xlim(-2, 8)
ax.set_ylim(-2, 8)
ax.set_zlim(-4, 6)
ax.set_box_aspect([1,1,1])


plt.savefig('/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/4.4.8/figs/fig.png')
plt.show()

