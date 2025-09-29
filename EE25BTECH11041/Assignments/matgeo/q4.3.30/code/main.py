import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared object
lib = ctypes.CDLL("./main.so")

# Define function signature
lib.trisec.argtypes = [
    ctypes.c_double,  # k
    ctypes.c_double,  # x1
    ctypes.c_double,  # y1
    ctypes.c_double,  # x2
    ctypes.c_double,  # y2
    ctypes.POINTER(ctypes.c_double),  # *a
    ctypes.POINTER(ctypes.c_double)   # *b
]

# Known intercepts from math derivation
a = -32.0/3.0
b = 24.0/5.0

# Call trisec with k = 5/3
px = ctypes.c_double()
py = ctypes.c_double()
lib.trisec(5.0/3.0, a, 0.0, 0.0, b, ctypes.byref(px), ctypes.byref(py))

print(f"Computed point dividing AB in 5:3 = ({px.value}, {py.value})")

# Now plot line
x_vals = np.linspace(a, 0, 200)
y_vals = b*(1 - x_vals/a)

plt.plot(x_vals, y_vals, label="Line through intercepts")
plt.scatter([a,0], [0,b], color="green", label="Intercepts")
plt.scatter([-4], [3], color="red", marker="x", s=100, label="Given point (-4,3)")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()

