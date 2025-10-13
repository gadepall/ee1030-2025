import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- Load shared library (.so) ---
lib = ctypes.CDLL("./taxi_matrix.so")

# Prepare C float variables
x = ctypes.c_float()
y = ctypes.c_float()

# Call the C function
lib.solveByMatrix(ctypes.byref(x), ctypes.byref(y))

# Extract computed values
x_val = x.value
y_val = y.value

print(f"Fixed charge (x) = ₹{x_val:.2f}")
print(f"Charge per km (y) = ₹{y_val:.2f}")

# --- Generate data for plotting ---
x_vals = np.linspace(-20, 120, 400)

# Line equations from the problem
y1 = (105 - x_vals) / 10
y2 = (155 - x_vals) / 15
y3 = (255 - x_vals) / 25  # third line for c = 255

# Intersection point (from C)
x_int, y_int = x_val, y_val

# --- Plot configuration ---
plt.figure(figsize=(9, 6))
plt.style.use('seaborn-v0_8-whitegrid')

# Plot lines with clarity
plt.plot(x_vals, y1, color='royalblue', linewidth=2.8, label=r'$x + 10y = 105$')
plt.plot(x_vals, y2, color='darkorange', linewidth=2.8, linestyle='--', label=r'$x + 15y = 155$')
plt.plot(x_vals, y3, color='green', linewidth=2.8, linestyle='-.', label=r'$x + 25y = 255$')

# Intersection point
plt.scatter(x_int, y_int, color='red', s=100, edgecolors='black', zorder=5, label=f'Intersection ({x_int:.0f}, {y_int:.0f})')
plt.text(x_int + 5, y_int + 1, f'({x_int:.0f}, {y_int:.0f})', fontsize=12, color='red', fontweight='bold')

# --- Labels and aesthetics ---
plt.title("Graph of Taxi Fare Equations", fontsize=15, fontweight='bold')
plt.xlabel("x (Fixed Charge ₹)", fontsize=12)
plt.ylabel("y (Charge per km ₹)", fontsize=12)

plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.8)
plt.legend(fontsize=11, loc='upper right', frameon=True, shadow=True)
plt.xlim(-20, 120)
plt.ylim(-50, 50)
plt.tight_layout()

# --- Show the plot ---
plt.show()

