import numpy as np
import matplotlib.pyplot as plt
import ctypes

# ----------------------------
# (1) Call C shared library to get equation
# ----------------------------

lib = ctypes.CDLL("./libline.so")

lib.line_equation.argtypes = [ctypes.c_double, ctypes.c_double,
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double)]
lib.line_equation.restype = None

nx = ctypes.c_double()
ny = ctypes.c_double()
c  = ctypes.c_double()

# Pass point A(1,2)
lib.line_equation(1.0, 2.0, ctypes.byref(nx), ctypes.byref(ny), ctypes.byref(c))

# ----------------------------
# (2) Generate line points
# ----------------------------

x_vals = np.linspace(-1, 4, 200)
y_vals = (c.value - nx.value * x_vals) / ny.value

# ----------------------------
# (3) Plot line + point A
# ----------------------------

plt.figure(figsize=(6,6))

# Line
plt.plot(x_vals, y_vals, 'b-', label=fr"${nx.value:.2f}x_1 + {ny.value:.2f}x_2 = {c.value:.2f}$")

# Point A
A = np.array([1, 2])
plt.scatter(A[0], A[1], color="red", zorder=5)
plt.text(A[0]+0.1, A[1]+0.1, "A(1,2)", color="red")

# Axes formatting
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Line through A(1,2) making 30° with y-axis")
plt.legend()
plt.grid(True)
plt.axis("equal")

plt.show()

