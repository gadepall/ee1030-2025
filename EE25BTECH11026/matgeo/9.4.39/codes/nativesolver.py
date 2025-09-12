import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Variables
x, y = sp.symbols('x y', real=True)

# Equations
eq1 = sp.Eq(x**2 - y**2, 180)   # Hyperbola
eq2 = sp.Eq(y**2, 8*x)          # Parabola

# Solve system
solutions = sp.solve([eq1, eq2], [x, y], dict=True)
print("Solutions:")
for sol in solutions:
    print(sol)

# Extract real solutions
real_solutions = [(float(sol[x]), float(sol[y])) for sol in solutions if sol[y].is_real]

# ---- Plotting ----

# Setup plot
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Intersection of Hyperbola and Parabola")
ax.grid(True)

# Range for plotting
xx = np.linspace(-20, 40, 400)

# Hyperbola: x^2 - y^2 = 180 -> y = ±sqrt(x^2 - 180)
xh = np.linspace(-40, 40, 800)
for sign in [1, -1]:
    yh = sign*np.sqrt(np.maximum(xh**2 - 180, 0))  # avoid negatives under sqrt
    ax.plot(xh, yh, 'r', label="Hyperbola" if sign==1 else "")

# Parabola: y^2 = 8x -> y = ±sqrt(8x)
xp = np.linspace(0, 40, 400)  # parabola domain x>=0
for sign in [1, -1]:
    yp = sign*np.sqrt(8*xp)
    ax.plot(xp, yp, 'b', label="Parabola" if sign==1 else "")

# Mark intersection points
for (px, py) in real_solutions:
    ax.plot(px, py, 'ko', markersize=8)
    ax.text(px+0.5, py+0.5, f"({px:.0f},{py:.0f})")

ax.legend()
plt.savefig("/home/user/Matrix Theory: workspace/Matgeo_assignments/9.4.39/figs/Figure_1.png")
plt.show()

