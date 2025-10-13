import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os

# --- Load the C library ---
try:
    c_lib = ctypes.CDLL('./solve_system.so')
except OSError:
    print("Error: 'solve_system.so' not found. Compile using: gcc -shared -o solve_system.so -fPIC solve_system.c")
    exit()

# Define argument and return types
c_lib.solve_system.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
c_lib.solve_system.restype = None

# Prepare variables for result
x = ctypes.c_double()
y = ctypes.c_double()

# --- Call C function ---
c_lib.solve_system(ctypes.byref(x), ctypes.byref(y))
x_val = x.value
y_val = y.value

print(f"✅ Solution: x = {x_val}, y = {y_val}")

# --- Plotting in 2D ---
fig, ax = plt.subplots(figsize=(6,6))

# Define range for plotting
X = np.linspace(0, 50, 400)

# Equations: y = x - 26 and y = x / 3
Y1 = X - 26
Y2 = X / 3

# Plot the lines
ax.plot(X, Y1, label=r'$x - y = 26$', color="blue")
ax.plot(X, Y2, label=r'$x - 3y = 0$', color="green")

# Plot the intersection point
ax.scatter(x_val, y_val, color="red", s=60, label=f'Solution ({x_val:.0f}, {y_val:.0f})')

# Labels for intersection
ax.text(x_val+0.5, y_val, f'({x_val:.0f}, {y_val:.0f})', color="red")

# Formatting
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_title("Graphical Solution of 2x2 System")
ax.grid(True)
ax.legend()
ax.set_xlim(0, 50)
ax.set_ylim(0, 50)
ax.set_aspect("equal")

plt.show()
