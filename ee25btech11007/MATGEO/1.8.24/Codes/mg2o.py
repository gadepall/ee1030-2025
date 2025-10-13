import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared object
lib = ctypes.CDLL("./mg2.so")

# Define argument and return types
lib.solve_problem.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # Ax, Ay, By
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # p, q, r
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]
lib.solve_problem.restype = None

# Inputs
Ax, Ay = 10.0, -6.0
By = 4.0
p, q, r = 1.0, -2.0, 18.0   # constraint: a - 2b = 18

# Outputs (ctypes)
a = ctypes.c_double()
b = ctypes.c_double()
k = ctypes.c_double()
ABx = ctypes.c_double()
ABy = ctypes.c_double()
norm2 = ctypes.c_double()

# Call C function
lib.solve_problem(
    Ax, Ay, By, p, q, r,
    ctypes.byref(a), ctypes.byref(b), ctypes.byref(k),
    ctypes.byref(ABx), ctypes.byref(ABy), ctypes.byref(norm2)
)

# Convert results into NumPy arrays
A = np.array([Ax, Ay])
B = np.array([k.value, By])
O = np.array([a.value, b.value])

print("A =", A)
print("B =", B)
print("O (midpoint) =", O)
print("Vector A-B =", A - B)
print("Squared distance =", norm2.value)

# Plotting
plt.figure()
plt.plot([A[0], B[0]], [A[1], B[1]], 'k-')  # segment AB
plt.scatter(*A, color='red', label='A')
plt.scatter(*B, color='blue', label='B')
plt.scatter(*O, color='green', label='Midpoint O')

plt.text(A[0]+0.5, A[1], f"A{tuple(A.astype(int))}")
plt.text(B[0]+0.5, B[1], f"B{tuple(B.astype(int))}")
plt.text(O[0]+0.5, O[1], f"O{tuple(O.astype(int))}")

plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title("Segment AB and Midpoint O")
plt.show()
