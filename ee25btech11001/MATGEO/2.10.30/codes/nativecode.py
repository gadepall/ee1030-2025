import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./code.so")
lib.find_a.argtypes = [ctypes.c_double, ctypes.c_double,
                       ctypes.c_double, ctypes.c_double,
                       ctypes.c_double]
lib.find_a.restype = ctypes.c_double

# Input values from the question
x1, y1 = 60, 3
x2, y2 = 40, -6
y3 = -52

# Call C function to compute 'a'
a = lib.find_a(x1, y1, x2, y2, y3)
print("Value of a =", a)

# Define points
A = np.array([x1, y1])
B = np.array([x2, y2])
C = np.array([a, y3])

# Plot points
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color="red")

# Add labels near each point
plt.text(A[0] + 1, A[1] + 1, "A(60, 3)", fontsize=10, color="black")
plt.text(B[0] + 1, B[1] + 1, "B(40, -6)", fontsize=10, color="black")
plt.text(C[0] + 1, C[1] + 1, f"C({a:.2f}, -52)", fontsize=10, color="black")

# Plot line through them
plt.plot([A[0], B[0], C[0]], [A[1], B[1], C[1]], linestyle="--", color="blue")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Collinear Points")
plt.grid(True)
plt.show()
