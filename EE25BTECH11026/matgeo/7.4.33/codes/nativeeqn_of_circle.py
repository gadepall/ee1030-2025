import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import matplotlib as mp
mp.use("TkAgg")


x, y = sp.symbols('x y', real=True)
sqrt3 = sp.sqrt(3)

# center O and radius
O = sp.Matrix([sqrt3, 1])
r = sp.Integer(1)
X=np.array([x,y])
# quadratic form: x^T x - 2 O^T x + (O^T O - r^2) = 0
expr = (X.dot(X) - 2*O.dot(X) + (O.dot(O) - r**2)).expand()
sp.pprint(expr)
print("=0")

# --- numerical center for plotting ---
h = float(sqrt3.evalf())
k = 1.0
r_num = 1.0

# --- plotting ---
theta = np.linspace(0, 2*np.pi, 500)
x_circle = h + r_num * np.cos(theta)
y_circle = k + r_num * np.sin(theta)

# Line PQ: sqrt(3) x + y - 6 = 0
a, b, c = np.sqrt(3), 1.0, -6.0
# pick a range that shows circle and line
x_vals = np.linspace(h - 3, h + 6, 400)
y_vals = -(a*x_vals + c) / b

# Tangency point D (given)
D = np.array([3*np.sqrt(3)/2, 3/2])

plt.figure(figsize=(7,7))
plt.plot(x_circle, y_circle, label="Circle C")
plt.plot(x_vals, y_vals, label=r"Line PQ: $\sqrt{3}x + y - 6 = 0$")
plt.scatter([D[0]], [D[1]], color='red', zorder=5, label="D (tangency)")
plt.scatter([h], [k], color='black', zorder=5, label=r"Center $O=(\sqrt{3},1)$")

plt.gca().set_aspect('equal', 'box')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.title("Equation of Circle C")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("/home/user/Matrix/Matgeo_assignments/7.4.33/figs/Figure_1.png")
plt.show()

