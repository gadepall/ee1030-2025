import ctypes
import matplotlib.pyplot as plt
import numpy as np
import platform

# Load compiled C library
if platform.system() == "Windows":
    lib = ctypes.CDLL("./code6.dll")
else:
    lib = ctypes.CDLL("./libcode6.so")

# Tell ctypes about function signatures
lib.get_x_line.argtypes = [ctypes.c_double, ctypes.c_double]
lib.get_x_line.restype = ctypes.c_double

lib.get_y_line.argtypes = [ctypes.c_double, ctypes.c_double]
lib.get_y_line.restype = ctypes.c_double

lib.get_general_line.argtypes = [ctypes.c_double, ctypes.c_double,
                                 ctypes.c_double, ctypes.c_double]
lib.get_general_line.restype = ctypes.c_double

# Point A
Ax, Ay = 2.0, 3.0

# Case 1: Line parallel to x-axis (n = (0,1))
y_const = lib.get_y_line(Ax, Ay)

# Case 2: Line parallel to y-axis (n = (1,0))
x_const = lib.get_x_line(Ax, Ay)

# Case 3: General line (example n = (2,-1))
n1, n2 = 2.0, -1.0
rhs = lib.get_general_line(Ax, Ay, n1, n2)

# --- Plotting ---
fig, ax = plt.subplots(figsize=(7,7))

x_vals = np.linspace(-5, 10, 400)
y_vals_range = np.linspace(-5, 10, 400)

# Case 1: horizontal line
ax.plot(x_vals, y_const * np.ones_like(x_vals), 'r--',
        label=rf"$(0,1)\cdot x = {y_const:.1f}$  (Line parallel to x-axis)")

# Case 2: vertical line
ax.plot(x_const * np.ones_like(y_vals_range), y_vals_range, 'b--',
        label=rf"$(1,0)\cdot x = {x_const:.1f}$  (Line parallel to y-axis)")

# Case 3: general line (n·x = rhs)
y_vals = (rhs - n1*x_vals) / n2
ax.plot(x_vals, y_vals, 'g-',
        label=rf"$({n1:.0f},{n2:.0f})\cdot x = {rhs:.1f}$ (Equation of line passing through (2,3))")

# Mark point A
ax.scatter(Ax, Ay, color='black', zorder=5)
ax.text(Ax+0.1, Ay+0.1, r"$A(2,3)$")

ax.set_xlim(-5, 10)
ax.set_ylim(-5, 10)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True)
ax.set_aspect('equal', adjustable='box')
plt.savefig("fig6.png")
plt.show()