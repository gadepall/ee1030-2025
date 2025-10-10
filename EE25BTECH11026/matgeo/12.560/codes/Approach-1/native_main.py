import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Define symbols and function
x, y = sp.symbols('x y')
f = x**2 + y**2

# Gradient
grad = sp.Matrix([sp.diff(f, v) for v in (x, y)])

# Gradient at (3,4)
px, py = 3, 4
grad_val = grad.subs({x: px, y: py})
norm_val = grad_val.norm()
unit_grad = grad_val / norm_val

print("Unit vector along the direction where f grows the fastest:")
sp.pprint(unit_grad)

# Convert to float for plotting
grad_num = np.array([float(grad_val[0]), float(grad_val[1])])   # (6,8)
unit_grad_num = np.array([float(unit_grad[0]), float(unit_grad[1])])  # normalized

# Grid for contour plot
xx = np.linspace(-5, 5, 200)
yy = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(xx, yy)
Z = X**2 + Y**2

# Plot contour
plt.figure(figsize=(7,6))
contours = plt.contour(X, Y, Z, levels=20, cmap="viridis")
plt.clabel(contours, inline=True, fontsize=8)

# Mark the point (3,4)
plt.scatter(px, py, color="red", label="Point (3,4)")

# Draw full gradient vector
plt.quiver(px, py, grad_num[0], grad_num[1], angles="xy", scale_units="xy", scale=1, color="blue", width=0.005,
label="Full ∇f at (3,4)")

# Draw unit gradient vector
plt.quiver(px, py, unit_grad_num[0], unit_grad_num[1], 
           angles="xy", scale_units="xy", scale=1, color="green", width=0.005,
           label="Unit ∇f at (3,4)")

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Gradient and Unit Gradient at (3,4) for f(x,y) = x² + y²")
plt.legend()
plt.axis("equal")
plt.savefig("/home/user/Matrix Theory: workspace/Matgeo_assignments/12.560/figs/Figure_1.png")
plt.show()

