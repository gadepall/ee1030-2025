import ctypes
import numpy as np

# Load shared C library
lib = ctypes.CDLL("./generate_system.so")
lib.generate_system.argtypes = [ctypes.c_double, ctypes.c_double,
                                ctypes.POINTER(ctypes.c_double),
                                ctypes.POINTER(ctypes.c_double)]

def generate_system(p, q):
    A = (ctypes.c_double * 4)()
    b = (ctypes.c_double * 2)()
    lib.generate_system(p, q, A, b)
    A_np = np.array([[A[0], A[1]], [A[2], A[3]]])
    b_np = np.array([b[0], b[1]])
    return A_np, b_np

# Example usage
p, q = 2, 3
A, b = generate_system(p, q)

print("Given system:")
print(f"{p}x + {q}y = {p-q}")
print(f"{q}x - {p}y = {p+q}\n")

print("Matrix form:")
print("A =", A)
print("b =", b, "\n")

# Solve using normal equations: (A^T A)x = A^T b
lhs = A.T @ A
rhs = A.T @ b
x = np.linalg.solve(lhs, rhs)

print("Solution vector x =", x)

