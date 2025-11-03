import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the C library
lib = ctypes.CDLL('./10.so')

# Define argument and return types
lib.intersection.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                             ctypes.c_double, ctypes.c_double, ctypes.c_double,
                             ctypes.POINTER(ctypes.c_double)]

# Prepare variables
a1, b1, c1 = np.sqrt(2), np.sqrt(3), 0
a2, b2, c2 = np.sqrt(3), -np.sqrt(8), 0

# Result array
res = (ctypes.c_double * 2)()
lib.intersection(a1, b1, c1, a2, b2, c2, res)

x_inter, y_inter = res[0], res[1]
print(f"Intersection point: ({x_inter:.2f}, {y_inter:.2f})")

# Generate line points
x = np.linspace(-5, 5, 100)
y1 = (-a1 * x + c1) / b1
y2 = (-a2 * x + c2) / b2

# Plot lines
plt.plot(x, y1, label=r'$\sqrt{2}x + \sqrt{3}y = 0$')
plt.plot(x, y2, label=r'$\sqrt{3}x - \sqrt{8}y = 0$')
plt.scatter(x_inter, y_inter, color='red', label='Intersection Point (0,0)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Intersection of Two Lines')
plt.legend()
plt.grid(True)
plt.show()
