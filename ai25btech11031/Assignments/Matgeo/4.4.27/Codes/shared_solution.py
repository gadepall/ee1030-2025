import ctypes

# Load the shared library
lib = ctypes.CDLL("./solution.so")

# Define the Point struct in Python
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

# Tell ctypes about the function signature
lib.solve_for_x.argtypes = [Point, Point, Point]
lib.solve_for_x.restype = ctypes.c_double

# ---- Main Program ----
if __name__ == "__main__":
    # Take inputs for A, C, D
    A_vals = list(map(float, input("Enter coordinates of A (x y z): ").split()))
    C_vals = list(map(float, input("Enter coordinates of C (x y z): ").split()))
    D_vals = list(map(float, input("Enter coordinates of D (x y z): ").split()))

    A = Point(*A_vals)
    C = Point(*C_vals)
    D = Point(*D_vals)

    # Call C function
    x_value = lib.solve_for_x(A, C, D)

    print("The value of x such that A, B, C, D are coplanar is:", round(x_value, 2))

