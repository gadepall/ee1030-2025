# File: main.py
import ctypes
import platform
import math

# --- 1. Load the shared library ---
if platform.system() == "Windows":
    lib_path = "./libvector.dll"
else:
    lib_path = "./libvector.so"

try:
    lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"Error loading library: {e}")
    print("Have you compiled vector_ops.c?")
    exit()

# --- 2. Define types and function signatures ---
# Define a pointer to a C double
c_double_p = ctypes.POINTER(ctypes.c_double)
# Define a Python type for a C array of 3 doubles
Vector3D = ctypes.c_double * 3

# Signature for cross() -> void cross(double*, double*, double*)
lib.cross.argtypes = [c_double_p, c_double_p, c_double_p]
lib.cross.restype = None

# Signature for dot() -> double dot(double*, double*)
lib.dot.argtypes = [c_double_p, c_double_p]
lib.dot.restype = ctypes.c_double

# Signature for magnitude() -> double magnitude(double*)
lib.magnitude.argtypes = [c_double_p]
lib.magnitude.restype = ctypes.c_double


# --- 3. Re-create the logic from the C main() function in Python ---
# Initialize the same vectors
a = Vector3D(1, 0, 0)
b = Vector3D(0, 1, 0)
c = Vector3D(2, 0, 0)
d = Vector3D(0, 2, 0)

# Create empty vectors to hold the results (output buffers)
n1 = Vector3D()
n2 = Vector3D()

# Call the C 'cross' function twice
lib.cross(a, b, n1)
lib.cross(c, d, n2)

# Call the C 'dot' and 'magnitude' functions
dot_product = lib.dot(n1, n2)
mag_n1 = lib.magnitude(n1)
mag_n2 = lib.magnitude(n2)

# Perform the final calculation in Python
if mag_n1 == 0 or mag_n2 == 0:
    angle_radians = 0.0
else:
    # Clamp value to avoid math domain errors with acos
    cos_theta = max(-1.0, min(1.0, dot_product / (mag_n1 * mag_n2)))
    angle_radians = math.acos(cos_theta)

angle_degrees = angle_radians * 180 / math.pi

# --- 4. Print the final results ---
print("--- Logic from main() recreated in Python, using C functions for math ---")
print(f"Angle between the two planes (radians): {angle_radians}")
print(f"Angle between the two planes (degrees): {angle_degrees}")