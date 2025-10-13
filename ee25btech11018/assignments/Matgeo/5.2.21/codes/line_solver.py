import ctypes
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
mp.use("TkAgg")

# Load the shared C library (adjust filename if needed)
lib = ctypes.CDLL("./line_solver.so")

# Define argument and return types
lib.rref_solver.argtypes = [ctypes.c_double * 6, ctypes.c_double * 2]

# Augmented matrix for system:
# 2x + 3y = 13
# 4x + 5y = 23
aug = (ctypes.c_double * 6)(2, 3, 13,   4, 5, 23)  # Flattened 2x3
solution = (ctypes.c_double * 2)()

# Call C function
lib.rref_solver(aug, solution)

# Convert result to numpy vector (ensure flat)
x_sol = np.array([solution[0], solution[1]], dtype=float).flatten()
print("Solution vector from C:", x_sol)

# Plot lines
x_vals = np.linspace(-2, 10, 400)
y1 = (13 - 2*x_vals) / 3
y2 = (23 - 4*x_vals) / 5

plt.plot(x_vals, y1, label=r"$2x+3y=13$")
plt.plot(x_vals, y2, label=r"$4x+5y=23$")

# Plot solution point
plt.scatter(x_sol[0], x_sol[1], color="red", zorder=5)
plt.text(float(x_sol[0]) + 0.2, float(x_sol[1]),
         f"({x_sol[0]:.1f}, {x_sol[1]:.1f})", color="red")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphical Solution of the Linear System")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.legend()
plt.grid(True)

plt.show()

