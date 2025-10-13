import ctypes
import os
import numpy as np

# Must match the number of points defined in ellipse.c
N = 400

# Load the shared object
lib = ctypes.CDLL("./ellipse.so")

# Define argument and return types for the C function
lib.generate_ellipse.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS")
]
lib.generate_ellipse.restype = None

# Create numpy arrays to hold results
x_vals = np.zeros(N, dtype=np.float64)
y_upper = np.zeros(N, dtype=np.float64)
y_lower = np.zeros(N, dtype=np.float64)

# Call the C function
lib.generate_ellipse(x_vals, y_upper, y_lower)

# Print some sample results to verify
print("Sample Ellipse Points:")
for i in range(0, N, 50):  # print every 50th point
    print(f"x = {x_vals[i]:.3f}, y_upper = {y_upper[i]:.3f}, y_lower = {y_lower[i]:.3f}")

print("\nC function executed successfully.")

