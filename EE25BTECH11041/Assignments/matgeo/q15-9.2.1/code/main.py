import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load shared object
lib = ctypes.CDLL('./area.so')
lib.area_bounded.restype = ctypes.c_double

# Call C function
area = lib.area_bounded()
print("Area bounded =", area)

# Plot the region
y = np.linspace(0, 3, 100)
x1 = y**2          # x = y^2  (y = sqrt(x))
x2 = 2*y + 3       # x = 2y + 3

plt.plot(x1, y, label='y = sqrt(x) → x = y²')
plt.plot(x2, y, label='x = 2y + 3')

plt.fill_betweenx(y, x1, x2, color='lightblue', alpha=0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Area bounded by curves = {area:.2f}")
plt.legend()
plt.grid(True)
plt.show()

