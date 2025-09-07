import ctypes
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
mp.use("TkAgg")

# Load the shared C library
lib = ctypes.CDLL("./liblineq_solver.so")

# Define argument and return types
lib.rref_solver.argtypes = [ctypes.c_double * 6, ctypes.c_double * 2]

# Create augmented matrix for system:
# x + 3y = 6
# 2x - 3y = 12
aug = (ctypes.c_double * 6)(1, 3, 6,   2, -3, 12)  # Flattened 2x3
solution = (ctypes.c_double * 2)()

# Call C function
lib.rref_solver(aug, solution)

# Convert result to numpy vector (ensure flat)
x_sol = np.array([solution[0], solution[1]], dtype=float).flatten()
print("Solution vector from C:", x_sol)

# plot
x_vals = np.linspace(-2, 10, 400)
y1 = (6 - x_vals) / 3
y2 = (12 - 2*x_vals) / -3

plt.plot(x_vals, y1, label=r"$x+3y=6$")
plt.plot(x_vals, y2, label=r"$2x-3y=12$")

plt.scatter(x_sol[0], x_sol[1], color="red", zorder=5)
plt.text(float(x_sol[0])+0.2, float(x_sol[1]), f"({x_sol[0]:.1f}, {x_sol[1]:.1f})", color="red")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Garphical solution of the Linear system")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.legend()
plt.grid(True)
plt.savefig("/home/user/Matrix/Matgeo_assignments/5.2.29/figs/Figure_1.png")
plt.show()

