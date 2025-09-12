import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library (make sure libortho.so is in the same folder)
lib = ctypes.CDLL("./libortho.so")

# Define C function signature
lib.orthocenter.argtypes = [ctypes.POINTER(ctypes.c_double),
                            ctypes.POINTER(ctypes.c_double),
                            ctypes.POINTER(ctypes.c_double),
                            ctypes.POINTER(ctypes.c_double)]

# Define triangle vertices
A = np.array([1.0, 1.0], dtype=np.double)
B = np.array([5.0, 1.0], dtype=np.double)
C = np.array([3.0, 4.0], dtype=np.double)
D = np.zeros(2, dtype=np.double)

# Call C function
lib.orthocenter(A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                C.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                D.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

print("Orthocenter D =", D)

# ---- Plotting ----
plt.figure(figsize=(6,6))

# Triangle
plt.plot([A[0],B[0]],[A[1],B[1]],'b')
plt.plot([B[0],C[0]],[B[1],C[1]],'b')
plt.plot([C[0],A[0]],[C[1],A[1]],'b')

# Lines for perpendicularity check
plt.plot([A[0], D[0]], [A[1], D[1]], 'g--', label="AD")
plt.plot([B[0], C[0]], [B[1], C[1]], 'r--', label="BC")
plt.plot([B[0], D[0]], [B[1], D[1]], 'g--', label="BD")
plt.plot([A[0], C[0]], [A[1], C[1]], 'r--', label="AC")

# Points
plt.scatter(*A, color='red')
plt.scatter(*B, color='red')
plt.scatter(*C, color='red')
plt.scatter(*D, color='purple')

# Labels
plt.text(A[0]+0.1, A[1], 'A')
plt.text(B[0]+0.1, B[1], 'B')
plt.text(C[0]+0.1, C[1], 'C')
plt.text(D[0]+0.1, D[1], 'D (Orthocenter)')

plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
