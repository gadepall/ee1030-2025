import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load shared library
lib = ctypes.CDLL('./libsolver.so')
solve_quadratic = lib.solve_quadratic
solve_quadratic.argtypes = [ctypes.POINTER(ctypes.c_double)]
solve_quadratic.restype = None

# Prepare array for roots
roots = (ctypes.c_double * 2)()
solve_quadratic(roots)
x1, x2 = roots[0], roots[1]

# Define functions
def f(x): return (x - 2)**2 + 1
def g(x): return 2*x - 3

# Plot
x_vals = np.linspace(0, 5, 400)
plt.plot(x_vals, f(x_vals), label='f(x) = (x - 2)^2 + 1', color='blue')
plt.plot(x_vals, g(x_vals), label='g(x) = 2x - 3', color='red')
plt.scatter([x1, x2], [f(x1), f(x2)], color='black', zorder=5)

# Annotate roots
plt.text(x1, f(x1)+0.5, f"x = {x1:.2f}", ha='center')
plt.text(x2, f(x2)+0.5, f"x = {x2:.2f}", ha='center')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphical and Matrix-Theoretic Solution')
plt.legend()
plt.grid(True)
plt.show()

