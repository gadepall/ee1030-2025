import numpy as np
import matplotlib.pyplot as plt

# Define the line 3x - 4y - 8 = 0  =>  y = (3x - 8)/4
x = np.linspace(-2, 6, 400)
y = (3*x - 8)/4

# Points
points = [(3, 4), (2, -6)]

# Plot line
plt.plot(x, y, 'b', label='3x - 4y - 8 = 0')

# Plot points
for px, py in points:
    plt.plot(px, py, 'ro')
    plt.text(px+0.2, py, f"({px},{py})", fontsize=10)

# Formatting
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Line and Points")

# Save figure
plt.savefig("line_points.png", dpi=300)
plt.show()
