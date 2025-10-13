
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

u = np.array([1, 1, 1])
v = np.array([1, -1, 1])
w = np.array([3, -1, 3])
x = np.array([1, -1, -1])   

# =========================
# Plane through u, v, w (all from origin)
# =========================
# Two spanning vectors for the plane
uv = v - u
uw = w - u
normal = np.cross(uv, uw)   # plane normal
a, b, c = normal
d = 0   # plane passes through origin

# =========================
# Create grid for plane
# =========================
xx, yy = np.meshgrid(
    np.linspace(-3, 3, 10),
    np.linspace(-3, 3, 10)
)
zz = (-a * xx - b * yy - d) / c

# =========================
# Plotting
# =========================
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='grey')

# Plot vectors as arrows from origin
origin = np.zeros(3)
for vec, color, label in zip([u, v, w, x], ['r', 'g', 'b', 'orange'], [r'$\vec{a}$', r'$\vec{b}$', r'$\vec{v}$', r'$\vec{c}$']):
    ax.quiver(*origin, *vec, color=color, label=label)

# Axes labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.savefig("../Figs/plot(py).png")
plt.show()

