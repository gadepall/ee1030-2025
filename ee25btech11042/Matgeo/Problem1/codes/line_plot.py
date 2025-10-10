import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./line_division.so")

# Define argument and return types
lib.divide_point.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,
                             ctypes.c_float, ctypes.c_float,
                             np.ctypeslib.ndpointer(dtype=np.float32, ndim=1, flags="C_CONTIGUOUS")]
lib.divide_point.restype = None

# Given points A and B
x1, y1 = 1.0, 3.0  # Point A
x2, y2 = 4.0, 6.0  # Point B

# Hardcoded ratio m:n
m, n = 2.0, 1.0

# Output array to store coordinates of P
out = np.zeros(2, dtype=np.float32)

# Call the C function to get point P
lib.divide_point(x1, y1, x2, y2, m, n, out)
Px, Py = out[0], out[1]

# Print the coordinates of P
print(f"Coordinates of P dividing AB in {m}:{n} ratio: ({Px}, {Py})")

# Plot A, B, and P
plt.figure()
plt.plot([x1, x2], [y1, y2], 'k--', label="Line AB")  # line AB
plt.scatter([x1, x2, Px], [y1, y2, Py], color=['red','blue','green'], label="Points")
plt.text(x1, y1, " A", fontsize=10)
plt.text(x2, y2, " B", fontsize=10)
plt.text(Px, Py, " P", fontsize=10)
plt.legend(["Line AB","Points"])
plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"Point dividing AB in {m}:{n} ratio")
plt.grid(True)
plt.show()

