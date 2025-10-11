import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./circle.so')

# Define argument and return types
lib.circle_from_diameter_lines.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # line1 a,b,c
    ctypes.c_double, ctypes.c_double, ctypes.c_double,  # line2 a,b,c
    ctypes.c_double,                                    # circumference
    ctypes.POINTER(ctypes.c_double)                     # coeffs array
]
lib.circle_from_diameter_lines.restype = None

# Prepare coefficients array
coeffs = (ctypes.c_double * 5)()

# Call the function: example lines 2x+3y+1=0, 3x-y-4=0, circumference=10*pi
lib.circle_from_diameter_lines(2, 3, 1, 3, -1, -4, 10*3.141592653589793, coeffs)

coeffs_list = list(coeffs)
print("Circle coefficients [D, E, F, x^2 coeff, y^2 coeff]:", coeffs_list)

# Extract center and radius
D, E, F, _, _ = coeffs_list
x0 = -D/2
y0 = -E/2
r = np.sqrt(x0**2 + y0**2 - F)

# Plot the circle
theta = np.linspace(0, 2*np.pi, 500)
x = x0 + r*np.cos(theta)
y = y0 + r*np.sin(theta)

plt.figure(figsize=(6,6))
plt.plot(x, y, label='Circle')
plt.scatter([x0], [y0], color='red', label='Center')
plt.gca().set_aspect('equal', 'box')
plt.title('Circle from two diameter lines')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/7.4.17/figs/circle.png")
plt.show()
