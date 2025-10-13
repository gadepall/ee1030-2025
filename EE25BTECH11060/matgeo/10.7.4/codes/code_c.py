import ctypes
# Load the shared object file
conic = ctypes.CDLL("./conic_tangent.so")

# Call the function
result = conic.check_tangent()

if result == 1:
    print("The line is a common tangent to both the parabola and the ellipse.")
else:
    print("The line is NOT a common tangent.")
