import numpy as np
import ctypes

# ----------------------------
# (1) NumPy derivation
# ----------------------------

A = np.array([[1], [2]])   # column vector
print("(0.1) A =\n", A, "\n")

m = 1 / np.tan(np.deg2rad(30))
print("(0.2) m = 1/tan(30°)")
print("(0.3) m =", np.sqrt(3), "\n")

n = np.array([[np.sqrt(3)], [-1]])
print("(0.4) n =\n", n, "\n")

lhs = n.T
rhs = lhs @ A
print("(0.5) n^T x = n^T A\n")
print("(0.6)", lhs, " x = ", lhs, A, "\n")
print("(0.7)", lhs, " x = ", rhs, "\n")

# ----------------------------
# (2) Call C shared library
# ----------------------------

lib = ctypes.CDLL("./libline.so")

lib.line_equation.argtypes = [ctypes.c_double, ctypes.c_double,
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double)]
lib.line_equation.restype = None

nx = ctypes.c_double()
ny = ctypes.c_double()
c  = ctypes.c_double()

lib.line_equation(1.0, 2.0, ctypes.byref(nx), ctypes.byref(ny), ctypes.byref(c))

print("\n--- From C code ---")
print(f"n = ({nx.value:.3f}, {ny.value:.3f})")
print(f"Equation: {nx.value:.3f}*x1 + {ny.value:.3f}*x2 = {c.value:.3f}")

