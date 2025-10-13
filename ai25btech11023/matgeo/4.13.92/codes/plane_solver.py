import ctypes
import numpy as np

lib = ctypes.CDLL('./plane_solver.so')

solve_plane = lib.solve_plane
solve_plane.restype = None
solve_plane.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'),
    ctypes.c_double, ctypes.c_double,
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'),
    ctypes.c_double,
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

n1 = np.array([1.0, 2.0, 3.0], dtype=np.float64)
n2 = np.array([1.0, -1.0, 1.0], dtype=np.float64)
c1 = 2.0
c2 = 3.0
P = np.array([3.0, 1.0, -1.0], dtype=np.float64)
d = 2.0 / np.sqrt(3)

normal = np.zeros(3, dtype=np.float64)
C = ctypes.c_double()
lambda_out = ctypes.c_double()

solve_plane(n1, n2, c1, c2, P, d, normal, ctypes.byref(C), ctypes.byref(lambda_out))

print("Normal vector to the plane: ", normal)
print("Constant term (C): ", C.value)
print("Lambda solution: ", lambda_out.value)
print("Equation: (%.0f x + %.0f y + %.0f z) = %.0f" % (normal[0], normal[1], normal[2], C.value))
