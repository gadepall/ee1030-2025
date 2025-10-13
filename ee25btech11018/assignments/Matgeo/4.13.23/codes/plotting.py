
import matplotlib.pyplot as plt
import numpy as np

# Example coefficients (you can change these)
a, b, c, d = 1.0, 1.0, -2.0, -3.0

# Intersection point (from condition y = -x)
x = -c / (2 * a)
y = -x

# Create range of x values for plotting
X = np.linspace(-10, 10, 400)

# Line1: 4ax + 2ay + c = 0 -> y = -(4aX + c)/(2a)
Y1 = -(4 * a * X + c) / (2 * a)

# Line2: 5bx + 2by + d = 0 -> y = -(5 * b * X + d) / (2 * b)
Y2 = -(5 * b * X + d) / (2 * b)

# y = -x line
Y_diag = -X

# ---------- Plot ----------
plt.figure(figsize=(6, 6))
plt.axhline(0, color="black", linewidth=0.8)  # x-axis
plt.axvline(0, color="black", linewidth=0.8)  # y-axis

plt.plot(X, Y1, label="Line 1: 4a·x + 2a·y + c = 0")
plt.plot(X, Y2, label="Line 2: 5b·x + 2b·y + d = 0")
plt.plot(X, Y_diag, "g--", label="y = -x")

# Mark intersection point with symbolic label
plt.scatter([x], [y], color="red", s=80, zorder=5)
plt.text(x + 0.5, y - 0.5,
         "Intersection:\n(-c/(2a), c/(2a))\n= (-d/(3b), d/(3b))",
         fontsize=10, color="red")

plt.title("Intersection of Two Lines with Condition y = -x")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(loc="best")
plt.grid(True)
plt.show()

