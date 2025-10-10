import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object
lib = ctypes.CDLL('./liblinsolve.so')

# Define argument and result types
lib.solve2x2.restype = None
lib.solve2x2.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,2)),
    np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,)),
    np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,))
]

# Setup the matrix equation from the image
A = np.array([[np.sqrt(3)/2, 1/np.sqrt(2)],
              [1/2, -1/np.sqrt(2)]], dtype=np.float64)
b = np.array([8, 0], dtype=np.float64)
res = np.zeros(2, dtype=np.float64)

# Solve
lib.solve2x2(A, b, res)
b_side, c_side = res

# Compute triangle vertices
B = np.array([0, 0])
C = np.array([8, 0])
# Calculate A using values from image
A_x = (c_side * 1/np.sqrt(2))
A_y = (c_side * 1/np.sqrt(2))
A = np.array([A_x, A_y])

# Plot
x = [A[0], B[0], C[0], A[0]]
y = [A[1], B[1], C[1], A[1]]
plt.plot(x, y, marker='o')
plt.text(A[0], A[1], "A")
plt.text(B[0], B[1], "B(0,0)")
plt.text(C[0], C[1], "C(8,0)")
plt.title("Triangle ABC")
plt.axis('equal')
plt.savefig('../figs/fig.png')
plt.show()
