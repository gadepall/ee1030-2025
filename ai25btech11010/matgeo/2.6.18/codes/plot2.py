import os
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Compile the C program
os.system("gcc c.c -o triangle -lm")

# Step 2: Run the compiled C program
os.system("./triangle")

# Step 3: Load points data
points_data = np.genfromtxt("points.dat", skip_header=1, dtype=None, encoding="utf-8")
labels = [row[0] for row in points_data]
x_vals = np.array([float(row[1]) for row in points_data])
y_vals = np.array([float(row[2]) for row in points_data])

# Step 4: Load area
with open("area.dat") as f:
    area = float(f.read().strip())

# Step 5: Prepare triangle coordinates
triangle_coords = [(x_vals[i], y_vals[i]) for i in range(3)]
triangle_coords.append(triangle_coords[0])  # close the triangle
tx, ty = zip(*triangle_coords)

# Step 6: Plot the triangle
fig, ax = plt.subplots(figsize=(6,6))
ax.plot(tx, ty, 'b-o', label='Triangle')
ax.fill(tx, ty, 'skyblue', alpha=0.3)

# Label points
for i in range(3):
    ax.text(x_vals[i], y_vals[i], f"{labels[i]}", fontsize=12, color='red')

# Axes formatting
ax.axhline(0, color="black", linewidth=1.0, linestyle="--")
ax.axvline(0, color="black", linewidth=1.0, linestyle="--")
ax.set_aspect("equal")
ax.grid(True)
ax.set_title(f"Triangle Plot (Area = {area:.2f})")
plt.legend()

# Step 7: Save and show plot
os.makedirs("../figs", exist_ok=True)
plt.savefig("../figs/triangle_plot.png", dpi=300, bbox_inches="tight")
plt.show()
