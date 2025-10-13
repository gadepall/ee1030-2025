# main.py
import ctypes
from ctypes import Structure, c_double
import numpy as np
import matplotlib.pyplot as plt

class Solution(Structure):
    _fields_ = [("A", c_double), ("D", c_double)]

# Load the shared object
lib = ctypes.CDLL("./libsolver.so")
lib.solve_ages.restype = Solution

# Call C function
sol = lib.solve_ages()
print(f"Alwar's present age: {sol.A}")
print(f"Daughter's present age: {sol.D}")

# Graphical representation
D_vals = np.linspace(0, 30, 400)

# From eqn (1): A = 7D - 42
A1 = 7*D_vals - 42
# From eqn (2): A = 3D + 6
A2 = 3*D_vals + 6

plt.figure(figsize=(6,6))
plt.plot(D_vals, A1, label="A - 7D = -42")
plt.plot(D_vals, A2, label="A - 3D = 6")

# Plot solution from C
plt.scatter(sol.D, sol.A, c="red", zorder=5)
plt.text(sol.D+0.5, sol.A, f"({int(sol.D)}, {int(sol.A)})", fontsize=10)

plt.xlabel("Daughter's Present Age (D)")
plt.ylabel("Alwar's Present Age (A)")
plt.title("Graphical Solution of Age Problem")
plt.grid(True)
plt.legend()
plt.show()

