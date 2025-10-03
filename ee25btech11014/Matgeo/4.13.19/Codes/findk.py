import ctypes

# Load shared library
lib = ctypes.CDLL("./findk.so")

# Define argument types
lib.find_k.argtypes = [ctypes.POINTER(ctypes.c_double)]

# Prepare result array
sol = (ctypes.c_double * 3)()

# Call C function
lib.find_k(sol)

# Extract results
x, y, k = sol[0], sol[1], sol[2]

print(f"Point dividing AB in 3:2 = ({x}, {y})")
print(f"Value of k = {k}")
