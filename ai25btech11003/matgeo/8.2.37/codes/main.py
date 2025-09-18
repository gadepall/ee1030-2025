import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library to ensure linkage
ctypes.CDLL('./main.so')

# Read parameters: h, k, p, fx, fy, dx
h, k, p, fx, fy, dx = np.loadtxt('main.dat').T

# Generate parabola points
y = np.linspace(k - 10, k + 10, 400)
x = (y - k)**2 / (4 * p) + h

plt.figure(figsize=(6,6))
# Parabola curve
plt.plot(x, y, 'b', linewidth=2, label='Parabola')
# Vertex
plt.plot(h, k, 'ro', label='Vertex (V)')
# Focus
plt.plot(fx, fy, 'go', label='Focus (F)')
# Directrix
plt.axvline(dx, color='m', linestyle='--', label='Directrix x+5=0')
# Axes
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
# Labels positioned: V to left, F to right
plt.text(h - 1.0, k, 'V', fontsize=12, color='r')
plt.text(fx + 0.5, fy, 'F', fontsize=12, color='g')
# Legend
plt.legend(loc='upper right')
# Title and grid
plt.title('Parabola')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(True)
# Save figure
plt.savefig('fig1.png', dpi=150)
plt.close()

