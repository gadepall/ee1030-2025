import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load compiled shared library
lib = ctypes.CDLL("./code5.dll")

# Define signatures
lib.dot_product.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
lib.dot_product.restype = ctypes.c_int

lib.is_orthogonal.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
lib.is_orthogonal.restype = ctypes.c_int

lib.line_equation.argtypes = [ctypes.c_double]
lib.line_equation.restype = ctypes.c_double

# --- Line: x + y = 0 ---
normal_vector = (ctypes.c_int * 2)(1, 1)     # n = (1, 1)
direction_vector = (ctypes.c_int * 2)(-1, 1) # m = (-1, 1)
vector_origin = np.array([0, 0])

# Dot product + orthogonality check
dp = lib.dot_product(normal_vector, direction_vector)
print(f"Dot product of n and m: {dp}")

if lib.is_orthogonal(normal_vector, direction_vector):
    print("The vectors are orthogonal (as expected).")
else:
    print("The vectors are NOT orthogonal.")

# Compute points on line y = -x
x_vals = np.linspace(-5, 5, 200)
y_vals = [lib.line_equation(float(x)) for x in x_vals]

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(8, 8))

# Line
plt.plot(x_vals, y_vals, label='Line: x + y = 0', color='blue', zorder=1)

# Direction vector
plt.quiver(vector_origin[0], vector_origin[1],
           direction_vector[0], direction_vector[1],
           angles='xy', scale_units='xy', scale=1,
           color='green', label='Direction Vector', zorder=2)

# Normal vector
plt.quiver(vector_origin[0], vector_origin[1],
           normal_vector[0], normal_vector[1],
           angles='xy', scale_units='xy', scale=1,
           color='red', label='Normal Vector', zorder=2)

# Origin point
plt.plot(vector_origin[0], vector_origin[1], 'o', color='purple', markersize=8,
         label='Origin (0, 0)')

plt.title('Line x + y = 0 with Direction and Normal Vectors')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.axis('equal')
plt.legend()
plt.grid(True)

plt.xlim(-5, 5)
plt.ylim(-5, 5)

# Save figure
plt.savefig("fig5.png")
plt.show()
