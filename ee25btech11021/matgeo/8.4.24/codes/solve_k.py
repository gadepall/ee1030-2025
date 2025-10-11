import numpy as np
import ctypes

# Load the C shared library (optional, for constants if needed)
lib = ctypes.CDLL('./libparabola.so')

# Example: get constants from C (if needed)
# Not strictly required here, we define directly
n = np.array([[1], [0]])  # directrix vector
c = 1
e = 1
f_target = 8  # from parabola y^2 - kx + 8

# Solve k using matrix method formulas
# u = c*e^2*n - ||n||^2*F, f = ||n||^2 * ||F||^2 - c^2*e^2
# For parabola: F = [[1 + k/2], [0]], f = (1 + k/2)^2 - 1 = 8
temp = f_target + 1
k1 = 2*(np.sqrt(temp) - 1)
k2 = 2*(-np.sqrt(temp) - 1)

print("Possible k values:", k1, k2)

# Save k1 for plotting
with open("k_value.txt", "w") as f:
    f.write(str(k1))

