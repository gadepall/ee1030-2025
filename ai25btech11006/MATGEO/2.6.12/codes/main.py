import numpy as np

# Define vectors
a = np.array([3, 1, 2])
b = np.array([2, -2, 4])

# Cross product
cross = np.cross(a, b)

# Magnitudes
mag_a = np.linalg.norm(a)
mag_b = np.linalg.norm(b)
mag_cross = np.linalg.norm(cross)

# Sine of angle
sine_theta = mag_cross / (mag_a * mag_b)

print("sin(theta) =", sine_theta)

