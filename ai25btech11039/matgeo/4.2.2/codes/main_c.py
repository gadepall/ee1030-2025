import ctypes

# Load the shared object file
lib = ctypes.CDLL('./lineparams.so')

# Set argument and return types
lib.line_params.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]
lib.line_params.restype = None

# Line: x - y/5 = 20  => a=1, b=-1/5, c=20
a, b, c = 1.0, -1.0/5.0, 20.0

# Outputs
m0 = ctypes.c_double(); m1 = ctypes.c_double()
n0 = ctypes.c_double(); n1 = ctypes.c_double()
Ax = ctypes.c_double(); Ay = ctypes.c_double()

# Call the C function
lib.line_params(a, b, c,
                ctypes.byref(m0), ctypes.byref(m1),
                ctypes.byref(n0), ctypes.byref(n1),
                ctypes.byref(Ax), ctypes.byref(Ay))

# Print results
print(f"Direction vector m = ({m0.value}, {m1.value})")
print(f"Normal vector n    = ({n0.value}, {n1.value})")
print(f"Point on line A    = ({Ax.value}, {Ay.value})")
