import ctypes
import os

# Define a class that mirrors the C struct.
# This tells ctypes how to interpret the memory.
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_float),
                ("y", ctypes.c_float)]

# --- Load the Shared Library ---
lib_name = 'line_generator.so'
if os.name == 'nt': # If on Windows
    lib_name = 'line_generator.dll'

# Load the library from the current directory
try:
    lib = ctypes.CDLL(os.path.abspath(lib_name))
except OSError as e:
    print(f"Error: Could not load the shared library '{lib_name}'.")
    print("Please make sure you have compiled the C code first.")
    print(f"Details: {e}")
    exit()


# --- Define Function Signatures (Argument and Return Types) ---

# Get a handle to the generate_points_on_line function
generate_points = lib.generate_points_on_line
# Define the types of the arguments for type safety
generate_points.argtypes = [
    Point,                                # Point A
    Point,                                # Point B
    ctypes.c_int,                         # num_steps
    ctypes.POINTER(ctypes.POINTER(Point)),# result_array (pointer to a pointer)
    ctypes.POINTER(ctypes.c_int)          # count (pointer to an int)
]
# This function does not return a value directly (it's void)
generate_points.restype = None

# Get a handle to the memory freeing function
free_memory = lib.free_points_memory
free_memory.argtypes = [ctypes.POINTER(Point)] # Takes a pointer to the Point array
free_memory.restype = None


# --- Call the C Function from Python ---

# 1. Define the input points
A = Point(x=7.0, y=-2.0)
B = Point(x=1.0, y=-5.0)
num_steps = 20

# 2. Prepare pointers to receive the output from the C function
result_ptr = ctypes.POINTER(Point)()
count = ctypes.c_int()

# 3. Call the function, passing the pointers using byref
generate_points(A, B, num_steps, ctypes.byref(result_ptr), ctypes.byref(count))

# 4. Convert the C array into a Python list
# The data is in result_ptr, and its size is in count.value
python_points = []
for i in range(count.value):
    point = result_ptr[i]
    python_points.append((point.x, point.y))

# 5. IMPORTANT: Free the C-allocated memory to prevent memory leaks
free_memory(result_ptr)


# --- Display the Results ---
print(f"Successfully generated {len(python_points)} points from the C function:")
for i, p in enumerate(python_points):
    print(f"Point {i:2d}: ({p[0]:.3f}, {p[1]:.3f})")
