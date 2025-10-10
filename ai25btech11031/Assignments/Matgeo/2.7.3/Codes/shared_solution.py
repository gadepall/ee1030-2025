import ctypes
import numpy as np

# Load shared library
lib = ctypes.CDLL("./solution.so")

# Define argument and return types
lib.compute_c.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
]

def compute_c(a, b, k):
    a_arr = (ctypes.c_double * 3)(*a)
    b_arr = (ctypes.c_double * 3)(*b)
    c_arr = (ctypes.c_double * 3)()
    lib.compute_c(a_arr, b_arr, ctypes.c_double(k), c_arr)
    return np.array([c_arr[0], c_arr[1], c_arr[2]])

# ---- Take input from user ----
a = list(map(float, input("Enter vector a (3 numbers separated by space): ").split()))
b = list(map(float, input("Enter vector b (3 numbers separated by space): ").split()))
k = float(input("Enter scalar k: "))

# ---- Compute c using .so ----
c = compute_c(a, b, k)

# ---- Output ----
print("Computed c =", c)

