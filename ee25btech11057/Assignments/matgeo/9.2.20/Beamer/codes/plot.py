import numpy as np
import matplotlib.pyplot as plt

# Function definitions
def parabola_x(y):
    return y**2

# Compute a = 4^(2/3)
a = 4**(2/3)

# y values for plotting
y = np.linspace(-2.2, 2.2, 400)

# x values for curves
x_parabola = parabola_x(y)
x_vertical = 4 * np.ones_like(y)
x_dividing = a * np.ones_like(y)

# Plot settings
plt.figure(figsize=(7,6))
plt.plot(x_parabola, y, 'b', linewidth=2, label='$x = y^2$')
plt.plot(x_vertical, y, 'r', linewidth=2, label='$x = 4$')
plt.plot(x_dividing, y, 'g--', linewidth=2, label=fr'$x = a = {a:.3f}$')

# Fill area between x = y^2 and x = 4
plt.fill_betweenx(y, x_parabola, x_vertical, color='lightcoral', alpha=0.3)

# Labels near the lines (not overlapping)
plt.text(1.0, 1.3, '$x = y^2$', color='b', fontsize=12)
plt.text(4.1, 1.7, '$x = 4$', color='r', fontsize=12)
plt.text(a + 0.05, 0.0, fr'$x = {a:.3f}$', color='g', fontsize=12)

# Axes and limits
plt.axhline(0, color='k', linewidth=1)
plt.axvline(0, color='k', linewidth=1)
plt.xlim(-0.5, 6.0)
plt.ylim(-3.0, 3.0)

# Title and labels
plt.title("Region between $x = y^2$ and $x = 4$ divided equally by $x = a$")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# Aspect ratio equal
plt.gca().set_aspect('equal', adjustable='box')

plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig("../figs/fig15.png")
plt.show()

