import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./func.so")

lib.dot_product.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
lib.dot_product.restype = ctypes.c_int

lib.is_orthogonal.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
lib.is_orthogonal.restype = ctypes.c_int

lib.line_equation.argtypes = [ctypes.c_double]
lib.line_equation.restype = ctypes.c_double

# ✅ normal and direction vectors
normal_vector = (ctypes.c_int * 2)(2, 1)
direction_vector = (ctypes.c_int * 2)(1, -2)
vector_origin = np.array([2, 4])

# Dot product check
dp = lib.dot_product(normal_vector, direction_vector)
print(f"Dot product of n and m: {dp}")

if lib.is_orthogonal(normal_vector, direction_vector):
    print("The vectors are orthogonal (as expected).")
else:
    print("The vectors are NOT orthogonal.")

# Evaluate line y = 3 - 2x
x_vals = np.linspace(-5, 7, 100)
y_vals = [lib.line_equation(float(x)) for x in x_vals]

# Plotting
plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(8, 8))

# ✅ Updated label
plt.plot(x_vals, y_vals, label='Line: 2x + y = 3', color='blue', zorder=1)

plt.quiver(vector_origin[0], vector_origin[1],
           direction_vector[0], direction_vector[1],
           angles='xy', scale_units='xy', scale=1,
           color='green', label='Direction Vector', zorder=2)

plt.quiver(vector_origin[0], vector_origin[1],
           normal_vector[0], normal_vector[1],
           angles='xy', scale_units='xy', scale=1,
           color='red', label='Normal Vector', zorder=2)

plt.plot(vector_origin[0], vector_origin[1], 'o', color='purple', markersize=8,
         label='Vector Origin (2, 4)')

plt.title('Line with Direction and Normal Vectors')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axis('equal')
plt.legend()
plt.grid(True)

plt.xlim(-5, 10)
plt.ylim(-5, 10)
plt.savefig("../figs/Figure_1.png")
plt.show()
