# nativecode.py
import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object
lib = ctypes.CDLL("./code.so")

# Define the function signature
lib.get_m.argtypes = [ctypes.POINTER(ctypes.c_double),
                      ctypes.POINTER(ctypes.c_double),
                      ctypes.POINTER(ctypes.c_double)]

# Prepare variables
mx = ctypes.c_double()
my = ctypes.c_double()
mz = ctypes.c_double()

# Call C function
lib.get_m(ctypes.byref(mx), ctypes.byref(my), ctypes.byref(mz))
m = np.array([mx.value, my.value, mz.value])
print("m vector from C:", m)

# Point through which line passes
P = np.array([2, 3, -5])

# Line: r = P + t*m
t = np.linspace(-10, 10, 100)
X = P[0] + t * m[0]
Y = P[1] + t * m[1]
Z = P[2] + t * m[2]

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(X, Y, Z, label="Line through (2,3,-5)")
ax.scatter(P[0], P[1], P[2], color="red", label="Point (2,3,-5)")
ax.legend()
plt.show()

