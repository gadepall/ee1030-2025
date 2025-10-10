import ctypes
import platform

# --- 1. Load the shared library ---
if platform.system() == "Windows":
    lib_path = "./libtriangle.dll"
else:
    lib_path = "./libtriangle.so"

try:
    lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"Error loading library: {e}")
    print("Have you compiled triangle_solver.c?")
    exit()

# --- 2. Define the function signature ---
lib.solve_for_p.argtypes = [
    ctypes.c_double,  # x1
    ctypes.c_double,  # y1
    ctypes.c_double,  # x2
    ctypes.c_double,  # x3
    ctypes.c_double,  # y3
    ctypes.c_double,  # area
    ctypes.POINTER(ctypes.c_double), # p1 (output)
    ctypes.POINTER(ctypes.c_double)  # p2 (output)
]
lib.solve_for_p.restype = None # void return type

# --- 3. Prepare input data and output buffers ---
# Input values from the original C code
x1, y1 = 1.0, -3.0
x2 = 4.0
x3, y3 = -9.0, 7.0
area = 15.0

# Create empty C double variables to hold the results.
# These act as output buffers.
p1_result = ctypes.c_double()
p2_result = ctypes.c_double()

# --- 4. Call the C function ---
# Pass the inputs directly and the output buffers by reference.
lib.solve_for_p(x1, y1, x2, x3, y3, area, 
                ctypes.byref(p1_result), 
                ctypes.byref(p2_result))

# --- 5. Print the results ---
# Access the values written by the C function using .value
print(f"Possible values of p are: {p1_result.value:.2f} and {p2_result.value:.2f}")