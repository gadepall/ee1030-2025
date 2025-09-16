import ctypes

# Load the shared library

lib = ctypes.CDLL("./mat.so")   # use "gram.dll" on Windows


# Define argument and return types
lib.check_coplanar.argtypes = [ctypes.POINTER(ctypes.c_int),
                               ctypes.POINTER(ctypes.c_int),
                               ctypes.POINTER(ctypes.c_int)]
lib.check_coplanar.restype = ctypes.c_int

def check_coplanar(a, b, c):
    arr_a = (ctypes.c_int * 3)(*a)
    arr_b = (ctypes.c_int * 3)(*b)
    arr_c = (ctypes.c_int * 3)(*c)
    result = lib.check_coplanar(arr_a, arr_b, arr_c)
    return bool(result)

# Example usage
a = [1, 0, 0]
b = [0, 1, 0]
c = [1, 1, 0]   # coplanar with a,b
print("Are they coplanar?", check_coplanar(a, b, c))

