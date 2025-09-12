import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared object
lib = ctypes.CDLL("./libmidpt.so")

# Define C function prototype
lib.midpt.argtypes = [ctypes.c_double, ctypes.c_double,
                      ctypes.c_double, ctypes.c_double,
                      ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

# Input diameter endpoints
x1, y1 = -6.0, 3.0
x2, y2 = 6.0, 4.0

# Prepare output variables
x_mid = ctypes.c_double()
y_mid = ctypes.c_double()

# Call C function
lib.midpt(x1, y1, x2, y2, ctypes.byref(x_mid), ctypes.byref(y_mid))

cx, cy = x_mid.value, y_mid.value
print("Centre of circle:", (cx, cy))

# Radius = half distance between endpoints
r = np.sqrt((x2 - x1)**2 + (y2 - y1)**2) / 2

# Generate circle points
theta = np.linspace(0, 2*np.pi, 500)
x_circle = cx + r * np.cos(theta)
y_circle = cy + r * np.sin(theta)

# Plot
plt.figure(figsize=(6,6))
plt.plot(x_circle, y_circle, label="Circle")

plt.scatter([x1, x2], [y1, y2], color="red", s=80, label="Diameter Endpoints")
plt.text(x1 - 1, y1 - 0.5, f"({x1:.0f}, {y1:.0f})", color="red", fontsize=10)
plt.text(x2 + 0.5, y2, f"({x2:.0f}, {y2:.0f})", color="red", fontsize=10)

plt.scatter(cx, cy, color="blue", marker="x", s=200, linewidths=3, label="Centre")
plt.text(cx + 0.5, cy + 0.5, f"({cx:.2f}, {cy:.2f})", color="blue", fontsize=10)
plt.plot([x1, x2], [y1, y2], 'g--', label="Diameter")
plt.axis("equal")
plt.legend(loc="upper right")
plt.title("Circle from Diameter Endpoints")
plt.savefig("/Users/bhargavkrish/Documents/ee1030-2025/ee25btech11013/matgeo/1.5.1/figs/Figure_1.png")
plt.show()

