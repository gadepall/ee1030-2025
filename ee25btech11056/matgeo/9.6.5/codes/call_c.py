import ctypes
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Folder to save figures
figs_folder = os.path.join("..", "figs")

# Load shared object
lib = ctypes.CDLL("./points.so")

# Define the C function signature
lib.intersection.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.intersection.restype = None

# Call the C function
sol = (ctypes.c_double * 2)()
lib.intersection(sol)
x0, y0 = sol[0], sol[1]
print(f"Intersection point from C: P({x0}, {y0})")

# Define grid for implicit plotting
x_vals = np.linspace(-5, 5, 500)
y_vals = np.linspace(-10, 10, 500)
X, Y = np.meshgrid(x_vals, y_vals)

# First hyperbola: 9x^2 - y^2 - 8y = 0
F1 = 9*X**2 - Y**2 - 8*Y

# Second hyperbola: 9x^2 - y^2 - 8x = 0
F2 = 9*X**2 - Y**2 - 8*X

# Line y = x
y_line = x_vals

# Plotting
fig, ax = plt.subplots(figsize=(8, 8))

# Plot first hyperbola using contour
ax.contour(X, Y, F1, levels=[0], colors="g", linewidths=1.5) #to plot levle curves of a cd scalar field z give x and y grids
ax.plot([], [], 'g', label=r"$9x^2 - y^2 - 8y = 0$")  # dummy for legend

# Plot second hyperbola using contour
ax.contour(X, Y, F2, levels=[0], colors="b", linewidths=1.5)
ax.plot([], [], 'b', label=r"$9x^2 - y^2 - 8x = 0$")  # dummy for legend

# Plot line y = x
ax.plot(x_vals, y_line, 'm', label=r"$y=x$")

# Plot intersection point
ax.scatter(x0, y0, color="red", zorder=5)
ax.text(x0 + 0.3, y0 , r"$P(1,1)$", fontsize=10, color="red")


# Axes at center
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)

# Formatting
ax.set_aspect("equal")
ax.set_xlim(-5, 5)
ax.set_ylim(-10, 10)
ax.legend()
ax.set_title("Intersection of Conics and Line y=x")
ax.grid(True)

# Save figure
plt.tight_layout()
fig.savefig(os.path.join(figs_folder, "conics_intersection.png"))
plt.show()

