import matplotlib.pyplot as plt
import numpy as np

# Given line: 2x + 3y - 5 = 0
a, b, c = 2, 3, -5

# Points
x1, y1 = 8, -9   # A
x2, y2 = 2, 1    # B
px, py = 8/3, -1/9   # Division point

# Line 2x + 3y - 5 = 0 -> y = -(a*x + c)/b
xx = np.linspace(min(x1, x2) - 2, max(x1, x2) + 2, 200)
yy = (-(a * xx + c)) / b

plt.figure(figsize=(6,6))

# Plot line
plt.plot(xx, yy, 'k-', linewidth=1)

# Plot segment AB
plt.plot([x1, x2], [y1, y2], 'b--')

# Plot points
plt.scatter([x1, x2, px], [y1, y2, py], color=['green','green','red'])

# Label points directly on figure
plt.text(x1+0.2, y1, f"A({x1},{y1})", color="green", fontsize=10)
plt.text(x2+0.2, y2, f"B({x2},{y2})", color="green", fontsize=10)
plt.text(px+0.2, py, f"P({px:.2f},{py:.2f})", color="red", fontsize=10)

# Axes lines
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)

# Grid and aspect
plt.grid(True, linestyle='--', alpha=0.6)
plt.gca().set_aspect('equal', adjustable='box')

plt.title("Line 2x+3y-5=0 with Segment AB and Division Point")
plt.savefig('2.png')
plt.show()
