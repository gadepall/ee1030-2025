import numpy as np
import matplotlib.pyplot as plt

# Points
x1, y1 = 2, -3
x2, y2 = 4, -5

# Step 1: direction vector m
m = np.array([x2 - x1, y2 - y1])

# Step 2: normal vector n (perpendicular to m)
n = np.array([m[1], -m[0]])

# Step 3: constant c using (x1,y1)
c = np.dot(n, np.array([x1, y1]))

print(f"Equation of line: {n[0]}*x + {n[1]}*y = {c}")

# ---- Plotting ----
# Create x range
x_vals = np.linspace(0, 6, 100)
# Solve for y from equation n1*x + n2*y = c
y_vals = (c - n[0]*x_vals) / n[1]

plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, 'b-', label=f'Line: {n[0]}x + {n[1]}y = {c}')

# Plot points
plt.scatter([x1, x2], [y1, y2], color='red', zorder=5)
plt.text(x1, y1, f'({x1},{y1})', fontsize=10, ha='right')
plt.text(x2, y2, f'({x2},{y2})', fontsize=10, ha='right')

# Axes setup
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Line passing through (2,-3) and (4,-5)")
plt.show()
