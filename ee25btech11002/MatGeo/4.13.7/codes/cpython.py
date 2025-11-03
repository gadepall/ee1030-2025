import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
mylib = ctypes.CDLL("./mylib.so")

# Define argument and return types
mylib.line_coefficients.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
mylib.line_coefficients.restype = None

# Wrapper function to call C function
def get_line_coeffs(a, d):
    coeffs = (ctypes.c_int * 3)()
    mylib.line_coefficients(a, d, coeffs)
    return coeffs[0], coeffs[1], coeffs[2]

# Fixed point
fixed_point = (1, -2)

# Define (a, d) pairs
lines = [(1, -1), (2, -1), (1, 0)]
colors = ['blue', 'green', 'purple']

x = np.linspace(-5, 5, 400)

plt.figure(figsize=(10,5))

for i, (a, d) in enumerate(lines):
    A, B, C = get_line_coeffs(a, d)
    
    if B != 0:
        y = (-A*x - C)/B
        plt.plot(x, y, color=colors[i], linewidth=1.5)
        if i == 1:
            plt.text(-1, 4, f'2x + y = 0', fontsize=10, color=colors[i])
            plt.plot(x, y, color=colors[i], linewidth=1.5, 
            label=f"(a={a}, d={d})")   # <-- add label
        elif i == 2:
            plt.text(-4, 4, f'x + y = -1', fontsize=10, color=colors[i])
            plt.plot(x, y, color=colors[i], linewidth=1.5, 
            label=f"(a={a}, d={d})")   # <-- add label
    else:
        x_vert = -C / A
        plt.plot([x_vert]*len(x), x, color=colors[i], linewidth=1.5)
        plt.text(x_vert+0.2, 4.5, f'x = {x_vert}', fontsize=10, color=colors[i])
        plt.plot([x_vert]*len(x), x, color=colors[i], linewidth=1.5, 
         label=f"(a={a}, d={d})")

# Plot fixed point
plt.plot(fixed_point[0], fixed_point[1], 'ro', markersize=6)
plt.text(fixed_point[0]+0.5, fixed_point[1]-0.3, '(1, -2)', fontsize=10, color='red')

# Axes settings
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Lines passing through fixed point (1, -2) for different values of a and common difference d")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(loc="upper right")
plt.grid(True)
plt.show()
