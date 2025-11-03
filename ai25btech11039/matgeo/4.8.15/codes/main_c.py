import ctypes
import os

# Load the shared object file
lib_path = os.path.abspath("libfootx.so")   # use "libfootx.dll" on Windows
lib = ctypes.CDLL(lib_path)

# Define the function's argument types and return type
lib.foot_to_xaxis_print.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.foot_to_xaxis_print.restype = None

# Example point P (change if you want)
Px, Py, Pz = 0.0, 1.0, 2.0

print("Calling C function from Python with:")
print(f"  P = ({Px}, {Py}, {Pz})\n")

# Call the C function (it prints the result)
lib.foot_to_xaxis_print(Px, Py, Pz)
