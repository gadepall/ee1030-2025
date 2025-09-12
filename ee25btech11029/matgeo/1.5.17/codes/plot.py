import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./line_segment.so")

# Define argument types for the C function
lib.line_segment_gen.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),  # X
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),  # Y
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),  # A
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),  # B
    ctypes.c_int
]

# Define start & end points
A = np.array([4.0, 4.0], dtype=np.double)    # Point (4,4)
B = np.array([-2.0, 6.0], dtype=np.double)   # Point (-2,6)
n = 20  # number of segments

# Allocate space for results
X = np.zeros(n+1, dtype=np.double)
Y = np.zeros(n+1, dtype=np.double)

# Call the C function
lib.line_segment_gen(X, Y, A, B, n)

# Compute midpoint
midpoint = np.array([(A[0] + B[0]) / 2, (A[1] + B[1]) / 2])

# --------- Plotting ---------
plt.figure(figsize=(6,6))

# Draw line segment
plt.plot(X, Y, 'b-', label="Line segment")

# Mark endpoints
plt.scatter(A[0], A[1], color='red', s=80, zorder=3, label="Point A (4,4)")
plt.scatter(B[0], B[1], color='green', s=80, zorder=3, label="Point B (-2,6)")

# Mark midpoint
plt.scatter(midpoint[0], midpoint[1], color='purple', s=100, marker='x', zorder=4, label="Midpoint (1,5)")

# Labels & grid
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line segment between A(4,4) and B(-2,6) with Midpoint")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.savefig("../figs/line_segment.png")
plt.show()

