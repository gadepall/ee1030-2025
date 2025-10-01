import sympy as sp

# Define variables
x, y = sp.symbols('x y', real=True)

# Curve equation
eq = x**2 + y**2 - 2*x - 3

# Differentiate implicitly (dy/dx)
dy_dx = sp.diff(eq, x) + sp.diff(eq, y)*sp.Symbol('dy_dx')
# Solve for dy/dx
dy_dx = sp.solve(sp.Eq(dy_dx, 0), sp.Symbol('dy_dx'))[0]

# Condition for tangent parallel to x-axis -> dy/dx = 0
condition = sp.Eq(dy_dx, 0)

# Solve condition -> gives x
x_val = sp.solve(condition, x)

points = []
for xv in x_val:
    # Substitute x into curve to solve for y
    sol_y = sp.solve(eq.subs(x, xv), y)
    for yv in sol_y:
        points.append((float(xv), float(yv)))

print("Points where tangent is parallel to x-axis:")
for p in points:
    print(p)


