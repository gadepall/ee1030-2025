import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load shared library
lib = ctypes.CDLL('./code.so')  # 

# Define the struct in Python
class LineVectors(ctypes.Structure):
    _fields_ = [
        ('nx', ctypes.c_double),
        ('ny', ctypes.c_double),
        ('dx', ctypes.c_double),
        ('dy', ctypes.c_double)
    ]

# Function signature
lib.find_vectors.restype = LineVectors
lib.find_vectors.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]

# Call the function for y = x -> x - y = 0 -> a=1, b=-1, c=0
v = lib.find_vectors(1.0, -1.0, 0.0)

# Print results
print("Normal vector:", (v.nx, v.ny))
print("Direction vector:", (v.dx, v.dy))

# Plotting the line and direction vector
# Line equation: a*x + b*y + c = 0 -> y = (-a*x - c)/b
a, b, c = 1.0, -1.0, 0.0
x_vals = np.linspace(-5, 5, 100)
y_vals = (-a * x_vals - c) / b

plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, label='Line y = x', color='blue')

# Plot direction vector as an arrow from origin
plt.quiver(0, 0, v.dx, v.dy, angles='xy', scale_units='xy', scale=1, color='red', label='Direction vector')

# Plot normal vector as arrow from origin
plt.quiver(0, 0, v.nx, v.ny, angles='xy', scale_units='xy', scale=1, color='green', label='Normal vector')

plt.xlim(-6,6)
plt.ylim(-6,6)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.title("Line y = x with Normal and Direction Vectors")
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/4.2.13/figs/q6.png")
plt.show()
