import ctypes
from ctypes import c_double

# Load the compiled shared library
lib = ctypes.CDLL('./main.so')

# Set up argument and return types for the function
lib.point_to_plane_distance.argtypes = [c_double, c_double, c_double]
lib.point_to_plane_distance.restype = c_double

# Try two values of λ from your solution
lambda_values = [2.5, -7.5]

# Fixed point x=2, y=1; varying z = lambda
for lam in lambda_values:
    distance = lib.point_to_plane_distance(2.0, 1.0, lam)
    print(f"λ = {lam} -> Distance = {distance}")

