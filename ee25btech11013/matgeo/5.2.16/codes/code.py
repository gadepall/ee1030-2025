import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library (must be in the same directory)
lib = ctypes.CDLL("./code.so")

# Define argument and return types
lib.line1.argtypes = [ctypes.c_double]
lib.line1.restype = ctypes.c_double

lib.line2.argtypes = [ctypes.c_double]
lib.line2.restype = ctypes.c_double

# Generate values using C functions
x_vals = np.linspace(-10, 10, 400)
y1 = np.array([lib.line1(float(x)) for x in x_vals])
y2 = np.array([lib.line2(float(x)) for x in x_vals])

# Plot
plt.figure(figsize=(6,6))
plt.plot(x_vals, y1, label=r'$3x - 5y = 20$')
plt.plot(x_vals, y2, '--', label=r'$6x - 10y = 40$ (same line)')

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("System of Equations (C + Python)")
plt.legend()
plt.grid(True)
plt.savefig("/Users/bhargavkrish/Desktop/BackupMatrix/ee25btech11013/matgeo/5.2.16/figs/Figure_1.png")
plt.show()
