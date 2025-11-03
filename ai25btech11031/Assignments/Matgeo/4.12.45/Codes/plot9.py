import numpy as np
import matplotlib.pyplot as plt

# Semi-axis lengths
a = 5
b = 3
c = 3

# Create a grid of angles
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)

# Parametric equations of ellipsoid
x = a * np.outer(np.cos(u), np.sin(v))
y = b * np.outer(np.sin(u), np.sin(v))
z = c * np.outer(np.ones_like(u), np.cos(v))

# Plot the ellipsoid
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, rstride=4, cstride=4, color='cyan', alpha=0.6, edgecolor='k')

# Plot the foci points A and B
A = np.array([4, 0, 0])
B = np.array([-4, 0, 0])
ax.scatter(*A, color='red', s=100, label=r'$\mathbf{A}(4,0,0)$')
ax.scatter(*B, color='blue', s=100, label=r'$\mathbf{B}(-4,0,0)$')

# Labels and legend
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('w-axis')
ax.set_title(r'Locus: $\frac{x^2}{25}+\frac{y^2}{9}+\frac{z^2}{9}=1$')
ax.legend()

# Equal aspect ratio
ax.set_box_aspect([a,b,c])

plt.savefig("plot9.png")
plt.show()

