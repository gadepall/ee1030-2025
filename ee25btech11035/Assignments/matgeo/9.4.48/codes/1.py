import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./mat.so")

lib.roots.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                      ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.roots.restype = None

# Set the quadratic coefficients for your equation: x^2 + 2x - 143 = 0
a, b, c = 1.0, 2.0, -143.0

x1 = ctypes.c_double()
x2 = ctypes.c_double()

# Call the C function, passing the addresses of x1 and x2
lib.roots(a, b, c, ctypes.byref(x1), ctypes.byref(x2))

# Extract the Python float values from the ctypes objects
r1, r2 = x1.value, x2.value
print(f"The equation is: {a:.1f}x^2 + {b:.1f}x + {c:.1f} = 0")
print(f"Roots from C function: x1 = {r1}, x2 = {r2}")

# Generate a range of x-values for a smooth curve
x_vals = np.linspace(min(r1, r2) - 5, max(r1, r2) + 5, 400)
# Calculate the corresponding y-values
y_vals = a * x_vals**2 + b * x_vals + c

# Create the plot
plt.figure(figsize=(10, 8))

# Plot the axes
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

# Plot the parabola
plt.plot(x_vals, y_vals, label=f"$y = x^2 + 2x - 143$", color="blue")

# Mark the roots on the x-axis
plt.scatter([r1, r2], [0, 0], color="red", zorder=5, label=f"Roots at ({r1}, 0) and ({r2}, 0)")

# Add labels near the roots for clarity
plt.text(r1, 15, f"({r1:.0f}, 0)", fontsize=11, color="red", ha="center")
plt.text(r2, 15, f"({r2:.0f}, 0)", fontsize=11, color="red", ha="center")

# Add formatting to the plot
plt.title("Parabola for $x^2 + 2x - 143 = 0$", fontsize=16)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True)
plt.savefig('1.png')
plt.show()