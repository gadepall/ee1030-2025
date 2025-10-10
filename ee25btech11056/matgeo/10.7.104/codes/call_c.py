import ctypes
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Folder to save figures
figs_folder = os.path.join("..", "figs")

# Load shared object (compiled from your C code)
lib = ctypes.CDLL("./points.so")

# Define function signature
lib.eccentricity.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.eccentricity.restype = ctypes.c_double

# Input values
lam = 1.0
a = 1.0
b = np.sqrt(2.0)

# Call C function
e = lib.eccentricity(lam, a, b)
print(f"Eccentricity from C function: e = {e}")

# Generate parabola points: y^2 = 4 λ x
y_vals = np.linspace(-5, 5, 500)
x_parab = (y_vals**2) / (4 * lam)

# Generate ellipse points using linspace: x in [-a, a]
x_vals = np.linspace(-a, a, 500)
inside = 1 - (x_vals**2) / (a**2)
y_upper = np.where(inside >= 0, b * np.sqrt(inside), np.nan)
y_lower = np.where(inside >= 0, -b * np.sqrt(inside), np.nan)

# Key points
Px, Py = lam, 2 * lam       # End of latus rectum
Ax, Ay = a, 0.0             # Vertex A
Bx, By = 0.0, b             # Vertex B
Ox, Oy = 0.0, 0.0           # Origin

# Plotting
fig, ax = plt.subplots(figsize=(8, 8))

# Plot parabola
ax.plot(x_parab, y_vals, 'g', label=r"$y^2 = 4\lambda x$")

# Plot ellipse (upper and lower halves)
ax.plot(x_vals, y_upper, 'b', label=r"$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$")
ax.plot(x_vals, y_lower, 'b')

# Mark P
ax.scatter(Px, Py, color="red")
ax.text(Px + 0.2, Py, r"$P(\lambda, 2\lambda)$", fontsize=10, color="red")

# Mark A, B, and O
ax.scatter(Ax, Ay, color="purple")
ax.text(Ax + 0.1, Ay - 0.2, r"$A(a,0)$", fontsize=10, color="purple")

ax.scatter(Bx, By, color="purple")
ax.text(Bx - 0.5, By + 0.2, r"$B(0,b)$", fontsize=10, color="purple")

ax.scatter(Ox, Oy, color="black")
ax.text(Ox - 0.4, Oy - 0.3, r"$O(0,0)$", fontsize=10, color="black")

# Axes at center
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)

# Formatting
ax.set_aspect("equal")
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.legend()
ax.set_title("Parabola and Ellipse")
ax.grid(True)

# Save figure
plt.tight_layout()
fig.savefig(os.path.join(figs_folder, "parabola_ellipse.png"))
plt.show()

