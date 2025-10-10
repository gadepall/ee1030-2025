# File: main.py
import ctypes
import platform

# --- 1. Load the shared library ---
if platform.system() == "Windows":
    lib_path = "./liblambda.dll"
else:
    lib_path = "./liblambda.so"

try:
    lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"Error loading library: {e}")
    print("Have you compiled lambda_solver.c?")
    exit()

# --- 2. Define function signatures ---

# Signature for the first function: solve_for_lambda()
lib.solve_for_lambda.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.solve_for_lambda.restype = ctypes.c_double

# Signature for the second function: verify_scalar_product()
lib.verify_scalar_product.argtypes = [ctypes.c_double]
lib.verify_scalar_product.restype = ctypes.c_double

# --- 3. Prepare input data ---
left_bound = -10.0
right_bound = 10.0
tolerance = 1e-8

# --- 4. Call the C functions ---

# Call the first C function to solve for lambda
computed_lambda = lib.solve_for_lambda(left_bound, right_bound, tolerance)

# Use the result to call the second C function for verification
scalar_product = lib.verify_scalar_product(computed_lambda)

# --- 5. Print the results ---
print("--- Results from C library ---")
print(f"Computed value of lambda: {computed_lambda:.10f}")
print(f"Verification (scalar product) : {scalar_product:.10f}")