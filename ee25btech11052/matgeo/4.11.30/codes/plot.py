import numpy as np
import matplotlib.pyplot as plt

# Solve manually
x = 2
y = 3

xx = np.linspace(-2, 6, 100)
y1 = xx + 1
y2 = (12 - 3*xx) / 2

plt.plot(xx, y1, label="x - y + 1 = 0")
plt.plot(xx, y2, label="3x + 2y - 12 = 0")

plt.plot(x, y, 'ro')
plt.text(x+0.1, y, f"({x}, {y})")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.title("Graph of Equations")

plt.show()   # Only show, no save
