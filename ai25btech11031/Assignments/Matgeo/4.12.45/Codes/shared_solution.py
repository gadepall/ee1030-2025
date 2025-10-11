import ctypes
import numpy as np

# Load the shared library
locus = ctypes.CDLL("./solution.so")

# Define argument types
locus.standard_form.argtypes = [
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]

def standard_form(A, B, constant_sum):
    A_arr = (ctypes.c_double * 3)(*A)
    B_arr = (ctypes.c_double * 3)(*B)
    a2 = ctypes.c_double()
    b2 = ctypes.c_double()
    c2 = ctypes.c_double()
    locus.standard_form(A_arr, B_arr, constant_sum, ctypes.byref(a2), ctypes.byref(b2), ctypes.byref(c2))
    return a2.value, b2.value, c2.value

if __name__ == "__main__":
    A = list(map(float, input("Enter coordinates of point A (Ax Ay Az): ").split()))
    B = list(map(float, input("Enter coordinates of point B (Bx By Bz): ").split()))
    constant_sum = float(input("Enter the constant sum of distances: "))

    a2, b2, c2 = standard_form(A, B, constant_sum)

    print("\nStandard form of the locus equation:")
    print(f"x^2/({a2:.6f}) + y^2/({b2:.6f}) + z^2/({c2:.6f}) = 1")
    print("\nWhere:")
    print(f"a = {np.sqrt(a2):.6f}, b = {np.sqrt(b2):.6f}, c = {np.sqrt(c2):.6f}")

