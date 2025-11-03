import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os

# --- Load the C library ---
try:
    c_lib = ctypes.CDLL('./linear.so')  # use linear.dll on Windows
except OSError:
    print("Error: 'linear.so' not found. Compile using: gcc -shared -o linear.so -fPIC linear.c")
    exit()

# Define argument and return types
c_lib.solve_linear.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float,
                               ctypes.c_float, ctypes.c_float, ctypes.c_float,
                               ctypes.POINTER(ctypes.c_float),
                               ctypes.POINTER(ctypes.c_float)]
c_lib.solve_linear.restype = None

# --- Coefficients of system ---
# 8x + 5y = 9
# 3x + 2y = 4
a1, b1, c1 = 8.0, 5.0, 9.0
a2, b2, c2 = 3.0, 2.0, 4.0

# Allocate memory for outputs
x_out = ctypes.c_float()
y_out = ctypes.c_float()

# Call C function
c_lib.solve_linear(a1, b1, c1,
                   a2, b2, c2,
                   ctypes.byref(x_out),
                   ctypes.byref(y_out))

x_sol, y_sol = x_out.value, y_out.value
print(f"✅ Solution: x = {x_sol:.2f}, y = {y_sol:.2f}")

# --- Plotting ---
x = np.linspace(-5, 5, 400)
y1 = (c1 - a1*x)/b1   # from 8x + 5y = 9
y2 = (c2 - a2*x)/b2   # from 3x + 2y = 4

plt.plot(x, y1, label=r'$8x + 5y = 9$', color="blue")
plt.plot(x, y2, label=r'$3x + 2y = 4$', color="green")

# Intersection point
plt.plot(x_sol, y_sol, 'ro')
plt.text(x_sol+0.2, y_sol, f"({x_sol:.0f},{y_sol:.0f})", color="red")

# Formatting
plt.xlabel("x")
plt.ylabel("y")
plt.title("Solution of Linear System")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()
