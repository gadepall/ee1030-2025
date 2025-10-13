import ctypes
import os

# Adjust path if needed
libpath = os.path.abspath("./libcount.so")
lib = ctypes.CDLL(libpath)

lib.get_count.restype = ctypes.c_int

result = lib.get_count()
print("Number of 3x3 matrices with trace(M^T M)=5:", result)
