import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
# Compile C code using: gcc -shared -fPIC -o main.so main.c
so = ctypes.CDLL('./main.so')
so.find_k.restype = ctypes.c_double

# Get value of k from C function
k = so.find_k()
print(f"The value of k = {k}")

# Define polynomial: 6x^2 + 37x - (k - 2)
a, b, c = 6, 37, -(k - 2)

# Generate x values
x = np.linspace(-10, 2, 400)
y = a * x**2 + b * x + c

# Plot
plt.figure(figsize=(8,6))
plt.plot(x, y, label=r'$6x^2 + 37x - (k - 2)$', color='blue')

# X and Y axis lines
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Roots of polynomial
roots = np.roots([a, b, c])
plt.scatter(roots, [0, 0], color='red', zorder=5, label='Roots')

# Labels and Title
plt.title(f"Graph of 6x² + 37x - (k - 2),  where k = {k:.2f}")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid(True)
plt.show()
