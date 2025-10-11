import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./mat6.so")

lib.dot_product.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
lib.dot_product.restype = ctypes.c_int
lib.is_orthogonal.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
lib.is_orthogonal.restype = ctypes.c_int
lib.line_equation.argtypes = [ctypes.c_double]
lib.line_equation.restype = ctypes.c_double

normal_vector = (ctypes.c_int * 2)(2, 0)
direction_vector = (ctypes.c_int * 2)(0, 1)
vector_origin = np.array([2.5, 0])

dp = lib.dot_product(normal_vector, direction_vector)
print(f"Dot product of n and m: {dp}")

if lib.is_orthogonal(normal_vector, direction_vector):
    print("The vectors are orthogonal (as expected).")
else:
    print("The vectors are NOT orthogonal.")

y_vals = np.linspace(-5, 5, 200)
x_vals = [lib.line_equation(float(y)) for y in y_vals]

plt.figure(figsize=(7, 7))

plt.plot(x_vals, y_vals, color="blue", linewidth=2)

plt.quiver(vector_origin[0], vector_origin[1],
           direction_vector[0], direction_vector[1],
           angles='xy', scale_units='xy', scale=1,
           color='green')

plt.quiver(vector_origin[0], vector_origin[1],
           normal_vector[0], normal_vector[1],
           angles='xy', scale_units='xy', scale=1,
           color='red')

plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)

plt.title("Line: 2x - 5 = 0 (x = 2.5)")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.axis("equal")
plt.grid(True)
plt.show()

