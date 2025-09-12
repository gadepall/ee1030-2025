import numpy as np
import matplotlib.pyplot as plt

# Endpoints of diameter
x1, y1 = -6, 3
x2, y2 =  6, 4

# Compute center (midpoint)
cx = 0.5 * (x1 + x2)
cy = 0.5 * (y1 + y2)

# Compute radius
dx, dy = x2 - x1, y2 - y1
r = 0.5 * np.sqrt(dx**2 + dy**2)

print("Center:", (cx, cy))
print("Radius:", r)

# Parametric circle
theta = np.linspace(0, 2*np.pi, 400)
xc = cx + r*np.cos(theta)
yc = cy + r*np.sin(theta)

# Plot
fig, ax = plt.subplots()

# Circle (blue)
ax.plot(xc, yc, color="blue", label="Circle")

# Diameter endpoints + line (green)
ax.plot([x1, x2], [y1, y2], 'o-', color="green", label="Diameter")

# Center (red point)
ax.plot(cx, cy, 'ro', label="Center")

# Formatting
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend()
ax.set_title(f"Circle with diameter endpoints ({x1},{y1}) and ({x2},{y2})")

plt.show()

