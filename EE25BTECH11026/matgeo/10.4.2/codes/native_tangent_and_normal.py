import numpy as np
import matplotlib.pyplot as plt

# Define the curve y = (x-7)/((x-2)(x-3))
def curve(x):
    denom = (x - 2) * (x - 3)
    mask = np.isclose(denom, 0)   # True where denominator ~ 0
    y = (x - 7) / denom
    y[mask] = np.nan
    return y

# Point of interest (x-intercept)
x0, y0 = 7, 0

# Gradient of F(x,y) = x^2 y - 5xy + 6y - x + 7
def grad_F(x, y):
    Fx = 2 * x * y - 5 * y - 1
    Fy = x**2 - 5*x + 6
    return np.array([Fx, Fy])

# Evaluate gradient at (7,0)
Fx, Fy = grad_F(x0, y0)

# Tangent line: Fx*(x-x0) + Fy*(y-y0) = 0
# => slope = -Fx/Fy (if Fy != 0)
m_tan = -Fx / Fy
def tangent(x):
    return y0 + m_tan * (x - x0)

# Normal line: slope = -1/m_tan (perpendicular)
m_norm = -1 / m_tan
def normal(x):
    return y0 + m_norm * (x - x0)

# Print equations
def print_equations():
    print(f"Tangent equation: y = {m_tan:.1f}*(x - {x0}) + {y0}")
    print(f"Normal equation:  y = {m_norm:.1f}*(x - {x0}) + {y0}")

print_equations()


# Plot
x_vals1 = np.linspace(-2, 1.9, 200)
x_vals2 = np.linspace(2.1, 2.9, 200)
x_vals3 = np.linspace(3.1, 12, 200)
y_vals1 = curve(x_vals1)
y_vals2 = curve(x_vals2)
y_vals3 = curve(x_vals3)


plt.figure(figsize=(8,6))

# Curve
plt.plot(x_vals1, y_vals1, 'b')
plt.plot(x_vals2, y_vals2, 'b')
plt.plot(x_vals3, y_vals3, 'b')


# Tangent and normal (extended around x0)
x_line = np.linspace(4, 10, 200)
plt.plot(x_line, tangent(x_line), 'r--', label="Tangent at (7,0)")
plt.plot(x_line, normal(x_line), 'g--', label="Normal at (7,0)")

# Mark the point of tangency
plt.scatter([x0], [y0], color='k', zorder=5)
plt.text(x0+0.2, y0+0.2, "(7,0)")

# Axes and formatting
plt.axhline(0, color='gray', lw=1)
plt.axvline(0, color='gray', lw=1)
plt.ylim(-2, 2)
plt.xlim(-2, 12)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Curve with Tangent and Normal at (7,0)")
plt.grid(True)
plt.savefig("/home/user/Matrix Theory: workspace/Matgeo_assignments/10.4.2/figs/Figure_1.png")
plt.show()

