import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

# Load compiled C library
c_lib = ctypes.CDLL('./formula.so')

# Set argtypes for section formula
c_lib.section_formula.argtypes = [
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.c_int, ctypes.c_int, ctypes.c_int
]
c_lib.section_formula.restype = None

# Set argtypes for triangle area
c_lib.triangle_area.argtypes = [
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
]
c_lib.triangle_area.restype = ctypes.c_float

# Given vertices
A = np.array([4, 6], dtype=np.float32)
B = np.array([1, 5], dtype=np.float32)
C = np.array([7, 2], dtype=np.float32)

# Points for output
D = np.zeros(2, dtype=np.float32)
E = np.zeros(2, dtype=np.float32)

# Compute D = section formula (A,B, ratio 1:2 → m=1,n=2)
c_lib.section_formula(
    D.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    1, 2, 2
)

# Compute E = section formula (A,C, ratio 1:2 → m=1,n=2)
c_lib.section_formula(
    E.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    C.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    1, 2, 2
)

# Compute areas using C function
area_ABC = c_lib.triangle_area(
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    C.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
)

area_ADE = c_lib.triangle_area(
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    D.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    E.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
)

ratio = area_ADE / area_ABC

# Print results
print("Coordinates:")
print("A =", A)
print("B =", B)
print("C =", C)
print("D =", D)
print("E =", E)
print("\nAreas:")
print("Area(ΔABC) =", area_ABC)
print("Area(ΔADE) =", area_ADE)
print("Ratio (ADE/ABC) =", ratio)

# --- Plot ---
os.makedirs("figs", exist_ok=True)

plt.figure(figsize=(6,6))
# ΔABC
plt.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], 'b-', label="ΔABC")
# ΔADE
plt.plot([A[0], D[0], E[0], A[0]], [A[1], D[1], E[1], A[1]], 'r--', label="ΔADE")

points = np.vstack([A,B,C,D,E])
labels = ['A(4,6)', 'B(1,5)', 'C(7,2)', f"D({D[0]:.