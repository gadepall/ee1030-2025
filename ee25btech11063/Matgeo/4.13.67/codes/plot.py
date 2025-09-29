import numpy as np
import matplotlib.pyplot as plt

# Define range for x
x = np.linspace(-5, 5, 400)

# Equations of the two lines
y1 = 2*x + 1
y2 = -2*x + 1

# Create the plot
plt.figure(figsize=(7, 7))

# Plot both lines
plt.plot(x, y1, label="y = 2x + 1", color="blue", linewidth=2)
plt.plot(x, y2, label="y = -2x + 1", color="red", linewidth=2)

# Mark the point of intersection (0,1)
plt.scatter(0, 1, color="black", zorder=5)
plt.text(0.1, 1.1, "(0,1)", fontsize=10)

# Axes setup
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)

# Labels, grid and title
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Locus of P: Two Intersecting Lines")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Save the figure
plt.savefig("locus_plot.png", dpi=300)
plt.show()

