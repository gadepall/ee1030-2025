import ctypes

# Load the compiled shared object
# Make sure rectangle_locus.so is in the same directory
lib = ctypes.CDLL('./rectangle_locus.so')

# Define the argument and return types of the C function
# double find_locus(double m, double a, double x)
lib.find_locus.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.find_locus.restype = ctypes.c_double

def call_find_locus(m, a, b):
    results = []
    for x in [b, -b]:
        y = lib.find_locus(m, a, x)
        results.append((x, y))
    return results

if __name__ == "__main__":
    # Example values (you can change these)
    m, a, b = 2.0, 3.0, 4.0

    points = call_find_locus(m, a, b)
    for x, y in points:
        print(f"R = ({x:.2f}, {y:.2f})")

