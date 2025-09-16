import os
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Compile the C program
os.system("gcc c.c -o vectors -lm")

# Step 2: Run the compiled C program
os.system("./vectors")

# Step 3: Load data (skip header row, read mixed types)
data = np.genfromtxt("vectors_data.dat", skip_header=1, dtype=None, encoding="utf-8")

# Separate columns
labels = [row[0] for row in data]   # first column is text
x_vals = np.array([float(row[1]) for row in data])
y_vals = np.array([float(row[2]) for row in data])
mags   = np.array([float(row[3]) for row in data])

# Step 4: Plot vectors
fig, ax = plt.subplots(figsize=(6,6))

for label, x, y, mag in zip(labels, x_vals, y_vals, mags):
    ax.arrow(0, 0, x, y, head_width=0.1, head_length=0.1,
             fc="blue", ec="blue", alpha=0.7, length_includes_head=True)
    ax.text(x*1.1, y*1.1, f"{label}\n|{label}|={mag:.2f}", fontsize=10, ha="center")

# Plot x and y axes
ax.axhline(0, color="black", linewidth=1.0, linestyle="--")  # X-axis
ax.axvline(0, color="black", linewidth=1.0, linestyle="--")  # Y-axis

# Formatting
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect("equal")
ax.grid(True)
ax.set_title("Vectors from C Program with X and Y Axes")

# Save and show plot
plt.savefig("../figs/vectors_from_c.png", dpi=300, bbox_inches="tight")
plt.show()

