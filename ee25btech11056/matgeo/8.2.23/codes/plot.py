import numpy as np
import matplotlib.pyplot as plt
import os

# save figure in figs folder
figs_folder = os.path.join("..", "figs")

# Given ellipse parameters
f1 = (0.0, 5.0)
f2 = (0.0, -5.0)
vert = (0.0, 13.0)
vert2 = (0.0, -13.0)

# semi-major and semi-minor axes
b = vert[1]   # semi-major axis (along y-axis)
c_f = f1[1]   # distance to focus from origin
a = np.sqrt(b**2 - c_f**2)  # semi-minor axis (along x-axis)

# x and y values for ellipse
x_vals = np.linspace(-a, a, 400)
y_upper = b * np.sqrt(1 - (x_vals**2 / a**2))
y_lower = -y_upper

# Plotting
fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(x_vals, y_upper, 'r')
ax.plot(x_vals, y_lower, 'r', label="Ellipse")

# plot foci
ax.scatter([f1[0], f2[0]], [f1[1], f2[1]], color="blue", label="Foci")
ax.text(f1[0] + 0.5, f1[1], f"F1{f1}", fontsize=10, color="blue")
ax.text(f2[0] + 0.5, f2[1], f"F2{f2}", fontsize=10, color="blue")

# plot vertices
ax.scatter([vert[0]], [vert[1]], color="green", label="Vertex1")
ax.text(vert[0] + 0.5, vert[1], f"B1{vert}", fontsize=10, color="green")

ax.scatter([vert2[0]], [vert2[1]], color="orange", label="Vertex2")
ax.text(vert2[0] + 0.5, vert2[1], f"B2{vert2}", fontsize=10, color="orange")

# center axes
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# formatting
ax.set_aspect('equal')
ax.set_title("Ellipse")
ax.legend()
ax.grid(True)

# save figure
plt.tight_layout()
fig.savefig(os.path.join(figs_folder, "ellipse.png"))
plt.show()

