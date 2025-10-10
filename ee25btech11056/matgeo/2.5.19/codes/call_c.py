import ctypes
import sys
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./points.so")
lib.product.restype = ctypes.c_double
lib.product.argtypes = [ctypes.c_double]

solution_p = None
for p in range(-10, 11):
    dot = lib.product(ctypes.c_double(p))
    if abs(dot) < 1e-6:   # check near zero
        solution_p = p
        print(f"Solution found: p = {p}")
        break

if solution_p is None:
    print("No solution found")
    sys.exit(0)

p = solution_p

# Parametric equations
t = np.linspace(-10, 10, 100)
x1 = 1 - 3*t
y1 = 7 + p*t
z1 = 3 + 2*t

s = np.linspace(-10, 10, 100)
x2 = 1 - 3*p*s
y2 = 5 + s
z2 = 6 - 5*s

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x1, y1, z1, label="Line A", color="blue")
ax.plot(x2, y2, z2, label="Line B", color="orange")

ax.set_title("Perpendicular 3D Lines (P = 1)")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()

# Save the figure
plt.savefig("perpendicular_lines.png", dpi=300, bbox_inches="tight")

# Show the plot
plt.show()

