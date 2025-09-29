import ctypes
from ctypes import c_double, POINTER

# Load the compiled shared object
lib = ctypes.CDLL("./code.so")

# Define argument and return types for the function
lib.compute_line_params.argtypes = [c_double, c_double,
                                    POINTER(c_double), POINTER(c_double),
                                    POINTER(c_double), POINTER(c_double)]

# Inputs
m = -2 - 3**0.5  # given slope
d = 4.0          # distance from origin

# Outputs
A = c_double()
B = c_double()
C1 = c_double()
C2 = c_double()

# Call the C function
lib.compute_line_params(m, d, ctypes.byref(A), ctypes.byref(B), ctypes.byref(C1), ctypes.byref(C2))

# Print the result
print("Equation of the line(s):")
print(f"{A.value:.4f}x + {B.value:.4f}y = {C1.value:.4f}")
print(f"{A.value:.4f}x + {B.value:.4f}y = {C2.value:.4f}")

