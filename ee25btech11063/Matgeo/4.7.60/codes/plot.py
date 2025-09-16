import numpy as np
import matplotlib.pyplot as plt

# Line: sqrt(3)x + y - 8 = 0
# => y = -sqrt(3)x + 8
x = np.linspace(-2, 8, 400)
y = -np.sqrt(3) * x + 8

# Plot line
plt.plot(x, y, 'b', label=r'$\sqrt{3}x + y - 8 = 0$')

# Plot normal vector at the foot of perpendicular (p=4, omega=30°)
p = 4
omega = np.pi / 6  # 30 degrees
# Point on the line at perpendicular distance p from origin
x0 = p * np.cos(omega)
y0 = p * np.sin(omega)

# Draw perpendicular from origin
plt.plot([0, x0], [0, y0], 'r--', label='Normal (p=4, ω=30°)')
plt.scatter([x0], [y0], color='k')  # mark foot of perpendicular
plt.scatter([0], [0], color='g', label='Origin')

# Labels, legend, grid
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Line in Normal Form")
plt.legend()
plt.grid(True)
plt.axis("equal")

# Save figure
plt.savefig("line_normal_form.png", dpi=300)
plt.close()

