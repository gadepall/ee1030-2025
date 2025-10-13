import ctypes
from ctypes import c_double, byref

lib = ctypes.CDLL('./problem.so')

lib.reflect_stored.argtypes = [ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
lib.get_point.argtypes = [ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
lib.get_line.argtypes  = [ctypes.POINTER(c_double), ctypes.POINTER(c_double), ctypes.POINTER(c_double)]

x0 = c_double(); y0 = c_double()
a  = c_double(); b  = c_double(); c  = c_double()
lib.get_point(byref(x0), byref(y0))
lib.get_line(byref(a), byref(b), byref(c))

xr = c_double(); yr = c_double()
lib.reflect_stored(byref(xr), byref(yr))

def give_data():
    return x0.value, y0.value, a.value, b.value, c.value, xr.value, yr.value

print(f"Point P: ({x0.value}, {y0.value})")
print(f"Line: {a.value}*x + {b.value}*y + {c.value} = 0")
print(f"Reflected image: ({xr.value}, {yr.value})")

