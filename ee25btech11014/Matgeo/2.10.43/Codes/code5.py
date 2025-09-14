import ctypes

# Load the shared library (adjust filename & path if needed)
lib = ctypes.CDLL('./code5.so')  # use 'vectorops.dll' on Windows

# Declare argument and return types for dot
lib.dot.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.dot.restype = ctypes.c_double

# Declare argument types for cross
lib.cross.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.cross.restype = None

def dot(a, b):
    a_c = (ctypes.c_double * 3)(*a)
    b_c = (ctypes.c_double * 3)(*b)
    return lib.dot(a_c, b_c)

def cross(u, v):
    u_c = (ctypes.c_double * 3)(*u)
    v_c = (ctypes.c_double * 3)(*v)
    res_c = (ctypes.c_double * 3)()
    lib.cross(u_c, v_c, res_c)
    return list(res_c)

# Vector a = i - k
a = [1, 0, -1]

# Test values for x and y
xs = [0, 1, 2]
ys = [0, 1, -1]

print("x    y    [a b c]")
for x in xs:
    for y in ys:
        b = [x, 1, 1 - x]
        c = [y, x, 1 + x - y]
        bc = cross(b, c)
        scalar_triple = dot(a, bc)
        print(f"{x:<4} {y:<4} {scalar_triple:.2f}")
