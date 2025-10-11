import ctypes
import numpy as np
import itertools

# --- Load C shared library ---
lib = ctypes.CDLL("./gen_system_points.so")
lib.gen_system_points.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

# Storage
A_storage = (ctypes.c_double * 9)()
B_storage = (ctypes.c_double * 3)()
lib.gen_system_points(A_storage, B_storage)

# Convert to numpy
A = np.array(A_storage).reshape(3, 3)
B = np.array(B_storage)

print("Coefficient matrix A:\n", A)
print("RHS vector B:\n", B)

# Solve AX = B
X, Y, Z = np.linalg.solve(A, B)
print("\nSolution (X,Y,Z) = ({}, {}, {})".format(X, Y, Z))

# Symbolic answer
symbolic_points = []
for sx, sy, sz in itertools.product([1, -1], repeat=3):
    symbolic_points.append((f"{'+' if sx>0 else '-'}a",
                            f"{'+' if sy>0 else '-'}b",
                            f"{'+' if sz>0 else '-'}c"))

print("\nSymbolic solutions (in terms of a,b,c):")
for p in symbolic_points:
    print(p)

# Example numeric values
a, b, c = 2.0, 3.0, 1.0   # change these values
numeric_points = [(sx*a, sy*b, sz*c) for sx, sy, sz in itertools.product([1,-1],[1,-1],[1,-1])]

print("\nNumeric solutions (for a={}, b={}, c={}):".format(a, b, c))
for p in numeric_points:
    print(p)

# Save numeric points to file for plotting
np.savetxt("points_abc.txt", numeric_points)
print("\nSaved numeric points to points_abc.txt")

