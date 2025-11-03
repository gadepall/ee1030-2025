import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt

# --- Part 1: Call the C Function ---

# Load the shared library
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '1.so')
c_library = ctypes.CDLL(lib_path)

# Define the function's return type (a C double)
c_function = c_library.getLatusRectumLowerBound
c_function.restype = ctypes.c_double

latus_rectum_bound = c_function()

print(f"The calculated lower bound for the latus rectum is: {latus_rectum_bound:.2f}\n")

theta = np.pi / 3

a = np.cos(theta)
b = np.sin(theta)

# Foci location c, where c^2 = a^2 + b^2
c = np.sqrt(a**2 + b**2) # This will be 1

# Generate x-values for the hyperbola plot
# We need to avoid the region between the vertices (-a to a)
x_right = np.linspace(a, 5, 200)
x_left = np.linspace(-5, -a, 200)
x_hyperbola = np.concatenate([x_left, x_right])

# Calculate y-values from the hyperbola equation: y = +/- b * sqrt(x^2/a^2 - 1)
y_hyperbola_pos = b * np.sqrt(x_hyperbola**2 / a**2 - 1)
y_hyperbola_neg = -y_hyperbola_pos

plt.figure(figsize=(12, 8))

# Plot the two branches of the hyperbola
plt.plot(x_hyperbola, y_hyperbola_pos, color='blue', label=f'Hyperbola for $\\theta = \\pi/3$')
plt.plot(x_hyperbola, y_hyperbola_neg, color='blue')

# Plot the foci
plt.plot([-c, c], [0, 0], 'ro', markersize=8, label=f'Foci at $(\pm {c:.1f}, 0)$')

# Plot the latus rectum chords at the foci
# x = c, y = +/- b^2/a
latus_rectum_y = b**2 / a
plt.plot([c, c], [-latus_rectum_y, latus_rectum_y], 'r--', linewidth=2, label=f'Latus Rectum (length={2*latus_rectum_y:.1f})')
plt.plot([-c, -c], [-latus_rectum_y, latus_rectum_y], 'r--', linewidth=2)

plt.title(f'Hyperbola at the Boundary Case ($l = {latus_rectum_bound:.1f}$)', fontsize=16)
plt.xlabel('x-axis', fontsize=12)
plt.ylabel('y-axis', fontsize=12)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle=':')
plt.legend()
plt.axis('equal') # Ensure the aspect ratio is correct

plt.savefig('1.png')
plt.show()
