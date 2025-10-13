import numpy as np
import matplotlib.pyplot as plt

# Ellipse: 4x^2 + y^2 = 4  ->  (x^2/1^2) + (y^2/2^2) = 1
a = 2   # semi-major axis along y
b = 1   # semi-minor axis along x

theta = np.linspace(0, 2*np.pi, 400)
x = b * np.cos(theta)
y = a * np.sin(theta)

# Plot the ellipse
plt.figure(figsize=(10,10))
plt.plot(x, y, 'g', linewidth=2, label=r'$4x^2 + y^2 = 4$')

# Axes and formatting
plt.axhline(0, color='k', linewidth=0.8)
plt.axvline(0, color='k', linewidth=0.8)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Ellipse: $4x^2 + y^2 = 4$')
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()