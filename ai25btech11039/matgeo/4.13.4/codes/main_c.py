import ctypes
import os

# Load the shared object file
lib_path = os.path.abspath("libreflect.so")   # use "libreflect.dll" on Windows
lib = ctypes.CDLL(lib_path)

# Define the function's argument and return types
lib.reflect_point_y_eq_x.argtypes = [ctypes.c_double]
lib.reflect_point_y_eq_x.restype  = None

# Example parameter t > 0
t = 2.0

print("Calling C function with:")
print(f"  t = {t}\n")

# Call the C function (it prints Q and R and the mirror line)
lib.reflect_point_y_eq_x(t)

