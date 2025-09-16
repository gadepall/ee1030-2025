import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
a = np.array([2, 2, 1])
b = np.array([1, 3, 1])
c = np.array([1, 0, 1])
bc = b + c

# Projection of (b+c) onto a
coeff = np.dot(bc, a) / np.dot(a, a)
proj = coeff * a

# Create 3D plot
fig = plt.figure(figsize=(8,7))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1,1,1])

# Origin
origin = np.zeros(3)

# Plot vectors
def draw_vector(vec, label):
    ax.quiver(*origin, *vec, color="orange")
    ax.text(*(vec + 0.1), label, fontsize=12)

draw_vector(a, r'$\vec{a}$')
draw_vector(b, r'$\vec{b}$')
draw_vector(c, r'$\vec{c}$')
draw_vector(bc, r'$\vec{b}+\vec{c}$')
draw_vector(proj, r'$\mathrm{proj}_{\vec a}(\vec b+\vec c)$')

# Dashed reference line along a
t = np.linspace(-1, 2, 30)
line = np.outer(t, a)
ax.plot(line[:,0], line[:,1], line[:,2], linestyle='dashed', color="orange")

# Scatter end points
ax.scatter([a[0], b[0], c[0], bc[0], proj[0]], 
           [a[1], b[1], c[1], bc[1], proj[1]], 
           [a[2], b[2], c[2], bc[2], proj[2]], s=30, color="orange")

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(r"Vectors and projection of (b+c) onto a" + 
             f"\ncoeff = (b+c)·a / a·a = {np.dot(bc,a)}/{np.dot(a,a)} = {coeff:.3f}")

plt.show()
