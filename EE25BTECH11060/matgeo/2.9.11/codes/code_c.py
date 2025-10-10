import ctypes
import numpy as np
import platform
import os

# Load C shared library
if platform.system() == 'Windows':
    lib = ctypes.CDLL('./vector_math.dll')
else:
    lib = ctypes.CDLL('./libvector.so')
# Define argtypes and restype
lib.half_diff_norm.argtypes = [ctypes.c_double]*4
lib.half_diff_norm.restype = ctypes.c_double

lib.sin_theta_over_2.argtypes = [ctypes.c_double]
lib.sin_theta_over_2.restype = ctypes.c_double

# Define two vectors (they will be normalized in Python)
a = np.array([1, 2], dtype=np.float64)
b = np.array([2, 1], dtype=np.float64)

# Normalize
a_hat = a / np.linalg.norm(a)
b_hat = b / np.linalg.norm(b)

# Compute dot product
dot_ab = np.dot(a_hat, b_hat)


# Call C functions
lhs = lib.half_diff_norm(a_hat[0], a_hat[1], b_hat[0], b_hat[1])
rhs = lib.sin_theta_over_2(dot_ab)

# Show results
print(f'||0.5(a - b)|| = {lhs:.6f}')
print(f'sin(θ / 2)    = {rhs:.6f}')
print(f'Difference    = {abs(lhs - rhs):.6e}')
import ctypes
import numpy as np
import platform
import os

# Load C shared library
if platform.system() == 'Windows':
    lib = ctypes.CDLL('./vector_math.dll')
else:
    lib = ctypes.CDLL('./libvector.so')

# Define argtypes and restype
lib.half_diff_norm.argtypes = [ctypes.c_double]*4
lib.half_diff_norm.restype = ctypes.c_double

lib.sin_theta_over_2.argtypes = [ctypes.c_double]
lib.sin_theta_over_2.restype = ctypes.c_double

# Define two vectors (they will be normalized in Python)
a = np.array([1, 2], dtype=np.float64)
b = np.array([2, 1], dtype=np.float64)

# Normalize
a_hat = a / np.linalg.norm(a)
b_hat = b / np.linalg.norm(b)

# Compute dot product
dot_ab = np.dot(a_hat, b_hat)

# Call C functions
lhs = lib.half_diff_norm(a_hat[0], a_hat[1], b_hat[0], b_hat[1])
rhs = lib.sin_theta_over_2(dot_ab)

# Show results
print(f'||0.5(a - b)|| = {lhs:.6f}')
print(f'sin(θ / 2)    = {rhs:.6f}')
print(f'Difference    = {abs(lhs - rhs):.6e}')
