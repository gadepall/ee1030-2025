import numpy as np
import matplotlib.pyplot as plt

# Inputs
cx, cy = 4.0, 4.0   # centre
x1, y1 = 4.0, 0.0   # one endpoint

# Other endpoint using symmetry
x2 = 2*cx - x1
y2 = 2*cy - y1
print("Other end of diameter:", (x2, y2))

# Radius = distance from centre to endpoint
r = np.sqrt((x1 - cx)**2 + (y1 - cy)**2)

# Generate circle points
theta = np.linspace(0, 2*np.pi, 500)
x_circle = cx + r * np.cos(theta)
y_circle = cy + r * np.sin(theta)

# Plot
plt.figure(figsize=(6,6))
plt.plot(x_circle, y_circle, label="Circle")

plt.scatter([x1, x2], [y1, y2], color="red", s=80, label="Diameter Endpoints")
plt.text(x1 - 0.5, y1 - 0.5, f"({x1:.0f}, {y1:.0f})", color="red", fontsize=10)
plt.text(x2 + 0.5, y2, f"({x2:.0f}, {y2:.0f})", color="red", fontsize=10)

plt.scatter(cx, cy, color="blue", marker="x", s=200, linewidths=3, label="Centre")
plt.text(cx + 0.5, cy + 0.5, f"({cx:.0f}, {cy:.0f})", color="blue", fontsize=10)

plt.plot([x1, x2], [y1, y2], 'g--', label="Diameter")
plt.axis("equal")
plt.legend(loc="upper right")
plt.title("Circle with Given Centre and Diameter")
plt.savefig("/Users/tarak/Documents/ee1030-2025/MatGeo/1.5.4/figs/Figure_1.png")
plt.show()
