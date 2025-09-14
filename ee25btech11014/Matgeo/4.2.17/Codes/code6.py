import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Define the Vector2D struct in Python to match the C struct
class Vector2D(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

lib = ctypes.CDLL("./code6.so")

# Set argument and return types for the function
lib.computeVectors.argtypes = (Vector2D,Vector2D,ctypes.POINTER(Vector2D), ctypes.POINTER(Vector2D))
lib.computeVectors.restype = None

# Create input points
p1 = Vector2D(1.0, 2.0)
p2 = Vector2D(4.0, 6.0)

# Prepare output vectors
direction = Vector2D()
normal = Vector2D()

# Call the C function
lib.computeVectors(p1, p2, ctypes.byref(direction), ctypes.byref(normal))

print(f"Direction Vector: ({direction.x:.2f}, {direction.y:.2f})")
print(f"Normal Vector: ({normal.x:.2f}, {normal.y:.2f})")

# Line equation: y = x + 2
# Normal vector = (1, -1)
# Direction vector = (1, 1)

# Define range for x
x_vals = np.linspace(-5, 5, 200)
y_vals = x_vals + 2   # original line

# Perpendicular line: slope = -1 (since slope of y=x+2 is 1)
# Pass it through the y-intercept (0,2)
x_perp = np.linspace(-5, 5, 200)
y_perp = -x_perp + 2  # equation of perpendicular

# Plot
plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, 'r-')
plt.plot(x_perp, y_perp, 'b-')

# Mark intercept
plt.scatter(0, 2, color='black', zorder=5)
plt.text(0.2, 2.1, '(0,2)', fontsize=9)

# Show direction and normal vectors at point (0,2)
plt.arrow(0, 2, 1, 1, head_width=0.2, head_length=0.3, 
          fc='red', ec='red')
plt.arrow(0, 2, 1, -1, head_width=0.2, head_length=0.3, 
          fc='blue', ec='blue')

# --- Label the original line with its equation directly on the line ---
plt.text(1, 1+2+0.2, r"$y = x + 2$", color='red', fontsize=11)

# --- Add text labels in the top-right corner ---
plt.text(3.5, 7, "Red – Original Line (y = x + 2)", color='red', fontsize=10)
plt.text(3.5, 6.3, "Blue – Perpendicular Line (y = -x + 2)", color='blue', fontsize=10)

# Axes and grid
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)

# Save as fig_6.png
plt.savefig("fig_6.png", dpi=300)
plt.show()
