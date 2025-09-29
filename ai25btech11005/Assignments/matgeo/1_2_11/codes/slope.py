import matplotlib.pyplot as plt
import numpy as np

# Points
A = (3, -2)
B1 = (-1, 4)
B2 = (7, -2)
B3 = (3, 4)

# 1) Line through (3,-2) & (-1,4)
x1 = np.linspace(-2, 5, 100)
m1 = (4 - (-2)) / (-1 - 3)  # slope = -1.5
y1 = m1 * (x1 - 3) + (-2)

# 2) Horizontal line through (3,-2) & (7,-2)
x2 = np.linspace(-2, 8, 100)
y2 = np.full_like(x2, -2)

# 3) Vertical line through (3,-2) & (3,4)
x3 = np.full(100, 3)
y3 = np.linspace(-3, 5, 100)

# 4) Line with inclination 60° (slope = tan(60°) = √3 ≈ 1.732) through origin
x4 = np.linspace(-2, 4, 100)
m4 = np.tan(np.radians(60))
y4 = m4 * x4

# Plot all lines
plt.plot(x1, y1, 'orange', label="Through (3,-2) & (-1,4); slope = -1.50")
plt.plot(x2, y2, 'blue', label="Through (3,-2) & (7,-2); slope = 0")
plt.plot(x3, y3, 'green', label="Through (3,-2) & (3,4); vertical (undefined slope)")
plt.plot(x4, y4, 'gold', label="Inclination 60°; slope = 1.732")

# Points
plt.scatter([3, -1, 7, 3, 0], [-2, 4, -2, 4, 0], color='black', zorder=5)
plt.text(3, -2.4, "(3,-2)")
plt.text(-1.5, 4, "(-1,4)")
plt.text(7, -2.4, "(7,-2)")
plt.text(3.1, 4, "(3,4)")
plt.text(0.1, 0.2, "(0,0)")

# Labels and grid
plt.title("Lines and Slopes from the Problem")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True)
plt.legend()
plt.show()
