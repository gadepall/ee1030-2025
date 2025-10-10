import ctypes
import numpy as np
# Load the shared library
gauss = ctypes.CDLL("./gauss.so")
# Define argument types
gauss.gauss.argtypes = [((ctypes.c_double * 4) * 3), ctypes.POINTER(ctypes.c_double)]
# Input augmented matrix
A = np.array([
    [3, -2, 3, 8],
    [2,  1, -1, 1],
    [4, -3, 2, 4]
], dtype=np.float64)

# Convert numpy to C array
a_c = ((ctypes.c_double * 4) * 3)(*([tuple(row) for row in A]))

# Allocate solution vector
sol = (ctypes.c_double * 3)()

# Call C function
gauss.gauss(a_c, sol)

# Print solution
print("Solution from C function:")
print("x =", sol[0])
print("y =", sol[1])
print("z =", sol[2])