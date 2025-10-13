import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt

# Folder to save figures
figs_folder = os.path.join("..", "figs")

# Load shared object
lib = ctypes.CDLL("./eigen.so")

# Define function signature
lib.eigen_2x2.argtypes = [
    (ctypes.c_double * 2) * 2,           # A matrix
    ctypes.POINTER(ctypes.c_double),     # eigenvalues[2]
    
]
lib.eigen_2x2.restype = None

# Define matrix A = [[4,0],[0,4]]
A = ((ctypes.c_double * 2) * 2)()
A[0][0], A[0][1] = 0.0, 1.0
A[1][0], A[1][1] = 0.0, 1.0

# Allocate arrays for eigenvalues
eigenvalues = (ctypes.c_double * 2)()


# Call C function
lib.eigen_2x2(A, eigenvalues)

# Convert results to Python lists
eigs = [eigenvalues[i] for i in range(2)]

print("Eigenvalues from C:", eigs)

