import ctypes

# Load the shared library
lib = ctypes.CDLL("./triangle.so")

# Define return/argument types
lib.compute_triangle.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.compute_triangle.restype = None

# Prepare array for results (6 doubles: Ax, Ay, Bx, By, Cx, Cy)
coords = (ctypes.c_double * 6)()

# Call the C function
lib.compute_triangle(coords)

# Extract results
Ax, Ay, Bx, By, Cx, Cy = coords

print(f"Coordinates of A: ({Ax:.2f}, {Ay:.2f})")
print(f"Coordinates of B: ({Bx:.2f}, {By:.2f})")
print(f"Coordinates of C: ({Cx:.2f}, {Cy:.2f})")

