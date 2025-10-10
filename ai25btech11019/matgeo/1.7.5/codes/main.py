import numpy as np
import matplotlib.pyplot as plt

# Value of p for collinearity
p = -1

# Define points (x, y, z=0)
points = np.array([
    [-5,  1, 0],   # A
    [ 1,  p, 0],   # B
    [ 4, -2, 0]    # C
])

# Line equation through the points (in plane z=0)
def line_y(x):
    return (-1/3)*x - (2/3)   # slope = -1/3

xs = np.linspace(-8, 6, 200)
ys = line_y(xs)
zs = np.zeros_like(xs)

# Plot
fig = plt.figure(figsize=(7,6))
ax = fig.add_subplot(111, projection='3d')

# Plot line
ax.plot(xs, ys, zs, color="orange", linewidth=2)

# Scatter the three points
ax.scatter(points[:,0], points[:,1], points[:,2], color="red", s=60)

# Labels for points
labels = ["A(-5,1)", f"B(1,{p})", "C(4,-2)"]
for (x,y,z), label in zip(points, labels):
    ax.text(x, y, z, "  " + label)

# Axes labels
ax.set_title("Collinear Points in 3D View (z=0 plane)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# Adjust aspect ratio and view
ax.set_box_aspect((1,1,0.35))
ax.view_init(elev=22, azim=-60)

plt.show()
