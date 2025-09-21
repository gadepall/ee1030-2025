import ctypes

lib = ctypes.CDLL('./mat2.so')

lib.equidistant_line.argtypes = [
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),  # Output array for coeffs
]

lib.equidistant_line.restype = None

res = (ctypes.c_double * 3)()  # To hold a,b,c in ax + by = c

lib.equidistant_line(-5, 4, -1, 6, res)

print(f"Line: {res[0]} x + {res[1]} y = {res[2]}")