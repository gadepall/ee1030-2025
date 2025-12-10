import numpy as np
import matplotlib.pyplot as plt

# --- Setup for the 3D plot ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# --- Create a grid of points ---
# We will evaluate the z-coordinate for each plane on this x-y grid
x_range = np.linspace(-5, 10, 50)
y_range = np.linspace(-5, 10, 50)
X, Y = np.meshgrid(x_range, y_range)

# --- Define the three planes by solving for z ---
# The equations are:
# 1) x + y + z = 3
# 2) x + 2y + 3z = 4
# 3) x + 4y + 7z = 6  (since k=7)

# Plane 1: z = 3 - x - y
Z1 = 3 - X - Y

# Plane 2: z = (4 - x - 2y) / 3
Z2 = (4 - X - 2*Y) / 3

# Plane 3: z = (6 - x - 4y) / 7
Z3 = (6 - X - 4*Y) / 7

# --- Plot the surfaces of the planes ---
# We use transparency (alpha) so we can see through the planes
ax.plot_surface(X, Y, Z1, alpha=0.6, color='skyblue', label='x + y + z = 3')
ax.plot_surface(X, Y, Z2, alpha=0.6, color='salmon', label='x + 2y + 3z = 4')
ax.plot_surface(X, Y, Z3, alpha=0.6, color='lightgreen', label='x + 4y + 7z = 6')

# --- Calculate and plot the line of intersection ---
# To find the line, we can express x and y in terms of a parameter, t (let z=t)
# From row reduction, we found:
# y = 1 - 2z
# x = 2 + z
# Let z = t, so:
# x = 2 + t
# y = 1 - 2t
# z = t
t = np.linspace(-5, 5, 100)
x_line = 2 + t
y_line = 1 - 2 * t
z_line = t

# Plot the line with a thicker, darker style to make it stand out
ax.plot(x_line, y_line, z_line, color='black', linewidth=3, label='Line of Intersection')

# --- Formatting the plot ---
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Intersection of Three Planes when k=7', fontsize=16)

# Adjust the viewing angle for better clarity
ax.view_init(elev=20, azim=-50)

# The legend for surface plots can be tricky, so a descriptive title is often better.
# However, we can add a simple proxy legend.
import matplotlib.patches as mpatches
p1 = mpatches.Patch(color='skyblue', label='x + y + z = 3')
p2 = mpatches.Patch(color='salmon', label='x + 2y + 3z = 4')
p3 = mpatches.Patch(color='lightgreen', label='x + 4y + 7z = 6')
p4 = plt.Line2D([0], [0], color='black', linewidth=3, label='Line of Intersection')
ax.legend(handles=[p1, p2, p3, p4])
plt.savefig('../figs/fig.png')
plt.show()
