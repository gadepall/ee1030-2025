import ctypes
from ctypes import c_double
import numpy as np
import matplotlib.pyplot as plt

# 1. Configure ctypes to match your C function signature
Array2 = c_double * 2
lib = ctypes.CDLL("./so_main.so")
lib.external_division_k1_array.argtypes = [Array2, Array2, c_double, Array2]
lib.external_division_k1_array.restype  = None

# 2. Define input vectors a, b and the scalar k
a_vals = [1.0, 0.0]
b_vals = [0.0, 1.0]
k = 2.0

# 3. Prepare C‐array arguments and call the C function to fill v_vals
a = Array2(*a_vals)
b = Array2(*b_vals)
v = Array2()                
lib.external_division_k1_array(a, b, k, v)
v_vals = [v[0], v[1]]

# 4. Compute X and Y in Python
X = 3 * np.array(a_vals) + np.array(b_vals)
Y = np.array(a_vals) - 3 * np.array(b_vals)

# 5. Plot vectors X, Y, V from the origin
plt.figure(figsize=(10, 10))
plt.quiver(0, 0, X[0], X[1], angles='xy', scale_units='xy', scale=1,
           color='r', label='X = 3a + b')
plt.quiver(0, 0, Y[0], Y[1], angles='xy', scale_units='xy', scale=1,
           color='g', label='Y = a - 3b')
plt.quiver(0, 0, v_vals[0], v_vals[1], angles='xy', scale_units='xy', scale=1,
           color='b', label='V = (kY – X)/(k–1)')

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Vector Plot of X, Y, and V (from C)')
plt.grid(True)
plt.legend(loc='upper left')
plt.gca().set_aspect('equal', 'box')

plt.show()
