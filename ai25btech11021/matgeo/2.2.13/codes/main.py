import matplotlib.pyplot as plt
import numpy as np

# Given values
a_mag = np.sqrt(3)
b_mag = 4
dot_product = 2 * np.sqrt(3)

# Compute angle
cos_theta = dot_product / (a_mag * b_mag)
theta = np.arccos(cos_theta)

# Vector a: along x-axis
a = np.array([a_mag, 0])

# Vector b: rotated by angle theta
b = np.array([b_mag * np.cos(theta), b_mag * np.sin(theta)])

# Plot
origin = np.array([0, 0])
plt.quiver(*origin, *a, angles='xy', scale_units='xy', scale=1, color='red', label=r'$\vec{a}$')
plt.quiver(*origin, *b, angles='xy', scale_units='xy', scale=1, color='blue', label=r'$\vec{b}$')

# Annotate the angle
angle_deg = np.degrees(theta)
plt.text(0.5, 0.5, f'$\\theta$ = {angle_deg:.1f}°', fontsize=12)

# Plot settings
plt.xlim(0, 5)
plt.ylim(0, 3)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Angle Between Vectors")
plt.legend()

# Save the plot
plt.savefig("python_plot.png")
plt.show()
