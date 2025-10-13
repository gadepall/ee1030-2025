import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Define variables
x, y = sp.symbols('x y')

# Circle equation: x^2 + y^2 - 25 = 0
expr = x**2 + y**2 - 25

# Gradient (normal direction is given by gradient at point)
grad = sp.Matrix([sp.diff(expr, x), sp.diff(expr, y)])

# Point of contact
q = {x: 3, y: 4}

# Normal direction vector (column vector form)
normal_vec = grad.subs(q)
print("Normal direction vector:")
sp.pprint(normal_vec)  # pretty print as column vector

# ---- Plotting ----
# Circle parameters
theta = np.linspace(0, 2*np.pi, 400)
circle_x = 5 * np.cos(theta)
circle_y = 5 * np.sin(theta)

# Plot circle
plt.plot(circle_x, circle_y, label='Circle: x^2+y^2=25')

# Plot point (3,4)
plt.plot(3, 4, 'ro', label='Point (3,4)')

# Normal vector from (3,4)
plt.quiver(3, 4, float(normal_vec[0]), float(normal_vec[1]),
           angles='xy', scale_units='xy', scale=1, color='g', label='Normal vector')

plt.gca().set_aspect('equal', adjustable='box')
plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.savefig("/home/user/Matrix Theory: workspace/Matgeo_assignments/12.560/figs/Figure_2.png")
plt.show()

