# solve_reflection.py
import ctypes
from ctypes import c_double, byref

lib = ctypes.CDLL('./problem.so')  # adjust path if needed

# Signatures
lib.reflect_stored.argtypes = [ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
lib.reflect_stored.restype  = None
lib.get_point.argtypes = [ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
lib.get_point.restype  = None
lib.get_line.argtypes  = [ctypes.POINTER(c_double), ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
lib.get_line.restype   = None

# Read stored inputs
x0 = c_double(); y0 = c_double()
a  = c_double(); b  = c_double(); c  = c_double()
lib.get_point(byref(x0), byref(y0))
lib.get_line(byref(a), byref(b), byref(c))

# Compute reflection
xr = c_double(); yr = c_double()
lib.reflect_stored(byref(xr), byref(yr))

print(f"Point P: ({x0.value}, {y0.value})")
print(f"Line: {a.value}*x + {b.value}*y + {c.value} = 0")
print(f"Reflected image: ({xr.value}, {yr.value})")  # (-1.0, 2.0)

