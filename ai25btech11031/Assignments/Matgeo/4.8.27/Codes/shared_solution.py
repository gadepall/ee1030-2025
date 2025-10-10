import ctypes
import numpy as np

# Load the shared object
plane_lib = ctypes.CDLL("./solution.so")

# Define argument & return types for the C functions
# cross_product: void cross_product(double,double,double,double,double,double,double*,double*,double*)
plane_lib.cross_product.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]
plane_lib.cross_product.restype = None

# dot_product: double dot_product(double,double,double,double,double,double)
plane_lib.dot_product.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double
]
plane_lib.dot_product.restype = ctypes.c_double

# plane_equation: void plane_equation(double,double,double,double,double,double,double,double,double,double*)
plane_lib.plane_equation.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double
]
plane_lib.plane_equation.restype = None


def main():
    # Input
    x0, y0, z0 = map(float, input("Enter point (x0 y0 z0): ").split())
    a1, b1, c1, d1 = map(float, input("Enter coefficients of plane1 (a1 b1 c1 d1): ").split())
    a2, b2, c2, d2 = map(float, input("Enter coefficients of plane2 (a2 b2 c2 d2): ").split())

    # Normal vectors
    n1x, n1y, n1z = a1, b1, c1
    n2x, n2y, n2z = a2, b2, c2

    # Cross product for normal
    nx = ctypes.c_double()
    ny = ctypes.c_double()
    nz = ctypes.c_double()
    plane_lib.cross_product(n1x, n1y, n1z, n2x, n2y, n2z,
                             ctypes.byref(nx), ctypes.byref(ny), ctypes.byref(nz))

    # Dot product for RHS
    rhs = plane_lib.dot_product(nx.value, ny.value, nz.value, x0, y0, z0)

    print(f"\nRequired plane equation:")
    print(f"{nx.value:.2f}x + {ny.value:.2f}y + {nz.value:.2f}z = {rhs:.2f}")


if __name__ == "__main__":
    main()

