import os
import numpy as np
import matplotlib.pyplot as plt

# Folder to save figures
figs_folder = os.path.join("..", "figs")

x, y, z = 0.0395, 0.4960, 0.1008  # example solution
print("Solution:", (x, y, z))

# -------------------------------
# Plotting the 3 planes as full sheets
# -------------------------------
# Define wider ranges for X, Y, Z to make planes look like sheets
x_vals = np.linspace(-5, 5, 100)
y_vals = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x_vals, y_vals)

# Plane 1: 10x - y + z = 0 -> z = -10x + y
Z1 = -10*X + Y

# Plane 2: x + 10y = 5 -> vertical plane, z free
y2_vals = np.linspace(-5, 5, 100)
z2_vals = np.linspace(-5, 5, 100)
Y2, Z2 = np.meshgrid(y2_vals, z2_vals)
X2 = 5 - 10*Y2

# Plane 3: y + 5z = 1 -> z = (1 - y)/5
Z3 = (1 - Y)/5

# -------------------------------
# Plotting
# -------------------------------
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection="3d")

# Plane 1
ax.plot_surface(X, Y, Z1, alpha=0.5, color="red")

# Plane 2
ax.plot_surface(X2, Y2, Z2, alpha=0.5, color="blue")

# Plane 3
ax.plot_surface(X, Y, Z3, alpha=0.5, color="green")

# Solution point
ax.scatter(x, y, z, color="black")
ax.text(x+0.2, y+0.2, z+0.2, f"P({x:.4f},{y:.4f},{z:.4f})", fontsize=10, color="black")

# Axes labels and title
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
ax.set_title("Intersection of Three Planes - Gauss Seidel Solution")
ax.grid(True)

# Save figure
plt.tight_layout()
fig.savefig(os.path.join(figs_folder, "solution_gauss_seidel.png"))
plt.show()

