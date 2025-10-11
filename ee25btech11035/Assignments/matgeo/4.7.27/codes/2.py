import matplotlib.pyplot as plt
import numpy as np

# Point
x0, y0 = 3, 2

# Range of x values
x_vals = np.linspace(0, 6, 100)

# Given line: y = x
y_given = x_vals

# Perpendicular line: y = -x + 5
y_perp = -x_vals + 5

# Plot
plt.figure(figsize=(6,6))
plt.plot(x_vals, y_given, 'r--', label="Given line y = x")   # dashed red
plt.plot(x_vals, y_perp, 'b-', label="Perpendicular line")   # solid blue

# Point with label
plt.scatter(x0, y0, color='black')
plt.text(x0+0.1, y0+0.1, f"({x0},{y0})", fontsize=10)

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Given line (dashed), Perpendicular line (solid), Point (3,2)")
plt.grid(True)
plt.axis("equal")
plt.savefig('2.png')
plt.show()
