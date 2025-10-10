import ctypes
import os

# Load the shared object file
lib_path = os.path.abspath("liblineeq.so")
lib = ctypes.CDLL(lib_path)

# Define the function's argument types
lib.line_from_intercepts.argtypes = [ctypes.c_double, ctypes.c_double]

# Optional: Define the return type (void function, so None)
lib.line_from_intercepts.restype = None

# Example intercepts
x_intercept = -3.0
y_intercept = 2.0

print("Calling C function from Python with:")
print(f"  X-intercept = {x_intercept}")
print(f"  Y-intercept = {y_intercept}\n")

# Call the function
lib.line_from_intercepts(x_intercept, y_intercept)
