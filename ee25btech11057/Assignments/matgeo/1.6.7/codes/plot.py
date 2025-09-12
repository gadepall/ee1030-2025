import numpy as np
import matplotlib.pyplot as plt

# Equation: x + 3y - 7 = 0 → y = (7 - x)/3
x_vals = np.linspace(-2, 10, 100)
y_vals = (7 - x_vals) / 3

plt.plot(x_vals, y_vals, label="x + 3y - 7 = 0")

# Given points
points = [(1,2), (7,0)]
for p in points:
    plt.scatter(p[0], p[1], color='red')
    plt.text(p[0]+0.1, p[1]+0.1, f"{p}")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Collinearity of Points")
plt.legend()
plt.grid(True)
plt.savefig('../figs/fig1.png')
plt.show()

