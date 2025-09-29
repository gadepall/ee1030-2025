import ctypes

# Load the shared library compiled from line.c
# Make sure libline.so is in the same folder
lib = ctypes.CDLL("./libline.so")

# Setup the function signatures

# void line_equation(double t, double *x, double *y, double *z)
lib.line_equation.argtypes = [
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
lib.line_equation.restype = None

# void print_line(double t)
lib.print_line.argtypes = [ctypes.c_double]
lib.print_line.restype = None

# -------------------------------
# Example usage of the functions
# -------------------------------
if __name__ == "__main__":
    # Use line_equation() to get coordinates back into Python
    t = 2.0
    x = ctypes.c_double()
    y = ctypes.c_double()
    z = ctypes.c_double()

    lib.line_equation(t, ctypes.byref(x), ctypes.byref(y), ctypes.byref(z))
    print(f"Using line_equation from C: t={t} -> (x, y, z) = ({x.value}, {y.value}, {z.value})")

    # Use print_line() to let C handle printing
    print("\nCalling print_line from C:")
    lib.print_line(3.0)

    # Generate multiple points
    print("\nGenerating multiple points using print_line:")
    for i in range(6):
        lib.print_line(float(i))

