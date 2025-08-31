import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library (your .so file is named 2.so)
lib = ctypes.CDLL('./2.so')

# Define function signature: double find_distance(int a, int b)
lib.find_distance.argtypes = [ctypes.c_int, ctypes.c_int]
lib.find_distance.restype = ctypes.c_double

# Example input values
a, b = 5, 2   # you can change these

# Call C function
dist = lib.find_distance(a, b)
print(f"Distance between (0,0) and ({a-b},{a+b}) = {dist:.2f}")

# Define points
A = np.array([0, 0])               # Origin
B = np.array([a - b, a + b])       # Point (a-b, a+b)

# Plot line AB
plt.plot([A[0], B[0]], [A[1], B[1]], 'k-', label='$AB$')

# Plot points
plt.scatter([A[0], B[0]], [A[1], B[1]], c=['red', 'blue'])
labels = ['A(0,0)', f'B({a-b},{a+b})']
coords = [A, B]

# Annotate points
for label, coord in zip(labels, coords):
    plt.annotate(label,
                 (coord[0], coord[1]),
                 textcoords="offset points",
                 xytext=(10, -10),
                 ha='center')

# Decorations
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.title(f"Distance = {dist:.2f}")
plt.savefig("2.png", dpi=150)   # Save figure
plt.show()
