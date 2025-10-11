import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared C library
lib = ctypes.CDLL("./formula.so")

# Define argument and return types
lib.find_A.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
]
lib.find_A.restype = None

# Input vectors
P = np.array([3.0, -1.0], dtype=np.float64)
B = np.array([2.0, 6.0], dtype=np.float64)
A = np.zeros(2, dtype=np.float64)

# Call C function
lib.find_A(P, B, A)

print("A =", A)

# Plotting
fig, ax = plt.subplots()

# Circle parameters
center = P
radius = np.linalg.norm(A - P)  # radius = distance from center to A (or B)

theta = np.linspace(0, 2*np.pi, 300)
x_circle = center[0] + radius*np.cos(theta)
y_circle = center[1] + radius*np.sin(theta)
ax.plot(x_circle, y_circle, 'b')

# Plot diameter line AB
ax.plot([A[0], B[0]], [A[1], B[1]], 'g--')

# Midpoint of AB for placing text "Diameter"
mid_x = (A[0] + B[0]) / 2
mid_y = (A[1] + B[1]) / 2
ax.text(mid_x + 0.5, mid_y + 0.5, "Diameter", color="green")

# Mark points with coordinates
ax.scatter(*A, color='red')
ax.text(A[0]+0.3, A[1], f"A{tuple(A.astype(int))}")

ax.scatter(*B, color='red')
ax.text(B[0]+0.3, B[1], f"B{tuple(B.astype(int))}")

ax.scatter(*P, color='black')
ax.text(P[0]+0.3, P[1], f"P{tuple(P.astype(int))} (center)")

ax.set_aspect('equal')
ax.grid(True)
plt.show()