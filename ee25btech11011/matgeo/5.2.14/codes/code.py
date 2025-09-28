import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

# Path to DLL
dll_path = os.path.join(os.getcwd(), "code7.dll")
lib = ctypes.CDLL(dll_path)

# Define argument and return types
lib.solve.argtypes = [ctypes.c_int]*6 + [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)]
lib.solve.restype = ctypes.c_int

# Output variables
x = ctypes.c_float()
y = ctypes.c_float()

# Solve system via DLL
status = lib.solve(1, -3, 3, 3, -9, 2, ctypes.byref(x), ctypes.byref(y))

if status == 0:
    print(f"Unique solution: x={x.value:.2f}, y={y.value:.2f}")
elif status == 1:
    print("No solution (parallel lines).")
else:
    print("Infinite solutions (coincident lines).")

# Plot the lines
x_vals = np.linspace(-5, 5, 400)
y1 = (3 - 1*x_vals)/-3
y2 = (2 - 3*x_vals)/-9

plt.figure(figsize=(6,6))
plt.plot(x_vals, y1, label="x - 3y = 3", color="blue")
plt.plot(x_vals, y2, label="3x - 9y = 2", color="red", linestyle="--")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of Two Lines")
plt.legend()
plt.grid(True)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)

# Save figure
plt.savefig("fig7.png", dpi=150)
plt.show()
print("Graph saved as fig7.png")
