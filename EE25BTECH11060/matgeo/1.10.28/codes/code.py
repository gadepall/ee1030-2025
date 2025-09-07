import matplotlib.pyplot as plt
import numpy as np

# Angle in radians
theta = np.deg2rad(30)

# Components of the unit vector
x = np.cos(theta)
y = np.sin(theta)

# Plot settings
plt.figure(figsize=(5,5))
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Draw the unit vector
plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='r')

# Set axis limits
plt.xlim(-0.2, 1.2)
plt.ylim(-0.2, 1.2)

# Labels
plt.text(x/2, y/2, r'$\frac{\sqrt{3}}{2}\hat{i} + \frac{1}{2}\hat{j}$', fontsize=12, color='blue')
plt.title("Unit Vector at 30° with X-axis")
plt.gca().set_aspect('equal')

plt.show()
