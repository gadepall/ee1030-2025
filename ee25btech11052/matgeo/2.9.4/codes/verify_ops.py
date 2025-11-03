# File: verify_ops.py
import ctypes

# --- 1. Load the C library ---
vector_lib = ctypes.CDLL('./vector_ops.so')

# --- 2. Problem Setup (Hardcoded values) ---
# Values are taken directly from the problem statement.
a_py = [1.0, 1.0, 1.0]
dot_target_py = 1.0
cross_target_py = [0.0, 1.0, -1.0]

# The unique solution b = (1, 0, 0) we are verifying
b_py = [1.0, 0.0, 0.0]

print("--- Verifying the Hardcoded Solution ---")
print(f"Vector a = {a_py}")
print(f"Target a . b = {dot_target_py}")
print(f"Target a x b = {cross_target_py}")

# --- 3. Set up ctypes function interface ---
DoubleArray3 = ctypes.c_double * 3

vector_lib.verify_solution.argtypes = [
    DoubleArray3,      # Corresponds to a[3]
    DoubleArray3,      # Corresponds to b[3]
    ctypes.c_double,   # Corresponds to target_dot
    DoubleArray3       # Corresponds to target_cross[3]
]
vector_lib.verify_solution.restype = ctypes.c_int

# --- 4. Call the C function ---
a_c = DoubleArray3(*a_py)
b_c = DoubleArray3(*b_py)
cross_target_c = DoubleArray3(*cross_target_py)

print(f"\n--- Verifying solution b = {b_py} ---")
result_code = vector_lib.verify_solution(a_c, b_c, dot_target_py, cross_target_c)

# --- 5. Display the result ---
if result_code == 0:
    print("✅ Success! The vector b is correct.")
elif result_code == 1:
    print("❌ Failure: The dot product does not match.")
elif result_code == 2:
    print("❌ Failure: The cross product does not match.")
else:
    print("❌ Failure: Both the dot and cross product do not match.")