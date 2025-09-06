import ctypes
import numpy as np
import matplotlib.pyplot as plt
import math

# Load shared library
lib = ctypes.CDLL("./main.so")

# Define signatures
lib.distance_squared.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS"),
    ctypes.POINTER(ctypes.c_double)
]
lib.distance_squared.restype = None

def distance_squared(A, B):
    res = ctypes.c_double()
    lib.distance_squared(A, B, ctypes.byref(res))
    return res.value

# Point A
A = np.array([3.0, -1.0], dtype=np.float64)

# B points from solving equation (y = 5 or y = -7)
solutions = [5.0, -7.0]
points = []

for yB in solutions:
    B = np.array([11.0, yB], dtype=np.float64)
    d2 = distance_squared(A, B)
    d = math.sqrt(d2)
    print(f"For y = {yB}, distance AB = {d}")
    points.append(B)

# --- Plot ---
plt.figure(figsize=(6,6))
plt.scatter(A[0], A[1], color="red")
plt.text(A[0]+0.2, A[1]+0.2, "A(3, -1)", color="red", fontsize=10)

for i, B in enumerate(points, start=1):
    plt.scatter(B[0], B[1], color="blue")
    plt.text(B[0]+0.2, B[1]+0.2, f"B{ i }(11, {int(B[1])})", color="blue", fontsize=10)
    plt.plot([A[0], B[0]], [A[1], B[1]], linestyle="--")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Points A and B with distance 10 (using C distance_squared)")
plt.grid(True)
plt.axis("equal")
plt.show()
