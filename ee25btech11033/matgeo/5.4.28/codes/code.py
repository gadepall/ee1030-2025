import ctypes
import os

# --- 1. Load the shared library ---
c_lib = ctypes.CDLL('./code.so')

# --- 2. Define the C function's signature ---
# This tells Python what arguments the C function expects and what it returns.
# C function signature: int get_inverse(float* matrix_in, float* matrix_out);
get_inverse_func = c_lib.get_inverse
get_inverse_func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)]
get_inverse_func.restype = ctypes.c_int

# --- 3. Prepare the data for the C function ---
# Define a ctypes array type for a 4-element float array
FloatArray4 = ctypes.c_float * 4

# Input matrix [[2, 4], [-5, -1]] is flattened to [2, 4, -5, -1]
input_matrix = FloatArray4(2, 4, -5, -1)

# Create an empty array to store the result from the C function
inverse_matrix_result = FloatArray4()

print("Python script is running.")
print("Input Matrix from Python:")
print(f"  [[{input_matrix[0]:.1f}, {input_matrix[1]:.1f}],")
print(f"   [{input_matrix[2]:.1f}, {input_matrix[3]:.1f}]]\n")

# --- 4. Call the C function ---
print("Passing data to C function...")
success = get_inverse_func(input_matrix, inverse_matrix_result)
print("... C function has returned.\n")

# --- 5. Process the result ---
if success:
    print("Success! C function calculated the inverse.")
    print("Inverse Matrix received in Python:")
    print(f"  [[{inverse_matrix_result[0]:.3f}, {inverse_matrix_result[1]:.3f}],")
    print(f"   [{inverse_matrix_result[2]:.3f}, {inverse_matrix_result[3]:.3f}]]")
else:
    print("Failure: The C function indicated the matrix is singular (no inverse).")

