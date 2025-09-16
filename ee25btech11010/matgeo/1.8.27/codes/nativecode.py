import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define variables
x, y, z, k = sp.symbols('x y z k', real=True)

# Define points
A = sp.Matrix([3, 4, 5])
B = sp.Matrix([-1, 3, -7])
P = sp.Matrix([x, y, z])

# Distances squared
PA2 = (P - A).dot(P - A)
PB2 = (P - B).dot(P - B)

# Equation condition
eq = sp.Eq(PA2 + PB2, 2*k**2)
print("Expanded equation:")
print(sp.expand(eq))

# Simplify into standard sphere form
expr = sp.expand(PA2 + PB2 - 2*k**2)
expr = sp.simplify(expr)
print("\nSimplified expression = 0:")
print(expr)

# Complete the squares
sphere_eq = sp.together(sp.factor(expr))
print("\nEquation of locus (sphere):")
print(sphere_eq)

# ---- Extract center and radius ----
# We know it's of form (x-x0)^2 + (y-y0)^2 + (z-z0)^2 = R^2
center = sp.Matrix([1, sp.Rational(7,2), -1])
radius_sq = k**2 - sp.Rational(161,4)

print(f"\nCenter: {center}")
print(f"Radius^2: {radius_sq}")

# ---- Plot the sphere for k=10 ----
k_val = 10
R = float(sp.sqrt(radius_sq.subs(k, k_val)))

# Mesh grid
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)
X = float(center[0]) + R*np.outer(np.cos(u), np.sin(v))
Y = float(center[1]) + R*np.outer(np.sin(u), np.sin(v))
Z = float(center[2]) + R*np.outer(np.ones_like(u), np.cos(v))

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, color='cyan', alpha=0.5, edgecolor='k', linewidth=0.3)
ax.scatter([float(center[0])], [float(center[1])], [float(center[2])], color='red', s=50, label="Center")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Sphere locus: PA² + PB² = 2k² (k=10)")
ax.legend()

plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/1.8.27/figs/fig1.png")

plt.show()
