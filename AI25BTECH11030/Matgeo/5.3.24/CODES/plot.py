import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL('./matfun.so')

# Define C function argument and return types
lib.solve_linear_system.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
lib.solve_linear_system.restype = None

# Define matrix A and vector B for the system
A_c = (ctypes.c_double * 4)(3, -5, 9, -2)
B_c = (ctypes.c_double * 2)(4, 7)
X_c = (ctypes.c_double * 2)()

# Call the C function to solve the system
lib.solve_linear_system(A_c, B_c, X_c)

# Print solution as a column vector
print("Solution (column vector form):")
print(f"[\n [{X_c[0]}],\n [{X_c[1]}]\n]")

# Plot the lines corresponding to the equations
a1, b1 = 3, -5
c1 = 4
a2, b2 = 9, -2
c2 = 7

x_vals = np.linspace(-10, 10, 400)
y1 = (c1 - a1 * x_vals) / b1
y2 = (c2 - a2 * x_vals) / b2

plt.plot(x_vals, y1, label='3x - 5y = 4')
plt.plot(x_vals, y2, label='9x - 2y = 7')

# Plot the solution point
plt.scatter(X_c[0], X_c[1], color='red', label='Solution point', zorder=5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of the Linear System')
plt.legend()
plt.grid(True)
plt.savefig("fig1.png")
plt.show()

