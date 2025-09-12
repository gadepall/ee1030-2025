import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define vectors
u = np.array([2, 3, 2])
v = np.array([-2, 3, 6])
w = np.array([-2, 7, 2])

# Origin
O = np.array([0, 0, 0])

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# ---- Plot Vectors u, v, w ----
def plot_vector(vec, color, label, offset):
    ax.quiver(O[0], O[1], O[2],
              vec[0], vec[1], vec[2],
              color=color, arrow_length_ratio=0.1, linewidth=2)
    ax.text(vec[0]+offset[0], vec[1]+offset[1], vec[2]+offset[2],
            label, fontsize=12, color=color, weight="bold")

plot_vector(u, "red", "u(2,3,2)", offset=(0.5, 0.5, 0.5))
plot_vector(v, "green", "v(-2,3,6)", offset=(-1, 0.5, 0.5))
plot_vector(w, "blue", "w(-2,7,2)", offset=(-1, 0.5, -0.5))

# ---- Plot parallelepiped ----
vertices = np.array([
    O, u, v, w,
    u+v, v+w, w+u, u+v+w
])
faces = [
    [O, u, u+v, v],
    [O, v, v+w, w],
    [O, u, u+w, w],
    [u, u+v, u+v+w, u+w],
    [v, u+v, u+v+w, v+w],
    [w, v+w, u+v+w, u+w]
]
ax.add_collection3d(Poly3DCollection(faces, alpha=0.25, facecolor="cyan"))

# ---- Planes ----
xx, yy = np.meshgrid(range(-3, 6), range(-3, 9))

# Plane 1: 3x+2y+3z = 18
zz1 = (18 - 3*xx - 2*yy) / 3
ax.plot_surface(xx, yy, zz1, alpha=0.25, color="orange")
ax.text(4, -3, (18 - 3*4 - 2*(-3)) / 3,
        "Plane: 3x+2y+3z=18", color="orange", fontsize=12, weight="bold")

# Plane 2: 3x+2y+3z = 14 (label at bottom of plane)
zz2 = (14 - 3*xx - 2*yy) / 3
ax.plot_surface(xx, yy, zz2, alpha=0.25, color="red")
ax.text(0, -5, (14 - 3*0 - 2*(-5)) / 3,
        "Plane: 3x+2y+3z=14", color="red", fontsize=12, weight="bold")

# Plane 3: x+y+z = 7 (plane yellow, label dark green)
zz3 = 7 - xx - yy
ax.plot_surface(xx, yy, zz3, alpha=0.25, color="yellow")
ax.text(3, 6, 7 - 3 - 6,
        "Plane: x+y+z=7", color="darkgreen", fontsize=12, weight="bold")

# Plane 4: 3x+2y+3z = 16 (mid-plane)
zz4 = (16 - 3*xx - 2*yy) / 3
ax.plot_surface(xx, yy, zz4, alpha=0.25, color="purple")
ax.text(-4, -3, (16 - 3*(-4) - 2*(-3)) / 3,
        "Plane: 3x+2y+3z=16", color="purple", fontsize=12, weight="bold")

# ---- Axes settings ----
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 10)
ax.set_zlim(-5, 10)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Vectors u,v,w and Planes")

plt.savefig("../figs/fig5.png")
plt.show()

