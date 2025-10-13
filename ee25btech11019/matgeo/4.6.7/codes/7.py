import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./7.so")
lib.line_point.argtypes = [ctypes.c_double, np.ctypeslib.ndpointer(dtype=np.float64)]
lib.line_point.restype = None

def line_point(lambda_val):
    out = np.zeros(3, dtype=np.float64)
    lib.line_point(lambda_val, out)
    return out

# Generate line points
lambdas = np.linspace(-5, 5, 50)
points = np.array([line_point(l) for l in lambdas])

# Given point A
A = np.array([3, 4, 5])

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(points[:,0], points[:,1], points[:,2], label="Line")
ax.scatter(A[0], A[1], A[2], color='red', s=50, label="Point A (3,4,5)")

# Annotate the point
ax.text(A[0], A[1], A[2], "A(3,4,5)", fontsize=10, color='red')

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
plt.show()
